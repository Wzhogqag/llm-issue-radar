#!/usr/bin/env python3
"""Deep-dive a single issue: fetch metadata, comments, timeline; print a report.

Usage:
    python3 verify.py <owner/repo> <issue_number>
    python3 verify.py <github issue url>

Reads only — no writes, no state files, no CI integration. Complements radar.py:
the digest gives you the shortlist, verify.py tells you whether a candidate is
worth your time before you invest reading the full thread.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone

REPRO_MARKERS = ("traceback", "steps to reproduce", "reproduce:", "how to reproduce")
CODE_FENCE_RE = re.compile(r"```(\w*)\n(.*?)```", re.DOTALL)
URL_RE = re.compile(r"https://github\.com/([^/]+/[^/]+)/(?:issues|pull)/(\d+)")


def gh_api(path: str) -> list | dict:
    proc = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True, check=True, timeout=30
    )
    return json.loads(proc.stdout) if proc.stdout.strip() else []


def parse_args(argv: list[str]) -> tuple[str, int]:
    if len(argv) == 2:
        m = URL_RE.match(argv[1])
        if not m:
            sys.exit("usage: verify.py <owner/repo> <number>  |  verify.py <url>")
        return m.group(1), int(m.group(2))
    if len(argv) == 3:
        return argv[1], int(argv[2])
    sys.exit("usage: verify.py <owner/repo> <number>  |  verify.py <url>")


def humanize_age(iso: str) -> str:
    then = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - then
    days = delta.days
    if days == 0:
        hours = delta.seconds // 3600
        return f"{hours}h ago"
    if days < 30:
        return f"{days}d ago"
    return f"{days // 30}mo ago"


def section(title: str) -> None:
    print(f"\n─── {title} " + "─" * (60 - len(title)))


def report(repo: str, number: int) -> None:
    issue = gh_api(f"repos/{repo}/issues/{number}")
    if issue.get("pull_request"):
        print(f"warning: #{number} is a PR, not an issue")
    timeline = gh_api(f"repos/{repo}/issues/{number}/timeline?per_page=100")
    comments = gh_api(f"repos/{repo}/issues/{number}/comments?per_page=100")

    # 1. Meta
    section("meta")
    print(f"  {issue['html_url']}")
    print(f"  title:       {issue['title']}")
    print(f"  state:       {issue['state']}")
    print(f"  author:      {issue['user']['login']} ({issue.get('author_association', 'NONE')})")
    print(f"  created:     {issue['created_at']}  ({humanize_age(issue['created_at'])})")
    print(f"  updated:     {issue['updated_at']}  ({humanize_age(issue['updated_at'])})")
    print(f"  comments:    {issue['comments']}")
    if issue.get("labels"):
        print(f"  labels:      {', '.join(lb['name'] for lb in issue['labels'])}")
    if issue.get("assignees"):
        print(f"  assignees:   {', '.join(a['login'] for a in issue['assignees'])}")

    # 2. PR relations — dominant actionability signal
    section("PR relations")
    xrefs = [
        ev for ev in timeline
        if ev.get("event") == "cross-referenced"
        and (ev.get("source") or {}).get("type") == "issue"
    ]
    prs = [ev for ev in xrefs if ((ev.get("source") or {}).get("issue") or {}).get("pull_request")]
    open_prs = [ev for ev in prs if ev["source"]["issue"]["state"] == "open"]
    closed_prs = [ev for ev in prs if ev["source"]["issue"]["state"] == "closed"]
    if open_prs:
        print(f"  open PRs (fix in flight):")
        for ev in open_prs:
            iss = ev["source"]["issue"]
            print(f"    - {iss['html_url']}  {iss['title']}")
    if closed_prs:
        print(f"  closed PRs (prior attempts — check why they closed):")
        for ev in closed_prs:
            iss = ev["source"]["issue"]
            merged = "merged" if iss.get("pull_request", {}).get("merged_at") else "closed unmerged"
            print(f"    - [{merged}] {iss['html_url']}  {iss['title']}")
    non_pr_xrefs = [ev for ev in xrefs if not ((ev.get("source") or {}).get("issue") or {}).get("pull_request")]
    if non_pr_xrefs:
        print(f"  related issues:")
        for ev in non_pr_xrefs[:5]:
            iss = ev["source"]["issue"]
            print(f"    - {iss['html_url']}  {iss['title']}")
    if not prs and not non_pr_xrefs:
        print("  (none)")

    # 3. Repro signal
    section("repro signal")
    body = issue.get("body") or ""
    body_low = body.lower()
    markers_hit = [m for m in REPRO_MARKERS if m in body_low]
    code_blocks = CODE_FENCE_RE.findall(body)
    if markers_hit:
        print(f"  markers:     {', '.join(markers_hit)}")
    if code_blocks:
        print(f"  code blocks: {len(code_blocks)} (langs: {', '.join(sorted({lang or '(none)' for lang, _ in code_blocks}))})")
        for lang, blk in code_blocks[:2]:
            head = blk.strip().split("\n")[0][:100]
            print(f"    └─ [{lang or '?'}] {head}")
    if not markers_hit and not code_blocks:
        print("  (no traceback, no code blocks — likely low actionability)")

    # 4. Maintainer signal
    section("maintainer signal")
    maintainer_associations = {"MEMBER", "OWNER", "COLLABORATOR"}
    maint_comments = [
        c for c in comments
        if c.get("author_association") in maintainer_associations
    ]
    if maint_comments:
        print(f"  {len(maint_comments)} maintainer comment(s):")
        for c in maint_comments[:3]:
            snippet = (c.get("body") or "").strip().split("\n")[0][:120]
            print(f"    - @{c['user']['login']} ({c['author_association']}): {snippet}")
    else:
        print("  (no maintainer comments yet)")

    # 5. Verdict — one-line summary
    section("verdict")
    reasons = []
    if open_prs:
        reasons.append(f"has {len(open_prs)} open PR — likely being fixed, low priority to duplicate")
    if closed_prs and not open_prs:
        reasons.append(f"has {len(closed_prs)} closed PR — prior attempt(s), check diffs before starting")
    if not markers_hit and not code_blocks:
        reasons.append("no repro in body — needs more info before actionable")
    if issue.get("author_association") in maintainer_associations:
        reasons.append("authored by maintainer — often self-assigned work in disguise")
    if not reasons:
        reasons.append("clean actionability signals")
    print("  " + "; ".join(reasons))
    print()


def main() -> int:
    repo, number = parse_args(sys.argv)
    try:
        report(repo, number)
    except subprocess.CalledProcessError as e:
        print(f"gh api failed: {e.stderr}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
