#!/usr/bin/env python3
"""Scan vLLM + SGLang for unclaimed issues, classify by subsystem, write RADAR.md.

Pipeline (mirrors CNTRL-tek91/issue-radar's shape, adapted for two-repo scope):
    fetch → filter → pr-check → classify → rank → write

Runs on GitHub Actions with GITHUB_TOKEN, or locally with the `gh` CLI logged in.
Standard library + `gh` CLI only — no pip dependencies.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"
OUTPUT_PATH = Path(__file__).parent / "RADAR.md"
STATE_PATH = Path(__file__).parent / "seen.json"

BOT_LOGIN_SUFFIXES = ("[bot]",)
BOT_LOGIN_EXACT = {"dependabot", "renovate", "pre-commit-ci", "github-actions"}


def gh_api(path: str, paginate: bool = False, timeout: int = 30) -> list | dict:
    """Call `gh api <path>`; returns parsed JSON. Set paginate=True for list endpoints."""
    cmd = ["gh", "api"]
    if paginate:
        cmd += ["--paginate", "--slurp"]  # --slurp merges paginated arrays into one
    cmd.append(path)
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, check=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        print(f"gh api timed out ({timeout}s): {path}", file=sys.stderr)
        raise
    except subprocess.CalledProcessError as e:
        print(f"gh api failed: {path}\n{e.stderr}", file=sys.stderr)
        raise
    data = json.loads(proc.stdout) if proc.stdout.strip() else []
    if paginate and isinstance(data, list) and data and isinstance(data[0], list):
        # --slurp returns a list of pages, each a list of items; flatten.
        return [item for page in data for item in page]
    return data


def is_bot(login: str, user_type: str) -> bool:
    if user_type == "Bot":
        return True
    if any(login.endswith(s) for s in BOT_LOGIN_SUFFIXES):
        return True
    if login.lower() in BOT_LOGIN_EXACT:
        return True
    return False


# ---------- data model ----------

@dataclass
class Issue:
    repo: str
    number: int
    title: str
    body: str
    author: str
    author_type: str  # User / Bot / Organization
    author_association: str  # NONE / CONTRIBUTOR / MEMBER / OWNER / COLLABORATOR
    labels: list[str]
    assignees: list[str]
    created_at: datetime
    updated_at: datetime
    comments: int
    url: str
    is_pr: bool = False
    kind: str = "other"  # Bug / RFC / Feature / Perf / other / no-prefix
    category: str = "uncategorized"
    flags: list[str] = field(default_factory=list)


PREFIX_RE = re.compile(r"^\s*\[([^\]]+)\]")


def parse_kind(title: str, exclude: set[str], keep: set[str]) -> tuple[str, bool]:
    """Return (kind, is_excluded).

    Prefix matching is case-insensitive. A title without any [Prefix] is
    labeled "no-prefix" and passes through (SGLang templates are lax).
    Prefixes in `exclude` return is_excluded=True; the caller drops the issue.
    Prefixes in `keep` are canonicalized to Title-case; anything else → "other".
    """
    m = PREFIX_RE.match(title or "")
    if not m:
        return "no-prefix", False
    raw = m.group(1).strip()
    low = raw.lower()
    excl_low = {e.lower() for e in exclude}
    if low in excl_low:
        return raw, True
    keep_low = {k.lower(): k for k in keep}
    if low in keep_low:
        return keep_low[low], False
    return "other", False


# ---------- stages ----------

def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text())


def fetch_issues(repo: str, limit: int) -> list[Issue]:
    """Stage 1: pull open issues via `gh` REST list endpoint.

    The /issues endpoint returns both issues and PRs — we keep everything here
    and let filter_noise drop the PRs. per_page is capped at 100; for our
    two-repo scope, `limit` easily fits in a single page.
    """
    per_page = min(100, limit)
    raw = gh_api(f"repos/{repo}/issues?state=open&per_page={per_page}", paginate=False)
    assert isinstance(raw, list)
    issues: list[Issue] = []
    for r in raw[:limit]:
        issues.append(
            Issue(
                repo=repo,
                number=r["number"],
                title=r["title"] or "",
                body=r.get("body") or "",
                author=(r.get("user") or {}).get("login", ""),
                author_type=(r.get("user") or {}).get("type", ""),
                author_association=r.get("author_association", "NONE"),
                labels=[lb["name"] for lb in r.get("labels", [])],
                assignees=[a["login"] for a in r.get("assignees", [])],
                created_at=datetime.fromisoformat(r["created_at"].replace("Z", "+00:00")),
                updated_at=datetime.fromisoformat(r["updated_at"].replace("Z", "+00:00")),
                comments=r.get("comments", 0),
                url=r["html_url"],
                is_pr=r.get("pull_request") is not None,
            )
        )
    return issues


def filter_noise(
    issues: list[Issue],
    max_age_days: int,
    exclude_kinds: list[str],
    keep_kinds: list[str],
) -> list[Issue]:
    """Stage 2: drop PRs, bots, assigned, stale, and excluded issue kinds.

    Also tags each surviving issue with its parsed `kind` (Bug / RFC / …) and
    adds an ⚠no-prefix flag when the title has no [Prefix] — useful signal
    for readers deciding how much to trust the issue's shape.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    kept: list[Issue] = []
    for i in issues:
        if i.is_pr:
            continue
        if is_bot(i.author, i.author_type):
            continue
        if i.assignees:
            continue
        if i.updated_at < cutoff:
            continue
        kind, is_excluded = parse_kind(i.title, set(exclude_kinds), set(keep_kinds))
        if is_excluded:
            continue
        i.kind = kind
        if kind == "no-prefix":
            i.flags.append("⚠no-prefix")
        if i.author_association in ("MEMBER", "OWNER", "COLLABORATOR"):
            i.flags.append("⚠maintainer-authored")
        kept.append(i)
    return kept


