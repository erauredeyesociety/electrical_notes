"""Extract a PDF's existing text layer, and say honestly how good it is.

This is the CHEAP half of the pipeline and the half that should always run
first. A PDF that already carries good text needs no OCR at all; running a
vision model over it would be slower, cost GPU, and produce a *worse* answer
than the bytes already in the file.

The job of this module is therefore not just "get the text" but "get the text
AND report where it is too thin to trust", so the expensive OCR pass can be
aimed only at the pages that need it.

There are TWO independent questions here, and conflating them is a defect this
module already shipped once:

  density      -- "is there text?"       characters per page -> ok/sparse/empty
  faithfulness -- "is the text right?"   structural detectors -> intact/suspect

They stay separate because their REPAIRS differ. A `sparse` page needs OCR: the
content is in pixels. A `suspect` page must never be sent to OCR -- its glyphs
are already present with correct coordinates, and a model would spend GPU
recovering what is in the file and return a worse answer. See `structure.py`
and docs/plans/structural-faithfulness.md.

Density thresholds are per-page character counts. They are heuristics, and they
are deliberately reported rather than silently applied.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .structure import (  # noqa: F401  -- is_letter_spaced is public API
    INTACT,
    SUSPECT,
    Signal,
    is_letter_spaced,
)
from . import structure  # noqa: F401  -- textlayer.structure.WHY is used by cli

# A page averaging fewer characters than this carries no usable prose --
# a scan, or a slide that is one big diagram. Matches the threshold already
# used by content/cesc_410/hw/tools/course_text.py so the two agree.
SPARSE_CHARS = 400

# Below this a page is effectively empty: a slide number and nothing else.
EMPTY_CHARS = 30

# `drawings` is measured with get_cdrawings(), not get_drawings(). Measured
# 2026-09-06 over 7,187 corpus pages: the two return an IDENTICAL count on
# every page, and get_cdrawings costs 18.4 s against 83.4 s.
#
# It is also measured LAZILY -- only on pages where it can change a routing
# decision, which is `verdict != "ok" and images == 0` (483 of 7,187 pages).
# Measured on the same pass: lazy costs 2.2 s on top of a 20 s corpus sweep
# (11%), against 83.4 s eager (5.3x the whole text pass). `inspect` is
# advertised as free and has to stay that way.
#
# Where it was not measured the field is None, never 0: a count that was not
# taken and a count that came back zero are different facts.
#
# `drawn_images` rides along on the same lazy pages and costs 1.5 s more. It
# exists because `images` -- get_images(full=True) -- lists the image XObjects
# in the page's RESOURCES and misses one PAINTED from inside a Form XObject.
# Measured on the same 7,187 pages: 14 pages where get_images() says 0 and
# get_image_info() finds a real image, of which ONE (sys_304 'SYS 304 Test 1
# Fall 2026 - Key.pdf' page 6, a 56x40 logo) also has zero drawings and would
# otherwise be routed as `blank` -- the one direction that can silently lose a
# page. `images` itself is deliberately left alone: it prints into
# to_markdown() and its bytes are a must-not-break invariant.


@dataclass
class PageText:
    """One page's text layer plus the evidence for whether it can be trusted."""

    page: int          # 1-based
    text: str
    chars: int
    images: int
    verdict: str       # density:      "ok" | "sparse" | "empty"
    structure: str = INTACT                     # faithfulness: "intact" | "suspect"
    signals: tuple[Signal, ...] = ()            # every detector, fired or not
    drawings: int | None = None                 # vector paths; None = not measured
    drawn_images: int | None = None             # images PAINTED on the page; see below

    @property
    def needs_ocr(self) -> bool:
        """Density only. A structurally-suspect page is deliberately NOT sent
        to OCR -- its bytes are exact, only their arrangement was lost."""
        return self.verdict != "ok"

    @property
    def skip_reason(self) -> str | None:
        """Why this page must never be rendered or sent to a model.

        The one measured routing rule that SAVES work rather than spending it,
        and it has to be enforced before any render. A page with no text, no
        images and no vector paths has nothing on it; rendering it and loading
        a model is pure waste.

        The image count alone is NOT enough, and the correction is the whole
        reason `drawings` exists. Measured 2026-09-06 over 7,187 pages: 483
        non-`ok` pages carry zero images, but only 78 of those also carry zero
        drawings. The other 405 are vector content -- e.g.
        cec_315/hw_practice_problems/lctr22-exercise.pdf page 1 has 0
        characters, 0 images, 1,837 vector paths and 8.9% non-white pixels at
        72 dpi; ps160/m14/M14_textbook_chapter.pdf page 33 has 883 paths and
        20.6%. Skipping those on an images-only test would silently discard
        whole pages of content.
        """
        if (self.verdict == "empty" and not self.images
                and not self.drawings and not self.drawn_images):
            return "no content"
        return None

    @property
    def has_pixels(self) -> bool:
        """Is there content this page carries that the text layer did not?

        Only meaningful where the lazy counts were taken, i.e. where
        `needs_ocr` -- which is the only place a caller should be asking.
        """
        return bool(self.images or self.drawings or self.drawn_images)

    @property
    def suspect(self) -> bool:
        return self.structure == SUSPECT

    @property
    def fired(self) -> tuple[str, ...]:
        """Names of the detectors that fired, for reporting."""
        return tuple(s.name for s in self.signals if s.fired)


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
        """Document-level call on the DENSITY axis: is OCR worth running?"""
        if not self.ocr_pages:
            return "text-layer-sufficient"
        if len(self.ocr_pages) == len(self.pages):
            return "ocr-required"
        return "ocr-partial"

    @property
    def blank_pages(self) -> list[int]:
        """Pages with nothing on them at all -- never rendered, never sent to
        a model. Kept apart from `ocr_pages` because conflating "the page is
        blank" with "OCR returned nothing" is how a broken engine looks like a
        clean corpus (docs/plans/text-layer-first.md section 7)."""
        return [p.page for p in self.pages if p.skip_reason]

    @property
    def ocr_candidates(self) -> list[int]:
        """The pages OCR would actually be aimed at: the text layer failed AND
        there is something on the page to recover."""
        return [p.page for p in self.pages if p.needs_ocr and not p.skip_reason]

    @property
    def suspect_pages(self) -> list[int]:
        """1-based page numbers whose text layer is present but not faithful."""
        return [p.page for p in self.pages if p.suspect]

    @property
    def structure_verdict(self) -> str:
        """Document-level call on the FAITHFULNESS axis. Bands none/some/all,
        mirroring `verdict`, because a document 21% suspect is not one that is
        suspect throughout and the two must not read the same."""
        suspect = self.suspect_pages
        if not suspect:
            return "structure-intact"
        if len(suspect) == len(self.pages):
            return "structure-suspect"
        return "structure-suspect-partial"

    @property
    def signal_counts(self) -> dict[str, int]:
        """Pages fired, per detector name. Detectors that fired on nothing are
        still listed at 0 -- a silent detector and an absent one differ."""
        counts = dict.fromkeys(structure.NAMES, 0)
        for page in self.pages:
            for name in page.fired:
                counts[name] = counts.get(name, 0) + 1
        return counts


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
        sigs = structure.signals(text)
        verdict = _classify(len(text))
        images = len(page.get_images(full=True))
        # Lazy by design -- see the note on EMPTY_CHARS above. The count can
        # only change an answer where the text layer failed AND no image was
        # found; everywhere else it stays None, meaning "not measured".
        lazy = verdict != "ok" and images == 0
        drawings = len(page.get_cdrawings()) if lazy else None
        drawn_images = len(page.get_image_info(xrefs=False)) if lazy else None
        out.append(PageText(
            page=n,
            text=text,
            chars=len(text),
            images=images,
            verdict=verdict,
            structure=structure.classify(sigs),
            signals=sigs,
            drawings=drawings,
            drawn_images=drawn_images,
        ))
    doc.close()
    return DocText(path=pdf, pages=out)


# Rendering lives in `emit.py` -- one intermediate, four views. Re-exported
# here because `to_markdown`/`to_text` are the shipped names with existing
# callers, and a refactor should not churn them.
from .emit import to_latex, to_jsonl, to_markdown, to_text  # noqa: E402,F401
