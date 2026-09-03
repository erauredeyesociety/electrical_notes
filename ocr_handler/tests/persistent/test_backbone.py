"""Regression floor. Small on purpose -- these are the must-not-break paths.

Skips cleanly if the lecture PDFs are not present, so the suite stays green on
a machine without the course material.
"""

from pathlib import Path

import numpy as np
import pytest

from ocr_handler import ink, pdfops

LECTURES = Path(__file__).resolve().parents[2].parent / "content/cesc_410/lectures"
ANNOTATED = LECTURES / "f26_lctr02_DT signals and systems-plw.pdf"
BORN_DIGITAL = LECTURES / "dsp-lctr1-analog-signal-in-td-n-fd-26-08-26.pdf"

needs_pdfs = pytest.mark.skipif(
    not ANNOTATED.exists(), reason="course PDFs not available"
)


def test_reading_order_bands_before_columns():
    """Side-by-side items must come back left-to-right, not sorted by top edge.

    Regression: a 'cos(...)' and the 'sin(...)' beside it were returned
    swapped because their y0 differed by three pixels, which would silently
    reverse an equation.
    """
    left = ink.Region(x0=100, y0=1393, x1=300, y1=1497, pixels=500)
    right = ink.Region(x0=400, y0=1390, x1=600, y1=1504, pixels=500)   # starts higher
    below = ink.Region(x0=100, y0=1900, x1=300, y1=2000, pixels=500)

    ordered = ink._reading_order([right, below, left])
    assert [r.x0 for r in ordered[:2]] == [100, 400], "same line must read left to right"
    assert ordered[2].y0 == 1900, "lower band must come last"


def test_empty_mask_yields_no_regions():
    assert ink.regions(np.zeros((50, 50), bool)) == []


@needs_pdfs
def test_born_digital_pages_route_to_text_not_a_model():
    """A page with a real text layer must never be sent to recognition."""
    kinds = [p.kind for p in pdfops.inspect_all(BORN_DIGITAL)]
    assert kinds.count("text") >= 10, f"expected mostly text pages, got {kinds}"


@needs_pdfs
def test_annotated_pages_do_not_route_to_text():
    kinds = [p.kind for p in pdfops.inspect_all(ANNOTATED)]
    assert "text" not in kinds, f"handwriting pages must not claim a text layer: {kinds}"


@needs_pdfs
def test_producer_distinguishes_annotation_from_recompile():
    assert "Annotator" in pdfops.producer(ANNOTATED)
    assert "Annotator" not in pdfops.producer(BORN_DIGITAL)


@needs_pdfs
def test_pairs_annotated_file_with_its_base():
    base = pdfops.find_base(ANNOTATED)
    assert base is not None and base.exists()


@needs_pdfs
def test_ink_separation_and_grouping_on_known_page(tmp_path):
    """The fixture page: 5 regions, matching its logical content."""
    png = pdfops.render(ANNOTATED, 5, tmp_path, dpi=200)
    mask = ink.red_mask(png)
    assert 7000 < mask.sum() < 9500, f"red ink pixel count drifted: {mask.sum()}"

    regs = ink.regions(mask)
    assert len(regs) == 5, f"expected 5 logical regions, got {len(regs)}"
    assert regs[3].x0 < regs[4].x0, "the two filled-in blanks must read left to right"