def drop_issues_with_open_pr(
    issues: list[Issue], repo: str, max_checks: int
) -> list[Issue]:
    """Stage 3: skip issues that already have an open PR cross-referenced.

    Timeline calls are expensive (one per issue), so we cap at max_checks. Beyond
    the cap, issues pass through unchecked — we'd rather include a few duplicates
    than exhaust rate limits.
    """
    checked = 0
    kept: list[Issue] = []
    for i in issues:
        if checked >= max_checks:
            kept.append(i)
            continue
        checked += 1
        try:
            events = gh_api(f"repos/{repo}/issues/{i.number}/timeline?per_page=100")
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            kept.append(i)  # on error, keep it — better than silent drop
            continue
        assert isinstance(events, list)
        has_open_pr = any(
            ev.get("event") == "cross-referenced"
            and (ev.get("source") or {}).get("type") == "issue"
            and ((ev.get("source") or {}).get("issue") or {}).get("pull_request")
            and ((ev.get("source") or {}).get("issue") or {}).get("state") == "open"
            for ev in events
        )
        if not has_open_pr:
            kept.append(i)
    return kept


def classify(issues: list[Issue], categories: list[dict]) -> list[Issue]:
    """Stage 4: assign each issue a category via keyword + path match.

    For each category:
        score = 2 * (keyword hits in title) + (keyword hits in body) + 3 * (path hits in body)
    Titles count double per hit; paths count triple (they're precise signals).
    Ties resolved by category order in config.json. Score 0 → uncategorized.
    """
    for i in issues:
        title_low = i.title.lower()
        body_low = i.body.lower()
        best_score = 0
        best_cat = "uncategorized"
        for cat in categories:
            score = 0
            for kw in cat.get("keywords", []):
                kw_low = kw.lower()
                if kw_low in title_low:
                    score += 2
                if kw_low in body_low:
                    score += 1
            for path in cat.get("paths", []):
                if path.lower() in body_low:
                    score += 3
            if score > best_score:
                best_score = score
                best_cat = cat["id"]
        i.category = best_cat
    return issues


KIND_WEIGHT = {
    "Bug": 1.0,
    "Bugfix": 1.0,
    "Perf": 1.0,
    "Performance": 1.0,
    "Feature": 0.8,
    "other": 0.7,
    "RFC": 0.6,
    "no-prefix": 0.5,
}

REPRO_MARKERS = ("traceback", "repro", "steps to reproduce", "```")


def _score(issue: Issue, cutoff_days: int) -> float:
    age_days = (datetime.now(timezone.utc) - issue.updated_at).days
    freshness = max(0.0, min(1.0, (cutoff_days - age_days) / cutoff_days))
    kind_w = KIND_WEIGHT.get(issue.kind, 0.5)
    score = freshness * kind_w
    if "⚠maintainer-authored" in issue.flags:
        score -= 0.2
    body_low = issue.body.lower()
    if any(m in body_low for m in REPRO_MARKERS):
        score += 0.1
    return score


