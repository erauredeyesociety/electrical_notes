# Text-layer-first extraction — the four-mode contract

> **Type: ACTIVE-SPEC.** Build-ready design for M2. Living document, named by concept (no date in the
> filename) per [../directives/roadmap-and-plans.md](../directives/roadmap-and-plans.md).
> **Status 2026-09-06: the text half is BUILT.** `inspect`, `extract` and `check` exist; `text` was
> renamed to `extract --mode text`. `emit.py` renders all four formats. The three OCR modes refuse and
> say why — see § 2 and § 11. What is delivered, and what deliberately deviates from this spec, is
> § 11 at the bottom.
> `check` (§ 3) is not part of this contract — it landed 2026-09-06 under
> [./latex-repair-and-validity.md](./latex-repair-and-validity.md) § 7 and is listed here only
> because this document owns the verb inventory.
> Written 2026-09-04. Grounded in [../findings/corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md).
> Boundaries: [../scope.md](../scope.md) · Engine: **unresolved**, see [../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md)

---

## 1 · The principle

**The text layer is the ground truth wherever it exists.** OCR is a *repair* applied to pages where the
ground truth is missing or provably corrupt — never a replacement for bytes that are already correct.

Everything below follows from that one sentence. Where a design choice is arbitrary, the tie is broken by
asking which option makes it harder to silently discard exact text in favour of guessed text.

**Measured justification.** 67% of pages (4,790 / 7,146) and 50% of documents (214 / 430) need no
recognition at all. A tool that OCRs everything would be slower and *less accurate* on two thirds of the
corpus. The router is the product.

---

## 2 · The four modes

| Mode | What runs | Cost | For |
| --- | --- | --- | --- |
| `text` *(default)* | text layer only | ms | The 214 `text-layer-sufficient` documents. The everyday case. |
| `ocr` | recognition on every requested page | seconds/page, GPU | A known-bad file; building the comparison set; forcing a re-read. |
| `both` | both, on every requested page, side by side | text + full OCR | **Deciding whether OCR is worth it at all.** An evaluation mode, not a production one. |
| `auto` | text layer everywhere; OCR only on pages the text layer failed | text + OCR on the failures | The 188 `ocr-partial` documents. The mode that should end up doing most of the work. |

`auto` is `both` with a filter, and `text`/`ocr` are `both` with one half disabled. **One code path, four
gates** — writing four pipelines is how they diverge, which is the exact failure this project exists to fix.

### What `auto` decides to OCR, and what it must refuse to

Per page, from data the free `inspect` pass already produces:

| Page state | Action | Why |
| --- | --- | --- |
| `verdict == ok` and not letter-spaced | text layer, no OCR | The bytes are exact. |
| `verdict == ok` **but letter-spaced** | **OCR too, and compare** | A dense text layer can still be corrupt. Fires on 51 documents. |
| `sparse` or `empty`, **and the page has images or drawings** | OCR | 1,874 pages measured. Content is present, in pixels. |
| `empty`, **zero images, zero drawings** | **skip entirely** | **24 pages measured** — not 482, see below. There is nothing on the page. Rendering it and loading a model is pure waste. |

That last row is a measured routing rule, not a guess, and it must be enforced *before* any render.

> **Correction, 2026-09-06 — the 482 was a conflation, and it is now 24.**
> 482 counted pages with no text and *no images*. The census flagged this in its own caveats. Once the
> vector-drawing count this table already demanded is applied, **405 of those 483 pages turn out to be
> full of vector content** — `cec_315/hw_practice_problems/lctr22-exercise.pdf` page 1 is 0 characters,
> 0 images, **1,837 vector paths** and 8.9% non-white pixels. Skipping them would have silently
> discarded whole pages. The true skip set is **24 pages**; OCR candidates are **2,329**.
> [../findings/one-classifier-2026-09-06.md](../findings/one-classifier-2026-09-06.md)

`textlayer.PageText` now carries `images`, `drawings` **and** `drawn_images`. The third exists because
`get_images(full=True)` misses an image painted from inside a Form XObject — measured on 14 pages, one
of which had no drawings either and was being routed `blank`. Both new counts are **lazy**: taken only
where `verdict != "ok" and images == 0`, i.e. only where they can change an answer, which is 483 of
7,187 pages. Eager `get_drawings()` on every page costs 83.4 s against a 15.8 s text pass; lazy
`get_cdrawings()` (identical counts on all 7,187 pages, 18.4 s eager) costs about 5 s.

