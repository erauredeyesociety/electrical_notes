# Lessons Learned

**PRESCRIPTIVE.** Each entry is a rule *plus the specific failure that earned it*. If an entry cannot
name its incident, it belongs in [../directives/INDEX.md](../directives/INDEX.md) instead.

Index and the directive/lesson boundary: [INDEX.md](./INDEX.md).
This file tracks the **repo and its toolchain**. Lessons about the OCR pipeline live in
[`ocr_handler/docs/lessons_learned/lessons.md`](../../ocr_handler/docs/lessons_learned/lessons.md).

---

## Coursework and LaTeX

- **WHEN a problem's mathematics matters, DON'T read it out of a PDF text layer — render the region at
  ~400 dpi and look at the image — BECAUSE the flattening is silent and changes the answer.**
  `pdftotext` turned $\cos(\tfrac{\pi}{6}n)$ into `cos( 6π n)` — a stacked fraction flattened onto one
  line, which reads as a *constant* signal rather than a periodic one — and dropped a $\sqrt{\;}$ onto
  the wrong line, which decided whether a signal was periodic. **Neither raised an error.** (2026-09-04)
  Source: [`content/cesc_410/hw/reference_docs/findings.md`](../../content/cesc_410/hw/reference_docs/findings.md) HW-01

- **WHEN a document will be submitted, DON'T let a tooling reference survive into it — BECAUSE the
  grader sees the scaffolding, not the work.** Script names, build flags and repo paths reached a lab
  report that was zipped for submission. Now enforced in two places: the doctrine
  ([../directives/coursework-solutions.md](../directives/coursework-solutions.md) § Repo hygiene) and
  `docs/latex/flatten_tex.sh`, which strips tooling comments at inline depth and stamps only a
  basename — never a repo path — into the header it generates. (2026-09-04, header fixed 2026-09-05)
  Source: [`content/cesc_410/labs_and_projects/reference_docs/known_issues.md`](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md) KI-09

- **WHEN a `.tex` file is destined for Overleaf, DON'T rely on a shared preamble by relative path —
  inline it — BECAUSE an Overleaf project is self-contained and cannot resolve anything above its own
  root.** `\input{../../../../docs/latex/coursework_preamble.tex}` builds locally under `tectonic` and
  fails in Overleaf with `File not found`. `docs/latex/flatten_tex.sh` produces the self-contained copy
  and **fails loudly if any `\input` survives** rather than emitting a file that breaks later.
  (2026-09-05)

- **WHEN a course needs generated artifacts ignored, DON'T write an allow-list of the names you expect —
  ignore only what you generate — BECAUSE the pattern you did not predict is a handout you just lost.**
  `*.pdf` plus `!HW*.pdf` drops every instructor PDF whose name does not start with `HW`. The rule is
  `p[0-9][0-9]_*.pdf`, `*_solutions.pdf`, `overleaf/`. Source:
  [../directives/coursework-solutions.md](../directives/coursework-solutions.md)

---

## docs-rag

- **WHEN a pipeline reports success, DON'T believe it covered your inputs — check the count it actually
  indexed — BECAUSE a silent success is worse than a failure.** The ingester has no `.tex` handler. It
  logs one warning, indexes **zero** `.tex` files, and reports success — so a knowledge base built over
  a LaTeX-heavy corpus looks healthy while containing none of the homework or solutions. The workaround
  needs `pandoc -f latex+raw_tex`; plain `-f latex` discards exactly the custom-macro content the
  answers live in. (2026-09-04) Source: [`docs-rag/FINDINGS.md`](../../docs-rag/FINDINGS.md) F-01

- **WHEN you re-ingest, DON'T assume it replaces — purge first — BECAUSE the index only ever grows.**
  A re-ingest *inserts* a new `documents` row when a file's content has changed and leaves the old row
  in place, embeddings intact, so a corrected homework solution competes in search with the version it
  corrected and nothing marks which is which. Measured: one file, two rows, different content hashes,
  both retrievable. 28 stale documents / 145 chunks were live across two courses.
  `docs-rag/purge_stale.sh` now makes the cleanup executable and is a required step in
  [`docs-rag/RUN.md`](../../docs-rag/RUN.md). (2026-09-06)
  Source: [`docs-rag/FINDINGS.md`](../../docs-rag/FINDINGS.md) F-06

- **WHEN you add an exclusion, DON'T expect it to apply to what is already indexed — BECAUSE
  exclusions are not retroactive.** Five `overleaf/` documents stayed in the index after `"overleaf/"`
  was added to `config.yaml`; all five predated the pattern, and the 09-06 ingest correctly skipped
  them. **The obvious diagnosis — a bad glob — is wrong** and sends you to edit a config that is already
  correct. (2026-09-06) Source: [`docs-rag/FINDINGS.md`](../../docs-rag/FINDINGS.md) F-06

- **WHEN a query returns the wrong scope, DON'T conclude routing is broken — check the parameter name
  against the endpoint — BECAUSE an unrecognised field is silently ignored and the query runs
  unscoped.** `/api/search` and `/api/v1/search` take **`corpus`**; `/api/v2/search` takes **`kb`**.
  Passing `knowledge_base` succeeds and returns other courses' documents, which looks exactly like
  broken per-course routing. (2026-09-06) Source: [`docs-rag/RUN.md`](../../docs-rag/RUN.md) § Query

---

## Shell and operations

- **WHEN testing a condition with grep, DON'T write `cmd | grep -q` under `set -o pipefail` — capture
  into a variable, then grep — BECAUSE `grep -q` exits on the first match, the producer dies of
  SIGPIPE, and pipefail reports the whole pipeline as failed.** Measured on this box: **18 of 40 runs
  returned a false "VPN down"**, which would have silently disabled the Ollama tunnel guard.
  (2026-09-06) Source: [`docs-rag/port_forwards/ollama-guard.sh`](../../docs-rag/port_forwards/ollama-guard.sh)

- **WHEN forwarding a port for something a container must reach, DON'T bind only localhost — add the
  docker bridge — BECAUSE `localhost` inside a container is the container.** The Ollama tunnel carries
  two `-L` flags: `11435:localhost:11434` for host processes and `172.17.0.1:11435:localhost:11434` for
  containers. (2026-09-06)
  Source: [`docs-rag/port_forwards/skytracker-ollama-tunnel.sh`](../../docs-rag/port_forwards/skytracker-ollama-tunnel.sh)

- **WHEN a dependency is missing from a third-party image, DON'T patch it by copying a Dockerfile
  pattern — check what user the base image actually runs as — BECAUSE the `USER appuser` you copied may
  not exist.** The first `Dockerfile.patch-numpy` assumed a non-root user; the base image runs as root
  with no such account. Caught by checking before building. (2026-09-05)

---

## Repo governance

- **WHEN a decision was made in conversation, DON'T leave it in prose — write the ADR — BECAUSE the
  next session re-litigates anything it cannot find.** Two now exist:
  [decisions/0001](../decisions/0001-publishing-and-git-are-not-a-concern.md) (publishing and git are
  not this project's concern — the operator said so explicitly, and it was being re-raised) and
  [decisions/0002](../decisions/0002-no-local-ollama-on-err0r.md) (no local Ollama on err0r). 0002 was
  **scoped down after a peer correction**: it applies to this machine only, because pwnstar runs
  services locally by design. (2026-09-06)

- **WHEN git state is untidy, DON'T resolve it — report it — BECAUSE mutations are human-only in this
  repo.** Reading and interrogating git is expected; committing, staging and cleaning are not.
  Source: [decisions/0001](../decisions/0001-publishing-and-git-are-not-a-concern.md)
