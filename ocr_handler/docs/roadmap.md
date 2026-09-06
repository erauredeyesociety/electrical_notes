# Roadmap v2

> Lean index only: milestone bullets + path refs. Detail lives in [plans/](./plans/INDEX.md), never here.
> Boundaries: [scope.md](./scope.md) · Rules: [directives/INDEX.md](./directives/INDEX.md) · Tasks: [todo.md](./todo.md)
> Session narrative: [session_records/](./session_records/INDEX.md) (live) · [archives/session_records/](./archives/session_records/INDEX.md) (rotated)
> Earned rules: [lessons_learned/lessons.md](./lessons_learned/lessons.md)

**Mode: DEVELOPMENT.** The non-ML backbone works and is verified on real lectures. Nothing is blocked on a model.

**Re-sequenced 2026-09-04, by leverage.** Structural ink extraction and the engine choice were ahead of
the extractor; they serve **2 documents**, the extractor serves **430** ([findings/corpus-census-2026-09-04.md](./findings/corpus-census-2026-09-04.md)).
Ink work now follows the extractor. v1 of this roadmap: [archives/roadmap_v1_2026-09-04.md](./archives/roadmap_v1_2026-09-04.md).

## M1 — Non-ML backbone ✓ done (2026-09-02)
- [x] `src/ocr_handler/pdfops.py` — classify / producer / render / pair *(classifier converged onto PyMuPDF in M2; only `render` is still poppler)*
- [x] `src/ocr_handler/ink.py` — colour + diff masks, region grouping, crop
- [x] `src/ocr_handler/textlayer.py` + `cli.py` — `inspect` / `text`, PyMuPDF, per-page verdicts *(`text` became `extract --mode text` in M2)*
- [x] 7-test floor, verified on real lectures — [archives/session_records/2026-09-02_initialize-and-teardown.md](./archives/session_records/2026-09-02_initialize-and-teardown.md)

