# ocr_handler

Turn lecture PDFs into Markdown or LaTeX — **equations as text, figures as cropped images.**

Built for one specific problem: DSP lecture notes that are handwritten, exported to PDF, and then annotated live in red ink by the instructor. Generalises to any PDF where some pages have a text layer and some do not.

**Status:** early. Non-ML backbone works; recognition path is being chosen — see [`docs/roadmap.md`](roadmap.md).

---

## The load-bearing insight

**Most pages need no recognition at all.**

Measured across one course's material, lecture PDFs fall into three kinds:

| Kind | Producer | Text layer | Needs a model? |
| --- | --- | --- | --- |
| **A** born-digital | pdfTeX / pandoc | ~1,500 chars/page, math as Unicode | **No** — extract directly |
| **B** handwriting scan | Ghostscript | ~140 chars/page, headers only | Yes |
| **C** annotated | **PDF Annotator** | adds zero text | Yes, and separate the ink first |

Routing on that table before touching a GPU is the difference between a fast tool and a slow one. `pdfops.inspect()` does the routing; the threshold lives in one constant.

**Two `-plw` files are not the same thing.** One producer means live ink was added; a matching producer on both means the source was merely recompiled, and the "annotation" is typed text already in the text layer. Check `pdfops.producer()` before assuming.

---

## Install

```sh
uv sync
uv run ocr-handler --help
```

## Layout

```
src/ocr_handler/
├── pdfops.py     inspect / classify / render / pair            no ML
├── ink.py        colour + difference separation, crop regions  no ML
├── emit.py       Markdown and LaTeX output                     (pending)
└── cli.py        file, page, procedure, format                 (pending)
docs/             scope, roadmap, research, decisions
tmp/              scratch output — gitignored
tests/persistent/ regression floor
```

Each module stays **under 300 lines**. If one grows past that, it is doing two jobs.

---

## Conventions

- **No ML in `pdfops` or `ink`.** Both are deterministic and must stay runnable with no GPU.
- **Never modify the source PDF.** Everything writes to an output directory.
- Comment the step, not the syntax — every constant that came from measurement says what was measured.

---

**See:** [`scope.md`](scope.md) · [`roadmap.md`](roadmap.md) · [`todo.md`](todo.md) · [`research/INDEX.md`](research/INDEX.md)
