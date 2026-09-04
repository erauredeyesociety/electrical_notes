# docs-rag — electrical_notes

Semantic search over the coursework, **one knowledge base per course** so a
routed query searches a small index instead of the whole repo.

Web UI: **<http://127.0.0.1:10120>**

```sh
docker compose up -d                                        # start
./port_forwards/status-all.sh                               # are the tunnels up?
RAG_ENDPOINT_URL=http://127.0.0.1:10120 python3 client/ragq.py --kb cesc_470 "amdahl's law"
```

---

## Query it

**Always pass `--kb`** — that is the entire point of the layout. Without it the
query hits `primary` (everything) and is both slower and noisier.

```sh
R="RAG_ENDPOINT_URL=http://127.0.0.1:10120"

# one course
env $R python3 client/ragq.py --kb cesc_470 "how do I compute CPI"

# several
env $R python3 client/ragq.py --kb cec_315,cesc_410 "convolution"

# everything
env $R python3 client/ragq.py --kb all "phasor"
```

### Knowledge bases

| KB | Course | KB | Course |
| --- | --- | --- | --- |
| `cec_320` | Microprocessors | `cesc_420` | Capstone (drone swarm) |
| `cec_315` | Signals & Systems | `cesc_410` | DSP |
| `syse_301` | Systems Engineering | `cesc_470` | Computer Architecture |
| `stat_412` | Statistics | `ee_300` / `ee_302` | Electrical Engineering |
| `ps160` | Physics | `sys_304` | Systems |
| `cec_300` | — | `ae318` | Aerospace |
| `cpsc_462` | Networks / Wireshark | `misc` | small leftovers |
| `primary` | **everything** — the default | | |

---

## ⚠ Rebuild the corpus after adding LaTeX

**`.tex` cannot be indexed.** It has no handler and is dropped *silently* — the
ingest reports success having indexed zero of them. `prepare_corpus.py` converts
`.tex` → `.md` into `corpus/`, which is what the KBs actually read:

```sh
./prepare_corpus.py          # after writing new .tex
./prepare_corpus.py --plan   # dry run
```

It also drops 73 byte-identical duplicate PDFs and 62 PDFs that are just the
compiled twin of a `.tex`, so the same lecture stops coming back three times.

Full detail and the evidence: [`FINDINGS.md`](FINDINGS.md).

## Re-ingest after content changes

```sh
docker compose run --rm --no-deps -v "$PWD/ops:/src/scripts:ro" \
  api python /src/scripts/ingest_kb.py --kb cesc_470 --rebuild
```

`--kb primary` is **refused** — it belongs to the v1 flow (`rag ingest`).

---

## Health

```sh
curl -s http://127.0.0.1:10120/api/v1/health
```

`{"status":"degraded", ..., "llm":false}` is **expected and fine**. Search and
embeddings work; `llm:false` only means no *generation* model is configured, so
there is no synthesized prose answer — retrieval returns passages. Local Ollama
(`:11434`) carries `nomic-embed-text` and nothing else.

To enable synthesized answers you need a generation model. `qwen3.5:9b` is
tunnelled from pwnstar at `:11436` — **but temper expectations**: pwnstar is an
**RTX 2060 with the same 6144 MiB as this laptop**, typically ~4.8 GB already
occupied, with swap exhausted and load averages in the tens. Measured, that
model runs with only ~1.4 GB resident in VRAM (i.e. mostly on CPU) at a
4096-token context, taking **~200 s** for one page-sized prompt. It is a
correctness resource, not a throughput one, and the tunnel drops regularly.

Pulling a small generation model into **local** Ollama is likely the better
route. See [`port_forwards/README.md`](port_forwards/README.md).

---

## Local deviations from stock rag-bootstrap

Both are worked around here; neither is our bug.

| | Problem | Fix |
| --- | --- | --- |
| **Image** | `rag-bootstrap-api-multikb` was never built on this host | built from `app/Dockerfile.multi-kb`, then patched below |
| **numpy** | `similarity_report.py` imports numpy unconditionally; it is not in `app/requirements.txt`, so the api restart-loops | [`Dockerfile.patch-numpy`](Dockerfile.patch-numpy) → tag `0.8.3-en` |

A third is a config requirement, not a bug: **every KB needs an explicit
`database:`**. `registry.py` has a `ragdb_<name>` default but `config_manager.py`
does not apply it and hard-fails at startup.

Pinned in `.env`: `RAG_IMAGE_TAG=0.8.3-en`. The frontend must carry a matching
tag (`docker tag rag-bootstrap-frontend:0.8.3 rag-bootstrap-frontend:0.8.3-en`).

---

## What is NOT searchable

**71 of 430 PDFs have no text layer** (17%, but 63% of PDF bytes) — scanned
textbooks and image-only slide decks. Worst: `ps160` (54% image-only, including
a 202 MB scanned textbook), `cec_300` (48%), `cesc_470` Module 01 (62 of 88
pages).

**A RAG cannot fix this** — it indexes text, so it inherits the gap exactly.
OCR is the fix: [`../ocr_handler/`](../ocr_handler/). Check any PDF with:

```sh
cd ../ocr_handler && uv run ocr-handler inspect FILE.pdf
```

---

**Related:** [`FINDINGS.md`](FINDINGS.md) · [`port_forwards/README.md`](port_forwards/README.md) · [`RUN.md`](RUN.md)
