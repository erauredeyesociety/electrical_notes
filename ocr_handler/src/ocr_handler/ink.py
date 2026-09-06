"""Separate annotation ink from prepared content, and crop regions. No ML.

Two independent ways to find what an instructor added during a lecture:

  colour     -- red ink vs black content, by channel arithmetic
  difference -- annotated page vs its un-annotated twin

Colour is used when only the annotated file exists. Differencing is stronger
when the pair is available, because it does not care what colour the ink is.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

# Red ink: clearly red, and clearly separated from both other channels.
# Verified on a real annotated lecture page -- these thresholds pulled 8,090
# ink pixels with no bleed from the 26,988 black content pixels.
RED_MIN = 100
RED_MARGIN = 55

# Anything this dark in all channels is prepared content, not coloured ink.
DARK_MAX = 140


@dataclass
class Region:
    """A bounding box in pixel coordinates, with its pixel count."""

    x0: int
    y0: int
    x1: int
    y1: int
    pixels: int

    @property
    def box(self) -> tuple[int, int, int, int]:
        return (self.x0, self.y0, self.x1, self.y1)

    @property
    def area(self) -> int:
        return (self.x1 - self.x0) * (self.y1 - self.y0)


def _load(path: Path) -> np.ndarray:
    return np.asarray(Image.open(path).convert("RGB")).astype(int)


def red_mask(png: Path) -> np.ndarray:
    """Pixels that are coloured ink rather than content."""
    a = _load(png)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    return (r > RED_MIN) & (r - g > RED_MARGIN) & (r - b > RED_MARGIN)


def dark_mask(png: Path) -> np.ndarray:
    """Pixels that are prepared content rather than coloured ink."""
    a = _load(png)
    return (a[:, :, 0] < DARK_MAX) & (a[:, :, 1] < DARK_MAX) & (a[:, :, 2] < DARK_MAX)


def page_and_masks(png: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """The page plus both masks, from a single decode.

    `red_mask` and `dark_mask` each re-open the file. Anything that wants the
    pixels and both masks -- `crops.prepare` does, to composite ink over a
    clean background and to measure the distance to neighbouring content --
    would otherwise decode the same PNG three times.
    """
    a = _load(png)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    red = (r > RED_MIN) & (r - g > RED_MARGIN) & (r - b > RED_MARGIN)
    dark = (r < DARK_MAX) & (g < DARK_MAX) & (b < DARK_MAX)
    return a.astype("uint8"), red, dark


def diff_mask(base_png: Path, annotated_png: Path, tol: int = 40) -> np.ndarray:
    """Pixels present in the annotated render but not the base one.

    Colour-blind, so it catches ink of any colour -- but it needs both files
    and it is sensitive to any rendering difference, so pages that merely
    reflowed will light up everywhere. Check the fraction before trusting it.
    """
    a, b = _load(base_png), _load(annotated_png)
    if a.shape != b.shape:
        raise ValueError(f"page sizes differ: {a.shape} vs {b.shape}")
    return np.abs(a - b).max(axis=2) > tol


def regions(mask: np.ndarray, merge_px: int = 64, min_pixels: int = 120) -> list[Region]:
    """Group scattered ink pixels into crop boxes.

    Handwriting arrives as thousands of disconnected strokes. Dilating before
    labelling merges strokes that belong to the same expression; merge_px is
    roughly the largest gap that should still count as one thing. Too small
    and one equation becomes twenty boxes; too large and the whole page
    becomes one box.

    The default 64 comes from a sweep on a real annotated page at 200 dpi:
    16 -> 18 regions, 24 -> 15, 32 -> 10, 48 -> 6, then a stable plateau of 5
    across 56-80 matching the page's actual logical content (two stem plots,
    one margin equation, two filled-in blanks). Re-sweep if the dpi changes --
    this is a pixel distance, so it scales with resolution.
    """
    if not mask.any():
        return []

    grown = ndimage.binary_dilation(mask, np.ones((merge_px, merge_px), bool))
    labels, count = ndimage.label(grown)

    out: list[Region] = []
    for sl_y, sl_x in ndimage.find_objects(labels):
        # Count only true ink inside the box, not the dilation padding.
        pixels = int(mask[sl_y, sl_x].sum())
        if pixels < min_pixels:
            continue
        out.append(Region(sl_x.start, sl_y.start, sl_x.stop, sl_y.stop, pixels))

    return _reading_order(out)


def _reading_order(regs: list[Region]) -> list[Region]:
    """Sort top-to-bottom, then left-to-right within a line.

    Sorting on (y0, x0) alone is wrong: two things written side by side rarely
    start at the same pixel row, so a naive sort returns them right-to-left.
    Seen for real -- a 'cos(...)' and the 'sin(...)' beside it came back
    swapped, which would have silently reversed an equation.

    Group into bands first: a region joins the current band if it vertically
    overlaps it, then bands are read left to right.
    """
    if not regs:
        return []

    bands: list[list[Region]] = []
    for r in sorted(regs, key=lambda r: r.y0):
        for band in bands:
            top = min(b.y0 for b in band)
            bottom = max(b.y1 for b in band)
            # Overlap by at least half this region's height counts as same line.
            overlap = min(bottom, r.y1) - max(top, r.y0)
            if overlap > (r.y1 - r.y0) * 0.5:
                band.append(r)
                break
        else:
            bands.append([r])

    out: list[Region] = []
    for band in bands:
        out.extend(sorted(band, key=lambda r: r.x0))
    return out


def crop(png: Path, region: Region, out_path: Path, pad: int = 12) -> Path:
    """Write one region to its own image file.

    A fixed pad, which is safe on this project's fixture page but is not a rule:
    padding costs nothing until the crop touches the next thing on the page, and
    then the answer is lost outright (`crops.py`). Prefer `crops.prepare`, which
    measures that distance per side instead of assuming 12 px of clearance.
    """
    im = Image.open(png)
    x0 = max(0, region.x0 - pad)
    y0 = max(0, region.y0 - pad)
    x1 = min(im.width, region.x1 + pad)
    y1 = min(im.height, region.y1 + pad)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    im.crop((x0, y0, x1, y1)).save(out_path)
    return out_path


def save_mask(mask: np.ndarray, out_path: Path) -> Path:
    """Write a mask as a black-on-white PNG, for eyeballing or for a model."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img = np.where(mask[..., None], 0, 255).astype("uint8").repeat(3, axis=2)
    Image.fromarray(img).save(out_path)
    return out_path
