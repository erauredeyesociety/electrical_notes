# Extracting a course's text

**What works today.** Two commands exist: `inspect` and `text`. `extract --mode ...` is designed
([../plans/text-layer-first.md](../plans/text-layer-first.md)) but **not built** — there is no OCR path yet,
so everything below reads text layers only.

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
uv run ocr-handler text FILE.pdf                     # to stdout
uv run ocr-handler text FILE.pdf -o out/             # writes out/<slug>.md
uv run ocr-handler text FILE.pdf -o out/ -f txt      # plain text, for grep
uv run ocr-handler text FILE.pdf -p 1-10,15          # selected pages
```

The Markdown carries a header stating the page count, chars/page, which pages have no text layer, and any
letter-spacing warning. **Do not strip that header** — it is the only place a downstream reader learns
what is missing.

## 3 · A whole course

There is no batch mode yet (roadmap M6). Until then:

```sh
find ../content/cec_320 -name '*.pdf' -print0 \
  | xargs -0 -I{} uv run ocr-handler text "{}" -o /tmp/cec320_text/
```

## 4 · Re-run the corpus census

Regenerates the numbers in [../findings/corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md).
Takes a couple of minutes over 430 PDFs.

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
PY
```

## Coming change — the command will be renamed

`ocr-handler text` becomes `ocr-handler extract --mode text` in M2. Nothing calls it yet, so the rename is
free now and expensive later. **Do not wire a course script to `text`** — wait for `extract`, or expect to
update it.

---

**See:** [testing.md](./testing.md) · [../plans/text-layer-first.md](../plans/text-layer-first.md) · [../scope.md](../scope.md)