---

## 3 · CLI surface

```
ocr-handler inspect FILE.pdf [-p 1-10,15]
        Verdict only. Writes nothing, loads no model, needs no GPU. Always free.

ocr-handler extract FILE.pdf --mode text|ocr|both|auto  [-o OUT/] [-f md|txt|tex|json] [-p PAGES]
        The one extraction verb. BUILT 2026-09-06; the three OCR modes refuse and say why.
        `--dpi` / `--engine` / `--force` are NOT shipped — see § 11.

ocr-handler check   READINGS [--crop WxH] [--repair]
        Is a recorded equation-model reading trustworthy, and what would LaTeX repair change?
        Free, no GPU, writes nothing. Added 2026-09-06 —
        [./latex-repair-and-validity.md](./latex-repair-and-validity.md) § 7.

ocr-handler version
```

**Four verbs of the five [../scope.md](../scope.md) allows.** New capability arrives as a new *value*
of `--mode`, `--format` or `--engine`, never as a new verb — see
[../scope.md](../scope.md) § A note on the CLI. `check` is the one exception taken so far, and it is
taken because its input is a recorded model output, not a PDF: making it a `--mode` of `extract`
would mean `extract` accepted two unrelated input types. The reasoning and the numbers behind it are
in [./latex-repair-and-validity.md](./latex-repair-and-validity.md) § 7.1.

### Flag decisions

- **`--mode` defaults to `text`.** The cheap, safe, non-GPU behaviour is what you get by not thinking.
  `auto` is the better everyday choice but must be asked for, because it can spend minutes on a GPU.
- **`-o/--out` has no default.** Without it, output goes to stdout and nothing is written. *Open
  decision — [../scope.md](../scope.md) #2.*
- **`--engine`, `--force` and `--dpi` are NOT SHIPPED.** All three parameterise a path that does not
  exist, and a flag that silently does nothing is exactly the dishonesty this project is built against —
  [../directives/code-discipline.md](../directives/code-discipline.md), *"options are where small tools
  go to die."* They arrive with M3, together with the thing they configure. Their intended meanings, kept
  for M3: `--engine` names the model (naming one now would bake in a choice the research pass has not
  made); `--force` re-runs OCR the cache would skip (§ 7); `--dpi` defaults to 200 — where handwritten
  subscripts became reliably readable, 150 lost them, 300 only cost time. Re-sweep `--dpi` if the
  renderer changes, because *the renderer changes answers*: poppler at 200 dpi produced `c o s (w o n)`
  where PyMuPDF at 150/200/300 all produced `\cos(\omega_0 n)`. `--dpi` lives on `recognize.py` today
  as a keyword argument with that default and that comment.

### The existing `text` command — RENAMED 2026-09-06, and it did not survive

`ocr-handler text` **is** `ocr-handler extract --mode text`. The rename was taken, not deferred, and
`text` was **removed rather than aliased**: keeping both would spend the fifth of five verbs
[../scope.md](../scope.md) allows on one capability under two names, which is the divergence this
project exists to end.

Re-grepped 2026-09-06 across the whole of `electrical_notes` before renaming: **nothing outside
`ocr_handler/docs/` invokes `text`.** The four external mentions of the CLI
(`content/cesc_470/md_notes/README.md`, `content/cesc_470/hw/prompt.md`,
`content/cesc_470/reference_docs/findings.md`, `docs/directives/coursework-solutions.md`, `docs-rag/README.md`)
all call `inspect`, which is unchanged. The two internal ones — this file and
[../runbooks/extract-course-text.md](../runbooks/extract-course-text.md) — were updated with the rename.

Byte-stability was proven, not assumed: 48 captured `text` stdout/stderr runs and 6 output directories
are identical under `extract --mode text`, and `to_markdown`/`to_text` hash identically across all 448
corpus documents. What was true on 2026-09-04 and still holds:

- `content/cesc_470/md_notes/README.md` documents `uv run ocr-handler inspect ...` — a real external
  consumer already, but of `inspect`, which is **not** being renamed.
- `content/cesc_410/hw/tools/course_text.py`, `hw/prompt.md` and `reference_docs/hw_workflow.md` refer to
  `ocr_handler` by directory, as the thing to use for pages they cannot read. None call the CLI.

`inspect` is a published surface and is treated as stable.

---

## 4 · The intermediate

One record per page, written as JSONL. It is the artifact; every other output is a *view rendered from
it*. Writing two extractors, or extracting to one format and converting, both end badly.

