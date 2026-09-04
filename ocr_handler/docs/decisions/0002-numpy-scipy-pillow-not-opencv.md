# ADR-0002 — numpy + scipy + Pillow, not OpenCV or scikit-image

**Date:** 2026-09-02 · **Status:** Accepted
*Transcribed 2026-09-04 from `todo.md`, where it was living unrecorded.*

## Context

Ink separation and region grouping need masking, morphology and connected components. OpenCV and
scikit-image are the obvious reaches.

## Decision

**numpy + scipy.ndimage + Pillow.** No OpenCV, no scikit-image.

## Rationale

Both were installed and benchmarked against the alternative on this project's own pages, and both lost
on merit — not on principle:

- Hough line detection needed the same collinear-merge post-processing as plain morphology, so it bought
  nothing the simpler path did not already have.
- `skimage.measure.regionprops` is ergonomics over `scipy.ndimage.find_objects`.

## Consequences

- `ink.py` stays small (162 lines) and has no heavyweight image dependency.
- Two fewer large wheels in an environment that will also carry torch and model weights.
- Re-opening this needs a new ADR and a benchmark, not an argument.
