# Roadmap v2

> Lean index only: milestone bullets + path refs. Detail lives in [plans/](./plans/INDEX.md), never here.
> Boundaries: [scope.md](./scope.md) · Rules: [directives/INDEX.md](./directives/INDEX.md) · Tasks: [todo.md](./todo.md)
> Session narrative: [archives/session_records/](./archives/session_records/INDEX.md)

**Mode: DEVELOPMENT.** The non-ML backbone works and is verified on real lectures. Nothing is blocked on a model.

**Re-sequenced 2026-09-04, by leverage.** Structural ink extraction and the engine choice were ahead of
the extractor; they serve **2 documents**, the extractor serves **430** ([findings/corpus-census-2026-09-04.md](./findings/corpus-census-2026-09-04.md)).
Ink work now follows the extractor. v1 of this roadmap: [archives/roadmap_v1_2026-09-04.md](./archives/roadmap_v1_2026-09-04.md).

## M1 — Non-ML backbone ✓ done (2026-09-02)
- [x] `src/ocr_handler/pdfops.py` — classify / producer / render / pair (poppler)
- [x] `src/ocr_handler/ink.py` — colour + diff masks, region grouping, crop
- [x] `src/ocr_handler/textlayer.py` + `cli.py` — `inspect` / `text`, PyMuPDF, per-page verdicts
- [x] 7-test floor, verified on real lectures — [archives/session_records/2026-09-02_initialize-and-teardown.md](./archives/session_records/2026-09-02_initialize-and-teardown.md)

## M2 — One extractor, converged  ← **next**  (the 430-document path)
Spec: [plans/text-layer-first.md](./plans/text-layer-first.md) · Gaps: [plans/doctrine-compliance.md](./plans/doctrine-compliance.md)
- [ ] **Converge the two classifiers.** `pdfops.TEXT_LAYER_MIN_CHARS` and `textlayer.SPARSE_CHARS` are the same 400 twice, on two PDF libraries. One classifier, PyMuPDF only — [decisions/0001](./decisions/0001-pymupdf-is-the-only-pdf-library.md)
- [ ] **Floor test for `textlayer`** — the CLI's only dependency currently has zero tests
- [ ] `extract` with `--mode text|ocr|both|auto` (OCR paths stubbed until M3)
- [ ] `emit.py` — Markdown / plain text / LaTeX from one intermediate
- [ ] **Retire the three per-course scripts** once parity is proven — `cesc_410/hw/tools/course_text.py`, `cpsc_462/tools/extract_notes.py`, `cec_300/exam*/extract_pdfs.py`
- [ ] Put the S2 regression fixture under version control (it is in gitignored `tmp/`)
- **Must-not-break:** page classification · document verdict · reading order · text-layer output bytes

## M3 — Engine choice  (blocked on research)
- [ ] Head-to-head on the fixture page, control run on the un-annotated twin — [decisions/0004](./decisions/0004-engine-choice-deferred-decide-by-head-to-head.md)
- [ ] `recognize.py` behind one swappable interface, so the loser is cheap to replace

## M4 — Annotated lectures  (the 2-document path)
- [ ] `pdfops.py` onto PyMuPDF; drop the poppler subprocess calls
- [ ] `ink.structural_regions()` — **unresolved whether the ink is embedded images or vector `/Ink` objects**; both were measured. Resolve before building.
- [ ] Recognition over the cropped regions

## M5 — Assembly
- [ ] Final document with equations as text and figures embedded; crops deletable afterwards

## M6 — Batch
- [ ] Directory in, documents out. Only after one document works end to end.

## FRONTIER (parked)
- [ ] Non-PDF sources (`.docx` via pandoc) — [scope.md](./scope.md) § Open decisions #6

## Scripts
- Install `uv sync` · Test `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH= uv run pytest` ([runbooks/testing.md](./runbooks/testing.md)) · No deploy target
- [ ] `scripts/test.sh` — the two env vars are a ritual, and rituals get scripted
