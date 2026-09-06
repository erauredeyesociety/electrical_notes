"""PDF inspection and rendering. No ML.

Everything here is deterministic and cheap. Run it before reaching for any
model -- most pages need no recognition at all, and this module is what proves
which ones those are.

**Classification lives in `textlayer.py` and nowhere else.** This module used
to carry a second implementation of it, on a second PDF library: poppler's
`pdftotext` + `pdfimages` behind subprocess, with its own 400-char threshold.
Two libraries answering one question is the exact divergence this project
exists to end, and ADR-0001 said so. `inspect` / `inspect_all` / `page_count` /
`page_text` / `producer` are now thin views over `textlayer.extract`, so there
is one classifier, on PyMuPDF, with one threshold.

What that convergence CHANGED is measured, not assumed:
docs/findings/one-classifier-2026-09-06.md.

`render` is the one poppler call left, and it is deliberate -- see its
docstring. Removing it is roadmap M4, not M2.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from . import textlayer
# Single source of truth for "is this page's text layer usable?".
# Defined in textlayer.py and re-exported here: two independent 400s is exactly
# the divergence this project exists to eliminate, and having it inside the
# project would be the worst version of it.
from .textlayer import SPARSE_CHARS as TEXT_LAYER_MIN_CHARS  # noqa: F401


@dataclass
class PageInfo:
    """What a single page contains, before any recognition."""

    number: int
    chars: int
    images: int
    has_text_layer: bool
    drawings: int | None = None       # vector paths; None = not measured
    drawn_images: int | None = None   # images painted from a Form XObject

    @property
    def kind(self) -> str:
        """Route the page. This decides whether a model is needed at all.

        `blank` means *nothing is on this page*, so all three counts have to
        agree. Measured 2026-09-06: testing `images` alone called 405 pages
        blank that carry vector content -- one of them 1,837 paths and 8.9%
        non-white pixels -- and one more that carries an image `get_images()`
        cannot see. See `textlayer.PageText.skip_reason`.
        """
        if self.has_text_layer:
            return "text"          # extract directly, no model
        if self.images or self.drawings or self.drawn_images:
            return "image"         # content is in pixels or vector paths:
            #                        needs render + crop + recognition
        return "blank"


def _run(cmd: list[str]) -> str:
    """Run a poppler tool, returning stdout and swallowing tool noise."""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return out.stdout
    except (subprocess.SubprocessError, FileNotFoundError):
        return ""


def _open(pdf: Path):
    import pymupdf
    return pymupdf.open(pdf)


def page_count(pdf: Path) -> int:
    doc = _open(pdf)
    try:
        return doc.page_count
    finally:
        doc.close()


def producer(pdf: Path) -> str:
    """The generating application.

    This is the cheapest reliable way to tell an annotated file from a
    recompiled one -- 'PDF Annotator' means real ink was added, while a
    pdfTeX/Ghostscript producer on both files means the source was rebuilt.
    """
    doc = _open(pdf)
    try:
        return (doc.metadata or {}).get("producer") or ""
    finally:
        doc.close()


def page_text(pdf: Path, page: int) -> str:
    """One page's text layer. `page` is 1-based."""
    pages = textlayer.extract(pdf, [page]).pages
    return pages[0].text if pages else ""


def _info(p: textlayer.PageText) -> PageInfo:
    """One `textlayer` page record, as this module's routing view of it."""
    return PageInfo(
        number=p.page,
        chars=p.chars,
        images=p.images,
        has_text_layer=not p.needs_ocr,
        drawings=p.drawings,
        drawn_images=p.drawn_images,
    )


def inspect(pdf: Path, page: int) -> PageInfo:
    """Classify one page without rendering it."""
    pages = textlayer.extract(pdf, [page]).pages
    if not pages:
        raise IndexError(f"{pdf}: no page {page}")
    return _info(pages[0])


def inspect_all(pdf: Path) -> list[PageInfo]:
    return [_info(p) for p in textlayer.extract(pdf).pages]


def render(pdf: Path, page: int, out_dir: Path, dpi: int = 200) -> Path:
    """Render one page to PNG.

    200 dpi is the default because it is where handwritten subscripts became
    reliably readable in testing; 150 lost them, 300 only cost time.

    STILL POPPLER, on purpose. ADR-0001 wants this on PyMuPDF too, but the two
    renderers differ on 6.66% of pixels from antialiasing alone, and the ink
    path's constants are calibrated against THESE pixels: `ink.red_mask` on
    this file yields a count the floor pins to 7,000-9,500, and `merge_px=64`
    is a pixel distance measured at 200 dpi. Swapping the renderer without
    re-sweeping both would move numbers the regression floor is guarding.
    That re-sweep is roadmap M4, which serves the 2-document ink path; M2 is
    the 430-document classifier and this is not on it.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / f"p{page:03d}"
    _run([
        "pdftoppm", "-png", "-r", str(dpi),
        "-f", str(page), "-l", str(page), str(pdf), str(stem),
    ])
    hits = sorted(out_dir.glob(f"p{page:03d}*.png"))
    if not hits:
        raise RuntimeError(f"render failed: {pdf} page {page}")
    return hits[0]


def find_base(annotated: Path) -> Path | None:
    """Locate the un-annotated twin of a '-plw' file.

    Pairing lets the annotation layer be isolated by differencing, which is
    more reliable than colour alone when the ink is not obviously coloured.
    """
    name = annotated.name
    for suffix in ("-plw", "_plw"):
        if suffix in name:
            candidate = annotated.with_name(name.replace(suffix, ""))
            return candidate if candidate.exists() else None
    return None
