"""Extract a PDF's existing text layer, and say honestly how good it is.

This is the CHEAP half of the pipeline and the half that should always run
first. A PDF that already carries good text needs no OCR at all; running a
vision model over it would be slower, cost GPU, and produce a *worse* answer
than the bytes already in the file.

The job of this module is therefore not just "get the text" but "get the text
AND report where it is too thin to trust", so the expensive OCR pass can be
aimed only at the pages that need it.

Density thresholds are per-page character counts. They are heuristics, and they
are deliberately reported rather than silently applied.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# A page averaging fewer characters than this carries no usable prose --
# a scan, or a slide that is one big diagram. Matches the threshold already
# used by content/cesc_410/hw/tools/course_text.py so the two agree.
SPARSE_CHARS = 400

# Below this a page is effectively empty: a slide number and nothing else.
EMPTY_CHARS = 30


@dataclass
class PageText:
    """One page's text layer plus the evidence for whether it can be trusted."""

    page: int          # 1-based
    text: str
    chars: int
    images: int
    verdict: str       # "ok" | "sparse" | "empty"

    @property
    def needs_ocr(self) -> bool:
        return self.verdict != "ok"


@dataclass
class DocText:
    path: Path
    pages: list[PageText]

    @property
    def total_chars(self) -> int:
        return sum(p.chars for p in self.pages)

    @property
    def chars_per_page(self) -> float:
        return self.total_chars / max(len(self.pages), 1)

    @property
    def ocr_pages(self) -> list[int]:
        """1-based page numbers whose text layer is too thin to trust."""
        return [p.page for p in self.pages if p.needs_ocr]

    @property
    def verdict(self) -> str:
        """Document-level call: is OCR worth running at all?"""
        if not self.ocr_pages:
            return "text-layer-sufficient"
        if len(self.ocr_pages) == len(self.pages):
            return "ocr-required"
        return "ocr-partial"


# Some encoders emit one glyph per text run, so extraction yields
# "C o m p u t e r  O r g a n i z a t i o n". Detected, not silently repaired:
# collapsing it is guesswork and would corrupt legitimately spaced text.
_SPACED_RE = re.compile(r"(?:\b\w\s){6,}")


def is_letter_spaced(text: str) -> bool:
    """True when extraction produced one-glyph-per-run spacing artefacts."""
    return bool(_SPACED_RE.search(text))


def _classify(chars: int) -> str:
    if chars < EMPTY_CHARS:
        return "empty"
    if chars < SPARSE_CHARS:
        return "sparse"
    return "ok"


def extract(pdf: Path, pages: list[int] | None = None) -> DocText:
    """Read the text layer. `pages` is 1-based; None means all."""
    import pymupdf

    doc = pymupdf.open(pdf)
    wanted = pages or range(1, doc.page_count + 1)
    out: list[PageText] = []
    for n in wanted:
        if not 1 <= n <= doc.page_count:
            continue
        page = doc[n - 1]
        text = page.get_text().strip()
        out.append(PageText(
            page=n,
            text=text,
            chars=len(text),
            images=len(page.get_images(full=True)),
            verdict=_classify(len(text)),
        ))
    doc.close()
    return DocText(path=pdf, pages=out)


def to_markdown(doc: DocText, *, include_empty: bool = True) -> str:
    """Render as Markdown with page markers and honest gap annotations."""
    head = [
        f"# {doc.path.stem}",
        "",
        f"*Text layer of `{doc.path.name}` — {len(doc.pages)} pages, "
        f"{doc.total_chars:,} chars ({doc.chars_per_page:.0f}/page).*",
    ]
    if doc.ocr_pages:
        shown = ", ".join(map(str, doc.ocr_pages[:20]))
        more = f" (+{len(doc.ocr_pages)-20} more)" if len(doc.ocr_pages) > 20 else ""
        head += [
            "",
            f"> ⚠ **{len(doc.ocr_pages)} of {len(doc.pages)} pages have little or no "
            f"text layer** — verdict `{doc.verdict}`.",
            f"> Pages: {shown}{more}.",
            "> Their content is in images. What follows is only what the PDF itself "
            "carries; run OCR to recover the rest.",
        ]
    if any(is_letter_spaced(p.text) for p in doc.pages):
        head += [
            "",
            "> ⚠ **Letter-spacing artefacts detected** (`C o m p u t e r`). The encoder "
            "emitted one glyph per text run. Left as-is deliberately: collapsing the "
            "spaces is guesswork and would corrupt legitimately spaced text.",
        ]
    head.append("")

    body: list[str] = []
    for p in doc.pages:
        if p.verdict == "empty" and not include_empty:
            continue
        tag = "" if p.verdict == "ok" else f"  *({p.verdict}, {p.images} image(s))*"
        body += ["", "---", "", f"## Page {p.page}{tag}", ""]
        body.append(p.text if p.text else "*(no text layer on this page)*")
    return "\n".join(head + body).rstrip() + "\n"


def to_text(doc: DocText) -> str:
    """Plain text with page markers, for grep."""
    parts = []
    for p in doc.pages:
        parts.append(f"\n=== page {p.page} ({p.verdict}) ===\n")
        parts.append(p.text or "(no text layer)")
    return "".join(parts).strip() + "\n"
