#!/usr/bin/env python3
"""Verify a lab's output artifacts.

AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.

Catches the KI-01 class of bug: a figure-numbering mistake in handout code
makes two saved figures the same image. Byte size is the giveaway, because
matplotlib writes randomised element ids into SVG, so identical pictures can
still differ in md5.

    uv run --project dsp26 python tools/check_artifacts.py lab00/figs
"""

import hashlib
import sys
from collections import defaultdict
from pathlib import Path

MIN_BYTES = 1024


def check(folder: Path) -> int:
    if not folder.is_dir():
        print(f"FAIL  no such folder: {folder}")
        return 1

    files = sorted(p for p in folder.iterdir() if p.is_file())
    if not files:
        print(f"FAIL  {folder} is empty")
        return 1

    problems = 0
    by_size = defaultdict(list)
    by_hash = defaultdict(list)

    print(f"{folder}  ({len(files)} files)\n")
    for p in files:
        size = p.stat().st_size
        digest = hashlib.md5(p.read_bytes()).hexdigest()
        by_size[size].append(p.name)
        by_hash[digest].append(p.name)
        flag = "  <-- suspiciously small" if size < MIN_BYTES else ""
        if size < MIN_BYTES:
            problems += 1
        print(f"  {size:>8,}  {digest[:8]}  {p.name}{flag}")

    # Identical bytes: definitely the same artifact saved twice.
    for digest, names in by_hash.items():
        if len(names) > 1:
            problems += 1
            print(f"\nFAIL  byte-identical: {', '.join(names)}")

    # Same size, different bytes, same extension: the KI-01 signature.
    for size, names in by_size.items():
        if len(names) > 1 and len({n for n in names}) == len(names):
            exts = {Path(n).suffix for n in names}
            same_hash = any(len(v) > 1 for v in by_hash.values())
            if len(exts) == 1 and not same_hash:
                problems += 1
                print(
                    f"\nWARN  same size ({size:,} B), different bytes: "
                    f"{', '.join(names)}"
                    "\n      This is the KI-01 signature -- likely the same "
                    "overplotted figure saved twice."
                    "\n      Check for a repeated plt.figure(N) in the lab code."
                )

    print()
    if problems:
        print(f"FAIL  {problems} problem(s). See reference_docs/known_issues.md")
        return 1
    print("OK    artifacts present, non-trivial, and distinct")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(check(Path(sys.argv[1])))
