# ocr_handler

**One text extractor for every course.** Turn a PDF into Markdown, plain text or LaTeX — reading the text
layer where one exists, and recognising the pages where it doesn't.

Built for a specific hard case: DSP lecture notes that are handwritten, exported to PDF, then annotated
live in red ink by the instructor. It generalises to any PDF where some pages have a text layer and some
do not — which, measured, is most of them.

**Status:** early. The non-ML backbone works and `ocr-handler inspect` / `text` are usable today. The OCR
half is unbuilt and its engine is deliberately unchosen — [`roadmap.md`](roadmap.md).

---

## The load-bearing insight

**Most pages need no recognition at all.**

Measured across `electrical_notes/content/` — **430 PDFs, 7,146 pages**
([`findings/corpus-census-2026-09-04.md`](findings/corpus-census-2026-09-04.md)):

| | Pages | Share |
| --- | ---: | ---: |
| Text layer already adequate | 4,790 | **67%** |
| Sparse — some content is in pixels | 1,736 | 24% |
| Empty — 482 of these have no images either, so there is nothing to recover | 620 | 8.7% |

Half of all documents (214 / 430) need no OCR anywhere. Routing on that before touching a GPU is the
difference between a fast tool and a slow one — and on those pages, extraction is *more* accurate than
any model. **The router is the product.**

Lecture PDFs fall into three kinds:

| Kind | Producer | Text layer | Needs a model? |
| --- | --- | --- | --- |
| **A** born-digital | pdfTeX / pandoc | ~1,500 chars/page, maths as Unicode | **No** — extract directly |
| **B** handwriting scan | Ghostscript | ~140 chars/page, headers only | Yes |
| **C** annotated | **PDF Annotator** | adds zero text | Yes, and separate the ink first |

**Two `-plw` files are not the same thing.** One producer means live ink was added; a matching producer on
both means the source was merely recompiled, and the "annotation" is typed text already in the text layer.

**A present text layer is not a correct one.** 51 documents extract as `C o m p u t e r` — one glyph per
text run. Detected and reported, never silently repaired: collapsing the spaces is guesswork.

---

## Install and use

```sh
uv sync
uv run ocr-handler inspect FILE.pdf        # is OCR even needed? free, no GPU
uv run ocr-handler text    FILE.pdf -o out/
```

Procedures: [`runbooks/extract-course-text.md`](runbooks/extract-course-text.md) ·
[`runbooks/testing.md`](runbooks/testing.md)

## Layout

```
src/ocr_handler/
├── textlayer.py  text-layer extraction + per-page verdict     no ML   ← the CLI's engine
├── cli.py        inspect / text                               no ML
├── pdfops.py     inspect / classify / render / pair (poppler)  no ML   ← to be folded into textlayer
├── ink.py        colour + difference separation, crop regions  no ML
├── emit.py       Markdown / text / LaTeX output               (pending, M2)
└── recognize.py  region → LaTeX behind one interface          (pending, M3)
docs/             scope, roadmap, plans, decisions, findings, research
tests/persistent/ regression floor — 7 tests
tmp/              scratch output — gitignored
```

Each module stays **under 300 lines**. If one grows past that, it is doing two jobs.

## Conventions

- **No ML outside `recognize.py`.** Everything else is deterministic and runs with no GPU.
- **Never modify the source PDF.** All output goes to a chosen directory.
- **Never run a model over a page that already has good text.** The founding rule —
  [ADR-0003](decisions/0003-text-layer-first-and-one-extractor.md).
- **Report gaps; never silently skip or repair.**
- **Git is human-only.** Agents propose commands; the operator runs them.
- Comment the step, not the syntax — every constant that came from measurement names what was measured.

## Documentation

| Read | For |
| --- | --- |
| [`scope.md`](scope.md) | What this is and is not. The blacklist, and six open operator decisions. |
| [`roadmap.md`](roadmap.md) | Milestones, re-sequenced by leverage. Lean index only. |
| [`todo.md`](todo.md) | Current state and next action. |
| [`plans/text-layer-first.md`](plans/text-layer-first.md) | **The M2 design** — four extraction modes, side by side. |
| [`plans/doctrine-compliance.md`](plans/doctrine-compliance.md) | What the doctrine requires and this project still lacks. |
| [`decisions/INDEX.md`](decisions/INDEX.md) | Why, in immutable ADRs. |
| [`findings/INDEX.md`](findings/INDEX.md) | What we measured about our own code and corpus. |
| [`research/INDEX.md`](research/INDEX.md) | What we measured about other people's tools. |
| [`directives/INDEX.md`](directives/INDEX.md) | How to work in this repo. |
