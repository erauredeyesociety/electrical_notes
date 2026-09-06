# TODO — single source of truth

> Last updated: 2026-09-06 · **MODE: development**
> Index, not an essay. Detail lives behind the links.

## CURRENT STATE

**The backbone works; the acceptance gate is built; the TEXT HALF of the extractor now works too.**

`pdfops` + `ink` classify, render, separate ink and crop regions on real lectures. `textlayer` + `cli`
give per-page density (`ok`/`sparse`/`empty`) **and** structural faithfulness (`intact`/`suspect`)
verdicts on two independent axes. `ocr-handler check` (2026-09-06) scores a recorded model reading
against eight detectors and repairs its LaTeX — free, CPU-only, writes nothing.

**M2's first three items landed 2026-09-06.** There is now **one classifier** (PyMuPDF; `pdfops` is a
view over `textlayer`, no poppler on that path), **one extraction verb** — `extract --mode
text|ocr|both|auto`, with the three OCR modes refusing honestly until M3 — and **one intermediate**
rendered four ways by `emit.py` (md / txt / tex / json). The text path's output bytes are unchanged, and
that was proven by SHA-256 over all 448 corpus documents rather than asserted.

**142 tests pass** (was 120). Run: `PYTHONPATH=src python3 -m pytest tests/ -q` (or the documented
`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH= uv run pytest` — [runbooks/testing.md](./runbooks/testing.md)).

**The project's shape changed 2026-09-04.** It is *the ONE text extractor for every course*, replacing
the per-course scripts: **430 PDFs / 7,146 pages** for the extractor against **2 documents** for the
annotated-ink path — [findings/corpus-census-2026-09-04.md](./findings/corpus-census-2026-09-04.md).

**Engine choice remains open.** Do not build against any named model. What changed 2026-09-06 is that
the gate to *judge* engines now exists and is engine-agnostic —
[plans/latex-repair-and-validity.md](./plans/latex-repair-and-validity.md).

Last session: [session_records/2026-09-06_repair-audit-recall-and-validity.md](./session_records/2026-09-06_repair-audit-recall-and-validity.md).

## NEXT ACTION

**M2's remaining items**, in [roadmap.md](./roadmap.md) § M2 order:

1. **Retire the three per-course scripts** — `cesc_410/hw/tools/course_text.py`,
   `cpsc_462/tools/extract_notes.py`, `cec_300/exam*/extract_pdfs.py`. **Parity has to be proven first**,
   and one gap is already known: `extract_notes.py` handles `.docx` via pandoc, which is
   [scope.md](./scope.md) open decision #6, not something to absorb quietly.
2. **Split `cli.py`** — 432 lines against a ~300 cap. See Doctrine gaps below.
3. **Put the S2 regression fixture under version control** (it is in gitignored `tmp/`).

Then M3 — the engine head-to-head, which everything OCR-shaped is now waiting on and nothing else is
blocked by. `recognize.py` exists as one honest refusal and is the file M3 fills in.

## Blocked / awaiting operator

Named calls in [scope.md](./scope.md) § Open decisions — batch them, guess none. Highest-impact first:
**output destination**, **the 400-char `sparse` gate**, **non-PDF inputs**.

**New 2026-09-06:** `check` puts the CLI at **four verbs of five** — `inspect`, `extract`, `check`,
`version`. [scope.md](./scope.md) § 96 calls a new verb a scope question, not a coding task. It could
not be a `--mode` of `extract` — its input is a recorded model output, not a PDF. Confirm or reshape.

**New 2026-09-06:** **`--format tex` emits a FRAGMENT**, not a document — plan open question #4. The
fragment was chosen because it is the reversible half, not because the question is settled. Confirm.

## Known issues