```json
{"page": 5,
 "verdict": "sparse", "chars": 142, "images": 3, "drawings": 7, "letter_spaced": false,
 "variants": {
   "text": {"source": "textlayer/pymupdf", "chars": 142, "ms": 3, "text": "..."},
   "ocr":  {"source": "<engine>@<precision>", "chars": 987, "ms": 8500, "dpi": 200, "text": "..."}},
 "agreement": {"text_tokens": 21, "ocr_tokens": 180, "shared": 19,
               "text_tokens_lost_by_ocr": 2, "new_chars": 845},
 "chosen": "ocr",
 "reason": "text layer sparse (142 chars); ocr added 845 chars and kept 19/21 text-layer tokens"}
```

**`chosen` and `reason` are mandatory on every record, in every mode.** A tool that picks one text over
another without saying why is the "system that does not tell the truth about itself" the doctrine names as
the #1 velocity tax. In `both` mode `chosen` records the *recommendation*; the file still carries both.

> **Open decision — [../scope.md](../scope.md) #5.** JSONL is the proposal. The alternative on the table is
> the `<|det|>CATEGORY [bbox]<|/det|>CONTENT` representation adopted from Baidu Unlimited-OCR. That
> adoption predates the operator's warning that *"the example repos it might be picking apart might not be
> the best solutions either"* — it should be re-justified on its own merits, or dropped. JSONL is
> recommended because it is greppable, streamable, and owes nothing to an inspiration under review.

**Built 2026-09-06 — only the half that is not in dispute.** `emit.to_jsonl` emits one record per page
with `page`, `verdict`, `chars`, `images`, `drawings`, `drawn_images`, `structure`, `signals`,
`letter_spaced`, `variants.text`, `chosen`, `reason` and — where it applies — `skipped`. There is **no
`ocr` variant and no `agreement` block**, because ADR-0005 is still under review and no engine's native
format was ever a candidate for the *text* variant. Nothing downstream is built against the disputed
half. Reachable as `extract -f json`, written as `<slug>.pages.jsonl`.

---

## 5 · Output layout

```
OUT/
  <slug>.md            the chosen text — what a consumer reads
  <slug>.pages.jsonl   the intermediate; written whenever more than one variant exists
  <slug>.compare.md    the side-by-side review view — --mode both only
  <slug>.ocr/          page renders and crops — only when OCR actually ran
```

`<slug>.md` always exists and always carries the same header block `to_markdown()` writes today: page
count, chars/page, the list of pages needing OCR, and the letter-spacing warning. That header is the
project's honesty contract with a reader who never opens the JSONL.

### The comparison view

One section per page, both variants at full width and clearly labelled — **not** a two-column table.
Equations and code wrap badly in narrow columns, and the reviewer's actual task is reading two blocks of
text closely, not scanning a grid.

```markdown
## Page 5 — sparse (142 chars, 3 images)   →  recommend: OCR

**Signals** — text 142 ch · ocr 987 ch · +845 new · 19/21 text-layer tokens kept · no loss

### A · text layer  (pymupdf, 3 ms)
    ω₀
    Example 2.4

### B · ocr  (<engine>, 8.5 s, 200 dpi)
    \cos(\omega_0 n) + j\sin(\omega_0 n)
    Example 2.4 — evaluate at ...

### Tokens only in A  (2)
    `2.4`  `ω₀`
```

**"Tokens only in A" is the load-bearing section.** Everything else flatters OCR, because OCR is almost
always longer. What a reviewer needs to see fastest is *what the text layer had and OCR lost* — that is
the only evidence that switching would be a downgrade.

---

## 6 · How a reviewer decides which is better

Five signals, ordered by how much they should move the decision. All are computable; none require the
reviewer to read both blocks in full.

1. **Loss.** `text_tokens_lost_by_ocr` — text-layer tokens absent from the OCR output. **Non-zero loss on
   an `ok` page is a veto.** Exact bytes are never traded for guessed ones without a human saying so.
2. **Gain.** `new_chars` — characters OCR produced that the text layer did not have. Zero gain means OCR
   is not worth its cost on this page, whatever else is true.
3. **Corruption.** `letter_spaced` on the text layer. When it fires, the text layer is present but wrong,
   and OCR is the *only* honest source. This is the case where a dense page should still be OCR'd.
4. **Maths yield.** Count of LaTeX math tokens (or Unicode math characters) in each variant. On
   born-digital LaTeX the text layer wins outright — `∑ ∫ 𝜋 𝜔` all extract as real characters, and
   converting Unicode maths to LaTeX is a *transformation*, not a recognition problem.
