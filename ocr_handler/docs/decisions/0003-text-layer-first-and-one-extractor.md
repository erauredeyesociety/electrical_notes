# ADR-0003 — Text-layer first, and one extractor for every course

**Date:** 2026-09-04 · **Status:** Accepted (operator direction)

## Context

Three per-course PDF extractors already existed and disagreed about what counts as a usable text layer:

| Script | Library | Verdict logic |
| --- | --- | --- |
| `content/cesc_410/hw/tools/course_text.py` | poppler `pdftotext -layout` | 400 chars/page, reported |
| `content/cpsc_462/tools/extract_notes.py` | PyMuPDF (+ pandoc for `.docx`) | 400 chars/page, flagged |
| `content/cec_300/exam*/extract_pdfs.py` | PyMuPDF | none — silently drops empty pages |

A fourth course, `cesc_470`, already documents `ocr-handler inspect` in
`content/cesc_470/md_notes/README.md` — so `inspect` is a published surface with an external consumer,
while the extraction verb is not yet.

The operator's direction: `ocr_handler` becomes the ONE text extractor for every course, and it must be
able to "just get text layer", "do OCR", or produce both side by side.

## Decision

1. **The text layer is ground truth wherever it exists.** OCR repairs pages where it is missing or
   provably corrupt. A model is never run over a page whose bytes are already correct.
2. **One tool, one threshold, one verdict.** Per-course extractors are retired once parity is proven.
3. **Gaps are reported, never silently skipped.**

## Rationale

Measured across 430 documents / 7,146 pages: 67% of pages and 50% of documents need no recognition at all
([findings/corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md)). A tool that OCRs
everything would be slower *and less accurate* on two thirds of the corpus. Divergent verdict logic across
three scripts is how a wrong citation gets written.

## Consequences

- The four-mode contract in [plans/text-layer-first.md](../plans/text-layer-first.md) follows from this.
- The three scripts above are scheduled for deletion in M2 — **only after** byte-level parity is shown.
- `.docx` support in `cpsc_462`'s script is a real gap this ADR does not close
  ([scope.md](../scope.md) § Open decisions #6).
- "One extractor" is a claim that needs a golden-master test to be honest. There is none yet.