- **`482 blank pages` was a conflation and is really 24.** It counted pages with no text and *no
  images*; 405 of those 483 pages are full of **vector** content — one is 0 characters, 0 images, 1,837
  vector paths and 8.9% non-white pixels. The census flagged the risk in its own caveats; it is now
  measured and the rule is fixed. Every doc quoting 482 has been corrected —
  [findings/one-classifier-2026-09-06.md](./findings/one-classifier-2026-09-06.md)
- ~~**The ink is images or vectors and we do not know which.**~~ **CLOSED 2026-09-06 — it is rasters.**
  Measured across all three annotated lectures: **0 `/Subtype/Ink` objects**, 6/36/14 raster XObjects.
  The `/Ink` keys an earlier note counted are opaque base64 blobs inside vendor `/Private` dicts, not
  PDF ink annotations, so `tmp_ocr_child.md`'s *"it is vector ink … geometry, not pixels"* is wrong.
  M4 can be built against the raster path —
  [findings/mask-separability-by-stratum-2026-09-06.md](./findings/mask-separability-by-stratum-2026-09-06.md).
- **`ink.py`'s constants are calibrated on P1 and do not transfer.** The mask *approach* works on all
  three strata, but `RED_MARGIN = 55` transposed to P3's blue ink **destroys the handwriting** — 18,995
  ink pixels at margin 25 fall to 6,296 at 55, a 67% loss (77% on `M17 Review.pdf`), leaving a broken
  dotted skeleton that would have scored as a *model* failure. Locator and paint have **opposite**
  tolerances: the locator dilates before labelling so it tolerates erosion, the paint is reproduced
  pixel-for-pixel so it tolerates contamination. Use `locator=blue(55)`, `paint=blue(25)|dark`.
  `merge_px = 64`'s plateau is likewise a P1 property — on P2 p5 it returns one region of 1,871 kpx,
  half the page. Re-sweep per stratum before M4.
- **`_is_strong` is blind in the direction of its own target.** When a fraction flattens, the font
  often mangles the operator with it — `∫`→`Z`, `√`→`r`, `Σ`→`X`, `∏`→`Q` — so **no mathematical
  character survives** and the rule that pays for `min_run 2` cannot fire on exactly the pages it most
  wants. Verified: a run of `Z / p / dV` fires nothing. Costs ~23 corpus pages of real loss [12, 37].
  Not fixable from a `str` — telling a mojibake'd `∫` from a literal `Z` needs the **font**, so this
  belongs with the flattened-superscript detector in the "needs a `page`, not a `str`" bucket.
- **A maths-free control corpus is vacuous against this detector.** 13 documents / 47 pages of syllabi,
  ARM assembly, Python listings and rubrics fire **0 at every `_SHRED_MAX_CHARS` from 4 to 12** — with
  no character in `_SYMBOLIC_RANGES`, `_is_strong` can never pass, so such a corpus **bounds nothing**.
  A useful control must contain mathematics that is *not* flattened. Two `ps160` exam papers do
  discriminate (FP 3/67 at 4, 4/67 flat from 5 to 12). ⚠ Screening is unreliable: a third exam paper
  passed the same screen and pages 2–3 were full formula sheets — roughly one candidate in three fails
  on a page nobody would predict.
- **`page.get_text()` splices FreeText annotation text into the body stream** — a fifth faithfulness
  fault, seen on the `-plw` lecture, that no detector currently sees.
- **The corpus is measurably duplicated.** 459 documents carry **355 distinct text layers**, and the
  732 flagged pages are **513 distinct pages** (1.43×, above the corpus average). Any sample drawn
  per-document over-weights whatever is filed three times.
- **`_SHRED_MAX_CHARS` is unsettled, not decided.** Its sweep priced recall as cost, because the
  "control corpus" it used is not one — **44 of its 49 hits are real flattened mathematics**.
  [findings/recall-was-a-symbol-test-not-a-run-length.md](./findings/recall-was-a-symbol-test-not-a-run-length.md)
- **A content-free reading can still hide below `content-free`'s floor.** A lone two-entry row vector
  is two content tokens and would fire. Zero readings in any corpus are that short, but that is the
  shape a false positive takes.
