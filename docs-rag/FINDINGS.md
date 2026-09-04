# docs-rag — findings before building

Investigation of `~/exudeai/rag-bootstrap` for a per-course knowledge base over
this repo. **Two findings change the design; read those first.**

Status: **not yet built.** Port forwards are up ([`port_forwards/`](port_forwards/)).

---

## ⚠ F-01 — `.tex` is NOT ingestible, and it fails *silently*

**This is the finding that shapes everything**, because much of this repo's
content is LaTeX.

The ingester filters by extension against a handler registry
(`app/ingestion.py:299-320`). Registered: `.pdf .md .txt .log .json .yaml .yml
.docx .xlsx .xlsm .pptx` plus code extensions. **`.tex` has no handler.**

Listing it does not raise an error. `_normalize_extensions`
(`app/ingestion.py:1035-1043`) intersects the requested list with the registry
and drops the rest with a *warning log*:

```
Ignoring extensions with no registered handler: ['.tex']
```

The ingest then reports success having indexed **zero** `.tex` files. A KB that
looks healthy would silently contain none of the homework or solutions.

### The workaround, and its own trap

pandoc reads LaTeX natively and produces clean Markdown with the maths intact as
`$...$` / `$$...$$` — good RAG input. **But it must be `-f latex+raw_tex`:**

| | `-f latex` | `-f latex+raw_tex` |
| --- | --- | --- |
| Body prose and equations | ✅ kept | ✅ kept |
| Content inside a **custom macro** | ❌ **silently dropped** | ✅ kept as a raw block |

Measured on `content/stat_412/QZ04/solutions/q01.tex`, which ends with
`\finalanswer{$\sigma_Z^2=180$.}`: plain `latex` yields **one** occurrence of
`180`, `latex+raw_tex` yields **two**. Plain conversion threw away the final
answer and reported success.

In this repo custom macros are *exactly* where answers live — `\finalanswer`
(stat_412), `answerbox` (cesc_410 hw). Verified `+raw_tex` preserves a full
`\begin{answerbox}…\end{answerbox}` from `cesc_410/hw/hw01/p06_convolution.tex`.

**Rule: any `.tex` → text conversion feeding the index must use
`-f latex+raw_tex`, and must be spot-checked for a known answer string.**

### Options

| | Approach | Cost |
| --- | --- | --- |
| **A** | Convert `.tex` → `.md` into a staging tree, index that | Duplicates content; needs a rebuild step |
| **B** | Index the compiled PDFs (`.pdf` *is* fully supported) | We already build them; but they are gitignored build products, so the index depends on local build state |
| **C** | Add a `.tex` handler upstream in rag-bootstrap | Cleanest, but modifies someone else's repo |

Not yet decided — depends on the content survey.

---

## ⚠ F-02 — The multi-KB image does not exist on this host

Every multikb consumer compose requires
`rag-bootstrap-api-multikb:${RAG_IMAGE_TAG}`
(`templates/consumer-compose.multikb.yml:185`). `docker images` shows
`rag-bootstrap-api`, `rag-bootstrap-api:0.8.3-sys301`, and
`rag-bootstrap-frontend` — **no `-multikb` at any tag**. `docker compose up`
would fail to find the image.

Build (context is the **repo root**, not `app/`):

```sh
cd ~/exudeai/rag-bootstrap
docker build -t rag-bootstrap-api-multikb:0.8.3 -t rag-bootstrap-api-multikb:latest \
  -f app/Dockerfile.multi-kb .
```

> ⚠ **Unresolved risk.** All three *running* stacks pin `0.8.3-sys301`, a
> locally-patched api variant (765 MB vs 687 MB; see
> `~/sys301_minesweeper/docs-rag/Dockerfile.patch-numpy`). Whether the multikb
> image needs the same numpy patch **cannot be determined from static files** —
> it will show up at runtime if it matters.

---

