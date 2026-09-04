# Research — INDEX

**EXTERNAL** teardowns: tools, libraries and services studied *before* building, so nothing here gets
reinvented. Analyses of this repo's own material go in [../findings/INDEX.md](../findings/INDEX.md).

**EMPTY.** No external study has been done at the root level, and none is currently needed — the root
repo's dependencies are all decided and stable (Hugo + hextra, tectonic, pandoc, `uv`).

**The research that exists is a child project's**, and is not restated here:

| Where | What was studied |
| --- | --- |
| [`ocr_handler/docs/research/INDEX.md`](../../ocr_handler/docs/research/INDEX.md) | The local-OCR landscape — UniMERNet, SmolDocling, Baidu Unlimited-OCR, Qwen2.5-VL and six ruled-out alternatives, several measured on this machine's 6 GB GPU. Also why PyMuPDF replaces poppler, and why numpy+scipy+Pillow beat OpenCV here. |
| [`ocr_handler/docs/research/unlimited-ocr.md`](../../ocr_handler/docs/research/unlimited-ocr.md) | The upstream project named as this work's inspiration, torn down and measured |

## What would belong here

- A **Hugo/hextra** teardown, if the site ever needs behaviour the theme does not give.
- A **tectonic vs. latexmk/xelatex** comparison, if the build ever needs something tectonic cannot do.
- A **pandoc** study, if `.docx`/`.pptx` → Markdown conversion outgrows
  [`content/cpsc_462/tools/extract_notes.py`](../../content/cpsc_462/tools/extract_notes.py).

Nothing above is needed today. Add a file when a decision actually gates on it —
[../directives/documentation-discipline.md](../directives/documentation-discipline.md).
