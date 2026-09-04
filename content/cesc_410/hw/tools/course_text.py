#!/usr/bin/env python3
"""Extract text from CESC 410 course materials so homework can cite them.

AUTOMATION -- never submitted.

The point is to stop guessing at what the course actually said. Lecture PDFs
and lab handouts are the authority for notation and method; this makes them
greppable in one command instead of one PDF at a time.

    tools/course_text.py --list                 what is available, and whether
                                                it has a usable text layer
    tools/course_text.py --dump out/            write every .txt
    tools/course_text.py --grep "periodic"      search everything, with source

Pages with no text layer are REPORTED, not silently skipped -- handwritten
lecture notes have almost none, and pretending otherwise is how a wrong
citation gets written. Those need ocr_handler (../../../ocr_handler).
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COURSE = HERE.parent.parent                      # content/cesc_410
SOURCES = [COURSE / "lectures", COURSE / "labs_and_projects", COURSE / "hw"]

# Below this many characters per page, the page is images/handwriting, not text.
# Same threshold ocr_handler uses, for the same reason.
MIN_CHARS_PER_PAGE = 400


def pdf_text(pdf: Path) -> str:
    try:
        r = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                           capture_output=True, text=True, timeout=120)
        return r.stdout
    except (subprocess.SubprocessError, FileNotFoundError):
        return ""


def pages(pdf: Path) -> int:
    try:
        r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, timeout=30)
        m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
        return int(m.group(1)) if m else 0
    except (subprocess.SubprocessError, FileNotFoundError):
        return 0


def collect():
    """Every source document, with its text and a usability verdict."""
    out = []
    for root in SOURCES:
        if not root.is_dir():
            continue
        for p in sorted(root.rglob("*")):
            # Exclude build/dependency trees for EVERY file type. A first pass
            # only filtered text files and pulled in matplotlib's icon PDFs
            # from .venv, which drowned the real material.
            if any(x in p.parts for x in (".venv", "__pycache__", "tmp",
                                          "node_modules", ".git", "figs")):
                continue
            if p.suffix.lower() == ".pdf":
                text = pdf_text(p)
                n = pages(p) or 1
                out.append((p, text, len(text.strip()) / n >= MIN_CHARS_PER_PAGE))
            elif p.suffix.lower() in {".md", ".txt", ".tex"}:
                out.append((p, p.read_text(errors="replace"), True))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--list", action="store_true", help="inventory + text-layer verdict")
    g.add_argument("--dump", type=Path, metavar="DIR", help="write .txt for each source")
    g.add_argument("--grep", metavar="PATTERN", help="case-insensitive search, with source")
    ap.add_argument("-C", "--context", type=int, default=1, help="lines of context for --grep")
    args = ap.parse_args()

    docs = collect()
    if not docs:
        print("no course materials found", file=sys.stderr)
        return 1

    if args.list:
        usable = sum(1 for _, _, ok in docs if ok)
        print(f"{len(docs)} documents, {usable} with a usable text layer\n")
        for p, text, ok in docs:
            flag = "   " if ok else "NO-TEXT"
            print(f"  {flag} {len(text.strip()):>7,}c  {p.relative_to(COURSE)}")
        if usable < len(docs):
            print(f"\n{len(docs) - usable} document(s) have no usable text layer.")
            print("Those are handwriting/scans -- use ocr_handler, do not guess at them.")
        return 0

    if args.dump:
        args.dump.mkdir(parents=True, exist_ok=True)
        for p, text, ok in docs:
            if not ok:
                continue
            name = str(p.relative_to(COURSE)).replace("/", "__") + ".txt"
            (args.dump / name).write_text(text)
        print(f"wrote {sum(1 for _, _, ok in docs if ok)} files to {args.dump}")
        return 0

    rx = re.compile(args.grep, re.I)
    hits = 0
    for p, text, ok in docs:
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if not rx.search(line):
                continue
            hits += 1
            print(f"\n{p.relative_to(COURSE)}:{i + 1}")
            lo, hi = max(0, i - args.context), min(len(lines), i + args.context + 1)
            for j in range(lo, hi):
                mark = ">" if j == i else " "
                print(f"  {mark} {lines[j].rstrip()[:110]}")
    print(f"\n{hits} match(es)" if hits else "\nno matches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