- **The flattened-superscript detector is specified but not shipped** — `7.50 × 10³ Pa` extracts as
  `103 Pa`, a *false numeric value*. A prototype catches 3 of 4 labelled rows; it needs a `page` rather
  than a `str` in the `_DETECTORS` signature and takes the corpus pass 22 s → 58 s.
- `diff_mask` untested against a *recompiled* twin, where the whole page shifts. Guard: check the
  changed fraction and refuse if implausibly large.
- `merge_px=64` is calibrated for 200 dpi only — a pixel distance, so re-sweep if dpi changes.
- Structural extraction gave 2 ink images on page 5 where pixel grouping gave 5 logical items.
  Expected; they compose. Neither count is canonical.

## Doctrine gaps

Full checklist: **[plans/doctrine-compliance.md](./plans/doctrine-compliance.md)**.

- **Five of ten modules exceed the project's own ~300-line cap** —
  [directives/code-discipline.md](./directives/code-discipline.md) line 3, *"past that it is doing two
  jobs and nobody re-reads it."* `structure.py` 462 · **`cli.py` 432** · `validity.py` 428 ·
  `latex_repair.py` 327 · `crops.py` 308. **`cli.py` grew 359 → 432 on 2026-09-06 when `extract`
  landed** — reported, not absorbed. Each is a **plausible split** rather than an obvious one —
  `structure.py` holds four detectors plus the tokenising helpers they share; `validity.py` holds eight
  plus its tokeniser; `cli.py` holds four verbs, and the real seam is that `check`'s reading-input
  parsing has nothing to do with PDFs. Split by *axis*, not by line count, and only where the seam is
  real. The new modules are inside the cap: `emit.py` 263, `recognize.py` 58, `pdfops.py` 169,
  `textlayer.py` 252.
- **Six modules are untracked by git** — `crops.py`, `latex_repair.py`, `structure.py`, `validity.py`
  and now `emit.py`, `recognize.py`, plus `tools/`, `tests/fixtures/` and
  `tests/persistent/test_extract.py`. One `git clean` from gone. **Git is human-only**; this is
  reported, never resolved.
- The S2 regression fixture sits in gitignored `tmp/`. The `check`-path fixtures are transcribed into
  the tests verbatim for exactly this reason, but S2 is not.
- `scripts/test.sh` — the two env vars are a ritual, and rituals get scripted.

## Recently closed

- ~~Two page classifiers, on two PDF libraries~~ — **one classifier**, PyMuPDF only. Changed 428 of
  7,187 pages, all of them toward finding content; ADR-0001 is satisfied except for `render`, which is
  M4 and says why in its docstring.
- ~~`ocr-handler text`~~ — renamed to `extract --mode text`, **removed rather than aliased**. Re-grepped
  first: nothing outside `ocr_handler/docs/` ever called it.
- ~~`emit.py` and `recognize.py` are pending~~ — both exist. `recognize.py` is one honest refusal, not a
  placeholder that returns `""`.
- ~~`is_letter_spaced` fires on 51 documents~~ — an **overcount of ~17×**. `\s` matched newlines, so
  plot tick labels scored as corrupt. Corrected pattern measures **3 documents**.
- ~~`textlayer.py` is untracked~~ — tracked.
- ~~The shipped CLI has zero test coverage~~ — `inspect` and `check` both carry CLI-level tests.
- ~~The `ti` ligature is silently dropped~~ — it extracts as **U+0017** and `unmapped-glyphs` already
  catches it on 89 of 92 pages.
- ~~MinerU's `mfr/utils.py` is worth vendoring~~ — **rejected**, 11 defects.

---

**See:** [roadmap.md](./roadmap.md) · [scope.md](./scope.md) · [plans/INDEX.md](./plans/INDEX.md) ·
[decisions/INDEX.md](./decisions/INDEX.md) · [lessons_learned/lessons.md](./lessons_learned/lessons.md)
