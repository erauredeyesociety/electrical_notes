"""Regression floor for the mask-first crop path.

Four of the five build their page in-process, so the suite still says something
on a machine with no course material. The fifth needs the real lecture, because
the whole design rests on a property of a real page -- clearance is asymmetric
by two orders of magnitude -- that a synthetic fixture would only assume.
"""

from pathlib import Path

import numpy as np
import pytest

from ocr_handler import crops, ink, pdfops

LECTURES = Path(__file__).resolve().parents[2].parent / "content/cesc_410/lectures"
ANNOTATED = LECTURES / "f26_lctr02_DT signals and systems-plw.pdf"

needs_pdfs = pytest.mark.skipif(
    not ANNOTATED.exists(), reason="course PDFs not available"
)


def _page(h=400, w=400):
    """A blank white page and its empty content mask."""
    return np.full((h, w, 3), 255, np.uint8), np.zeros((h, w), bool)


def test_padding_stops_at_the_neighbour_not_at_a_constant():
    """The cliff is at the next thing on the page, so the pad must be per side.

    Regression: a fixed pad is safe on a crop in open space and fatal on one
    that sits under a printed line -- measured, the same pad of 48 px was fine
    on a box with 141 px of clearance and turned the box with 6 px of clearance
    into `\\begin{array}` garbage.
    """
    page, mask = _page()
    mask[200:220, 100:300] = True  # our region
    mask[196:198, 100:300] = True  # a neighbour 2 px above
    r = ink.Region(100, 200, 300, 220, pixels=4000)

    p = crops.clamp(r, mask, pad=64)
    assert p.top < 64, "padding must not run into the line above"
    assert p.top <= 2 + crops.INTRUSION, f"top pad {p.top} overshoots the 2 px gap"
    assert p.bottom == 64, "clear space below must keep the full padding"
    assert p.clamped and "top" in p.note()


def test_the_guard_only_ever_removes_padding():
    """It is a cliff guard, not an optimiser. A region in open space is
    untouched, and no side is ever inflated past what was asked for."""
    page, mask = _page()
    mask[180:220, 180:220] = True
    r = ink.Region(180, 180, 220, 220, pixels=1600)

    p = crops.clamp(r, mask, pad=12)
    assert (p.top, p.right, p.bottom, p.left) == (12, 12, 12, 12)
    assert not p.clamped

    tight = crops.clamp(r, mask, pad=2)
    assert max(tight.top, tight.right, tight.bottom, tight.left) == 2


def test_composite_deletes_the_background_and_keeps_the_ink():
    """The measured win: the crop a model sees carries ink and nothing else.

    Regression: the graph-paper grid under the fixture handwriting was read as
    a fraction bar and produced a hallucinated `\\frac{1}{2}`. A composited
    crop cannot do that, because the grid is not in it.
    """
    page, mask = _page()
    page[::10, :] = (200, 220, 255)  # graph-paper grid, exactly the failure case
    page[200:220, 100:300] = (40, 40, 40)  # the ink
    mask[200:220, 100:300] = True
    r = ink.Region(100, 200, 300, 220, pixels=4000)

    c = crops.prepare(page, [r], paint=mask)[0]
    comp = np.asarray(c.composite)

    assert set(np.unique(comp)) == {0, 255}, "composite must be ink on clean paper"
    assert (comp == 0).all(axis=2).sum() == 4000, "every ink pixel must survive"
    assert (np.asarray(c.raw) == [200, 220, 255]).all(axis=2).any(), (
        "the raw crop must still carry the grid -- both renderings are kept"
    )


def test_overlapping_regions_are_reported_rather_than_silently_cropped():
    """Neighbour distance zero is a grouping failure no padding rule can fix.

    The crop already contains a second expression, so it is flagged instead of
    being handed to a recogniser looking safe.
    """
    page, mask = _page()
    mask[200:260, 100:200] = True
    mask[230:290, 150:250] = True
    a = ink.Region(100, 200, 200, 260, pixels=6000)
    b = ink.Region(150, 230, 250, 290, pixels=6000)

    made = crops.prepare(page, [a, b], paint=mask)
    assert all(c.contested for c in made), "overlapping boxes must be flagged"

    alone = crops.prepare(page, [a], paint=mask)[0]
    assert not alone.contested


@needs_pdfs
def test_clearance_on_a_real_page_is_asymmetric_by_orders_of_magnitude(tmp_path):
    """Why the guard is per side and not one number.

    The fixture equation has a printed line a handful of pixels above it and
    the better part of a page below. One scalar would either clip the room
    underneath or walk into the line overhead.
    """
    png = pdfops.render(ANNOTATED, 5, tmp_path, dpi=200)
    page, red, dark = ink.page_and_masks(png)
    occ = red | dark
    assert red.sum() and dark.sum(), "both masks must be populated"

    eq = ink.Region(500, 1370, 1220, 1500, pixels=0)
    top, _, bottom, _ = crops.gaps(eq, occ, reach=0)
    assert top < 20, f"printed line should sit just above the ink, got {top}px"
    assert bottom > 500, f"open space should sit below it, got {bottom}px"

    made = crops.prepare(png, ink.regions(red), paint=occ, occupancy=occ)
    assert len(made) == 5
    assert any(c.padding.clamped for c in made), "the guard must fire on this page"
    for c in made:
        x0, y0, x1, y1 = c.box
        assert 0 <= x0 < x1 <= page.shape[1] and 0 <= y0 < y1 <= page.shape[0]
        assert c.raw.size == c.composite.size
