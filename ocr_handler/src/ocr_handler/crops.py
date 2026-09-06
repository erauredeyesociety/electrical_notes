"""Prepare a region for a recogniser: composite the ink, clamp the padding.

The stage between `ink.regions()` and any model. Two measured findings drive
everything here (`docs/research/equation-ocr-specialists.md` §4.2, §4.5;
design in `docs/plans/mask-first-crops.md`):

  1. REMOVING THE BACKGROUND BEATS CHANGING THE MODEL. Feeding UniMERNet the
     binary mask `ink.py` already computes -- instead of raw pixels -- gave the
     best of 84 measured outputs: it recovered `|\\alpha|^{n}` and the
     `\\omega_0` subscripts, and deleted a hallucinated `\\frac{1}{2}` that was
     the slide's graph-paper grid being read as a fraction bar. Free,
     deterministic, no GPU.

  2. PADDING IS A CLIFF, NOT A GRADIENT. Output was byte-identical across pad
     -16..+4 (the model re-crops padding away itself), then collapsed into
     `\\begin{array}` garbage once the crop reached the next thing on the page
     -- at +48 for a box sitting 6 px under a printed line, at +160 for one
     sitting in 141 px of white space. Same shape as DocTron-Formula's
     published 0.919 -> 0.644 -> 0.009 CDM curve.

So the padding rule is not a constant. **Measure the distance to the nearest
neighbouring content, per side, and cap the padding just past it** -- the cliff
is at the neighbour, so a fixed pixel count is safe on one crop and fatal on the
next. Just past, not short of: see `INTRUSION`, which cost an accuracy
regression to get right.

numpy + scipy + Pillow only -- ADR-0002.
"""

from __future__ import annotations

import logging
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

from .ink import Region

log = logging.getLogger(__name__)

# Padding to ask for when nothing is in the way. Matches `ink.crop`'s default,
# which the measured sweep found sits inside the safe plateau on both fixture
# targets (plateau -16..+24 on the tighter one).
PAD = 12

# How far a crop may reach PAST the nearest neighbour before the guard cuts it.
#
# Not zero, and finding that out cost a measurable amount of accuracy. Clamping
# to `gap - 2` on the fixture equation -- whose printed neighbour is 6 px above
# it -- cut pad 12 down to 4 and turned
#     = \vert\alpha\vert^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).      <- correct
# into
#     = \vert\alpha\vert^{n}(\cos(\cos n)+j\sin(w_0,w)).
# The model re-crops its own input (`crop_margin`), so clipping a few pixels of
# a neighbour's descenders is free; the cliff comes when enough of the next line
# is legible to switch the decoder into `\begin{array}` mode.
#
# Measured on the composite rendering, 200 dpi, UniMERNet-Base:
#   gap 6 px   -> identical best output at pad 12/16/20, degraded 24, GARBAGE 32
#   gap 141 px -> held to pad 96, GARBAGE at 160                       (§4.2)
# Safe at gap+18, broken at gap+19 across the two -- so the true boundary is
# near +18 and 8 is a deliberate half-measure with n=2 evidence behind it.
#
# It also means the guard is INVISIBLE at the default pad: gap + 8 >= 12 for any
# gap >= 4. The guard exists to stop a large request, not to shave a safe one.
INTRUSION = 8


@dataclass
class Padding:
    """How much padding each side actually got, and why it was cut."""

    top: int
    right: int
    bottom: int
    left: int
    requested: int
    gaps: tuple[int, int, int, int]  # measured clearance per side, same order

    @property
    def clamped(self) -> bool:
        return min(self.top, self.right, self.bottom, self.left) < self.requested

    def note(self) -> str:
        """One line naming every side the neighbour guard cut, or ''."""
        names = ("top", "right", "bottom", "left")
        got = (self.top, self.right, self.bottom, self.left)
        cut = [
            f"{n} {g}px (gap {gap}px)"
            for n, g, gap in zip(names, got, self.gaps)
            if g < self.requested
        ]
        return f"pad {self.requested} clamped: " + ", ".join(cut) if cut else ""


