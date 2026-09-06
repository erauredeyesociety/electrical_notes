# Extracting a course's text

**What works today.** `inspect` and `extract` (plus `check`, which reads model output rather than PDFs).
`extract --mode text` is the default and is the whole of what runs: **the three OCR modes refuse**, because
the engine is deliberately unchosen ([../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md)).
Everything below reads text layers only.

```sh
cd /home/devel/electrical_notes/ocr_handler
uv sync                         # first time only
```

## 1 · Ask whether OCR is even needed

Free. Loads no model, writes nothing, needs no GPU. **Always do this first.**

```sh
uv run ocr-handler inspect "../content/cec_315/all_lectures/cec315-lctr12-fourier-transforms.pdf"
```

```
cec315-lctr12-fourier-transforms.pdf: 34 pages, 21,433 chars (630/page)
verdict: ocr-partial
  ok 28   sparse 5   empty 1
  pages needing OCR: 3, 17, 22, 29, 33, 34
  ! letter-spacing artefacts detected (one glyph per text run)
```

Read it as:

| Line | Means |
| --- | --- |
| `verdict: text-layer-sufficient` | Every page is fine. Extract and stop. |
| `verdict: ocr-partial` | Some pages carry nothing. The `.md` will be honest about which. |
| `verdict: ocr-required` | No page has usable text. A scan or handwriting. |
| `! letter-spacing artefacts` | **The text layer is present but corrupt.** What you extract will contain `C o m p u t e r`. It is left uncollapsed on purpose — repairing it is guesswork. |

## 2 · Extract

```sh
uv run ocr-handler extract FILE.pdf                     # to stdout, --mode text
uv run ocr-handler extract FILE.pdf -o out/             # writes out/<slug>.md
uv run ocr-handler extract FILE.pdf -o out/ -f txt      # plain text, for grep
uv run ocr-handler extract FILE.pdf -o out/ -f tex      # LaTeX FRAGMENT — \input it
uv run ocr-handler extract FILE.pdf -o out/ -f json     # out/<slug>.pages.jsonl, one record per page
uv run ocr-handler extract FILE.pdf -p 1-10,15          # selected pages
```

All four formats are views of one intermediate, so they cannot disagree. `-f tex` is a fragment with no
preamble and needs a Unicode engine (lualatex/xelatex + `unicode-math`); its own header comment says so.

### The modes

```sh
uv run ocr-handler extract FILE.pdf --mode auto      # OCR only the pages the text layer failed on
```

`--mode ocr` and `--mode both` always exit **1**. `--mode auto` exits 1 too *unless* no page needs a
model, which is 232 of 448 documents — for those it is the complete answer and it says how many pages it
skipped as blank. None of the three ever returns an empty result as if it had succeeded.

The Markdown carries a header stating the page count, chars/page, which pages have no text layer, and any
letter-spacing warning. **Do not strip that header** — it is the only place a downstream reader learns
what is missing.

## 3 · A whole course

There is no batch mode yet (roadmap M6). Until then:

```sh
find ../content/cec_320 -name '*.pdf' -print0 \
  | xargs -0 -I{} uv run ocr-handler extract "{}" -o /tmp/cec320_text/
```

## 4 · Re-run the corpus census

Regenerates the numbers in [../findings/corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md)
and [../findings/one-classifier-2026-09-06.md](../findings/one-classifier-2026-09-06.md).
Takes about half a minute over 448 PDFs.

```sh
uv run python - <<'PY'
import pathlib, collections
from ocr_handler import textlayer
root = pathlib.Path("/home/devel/electrical_notes/content")
docs, pages = collections.Counter(), collections.Counter()
for p in sorted(root.rglob("*.pdf")):
    if ".venv" in str(p) or "site-packages" in str(p): continue
    d = textlayer.extract(p)
    if not d.pages: continue
    docs[d.verdict] += 1
    for pg in d.pages: pages[pg.verdict] += 1
print(dict(docs)); print(dict(pages))
# blank pages (never render these) and the pages OCR would actually be aimed at:
#   sum(len(d.blank_pages)) -> 24      sum(len(d.ocr_candidates)) -> 2,329
PY
```

## Done — the command was renamed

`ocr-handler text` **is now** `ocr-handler extract --mode text` (2026-09-06). `text` was removed, not
aliased. Nothing outside these docs called it, and byte-stability was proven before the rename: 48
captured runs and all 448 corpus documents produce identical output.

`inspect` was **not** renamed and is a published surface — `content/cesc_470/`, `docs-rag/README.md` and
`docs/directives/coursework-solutions.md` all call it.

---

**See:** [testing.md](./testing.md) · [../plans/text-layer-first.md](../plans/text-layer-first.md) · [../scope.md](../scope.md)
