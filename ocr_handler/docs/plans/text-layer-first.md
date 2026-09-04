# Text-layer-first extraction — the four-mode contract

> **Type: ACTIVE-SPEC.** Build-ready design for M2. Living document, named by concept (no date in the
> filename) per [../directives/roadmap-and-plans.md](../directives/roadmap-and-plans.md).
> **Nothing here is built yet.** `inspect` and `text` exist; `extract` does not.
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
| `empty`, **zero images, zero drawings** | **skip entirely** | 482 pages measured. There is nothing on the page. Rendering it and loading a model is pure waste. |

That last row is a measured routing rule, not a guess, and it must be enforced *before* any render.
`textlayer.PageText` already carries `images`; a vector-drawing count is the one field it lacks.

---

## 3 · CLI surface

```
ocr-handler inspect FILE.pdf [-p 1-10,15]
        Verdict only. Writes nothing, loads no model, needs no GPU. Always free.

ocr-handler extract FILE.pdf --mode text|ocr|both|auto  [-o OUT/] [-f md|txt|tex|json] [-p PAGES]
                            [--dpi 200] [--engine NAME] [--force]
        The one extraction verb.

ocr-handler version
```

**Three verbs, fixed.** New capability arrives as a new *value* of `--mode`, `--format` or `--engine`,
never as a new verb — see [../scope.md](../scope.md) § A note on the CLI.

### Flag decisions

- **`--mode` defaults to `text`.** The cheap, safe, non-GPU behaviour is what you get by not thinking.
  `auto` is the better everyday choice but must be asked for, because it can spend minutes on a GPU.
- **`-o/--out` has no default.** Without it, output goes to stdout and nothing is written. *Open
  decision — [../scope.md](../scope.md) #2.*
- **`--engine` is not implemented until M3.** Naming a model now would bake in a choice the research
  pass has not made.
- **`--force` re-runs OCR that the cache would otherwise skip.** See § 7.
- **`--dpi` defaults to 200** — where handwritten subscripts became reliably readable; 150 lost them,
  300 only cost time. Re-sweep if the renderer changes, because *the renderer changes answers*: poppler
  at 200 dpi produced `c o s (w o n)` where PyMuPDF at 150/200/300 all produced `\cos(\omega_0 n)`.

### The existing `text` command

`ocr-handler text` becomes `ocr-handler extract --mode text`. **Renaming is free right now** — grepped
2026-09-04, nothing invokes `text`. What does exist:

- `content/cesc_470/md_notes/README.md` documents `uv run ocr-handler inspect ...` — a real external
  consumer already, but of `inspect`, which is **not** being renamed.
- `content/cesc_410/hw/tools/course_text.py`, `hw/prompt.md` and `reference_docs/hw_workflow.md` refer to
  `ocr_handler` by directory, as the thing to use for pages they cannot read. None call the CLI.

So `inspect` is now a published surface and should be treated as stable; `text` is not, and the rename
should happen before the first caller appears rather than after.

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
| Page is genuinely blank | `"skipped": "no content"` — no `ocr` variant at all | `482 pages skipped (blank)` | Correct and expected. Never rendered, never sent to a model. |
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

## 9 · Regression floor additions (M2)

The current 7-test floor covers `pdfops` and `ink`. `cli.py` imports neither. Add, behaviour-level only:

- `test_document_verdict_matches_page_verdicts` — invariant: all `ok` ⇒ `text-layer-sufficient`;
  none `ok` ⇒ `ocr-required`; otherwise `ocr-partial`.
- `test_blank_pages_are_never_sent_to_ocr` — the 482-page rule, on a synthetic blank PDF so it runs
  without the course material.
- `test_ocr_never_silently_replaces_a_clean_text_layer` — contract test on the § 6 rule.
- `test_extract_text_mode_is_byte_stable` — a golden-master on one small committed fixture, so the
  "one extractor" promise is provable when the per-course scripts are deleted.

`test_reading_order_bands_before_columns` currently asserts on `ink._reading_order`, a private function.
Behaviour-level would test it through `ink.regions`. Worth fixing while the floor is being extended.

---

## 10 · Open questions this plan does not answer

1. **Where does output land by default?** ([../scope.md](../scope.md) #2)
2. **Is 400 chars the right `sparse` gate?** It routes 1,736 pages. Needs a labelled sample of ~50 pages
   drawn across `cec_315`, `ps160` and `cec_320` before it is trusted or moved. ([../scope.md](../scope.md) #3)
3. **JSONL or the `<|det|>` representation?** ([../scope.md](../scope.md) #5, § 4 above)
4. **Does `--format tex` emit a document or a fragment?** A lab report includes it; the notes site does not.
5. **What is the OCR unit — a page, or a cropped region?** The engines disagree: a maths-only recogniser
   needs crops, a page-level VLM needs pages. This is downstream of the engine choice and must not be
   decided ahead of it.
6. **Does `both` mode need a machine-readable verdict for CI**, or is the human review view enough?

---

**Sources:** [../findings/corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md) ·
[../research/INDEX.md](../research/INDEX.md) ·
[../archives/session_records/2026-09-02_initialize-and-teardown.md](../archives/session_records/2026-09-02_initialize-and-teardown.md) ·
`src/ocr_handler/textlayer.py`, `src/ocr_handler/cli.py` · `/home/devel/electrical_notes/tmp_ocr_child.md`