@dataclass
class Crop:
    """One region, cropped two ways so both can be fed and compared."""

    region: Region
    box: tuple[int, int, int, int]  # final padded box, page pixel coordinates
    padding: Padding
    raw: Image.Image  # the page as it is
    composite: Image.Image  # ink only, on a clean background
    contested: bool  # another region's box overlaps this one

    def save(self, out_dir: Path, stem: str) -> tuple[Path, Path]:
        """Write `<stem>-raw.png` and `<stem>-mask.png`. Returns both paths."""
        out_dir.mkdir(parents=True, exist_ok=True)
        raw_p, comp_p = out_dir / f"{stem}-raw.png", out_dir / f"{stem}-mask.png"
        self.raw.save(raw_p)
        self.composite.save(comp_p)
        return raw_p, comp_p


def _page_array(page: Path | str | np.ndarray) -> np.ndarray:
    if isinstance(page, np.ndarray):
        return page if page.ndim == 3 else np.repeat(page[..., None], 3, axis=2)
    return np.asarray(Image.open(page).convert("RGB"))


def gaps(
    region: Region,
    occupancy: np.ndarray,
    reach: int = PAD,
) -> tuple[int, int, int, int]:
    """Clear pixels between this region's box and the nearest other content.

    Returns (top, right, bottom, left). The region's own box is excluded, so
    what is measured is the distance to *something else* -- and `occupancy`
    should therefore be everything the page holds, printed content included,
    not just other ink regions. The killer on the fixture page was the printed
    line 6 px above the handwriting, which no ink mask contains.

    Scanned over a band widened by `reach`, because a crop that pads sideways
    can reach content that does not overlap the bare box.

    A side with nothing beyond it gets its distance to the page edge, which is
    the most padding that side could use anyway.
    """
    h, w = occupancy.shape
    x0, y0, x1, y1 = region.box

    occ = occupancy.copy()
    occ[y0:y1, x0:x1] = False  # our own ink is not a neighbour

    xa, xb = max(0, x0 - reach), min(w, x1 + reach)
    ya, yb = max(0, y0 - reach), min(h, y1 + reach)

    rows = occ[:, xa:xb].any(axis=1)
    cols = occ[ya:yb, :].any(axis=0)

    up = np.nonzero(rows[:y0])[0]
    down = np.nonzero(rows[y1:])[0]
    left = np.nonzero(cols[:x0])[0]
    right = np.nonzero(cols[x1:])[0]

    return (
        int(y0 - up[-1] - 1) if up.size else y0,
        int(right[0]) if right.size else w - x1,
        int(down[0]) if down.size else h - y1,
        int(x0 - left[-1] - 1) if left.size else x0,
    )


def clamp(
    region: Region,
    occupancy: np.ndarray,
    pad: int = PAD,
    intrusion: int = INTRUSION,
) -> Padding:
    """Padding for one region, cut per side so the crop stops just past the
    nearest neighbour. Never grows past `pad` -- the guard only ever removes.

    Per side rather than one scalar, because clearance is wildly asymmetric:
    the fixture equation has 6 px above it and 675 px below, and a single
    number would throw away the room underneath to respect the line overhead.

    The rule is `min(pad, gap + INTRUSION)`, not `min(pad, gap)`. Reaching a
    little past the neighbour is measured-safe and sometimes measured-better;
    see `INTRUSION`.
    """
    g = gaps(region, occupancy, reach=pad)
    sides = tuple(max(0, min(pad, gap + intrusion)) for gap in g)
    p = Padding(*sides, requested=pad, gaps=g)  # type: ignore[call-arg]
    if p.clamped:
        log.info("region %s: %s", region.box, p.note())
    return p


