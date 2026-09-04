# ADR-0001 — PyMuPDF is the only PDF library

**Date:** 2026-09-02 · **Status:** Accepted
*Transcribed 2026-09-04 from `todo.md` and the M1 session record, where it was living unrecorded.*

## Context

Five candidates were available: PyMuPDF, pdfplumber, pypdf, pdfminer.six, Camelot, plus the poppler CLI
tools (`pdftotext`, `pdfinfo`, `pdfimages`, `pdftoppm`) already used by `pdfops.py` via subprocess.

## Decision

**PyMuPDF only.** No pdfplumber, pypdf, pdfminer or Camelot. Poppler subprocess calls are to be removed.

## Rationale

- pdfplumber duplicates what PyMuPDF already does; pdfminer is a subset of pdfplumber.
- pypdf cannot render.
- Camelot would corrupt output on this material.
- Poppler is ~10× slower, and — the load-bearing reason — **it changes answers, not just speed**:
  poppler at 200 dpi produced `c o s (w o n)` where PyMuPDF at 150/200/300 all produced
  `\cos(\omega_0 n)`. The two renderers differ on 6.66% of pixels from antialiasing alone.
- PyMuPDF also gives structural access to embedded images with exact page coordinates.

## Consequences

- `textlayer.py` is already PyMuPDF-only and is the model to converge on.
- `pdfops.py` still shells out to poppler and still carries its own 400-char classifier. **Two libraries
  and two classifiers are live simultaneously** — this ADR is not satisfied until that is fixed
  ([roadmap.md](../roadmap.md) M2).
- Poppler CLI stays a legitimate *diagnostic* tool at a terminal; it just isn't a dependency.
