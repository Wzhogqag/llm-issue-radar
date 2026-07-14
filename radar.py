#!/usr/bin/env python3
"""Scan vLLM + SGLang for unclaimed issues, classify by subsystem, write RADAR.md.

Pipeline (mirrors CNTRL-tek91/issue-radar's shape, adapted for two-repo scope):
    fetch → filter → pr-check → classify → rank → write

Runs on GitHub Actions with GITHUB_TOKEN, or locally with the `gh` CLI logged in.
Standard library + `gh` CLI only — no pip dependencies.
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"
OUTPUT_PATH = Path(__file__).parent / "RADAR.md"
STATE_PATH = Path(__file__).parent / "seen.json"


# ---------- data model ----------

@dataclass
class Issue:
    repo: str
    number: int
    title: str
    body: str
    author: str
    author_type: str  # User / Bot / MEMBER / OWNER
    labels: list[str]
    assignees: list[str]
    created_at: datetime
    updated_at: datetime
    comments: int
    url: str
    category: str = "uncategorized"
    flags: list[str] = field(default_factory=list)


# ---------- stages ----------

def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text())


def fetch_issues(repo: str, limit: int) -> list[Issue]:
    """Stage 1: pull open issues via `gh` REST list endpoint."""
    # TODO(Phase 3): implement gh api repos/{repo}/issues?state=open&per_page=...
    return []


def filter_noise(issues: list[Issue], max_age_days: int) -> list[Issue]:
    """Stage 2: drop PRs, bots, assigned, stale, template-only."""
    # TODO(Phase 3): implement drop rules
    return issues


def drop_issues_with_open_pr(issues: list[Issue], repo: str, max_checks: int) -> list[Issue]:
    """Stage 3: consult each issue's timeline; skip if an open PR is cross-referenced."""
    # TODO(Phase 3): use gh api repos/{repo}/issues/{n}/timeline
    return issues


def classify(issues: list[Issue], categories: list[dict]) -> list[Issue]:
    """Stage 4: assign each issue a category via keyword + path match."""
    # TODO(Phase 4): score against category rules; pick best-match
    return issues


def rank(issues: list[Issue]) -> list[Issue]:
    """Stage 5: order by freshness × approachability × repro signal."""
    # TODO(Phase 4): score and sort
    return issues


def write_digest(issues: list[Issue], categories: list[dict], per_section_limit: int) -> None:
    """Stage 6: emit RADAR.md, one section per category, vLLM/SGLang subsections."""
    lines: list[str] = []
    lines.append("# LLM Serving Issue Radar")
    lines.append("")
    lines.append(f"_Last run: {datetime.now(timezone.utc).isoformat(timespec='minutes')}_")
    lines.append("")
    lines.append("No issues yet — this is a scaffold. Phase 3 wires up fetching.")
    lines.append("")
    OUTPUT_PATH.write_text("\n".join(lines))
    print(f"wrote {OUTPUT_PATH} ({len(issues)} issues)")


# ---------- entry ----------

def main() -> int:
    cfg = load_config()
    all_issues: list[Issue] = []
    for repo in cfg["repos"]:
        raw = fetch_issues(repo, cfg["limits"]["per_repo_issue_limit"])
        raw = filter_noise(raw, cfg["limits"]["max_age_days"])
        raw = drop_issues_with_open_pr(raw, repo, cfg["limits"]["max_pr_checks_per_repo"])
        all_issues.extend(raw)

    all_issues = classify(all_issues, cfg["categories"])
    all_issues = rank(all_issues)
    write_digest(all_issues, cfg["categories"], cfg["limits"]["per_section_limit"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