5. **The control run.** Where an un-annotated twin exists, run OCR on it too. If the twin returns the
   same content as the annotated file, the model is confabulating rather than reading the ink. This
   caught a real failure once already and is a standing method, not an optional check.

**The recommendation rule, in order:** loss on an `ok` page → keep text · zero gain → keep text ·
letter-spaced → take OCR · otherwise gain > 0 and no loss → take OCR · anything else → **flag for a human**
and keep text. The tool recommends; `both` never overwrites.

---

## 7 · The "OCR returned nothing" cases — three, not one

Conflating these is how a broken engine looks like a clean corpus. Each gets its own record value and its
own line in the summary.

| Case | Record | Summary line | What it means |
| --- | --- | --- | --- |
| Page is genuinely blank | `"skipped": "no content"` — no `ocr` variant at all | `24 page(s) skipped (blank: no text, no images, no drawings)` | Correct and expected. Never rendered, never sent to a model. **Built.** The 482 was a conflation — see § 2. |
| OCR ran, produced **zero characters** | `"ocr": {"chars": 0, "error": null}` | `⚠ 3 pages: OCR returned empty` | **A tool problem, and loud.** A model that returns nothing on a page with three images has failed. |
| OCR ran, produced text, **all of it already present** | `"new_chars": 0`, `chosen: "text"` | `12 pages: OCR added nothing new` | Correct and useful — it is evidence that the text layer was already complete. |

A run where case 2 is non-zero must not exit 0 silently. **Never** collapse case 2 into case 1: a page
with images that yields no OCR text is a defect report, not a blank page.

---

## 8 · Caching and re-runs

Extraction over 430 documents will be re-run often; OCR at ~8.5 s/page over 2,356 candidate pages is
hours. Cache key: `(sha256 of the page's content stream, engine id, precision, dpi)`. A cache hit is
reported, not hidden. `--force` bypasses it.

**Determinism is a prerequisite for the regression floor**, so `temperature=0` on every engine, always.
And **serialise GPU work** — a concurrent 1,318 MiB process caused an OOM mid-session once already.

---

## 9 · Regression floor additions (M2) — DONE, `tests/persistent/test_extract.py`

**142 tests pass** (120 before M2; +22). All four named tests exist, plus the convergence guards. Every
one builds its own PDF in-process, so the floor holds on a machine with no course material.

- [x] `test_document_verdict_matches_page_verdicts` — all `ok` ⇒ `text-layer-sufficient`; none `ok` ⇒
  `ocr-required`; otherwise `ocr-partial`.
- [x] `test_blank_pages_are_never_sent_to_ocr` — the skip rule, on a synthetic blank PDF.
- [x] `test_ocr_never_silently_replaces_a_clean_text_layer` — contract test on the § 6 rule.
- [x] `test_extract_text_mode_is_byte_stable` — golden master, transcribed verbatim into the test rather
  than pointed at a gitignored fixture. Verified non-vacuous: a one-character change to the Markdown
  header fails it.
- [x] `test_pdfops_classification_is_textlayers_classification` and
  `test_no_poppler_subprocess_on_the_classification_path` — the convergence cannot silently regrow.
- [x] `test_a_vector_only_page_is_not_blank` — the 405-page correction, on a synthetic vector PDF.
- [x] `test_ocr_modes_fail_loudly_and_write_nothing` — exit 1, names ADR-0004, writes no half-answer.

Still open: `test_reading_order_bands_before_columns` asserts on `ink._reading_order`, a private
function. Behaviour-level would test it through `ink.regions`. **Not done** — `ink.py` was deliberately
not touched during M2 so that "reading order unchanged" could be proven by not changing it.

---

## 10 · Open questions this plan does not answer

