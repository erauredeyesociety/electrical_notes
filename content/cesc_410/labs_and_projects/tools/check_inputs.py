#!/usr/bin/env python3
"""Find referenced-but-missing files.

AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.

Instructor handouts cross-reference each other and link to starter zips. A link
to a file that was never downloaded is the most common reason a lab stalls, and
only a human can fetch it from Canvas.

    uv run --project dsp26 python tools/check_inputs.py          # everything
    uv run --project dsp26 python tools/check_inputs.py lab00    # one folder
"""

import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(\s*<?([^)>#\s]+)(?:#[^)]*)?\s*>?\)")
SKIP_PREFIX = ("http://", "https://", "mailto:", "ftp://")
SKIP_DIRS = {".venv", "__pycache__", ".git", ".pytest_cache"}


def scan(root: Path) -> int:
    md = [
        p for p in sorted(root.rglob("*.md"))
        if not SKIP_DIRS & set(p.parts)
    ]
    if not md:
        print(f"no markdown under {root}")
        return 0

    # Everything actually on disk, by basename, so we can tell a link that
    # broke because we moved a file from one that was never downloaded.
    on_disk = {}
    for p in root.rglob("*"):
        if p.is_file() and not SKIP_DIRS & set(p.parts):
            on_disk.setdefault(p.name, []).append(p)

    moved, absent = {}, {}
    for p in md:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in LINK.finditer(text):
            target = m.group(1).strip()
            if target.startswith(SKIP_PREFIX) or not target:
                continue
            if (p.parent / target).exists():
                continue
            name = Path(target).name
            bucket = moved if name in on_disk else absent
            bucket.setdefault(name, set()).add(p.relative_to(root))

    print(f"scanned {len(md)} markdown file(s) under {root}\n")
    if not moved and not absent:
        print("OK    every referenced file is present")
        return 0

    if absent:
        print("NOT ON DISK -- needs downloading from Canvas (human):\n")
        for name, srcs in sorted(absent.items()):
            print(f"  {name}")
            for s in sorted(srcs):
                print(f"      referenced by {s}")
        print()

    if moved:
        print("PRESENT ELSEWHERE -- link stale because the file was moved:\n")
        for name, srcs in sorted(moved.items()):
            print(f"  {name}  ->  {on_disk[name][0].relative_to(root)}")
            for s in sorted(srcs):
                print(f"      referenced by {s}")
        print()

    if absent:
        print("Fetch the NOT ON DISK files before starting the lab.")
    if moved:
        print("Stale links inside instructor handouts are expected if we")
        print("reorganised; note them in the lab README rather than editing")
        print("the handout.")
    return 1 if absent else 0


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent
    sys.exit(scan(root))
