#!/usr/bin/env python3
"""Refresh TRACKING.md — build per-issue timelines for issues you're following.

Reads the tracked-issue list from TRACKING.md's config header (above the
AUTOGEN marker), fetches timeline + comments + issue meta for each via `gh`,
and rewrites everything below the marker with a per-issue timeline.

Each timeline node is a single event; timelines stop growing once the issue
is closed or its fixing PR merges. Config header is preserved verbatim.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

TRACKING_PATH = Path(__file__).parent / "TRACKING.md"

CONFIG_HEADER = (
    "<!-- TRACKING: add/remove issue keys below "
    "(auto-refreshed below the marker) -->"
)
CONFIG_END = "<!-- END TRACKING CONFIG -->"
AUTOGEN_MARKER = "<!-- AUTOGEN: everything below is regenerated on each run -->"

TRACKED_RE = re.compile(r"^\s*-\s+([\w.-]+/[\w.-]+)#(\d+)\s*$")

# Timeline events we render; others are dropped as noise.
KEEP_EVENTS = {
    "opened",
    "closed",
    "reopened",
    "commented",
    "cross-referenced",
    "assigned",
    "unassigned",
    "labeled",  # kept only for the initial [Bug]/[RFC]-shaped labels; noisy otherwise
    "merged",
    "review_requested",
}


@dataclass
class Event:
    at: datetime
    kind: str  # normalized single-word tag
    actor: str
    detail: str = ""


@dataclass
class Timeline:
    repo: str
    number: int
    title: str = ""
    state: str = "unknown"
    state_reason: str | None = None
    is_pr: bool = False
    events: list[Event] = field(default_factory=list)


def gh_api(path: str) -> list | dict:
    proc = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True, check=True, timeout=30
    )
    return json.loads(proc.stdout) if proc.stdout.strip() else []


def parse_config(text: str) -> list[tuple[str, int]]:
    """Extract tracked issue keys from the config header block."""
    if CONFIG_HEADER not in text:
        return []
    start = text.index(CONFIG_HEADER) + len(CONFIG_HEADER)
    end = text.index(CONFIG_END, start) if CONFIG_END in text else len(text)
    keys: list[tuple[str, int]] = []
    for line in text[start:end].splitlines():
        m = TRACKED_RE.match(line)
        if m:
            keys.append((m.group(1), int(m.group(2))))
    return keys


def parse_dt(iso: str | None) -> datetime | None:
    if not iso:
        return None
    return datetime.fromisoformat(iso.replace("Z", "+00:00"))


def build_timeline(repo: str, number: int) -> Timeline:
    issue = gh_api(f"repos/{repo}/issues/{number}")
    tl = Timeline(
        repo=repo,
        number=number,
        title=issue.get("title", ""),
        state=issue.get("state", "unknown"),
        state_reason=issue.get("state_reason"),
        is_pr=issue.get("pull_request") is not None,
    )

    events: list[Event] = [
        Event(
            at=parse_dt(issue["created_at"]),
            kind="opened",
            actor=(issue.get("user") or {}).get("login", "?"),
            detail=f"as `{issue.get('author_association', 'NONE')}`",
        )
    ]

    raw = gh_api(f"repos/{repo}/issues/{number}/timeline?per_page=100")
    for ev in raw:
        kind = ev.get("event")
        if kind not in KEEP_EVENTS:
            continue
        at = parse_dt(ev.get("created_at") or ev.get("submitted_at") or ev.get("committed_at"))
        if at is None:
            continue
        actor = (
            (ev.get("actor") or {}).get("login")
            or (ev.get("user") or {}).get("login")
            or "?"
        )
        detail = ""
        if kind == "labeled":
            label = (ev.get("label") or {}).get("name", "")
            # Keep only informative first-appearance labels; skip most churn.
            if label.lower() in {"bug", "rfc", "feature", "enhancement"}:
                detail = f"`{label}`"
            else:
                continue
        elif kind == "cross-referenced":
            src = (ev.get("source") or {}).get("issue") or {}
            is_pr = src.get("pull_request") is not None
            state = src.get("state", "?")
            url = src.get("html_url", "")
            what = "PR" if is_pr else "issue"
            detail = f"{what} [{url}]({url}) ({state})"
        elif kind == "closed":
            reason = ev.get("state_reason") or (issue.get("state_reason") if issue.get("state") == "closed" else None)
            detail = f"as `{reason}`" if reason else ""
        elif kind == "assigned":
            assignee = (ev.get("assignee") or {}).get("login", "")
            detail = f"@{assignee}" if assignee else ""
        elif kind == "commented":
            body = (ev.get("body") or "").strip().replace("\r", "")
            snippet = body.split("\n")[0][:100]
            detail = snippet
        events.append(Event(at=at, kind=kind, actor=actor, detail=detail))

    events.sort(key=lambda e: e.at)
    tl.events = events
    return tl


EVENT_ICON = {
    "opened": "🆕",
    "closed": "✅",
    "reopened": "↩️",
    "commented": "💬",
    "cross-referenced": "🔗",
    "assigned": "👤",
    "unassigned": "👤",
    "labeled": "🏷",
    "merged": "🎉",
    "review_requested": "👀",
}


def render_timeline(tl: Timeline) -> list[str]:
    lines: list[str] = []
    lines.append(f"## {tl.repo}#{tl.number}  {tl.title}")
    lines.append("")
    state_marker = "✅" if tl.state == "closed" else "⏳"
    state_line = f"Status: **{tl.state}**"
    if tl.state == "closed" and tl.state_reason:
        state_line += f" (`{tl.state_reason}`)"
    lines.append(f"{state_marker} {state_line} — <https://github.com/{tl.repo}/issues/{tl.number}>")
    lines.append("")

    for ev in tl.events:
        icon = EVENT_ICON.get(ev.kind, "·")
        at_str = ev.at.strftime("%Y-%m-%d %H:%M")
        parts = [at_str, icon, ev.kind, f"by @{ev.actor}"]
        if ev.detail:
            parts.append(f"— {ev.detail}")
        lines.append(f"- {' '.join(parts)}")

    if tl.state == "open":
        lines.append("- ⏳ **still open**")
    lines.append("")
    return lines


def initial_scaffold() -> str:
    return (
        f"{CONFIG_HEADER}\n"
        "- \n"
        f"{CONFIG_END}\n"
        "\n"
        f"{AUTOGEN_MARKER}\n"
        "\n"
        "# Tracking\n"
        "\n"
        "_No issues tracked yet. Add `owner/repo#number` lines above the "
        "`END TRACKING CONFIG` marker._\n"
    )


def refresh() -> int:
    if TRACKING_PATH.exists():
        text = TRACKING_PATH.read_text()
    else:
        text = initial_scaffold()

    keys = parse_config(text)

    # Preserve everything up to and including the AUTOGEN marker.
    if AUTOGEN_MARKER in text:
        head = text.split(AUTOGEN_MARKER, 1)[0] + AUTOGEN_MARKER
    else:
        # Legacy / hand-written file: insert marker after CONFIG_END if present.
        anchor = CONFIG_END if CONFIG_END in text else text.rstrip()
        head = text.split(anchor, 1)[0] + anchor + "\n\n" + AUTOGEN_MARKER

    out: list[str] = [head, ""]
    out.append("# Tracking")
    out.append("")
    if not keys:
        out.append("_No issues tracked yet._")
        out.append("")
    else:
        out.append(f"_{len(keys)} issue{'s' if len(keys) != 1 else ''} tracked. "
                   f"Refreshed {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}._")
        out.append("")
        for repo, number in keys:
            try:
                tl = build_timeline(repo, number)
                out.extend(render_timeline(tl))
            except subprocess.CalledProcessError as e:
                out.append(f"## {repo}#{number}")
                out.append("")
                out.append(f"⚠️ fetch failed: `{e.stderr.strip().splitlines()[0] if e.stderr else 'unknown error'}`")
                out.append("")

    TRACKING_PATH.write_text("\n".join(out).rstrip() + "\n")
    print(f"wrote {TRACKING_PATH} ({len(keys)} tracked issues)")
    return 0


if __name__ == "__main__":
    sys.exit(refresh())