## F-03 — `.pdf` *is* fully supported, with real text extraction

`PDFHandler` (`app/ingestion.py:50-57`) uses PyMuPDF (`fitz`) page by page;
`pymupdf` is installed by `app/Dockerfile.multi-kb:30-31`. `.pdf` is also in the
default walk set, so a KB with no `extensions:` key indexes PDFs automatically.

skytracker's config excludes `*.pdf` and `*.tex` **deliberately** — that is its
choice for a Markdown-only corpus, not a platform limit. Do not copy it here.

**`exclude` beats `extensions`** (`_is_excluded`, `app/ingestion.py:1046-1063`).
Listing `pdf` while also excluding `*.pdf` yields nothing, silently.

Caveat that matters here: a PDF with no text layer indexes as near-nothing. This
repo has handwritten lecture scans in exactly that state — see
[`../ocr_handler/`](../ocr_handler/). **RAG does not fix them; OCR does.**

---

## F-04 — Layout constraints

| Thing | Value | Source |
| --- | --- | --- |
| Free port base | **10120** (then 10140, 10160, …) | 10040/10060/10080/10100/10240 taken |
| Port band | reserves `[BASE .. BASE+19]`; only the frontend publishes | `consumer-compose.multikb.yml:321` |
| Per-KB database | `ragdb_<name>`, dashes → underscores | `app/registry.py:35-45` |
| DB creation | **automatic** at API start; do not pre-create | `registry.py:315-366` |
| `primary` KB | must keep `database: ragdb`; **`ingest_kb.py --kb primary` is refused** | `scripts/ingest_kb.py:63-67` |
| `DOCS_PATH` | **one** read-only bind, `${DOCS_PATH}:${DOCS_PATH}:ro` | `consumer-compose.multikb.yml:285` |

**The `DOCS_PATH` constraint drives the layout:** every KB's `ingest_dirs` must
sit under a single root, or the container cannot see them. For per-course KBs
that means `DOCS_PATH=/home/devel/electrical_notes`, with each course KB
pointing at `content/<course>/`.

`rag new-consumer` refuses a default `--out` (it must not land inside the
rag-bootstrap repo), requires a port base that is a multiple of 20 and ≥ 10020,
and hard-refuses 10040.

```sh
~/exudeai/rag-bootstrap/rag new-consumer electrical-notes 10120 /home/devel/electrical_notes \
  --mode multikb --tag 0.8.3 \
  --out /home/devel/electrical_notes/docs-rag \
  --data-root /home/devel/rag-data/electrical-notes
```

⚠ That target directory is **not empty** — `port_forwards/` and this file live
there, and `new-consumer` refuses a non-empty `--out`. Generate elsewhere and
merge, or pass a subdirectory.

---

## F-05 — Six consumers already exist; follow their pattern

| Instance | Port | Mode | KBs |
| --- | --- | --- | --- |
| `sys301_minesweeper/docs-rag` | 10060 ▶ running | single | — |
| `tmp/photogram_tmp/docs-rag` | 10080 ▶ running | single | — |
| `floppi/docs-rag` | 10100 ▶ running | single | — |
| `skytracker_v2/docs-rag` | 10240 | multikb | 6 |
| `exudeai/docs-rag` | 10040 | multikb | 17 |
| `llm-project-bootstrap/docs-rag` | 10060 | multikb | 1 (stub) |

Established: instance at `<project>/docs-rag/`, `DOCS_PATH` = project root,
data root off on a roomier disk, `config.yaml` tracked, `.env` gitignored.

---

## Open decisions

1. **`.tex` strategy** — A (staging tree), B (compiled PDFs), or C (upstream handler).
2. **Which courses get a KB** — pending the content survey.
3. Whether the multikb image needs the sys301 numpy patch (runtime question).

**Related:** [`port_forwards/README.md`](port_forwards/README.md) · [`../ocr_handler/`](../ocr_handler/)
