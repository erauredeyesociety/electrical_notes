#!/usr/bin/env python3
"""Extract course materials to readable Markdown.

AUTOMATION -- never submitted.

    ./extract_notes.py                 extract everything that is out of date
    ./extract_notes.py --force         re-extract even if up to date
    ./extract_notes.py --list          show what would be done, change nothing
    ./extract_notes.py --only wireshark   only stems matching a substring

Source selection, per document stem:

    .docx  -> pandoc          BEST: keeps headings, lists, bold, and pulls the
                              embedded images out as real files.
    .pdf   -> PyMuPDF         Good: page-by-page text with page markers.
    .pptx  -> deliberately NOT used.

Why pptx is skipped: measured on this material, the pptx text layer is the same
text the PDF already carries ("Application Layer": 47,898 chars from pptx vs
47,990 from the PDF; "Intro and Syllabus": 676 vs 600). pandoc cannot read pptx
at all -- it only writes it -- so using pptx would mean hand-parsing slide XML
for no gain. When both a pptx and a pdf exist, the pdf is the better source.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC_DEFAULT = HERE.parent / "class_materials"
OUT_DEFAULT = HERE.parent / "md_notes"

# A page averaging fewer than this many characters is effectively image-only:
# a scanned page or a picture-heavy slide. Flagged, not skipped.
MIN_CHARS_PER_PAGE = 400


def slugify(name: str) -> str:
    """'Introduction to Wireshark' -> 'introduction_to_wireshark'."""
    s = re.sub(r"[^\w\s-]", "", name.lower())
    return re.sub(r"[\s-]+", "_", s).strip("_")


def pick_source(paths: list[Path]) -> Path | None:
    """Best available source for one document. docx beats pdf beats nothing."""
    by_ext = {p.suffix.lower(): p for p in paths}
    for ext in (".docx", ".pdf"):
        if ext in by_ext:
            return by_ext[ext]
    return None


def from_docx(src: Path, out_md: Path, media: Path) -> str:
    """pandoc docx -> markdown, with embedded images written under media/<slug>/."""
    if not shutil.which("pandoc"):
        raise RuntimeError("pandoc not found; install it or delete the .docx")
    media.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(src), "-t", "markdown", "--wrap=none",
         f"--extract-media={media}", "-o", str(out_md)],
        check=True, capture_output=True, timeout=300,
    )

    # pandoc always writes into a `media/` subfolder of --extract-media, giving
    # media/<slug>/media/image1.png. Flatten that away so links read
    # media/<slug>/image1.png.
    nested = media / "media"
    if nested.is_dir():
        for f in nested.iterdir():
            f.rename(media / f.name)
        nested.rmdir()

    text = out_md.read_text(encoding="utf-8", errors="replace")
    # pandoc writes ABSOLUTE image paths. Make them relative TO THE .md FILE,
    # which lives in out/ -- so strip out/, not out/media/. Getting this wrong
    # silently produces links that resolve nowhere.
    text = text.replace(str(out_md.parent) + "/", "")
    text = text.replace(f"{media.name}/media/", f"{media.name}/")
    # Drop pandoc's width/height attrs -- they are Word layout, not content.
    text = re.sub(r'\{width="[^"]*"\s*height="[^"]*"\}', "", text)
    # pandoc backslash-escapes apostrophes and quotes for round-tripping, which
    # renders as doesn\'t. Nothing here is round-tripped, so unescape for reading.
    text = re.sub(r"\\(['\"\[\]$*_])", r"\1", text)
    return text


def from_pdf(src: Path, media: Path) -> tuple[str, int, float]:
    """PyMuPDF pdf -> markdown with page markers. Returns (text, pages, ch/pg)."""
    import fitz

    doc = fitz.open(src)
    parts, total = [], 0
    for i, page in enumerate(doc, start=1):
        body = page.get_text().strip()
        total += len(body)
        parts.append(f"\n\n---\n\n## Page {i}\n\n{body}" if body
                     else f"\n\n---\n\n## Page {i}\n\n*(no text layer on this page)*")
    per_page = total / max(doc.page_count, 1)
    return "".join(parts).strip(), doc.page_count, per_page


def header(title: str, src: Path, note: str = "") -> str:
    # Angle-bracket the target: these filenames contain spaces, which break a
    # bare markdown link.
    rel = f"<../class_materials/{src.name}>"
    lines = [
        f"# {title}",
        "",
        f"*Extracted from [`{src.name}`]({rel}) by `tools/extract_notes.py`.*",
        "*Generated file -- edit the source, not this.*",
    ]
    if note:
        lines += ["", note]
    return "\n".join(lines) + "\n\n---\n\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", nargs="?", type=Path, default=SRC_DEFAULT)
    ap.add_argument("-o", "--out", type=Path, default=OUT_DEFAULT)
    ap.add_argument("--force", action="store_true", help="re-extract even if up to date")
    ap.add_argument("--list", action="store_true", help="show plan, change nothing")
    ap.add_argument("--only", metavar="SUBSTR", help="only stems containing SUBSTR")
    args = ap.parse_args()

    if not args.src.is_dir():
        print(f"error: no such directory: {args.src}", file=sys.stderr)
        return 1

    # Group files by stem so "X.pdf" and "X.docx" are one document.
    groups: dict[str, list[Path]] = {}
    for p in sorted(args.src.iterdir()):
        if p.is_file() and p.suffix.lower() in (".pdf", ".docx", ".pptx"):
            groups.setdefault(p.stem, []).append(p)

    if args.only:
        needle = args.only.lower()
        groups = {k: v for k, v in groups.items() if needle in k.lower()}
    if not groups:
        print("nothing to extract")
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    warnings: list[str] = []
    n_done = 0

    for stem, paths in sorted(groups.items()):
        src = pick_source(paths)
        slug = slugify(stem)
        out_md = args.out / f"{slug}.md"
        skipped = [p.suffix.lstrip(".") for p in paths if p != src]
        tag = f"{src.suffix.lstrip('.')}" + (f" (also have: {', '.join(skipped)})" if skipped else "")

        if src is None:
            warnings.append(f"{stem}: no usable source")
            continue

        # Up-to-date check: output newer than source and non-empty.
        if not args.force and out_md.exists() and out_md.stat().st_mtime >= src.stat().st_mtime:
            print(f"  up to date  {out_md.name:<38} <- {tag}")
            continue

        if args.list:
            print(f"  would build {out_md.name:<38} <- {tag}")
            continue

        media = args.out / "media" / slug
        try:
            if src.suffix.lower() == ".docx":
                body = from_docx(src, out_md, media)
                note = ""
            else:
                body, pages, per_page = from_pdf(src, media)
                note = ""
                if per_page < MIN_CHARS_PER_PAGE:
                    note = (f"> ⚠ **Low text density** -- {per_page:.0f} chars/page over {pages} "
                            f"pages. This document is mostly images; the text below is only what "
                            f"the PDF text layer carries. Open the original for the diagrams.")
                    warnings.append(f"{stem}: {per_page:.0f} ch/page ({pages}p) -- mostly images")
            out_md.write_text(header(stem, src, note) + body + "\n", encoding="utf-8")
            size = out_md.stat().st_size
            print(f"  built       {out_md.name:<38} <- {tag}  ({size/1024:.0f} KB)")
            n_done += 1
        except subprocess.CalledProcessError as e:
            warnings.append(f"{stem}: pandoc failed -- {e.stderr.decode()[:160]}")
        except Exception as e:  # noqa: BLE001 - report, never abort the batch
            warnings.append(f"{stem}: {type(e).__name__}: {e}")

    if warnings:
        print("\nwarnings:")
        for w in warnings:
            print(f"  ! {w}")
    if not args.list:
        print(f"\n{n_done} file(s) written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