def _background(page: np.ndarray, paint: np.ndarray, spec: str | int | tuple) -> np.ndarray:
    """Resolve a background specification to one RGB triple.

    "median" scans the whole page, so `prepare` resolves it once and hands the
    triple down rather than paying for it per region.
    """
    if isinstance(spec, str):
        if spec == "white":
            return np.array([255, 255, 255], dtype=np.uint8)
        if spec == "median":
            # The page's own paper colour: median of everything that is not ink.
            # Measured (255,255,255) on all three fixtures, the scan included --
            # this is here for tinted paper that has not turned up yet.
            bg = page[~paint] if (~paint).any() else page.reshape(-1, 3)
            return np.median(bg.reshape(-1, 3), axis=0).astype(np.uint8)
        raise ValueError(f"unknown background {spec!r}; use 'white', 'median', or a colour")
    if isinstance(spec, int):
        return np.array([spec] * 3, dtype=np.uint8)
    return np.asarray(spec, dtype=np.uint8)


def composite(
    page: np.ndarray,
    paint: np.ndarray,
    box: tuple[int, int, int, int],
    background: str | int | tuple = "white",
    binary: bool = True,
) -> Image.Image:
    """The ink of `paint`, on a clean background, cropped to `box`.

    `binary=True` paints every ink pixel flat black -- that is the rendering
    that won the measured sweep. `binary=False` keeps each ink pixel's true
    grey level and only replaces the background ("flatten"), which measured
    second: better than raw, worse than binary.
    """
    x0, y0, x1, y1 = box
    sub = page[y0:y1, x0:x1]
    m = paint[y0:y1, x0:x1]
    bg = _background(page, paint, background)
    ink_px = np.zeros(3, np.uint8) if binary else None
    out = np.where(m[..., None], sub if ink_px is None else ink_px, bg)
    return Image.fromarray(out.astype(np.uint8))


def prepare(
    page: Path | str | np.ndarray,
    regions: Sequence[Region],
    paint: np.ndarray,
    occupancy: np.ndarray | None = None,
    pad: int = PAD,
    intrusion: int = INTRUSION,
    background: str | int | tuple = "white",
    binary: bool = True,
) -> list[Crop]:
    """Crop every region twice -- raw pixels, and ink composited on clean paper.

    `paint`      page-shaped bool: the pixels the composite keeps. Use
                 `red_mask | dark_mask`. Painting the annotation ink ALONE was
                 measured and it is destructive -- the fixture equation's
                 printed skeleton `= |a|^n( ... + j ... )` vanished and the read
                 collapsed to `\\cos(w_1 r)\\sin(w_1\\varphi_h)`. The background
                 is the enemy, not the printed content.
    `occupancy`  page-shaped bool: what counts as a neighbour for the padding
                 guard. Defaults to `paint`, which is right when `paint` covers
                 all the page's content.

    Both renderings are returned rather than one, because the measurement
    behind the composite is n~84 outputs over four equations on one page --
    strong, but not enough to throw the raw pixels away. Feed both, compare,
    and delete this sentence when the evidence is bigger.
    """
    a = _page_array(page)
    h, w = a.shape[:2]
    if paint.shape != (h, w):
        raise ValueError(f"paint mask is {paint.shape}, page is {(h, w)}")
    occ = paint if occupancy is None else occupancy
    bg = _background(a, paint, background)  # resolved once, not once per region

    out: list[Crop] = []
    for r in regions:
        p = clamp(r, occ, pad=pad, intrusion=intrusion)
        box = (
            max(0, r.x0 - p.left),
            max(0, r.y0 - p.top),
            min(w, r.x1 + p.right),
            min(h, r.y1 + p.bottom),
        )
        out.append(
            Crop(
                region=r,
                box=box,
                padding=p,
                raw=Image.fromarray(a[box[1] : box[3], box[0] : box[2]]),
                composite=composite(a, paint, box, bg, binary),
                contested=_overlaps_another(r, regions),
            )
        )
    return out


def _overlaps_another(r: Region, regions: Sequence[Region]) -> bool:
    """True if another region's box intersects this one.

    Then the neighbour distance is genuinely zero: padding falls to its floor,
    but the crop *still* contains foreign ink, and no padding rule can fix
    that. It is a grouping failure, and the caller is told so it can merge the
    two regions or send the crop to something that tolerates several
    expressions -- not silently handed a crop that looks safe.
    """
    for o in regions:
        if o is r:
            continue
        if r.x0 < o.x1 and o.x0 < r.x1 and r.y0 < o.y1 and o.y0 < r.y1:
            return True
    return False
