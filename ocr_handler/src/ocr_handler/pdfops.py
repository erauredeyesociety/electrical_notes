"""PDF inspection and rendering. No ML.

Everything here is deterministic and cheap. Run it before reaching for any
model -- most pages need no recognition at all, and this module is what proves
which ones those are.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

# A page with more than this many extracted characters has a usable text layer
# and should never be sent to a recognition model. Measured on real lectures:
# born-digital LaTeX pages run ~1500 chars/page, handwriting-scan pages ~140
# (headers and footers only).
TEXT_LAYER_MIN_CHARS = 400


@dataclass
class PageInfo:
    """What a single page contains, before any recognition."""

    number: int
    chars: int
    images: int
    has_text_layer: bool

    @property
    def kind(self) -> str:
        """Route the page. This decides whether a model is needed at all."""
        if self.has_text_layer:
            return "text"          # extract directly, no model
        if self.images:
            return "image"         # figures present, needs crop + recognition
        return "blank"


def _run(cmd: list[str]) -> str:
    """Run a poppler tool, returning stdout and swallowing tool noise."""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return out.stdout
    except (subprocess.SubprocessError, FileNotFoundError):
        return ""


def page_count(pdf: Path) -> int:
    for line in _run(["pdfinfo", str(pdf)]).splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return 0


def producer(pdf: Path) -> str:
    """The generating application.

    This is the cheapest reliable way to tell an annotated file from a
    recompiled one -- 'PDF Annotator' means real ink was added, while a
    pdfTeX/Ghostscript producer on both files means the source was rebuilt.
    """
    for line in _run(["pdfinfo", str(pdf)]).splitlines():
        if line.startswith("Producer:"):
            return line.split(":", 1)[1].strip()
    return ""


def page_text(pdf: Path, page: int) -> str:
    return _run(["pdftotext", "-f", str(page), "-l", str(page), str(pdf), "-"])


def inspect(pdf: Path, page: int) -> PageInfo:
    """Classify one page without rendering it."""
    text = page_text(pdf, page)
    listing = _run(["pdfimages", "-list", "-f", str(page), "-l", str(page), str(pdf)])
    images = max(0, len(listing.splitlines()) - 2)   # two header rows
    chars = len(text.strip())
    return PageInfo(
        number=page,
        chars=chars,
        images=images,
        has_text_layer=chars >= TEXT_LAYER_MIN_CHARS,
    )


def inspect_all(pdf: Path) -> list[PageInfo]:
    return [inspect(pdf, p) for p in range(1, page_count(pdf) + 1)]


def render(pdf: Path, page: int, out_dir: Path, dpi: int = 200) -> Path:
    """Render one page to PNG.

    200 dpi is the default because it is where handwritten subscripts became
    reliably readable in testing; 150 lost them, 300 only cost time.
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
