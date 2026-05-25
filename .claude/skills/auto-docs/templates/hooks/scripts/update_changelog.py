#!/usr/bin/env python3
"""
update_changelog.py — Auto-append the last commit to CHANGELOG.md.

Runs after every git commit (called from .git/hooks/post-commit).
Reads the latest commit message and prepends an entry to CHANGELOG.md
under the appropriate section.
"""

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

CHANGELOG_PATH = Path("CHANGELOG.md")
PREFIXES = {"feat", "fix", "chore", "refactor", "test", "docs", "perf", "style"}


def get_last_commit():
    """Return (subject, hash) of the latest commit."""
    try:
        subject = subprocess.run(
            ["git", "log", "-1", "--pretty=%s"],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        short_hash = subprocess.run(
            ["git", "log", "-1", "--pretty=%h"],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        return subject, short_hash
    except subprocess.CalledProcessError:
        return None, None


def is_valid_commit(msg):
    """Only log commits with a known conventional commit prefix."""
    if not msg:
        return False
    prefix = msg.split(":", 1)[0].split("(", 1)[0].strip().lower()
    return prefix in PREFIXES


def already_logged(changelog_text, short_hash):
    """Don't double-log the same commit."""
    return short_hash in changelog_text


def prepend_entry(commit_msg, short_hash):
    """Add a new entry under [Unreleased] section."""
    if not CHANGELOG_PATH.exists():
        print(f"⚠️  CHANGELOG.md not found. Run /auto-docs init first.")
        return False

    text = CHANGELOG_PATH.read_text(encoding="utf-8")

    if already_logged(text, short_hash):
        return False

    today = date.today().isoformat()
    entry = f"- {commit_msg} ({short_hash})"

    if "## [Unreleased]" in text:
        text = text.replace(
            "## [Unreleased]",
            f"## [Unreleased]\n\n{entry}",
            1
        )
    else:
        # Insert after the title block
        lines = text.split("\n")
        # Find first ## section, or just prepend
        insert_at = 0
        for i, line in enumerate(lines):
            if line.startswith("## "):
                insert_at = i
                break
        lines.insert(insert_at, f"## [Unreleased] — {today}\n\n{entry}\n")
        text = "\n".join(lines)

    CHANGELOG_PATH.write_text(text, encoding="utf-8")
    return True


def main():
    commit_msg, short_hash = get_last_commit()
    if not commit_msg:
        print("⚠️  Could not read last commit.")
        sys.exit(0)

    if not is_valid_commit(commit_msg):
        # Silently skip — not all commits need a changelog entry
        sys.exit(0)

    if prepend_entry(commit_msg, short_hash):
        print(f"✅ CHANGELOG.md updated: {commit_msg}")
    else:
        # Already logged or no file — silent
        sys.exit(0)


if __name__ == "__main__":
    main()