1. **Where does output land by default?** ([../scope.md](../scope.md) #2)
2. **Is 400 chars the right `sparse` gate?** It routes 1,736 pages. Needs a labelled sample of ~50 pages
   drawn across `cec_315`, `ps160` and `cec_320` before it is trusted or moved. ([../scope.md](../scope.md) #3)
3. **JSONL or the `<|det|>` representation?** ([../scope.md](../scope.md) #5, § 4 above)
4. **Does `--format tex` emit a document or a fragment?** A lab report includes it; the notes site does not.
   **Still open — but the shipped answer is a FRAGMENT**, chosen because it is the reversible half:
   wrapping a fragment in a preamble is a two-line `\documentclass`, while unwrapping a document means
   parsing back out of it. Escaping is applied to the ten TeX specials, which is lossless and mechanical
   and is not covered by the ban on silently repairing text; Unicode maths passes through untouched, so
   the fragment needs lualatex/xelatex + `unicode-math`, and its own header comment says so.
5. **What is the OCR unit — a page, or a cropped region?** The engines disagree: a maths-only recogniser
   needs crops, a page-level VLM needs pages. This is downstream of the engine choice and must not be
   decided ahead of it.
6. **Does `both` mode need a machine-readable verdict for CI**, or is the human review view enough?

---

## 11 · What was delivered, 2026-09-06 — and where it deviates from this spec

**Built.** One classifier, four modes, one intermediate, four views.

| | |
| --- | --- |
| `src/ocr_handler/emit.py` | **new**, 263 lines. `to_markdown` / `to_text` moved here unchanged; `to_latex` and `to_jsonl` added; `FORMATS` maps a format name to a renderer, so adding a format is adding a row. |
| `src/ocr_handler/recognize.py` | **new**, 58 lines. The honest stub: `available()` is `False`, `recognize()` raises `EngineUnavailable`, and `UNAVAILABLE` is the one refusal string so every caller says the same thing. |
| `src/ocr_handler/pdfops.py` | 124 → 169 lines. `inspect` / `inspect_all` / `page_count` / `page_text` / `producer` are now views over `textlayer.extract`. **No poppler on the classification path.** |
| `src/ocr_handler/textlayer.py` | 228 → 252 lines. Renderers moved out (−62) and re-exported; `drawings`, `drawn_images`, `skip_reason`, `has_pixels`, `blank_pages`, `ocr_candidates` added, each carrying the measurement that produced it. Still under the cap. |
| `src/ocr_handler/cli.py` | 359 → 432 lines. `text` removed, `extract` added. ⚠ **worsens a known doctrine gap — see below.** |
| `tests/persistent/test_extract.py` | **new**, 22 tests. Total **142**, up from 120. |

**CLI surface now — four verbs of five:** `inspect`, `extract`, `check`, `version`.

### Deviations from this spec, and why

1. **`--dpi`, `--engine` and `--force` are not shipped.** § 3 lists them; all three parameterise a path
   that does not exist. A flag that silently does nothing is the dishonesty this project is built
   against. They arrive with M3 alongside the thing they configure.
2. **`--mode auto` succeeds on a document that needs no OCR.** § 2 defines `auto` as "OCR only on pages
   the text layer failed on". Where it failed nowhere, the run is genuinely complete without a model, and
   failing would be dishonest in the other direction — it would claim a model was needed when it was not.
   That is 232 of 448 documents. `ocr` and `both` always fail, because they are defined over *every*
   requested page. All three refusals exit **1**, name ADR-0004, and write nothing.
3. **`<slug>.compare.md` (§ 5) and the five reviewer signals (§ 6) are not built.** Both need a second
   variant to compare, and there is no engine to produce one. The `agreement` block is absent from the
   JSONL for the same reason. Building the comparison view against an imagined OCR output would be
   guessing at the shape of the thing M3 exists to measure.
4. **Caching (§ 8) is not built.** Its cache key includes the engine id and precision.

### Known cost of this work

**`cli.py` grew 359 → 432 lines**, against the project's own ~300 cap
([../directives/code-discipline.md](../directives/code-discipline.md) line 3). It was already over, and
this made it worse by 73 lines. The seam is real and named in
[./doctrine-compliance.md](./doctrine-compliance.md): `check`'s input parsing and reporting have nothing
to do with PDFs and would move cleanly to their own module. It was **not** done here because the axis to
split on is an open call the operator has not made, three modules are in the same state, and doing one of
them mid-M2 is the unrequested restructuring [../directives/scope-discipline.md](../directives/scope-discipline.md)
warns about. Reported, not absorbed.

---

**Sources:** [../findings/corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md) ·
[../findings/one-classifier-2026-09-06.md](../findings/one-classifier-2026-09-06.md) ·
[../research/INDEX.md](../research/INDEX.md) ·
[../archives/session_records/2026-09-02_initialize-and-teardown.md](../archives/session_records/2026-09-02_initialize-and-teardown.md) ·
`src/ocr_handler/textlayer.py`, `src/ocr_handler/cli.py` · `/home/devel/electrical_notes/tmp_ocr_child.md`