def rank(issues: list[Issue], cutoff_days: int) -> list[Issue]:
    """Stage 5: order by freshness × kind-weight × repro signal, minus flag penalties."""
    issues.sort(key=lambda i: _score(i, cutoff_days), reverse=True)
    return issues


def _format_issue_line(i: Issue) -> str:
    badges = f"[{i.kind}]"
    if i.flags:
        badges += " " + " ".join(i.flags)
    return f"- {badges} [#{i.number}]({i.url}) {i.title}"


def _render_category_section(
    title: str,
    items: list[Issue],
    per_section_limit: int,
) -> list[str]:
    lines = [f"## {title}", ""]
    by_repo: dict[str, list[Issue]] = {}
    for i in items:
        by_repo.setdefault(i.repo, []).append(i)
    for repo in sorted(by_repo):  # deterministic; alphabetic groups sglang above vllm
        lines.append(f"### {repo}")
        lines.append("")
        for i in by_repo[repo][:per_section_limit]:
            lines.append(_format_issue_line(i))
        lines.append("")
    return lines


def write_digest(issues: list[Issue], categories: list[dict], per_section_limit: int) -> None:
    """Stage 6: emit RADAR.md, one section per category, vLLM/SGLang subsections."""
    lines: list[str] = []
    lines.append("# LLM Serving Issue Radar")
    lines.append("")
    lines.append(f"_Last run: {datetime.now(timezone.utc).isoformat(timespec='minutes')}_")
    lines.append("")

    if not issues:
        lines.append("No matching issues after filtering.")
        lines.append("")
        OUTPUT_PATH.write_text("\n".join(lines))
        print(f"wrote {OUTPUT_PATH} (0 issues)")
        return

    by_cat: dict[str, list[Issue]] = {}
    for i in issues:
        by_cat.setdefault(i.category, []).append(i)

    # Summary line: totals per repo, then per category (in config order).
    per_repo_counts = {}
    for i in issues:
        per_repo_counts[i.repo] = per_repo_counts.get(i.repo, 0) + 1
    repo_summary = ", ".join(f"{k}: {v}" for k, v in sorted(per_repo_counts.items()))
    lines.append(f"**{len(issues)} issues** — {repo_summary}")
    lines.append("")

    # Table of contents.
    lines.append("## Contents")
    lines.append("")
    for cat in categories:
        cid = cat["id"]
        if cid in by_cat:
            lines.append(f"- [{cat['title']}](#{cat['title'].lower().replace(' ', '-').replace('/', '')}) — {len(by_cat[cid])}")
    if "uncategorized" in by_cat:
        lines.append(f"- [Uncategorized](#uncategorized) — {len(by_cat['uncategorized'])}")
    lines.append("")

    # Categories in config order.
    for cat in categories:
        cid = cat["id"]
        if cid not in by_cat:
            continue
        lines.extend(_render_category_section(cat["title"], by_cat[cid], per_section_limit))

    # Uncategorized last.
    if "uncategorized" in by_cat:
        lines.extend(_render_category_section("Uncategorized", by_cat["uncategorized"], per_section_limit))

    OUTPUT_PATH.write_text("\n".join(lines))
    print(f"wrote {OUTPUT_PATH} ({len(issues)} issues)")


# ---------- entry ----------

def main() -> int:
    cfg = load_config()
    kinds = cfg.get("kinds", {})
    exclude_kinds = kinds.get("exclude", [])
    keep_kinds = kinds.get("keep", [])
    all_issues: list[Issue] = []
    for repo in cfg["repos"]:
        raw = fetch_issues(repo, cfg["limits"]["per_repo_issue_limit"])
        after_noise = filter_noise(
            raw, cfg["limits"]["max_age_days"], exclude_kinds, keep_kinds
        )
        after_pr = drop_issues_with_open_pr(
            after_noise, repo, cfg["limits"]["max_pr_checks_per_repo"]
        )
        print(
            f"{repo}: fetched={len(raw)} "
            f"after_noise={len(after_noise)} "
            f"after_pr_check={len(after_pr)}"
        )
        all_issues.extend(after_pr)

    all_issues = classify(all_issues, cfg["categories"])
    all_issues = rank(all_issues, cfg["limits"]["max_age_days"])
    write_digest(all_issues, cfg["categories"], cfg["limits"]["per_section_limit"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