## M2 — One extractor, converged  (the 430-document path)
**Core delivered 2026-09-06** — one classifier, `extract --mode`, `emit.py`, all four must-not-break
invariants checked by measurement. What remains is the *retirement*, which is what actually closes
this milestone: three per-course scripts still exist. ← **next**
Spec: [plans/text-layer-first.md](./plans/text-layer-first.md) · Gaps: [plans/doctrine-compliance.md](./plans/doctrine-compliance.md)
- [x] **Structural faithfulness axis** (2026-09-05) — `inspect` reported 47/47 pages `ok` on a PDF whose every equation was rubble. Second axis added, density untouched — [plans/structural-faithfulness.md](./plans/structural-faithfulness.md)
- [x] **Recall raised 35.3% → 68.2% with strict precision RISING 84.8% → 93.1%** (2026-09-06). The standing hypothesis — that `_SHRED_MIN_RUN = 4` was the cause — was half wrong: lowering the run alone drops precision to 28% on Wingdings bullets that map to ASCII `z`. The fix was a *symbol* test, not a threshold — [findings/recall-was-a-symbol-test-not-a-run-length.md](./findings/recall-was-a-symbol-test-not-a-run-length.md)
- [x] **Converged the two classifiers** (2026-09-06) — `pdfops` is now a view over `textlayer`; no poppler on the classification path. It changed **428 of 7,187 corpus pages**, and the two causes are different in kind: 35 from the library swap (threshold noise — 24 of them within 20 chars of the 400 gate) and 406 from adding the vector-drawing term the plan already required. **No page moves toward `blank`.** The `482 blank pages` figure everywhere in these docs was a conflation and is really **24** — [findings/one-classifier-2026-09-06.md](./findings/one-classifier-2026-09-06.md)
- [x] **Floor test for `textlayer`** (2026-09-05/06) — 43 tests; the CLI paths are covered too
- [x] **`extract` with `--mode text|ocr|both|auto`** (2026-09-06) — `text` was renamed, not aliased; CLI is four verbs of five. The three OCR modes exit 1, name ADR-0004 and write nothing rather than returning empty as if they had succeeded. `auto` succeeds only where no page needs a model (232 of 448 documents). `--dpi`/`--engine`/`--force` deliberately NOT shipped: they parameterise a path that does not exist
- [x] **`emit.py`** (2026-09-06) — md / txt / tex / json from one intermediate. `to_markdown` and `to_text` moved unchanged and are re-exported; **output bytes verified identical across all 448 corpus documents by SHA-256**, and 48 captured CLI runs match. LaTeX is a fragment (the reversible half of open question 4); JSONL carries only the text variant, so ADR-0005's open half is untouched
- [ ] **Retire the three per-course scripts** once parity is proven — `cesc_410/hw/tools/course_text.py`, `cpsc_462/tools/extract_notes.py`, `cec_300/exam*/extract_pdfs.py`
- [ ] Put the S2 regression fixture under version control (it is in gitignored `tmp/`)
- [ ] Split `cli.py` — 359 → **432 lines** after `extract` landed, against the ~300 cap. The seam (`check`'s reading-input helpers) is real; the axis is an operator call — [plans/doctrine-compliance.md](./plans/doctrine-compliance.md)
- **Must-not-break:** page classification · document verdict · reading order · text-layer output bytes
  — **all four checked by measurement 2026-09-06, not asserted.** Output bytes, document verdict and page
  verdict: 0 of 448 documents differ. Reading order: `ink.py` untouched. Page classification: 428 of
  7,187 pages changed, decomposed and justified in [findings/one-classifier-2026-09-06.md](./findings/one-classifier-2026-09-06.md)

## M3 — Engine choice  (research closed 2026-09-06; blocked on the run itself)
- [x] **The acceptance gate is built, engine-agnostic** (2026-09-06) — `latex_repair.py` + `validity.py`, reachable as `ocr-handler check`. Compile-checking is dead (83/84 garbage outputs compiled); eight detectors on the `Signal` roll-call replace it, the eighth (`content-free`) added 2026-09-06 after the CLI found a reading of nested empty `aligned` environments that all seven called `plausible`. MinerU's repair suite was audited and rejected: over 44 recorded outputs it changes 4 and all four are damage — [plans/latex-repair-and-validity.md](./plans/latex-repair-and-validity.md)
- [ ] Head-to-head: **24 hand-transcribed equations × 3 renderings × 5 arms**, win condition fixed before the run. ⚠ The twin control is **dropped** — `diff_mask` needs no twin (PDF Annotator's optional content group reproduces it at IoU 1.0000), and P1 is one document, not two — [decisions/0004](./decisions/0004-engine-choice-deferred-decide-by-head-to-head.md)
- [x] **Designed 2026-09-06** — `recognize.py` as the façade, backends as `engines/<name>.py`, explicit dict registration (auto-discovery would let an engine become the default by being the only one that imported — ADR-0004's prohibition through the back door), **no fallback between engines ever** because the prose path destroys 2-D maths — [plans/engine-backends.md](./plans/engine-backends.md)
- [x] **Candidate slate + protocol** (2026-09-06) — five arms, VRAM from safetensors manifests not parameter counts; the target is **Turing sm_75**, confirmed by PCI ID, so Paddle's bf16 and PaddleOCR-VL's SDPA gates both fire — [research/stage2-slate-and-head-to-head-2026-09-06.md](./research/stage2-slate-and-head-to-head-2026-09-06.md)
- [ ] **Operator call: is a CPU `page-prose` backend in scope?** ADR-0004 defers only the *handwritten-maths* engine. OCRmyPDF/RapidOCR on ~400 `ps160` pages is zero verbs, zero GPU — [plans/engine-backends.md](./plans/engine-backends.md) § scope

## M4 — Annotated lectures  (the 2-document path)
- [ ] `pdfops.render()` onto PyMuPDF — the last poppler call. Blocked on re-sweeping `ink.red_mask`'s 7,000–9,500 pixel band and `merge_px = 64`, both calibrated against poppler's pixels; the renderers differ on 6.66% of pixels
- [x] **Resolved 2026-09-06: the ink is RASTERS.** 0 `/Subtype/Ink` across all three annotated lectures; the `/Ink` keys are base64 blobs in vendor `/Private` dicts. Build `ink.structural_regions()` against the raster path — [findings/mask-separability-by-stratum-2026-09-06.md](./findings/mask-separability-by-stratum-2026-09-06.md)
- [ ] **Re-sweep `RED_MARGIN` and `merge_px` per stratum** — both are P1-calibrated and P1 is one document, not two (`…-plw.pdf` carries FreeText/Highlight/Line annots and **no handwriting**)
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
