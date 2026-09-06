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

  **Outcome, 2026-09-06 (appended, not a rewrite).** Done for the classifier: `inspect`, `inspect_all`,
  `page_count`, `page_text` and `producer` are views over `textlayer.extract`, and no poppler process is
  spawned on that path. It moved **428 of 7,187 corpus pages** — decomposed in
  [../findings/one-classifier-2026-09-06.md](../findings/one-classifier-2026-09-06.md), which also
  confirms this ADR's central claim from a second direction: on `ps160/midterm_03/...` page 3, poppler
  reflows `CV = f / 2R` into `CV =\n\nf\nR\n2` where PyMuPDF keeps it together.
  `pdfops.render()` remains poppler on purpose — the ink path's `red_mask` band (7,000–9,500 px) and
  `merge_px = 64` are calibrated against poppler's pixels, and the renderers differ on 6.66% of them.
  Re-sweeping those is M4.
- Poppler CLI stays a legitimate *diagnostic* tool at a terminal; it just isn't a dependency.
