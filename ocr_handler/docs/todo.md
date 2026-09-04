# TODO — single source of truth

> Last updated: 2026-09-04 · **MODE: development**
> Index, not an essay. Detail lives behind the links.

## CURRENT STATE

**M1 backbone works and is committed** (`ae1dca5`). `pdfops` + `ink` classify, render, separate ink and
crop regions on real lectures. `textlayer` + `cli` added since: `ocr-handler inspect` / `ocr-handler text`
give a per-page `ok`/`sparse`/`empty` verdict and a document verdict.
**`src/ocr_handler/textlayer.py` is not yet tracked by git** — it exists on disk only.

**The project's shape changed 2026-09-04.** The operator restated it as *the ONE text extractor for every
course*, replacing the per-course scripts. A census measured what that means:
**430 PDFs / 7,146 pages** for the extractor against **2 documents** for the annotated-ink path —
[findings/corpus-census-2026-09-04.md](./findings/corpus-census-2026-09-04.md). The roadmap was
re-sequenced accordingly; v1 is at [archives/roadmap_v1_2026-09-04.md](./archives/roadmap_v1_2026-09-04.md).

**Engine choice is open and unresolved.** A separate research pass is re-examining the landscape.
Do not build against any named model until it lands.

## NEXT ACTION

**Start at [plans/text-layer-first.md](./plans/text-layer-first.md)** — the four-mode extraction contract.
Then work M2 in [roadmap.md](./roadmap.md) in order. The first two items are corrections, not features:

1. **Converge the two page classifiers.** `pdfops.TEXT_LAYER_MIN_CHARS = 400` (poppler) and
   `textlayer.SPARSE_CHARS = 400` (PyMuPDF) are the same rule implemented twice, on two libraries.
2. **Test the path the CLI actually uses.** The 7-test floor covers `pdfops` and `ink`; `cli.py` imports
   neither. The shipped command has zero test coverage.

## Blocked / awaiting operator

Six named calls, all in [scope.md](./scope.md) § Open decisions. Batch them; none should be guessed.
Highest-impact first: **output destination**, **the 400-char `sparse` gate**, **non-PDF inputs**.

## Doctrine gaps

Full checklist with file paths: **[plans/doctrine-compliance.md](./plans/doctrine-compliance.md)**.
The three that cost something today: no `docs/plans/` ACTIVE-SPEC to resume from (fixed by this pass),
decisions living only in this file (fixed — see [decisions/INDEX.md](./decisions/INDEX.md)), and the
S2 regression fixture sitting in gitignored `tmp/`.

## Known issues

- **The ink is images or vectors and we do not know which.** `research/INDEX.md` measured +2 embedded
  images on page 5; the earlier scoping note measured **7 `/Ink` objects** in the same file. Both may be
  true; only one is the right extraction path. Resolve before M4.
- `diff_mask` untested against a *recompiled* twin, where the whole page shifts. Guard: check the changed
  fraction and refuse if implausibly large.
- `merge_px=64` is calibrated for 200 dpi only — a pixel distance, so re-sweep if dpi changes.
- Structural extraction gave 2 ink images on page 5 where pixel grouping gave 5 logical items. Expected;
  they compose. Neither count is canonical.
- `is_letter_spaced` fires on **51 documents** — a present text layer that is corrupt. Detected, never
  repaired. This is the strongest known case for preferring OCR over a dense text layer.

---

**See:** [roadmap.md](./roadmap.md) · [scope.md](./scope.md) · [plans/INDEX.md](./plans/INDEX.md) · [decisions/INDEX.md](./decisions/INDEX.md)
