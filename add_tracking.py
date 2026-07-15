#!/usr/bin/env python3
"""Add an issue to TRACKING.md and push it up.

Usage:
    python3 add_tracking.py <owner/repo> <number>
    python3 add_tracking.py <github issue url>
    python3 add_tracking.py <url> [<url> ...]   # multiple in one go

Editable config header: this script just inserts a `- owner/repo#num` line
above the END-CONFIG marker (skipping duplicates), then runs tracking.py to
refresh, then git add + commit + push. Nothing else.

Fails loud on git errors; safe to re-run if network flakes.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
TRACKING_PATH = REPO_ROOT / "TRACKING.md"

CONFIG_HEADER = "<!-- TRACKING: add/remove issue keys below (auto-refreshed below the marker) -->"
CONFIG_END = "<!-- END TRACKING CONFIG -->"

URL_RE = re.compile(r"https://github\.com/([\w.-]+/[\w.-]+)/(?:issues|pull)/(\d+)")
KEY_RE = re.compile(r"^([\w.-]+/[\w.-]+)#(\d+)$")


def parse_target(arg: str) -> tuple[str, int]:
    m = URL_RE.match(arg)
    if m:
        return m.group(1), int(m.group(2))
    m = KEY_RE.match(arg)
    if m:
        return m.group(1), int(m.group(2))
    sys.exit(f"cannot parse target: {arg!r} (expected URL or owner/repo#num)")


def collect_targets(argv: list[str]) -> list[tuple[str, int]]:
    if len(argv) == 3 and argv[1].count("/") == 1 and argv[2].isdigit():
        return [(argv[1], int(argv[2]))]
    if len(argv) >= 2:
        return [parse_target(a) for a in argv[1:]]
    sys.exit(
        "usage:\n"
        "  add_tracking.py <owner/repo> <number>\n"
        "  add_tracking.py <url> [<url> ...]"
    )


def ensure_tracking_file() -> None:
    if TRACKING_PATH.exists():
        return
    TRACKING_PATH.write_text(
        f"{CONFIG_HEADER}\n{CONFIG_END}\n\n"
        "<!-- AUTOGEN: everything below is regenerated on each run -->\n"
    )


def insert_keys(new_keys: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Insert keys above CONFIG_END. Returns keys actually added (dedup)."""
    text = TRACKING_PATH.read_text()
    if CONFIG_HEADER not in text or CONFIG_END not in text:
        sys.exit(f"{TRACKING_PATH.name} is missing config markers; edit or delete and retry")

    head, rest = text.split(CONFIG_HEADER, 1)
    config_body, tail = rest.split(CONFIG_END, 1)

    existing = set()
    for line in config_body.splitlines():
        m = re.match(r"^\s*-\s+([\w.-]+/[\w.-]+)#(\d+)\s*$", line)
        if m:
            existing.add((m.group(1), int(m.group(2))))

    added: list[tuple[str, int]] = []
    to_append = []
    for k in new_keys:
        if k in existing:
            print(f"skip {k[0]}#{k[1]} (already tracked)")
            continue
        to_append.append(f"- {k[0]}#{k[1]}")
        added.append(k)

    if not added:
        return []

    # Keep existing lines verbatim; append new ones at the end of the config block.
    body_lines = config_body.rstrip("\n").splitlines()
    # Drop trailing blank/empty-hyphen placeholder lines.
    while body_lines and body_lines[-1].strip() in ("", "-"):
        body_lines.pop()
    body_lines.extend(to_append)
    new_body = "\n" + "\n".join(body_lines) + "\n"

    TRACKING_PATH.write_text(
        head + CONFIG_HEADER + new_body + CONFIG_END + tail
    )
    return added


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=REPO_ROOT, check=True, text=True, **kw)


def refresh_and_push(added: list[tuple[str, int]]) -> None:
    if not added:
        print("nothing to add")
        return

    print("refreshing TRACKING.md...")
    run(["python3", "tracking.py"])

    print("staging + committing...")
    run(["git", "add", "TRACKING.md"])
    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT
    )
    if diff.returncode == 0:
        print("no changes to commit (already up to date)")
        return
    joined = ", ".join(f"{r}#{n}" for r, n in added)
    msg = f"tracking: add {joined}"
    run(["git", "commit", "-m", msg])
    print("pushing...")
    run(["git", "push"])
    print("done.")


def main() -> int:
    targets = collect_targets(sys.argv)
    ensure_tracking_file()
    added = insert_keys(targets)
    refresh_and_push(added)
    return 0


if __name__ == "__main__":
    sys.exit(main())
