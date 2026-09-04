# Doctrine compliance — the gap list

> **Type: ACTIVE-SPEC.** Living checklist. Audit date 2026-09-04, against
> `~/llm-project-bootstrap/` (PROMPTS.md § Initialize, `directives/`) with
> `/home/devel/sys301_minesweeper/docs/` as the mature exemplar.
> Tick items here; do not re-derive the audit.

**Verdict.** The skeleton is right — every doctrine folder exists and every one has an `INDEX.md`. What is
missing is *content in the folders that carry the project's memory*, and one real integrity problem in the
test floor. Six of eleven `docs/` subfolders were empty placeholders; this pass filled four.

---

## A · Closed by this pass (2026-09-04)

- [x] `docs/scope.md` — rewritten: centralized-extractor role, text-layer-first principle, open engine question, blacklist re-tiered
- [x] `docs/roadmap.md` — re-leaned and **re-sequenced by leverage**; v1 archived to [../archives/roadmap_v1_2026-09-04.md](../archives/roadmap_v1_2026-09-04.md)
- [x] `docs/todo.md` — reduced from an essay to an index; content relocated, nothing deleted
- [x] `docs/plans/` — was EMPTY. Now [text-layer-first.md](./text-layer-first.md) + this file. A project with no ACTIVE-SPEC has no resume point.
- [x] `docs/decisions/` — was EMPTY while five decisions lived in `todo.md`. Five ADRs written; see [../decisions/INDEX.md](../decisions/INDEX.md)
- [x] `docs/findings/` — was EMPTY. [corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md) added
- [x] `docs/directives/` — was 1 file. Five added; see [../directives/INDEX.md](../directives/INDEX.md)
- [x] `docs/runbooks/` — was 1 file. [extract-course-text.md](../runbooks/extract-course-text.md) added
- [x] All `INDEX.md` files refreshed (except `docs/research/INDEX.md`, owned by a concurrent research pass)

## B · Open — integrity, do these first

- [ ] **`src/ocr_handler/textlayer.py` is untracked by git.** `git ls-files` does not list it. The
      centralized extractor's core module exists on disk only. *(Git is human-only — propose, don't run.)*
- [ ] **The shipped CLI has zero test coverage.** `cli.py` imports only `textlayer`; the 7-test floor
      imports only `pdfops` and `ink`. The floor protects the path the CLI does not use.
      → `tests/persistent/`, four tests specified in [text-layer-first.md](./text-layer-first.md) § 9
- [ ] **Two live classifiers for one concept.** `pdfops.TEXT_LAYER_MIN_CHARS = 400` (poppler) and
      `textlayer.SPARSE_CHARS = 400` (PyMuPDF). Violates [ADR-0001](../decisions/0001-pymupdf-is-the-only-pdf-library.md)
      and is exactly the divergence this project exists to remove.
- [ ] **The S2 success fixture is not in the repository.** `scope.md` points at
      `/home/devel/electrical_notes/tmp/page5_transcript.md`; `tmp/` is gitignored in both repos. One
      `rm -rf` from unverifiable. Move it under `tests/fixtures/` or `docs/`.
- [ ] **`test_reading_order_bands_before_columns` asserts on `ink._reading_order`, a private function.**
      Doctrine: behaviour-level only, so refactors don't churn the floor. Route it through `ink.regions`.
- [ ] **5 of 7 floor tests skip without the course PDFs.** Only two run on a clean machine, and both are
      `ink` unit tests. Add at least one synthetic-PDF test that always runs.

## C · Open — doctrine artifacts still missing

- [ ] **`docs/lessons_learned/` is EMPTY**, yet three earned lessons exist and are currently misfiled as
      *directives* in `docs/directives/code-discipline.md` (the `(y,x)` sort bug, the measured-constant
      rule, the text-layer-before-model rule). A directive is a standing rule; a lesson is
      WHEN→DON'T→BECAUSE distilled from a specific discovery, with the discovery attached. Split them.
- [ ] **`docs/features/` is EMPTY.** Correct for now — nothing is shipped-stable. Populate at M2 with the
      `extract` contract. No action until then.
- [ ] **No `docs/wiki.md` or external-usage doc.** Doctrine requires one at a stable milestone with
      operator approval. Other courses become "external developers" the moment the per-course scripts are
      retired, so this lands with M2, not later.
- [ ] **No `scripts/`.** `automation-first`: the test invocation needs two environment variables that are
      documented in prose and retyped every time. → `scripts/test.sh`, `scripts/install.sh`.
- [ ] **No `CLAUDE.md` in `ocr_handler/`.** The exemplar carries one at its root as the session entry
      point. A child project treated with doctrine needs its own, not the parent's (the parent
      `electrical_notes` has none either).
- [ ] **No pre-commit hook protecting `tests/persistent/`.** Doctrine wants the floor protected by a hook,
      not by prose. *(Installing it is a git operation — propose to the operator.)*
- [ ] **`docs/session_records/` exists but is empty**; the one record was written straight into
      `docs/archives/session_records/`. The doctrine is internally inconsistent here — PROMPTS.md
      § Initialize specifies `docs/session_records/` archived *to* `docs/archives/session_records/`,
      while the session-close prompt writes directly to `archives/`. The exemplar uses the top-level
      folder. **Operator call — nothing relocated unilaterally.** An `INDEX.md` now states the
      ambiguity rather than hiding it.

## D · Open — knowledge in the wrong place

- [ ] **`/home/devel/electrical_notes/tmp_ocr_child.md` is durable project knowledge sitting in a repo
      root.** Doctrine: never the repo root. It holds measurements found nowhere else — notably **7 `/Ink`
      objects** in the annotated lecture, which contradicts `research/INDEX.md`'s "the ink is embedded
      images". File it into `docs/research/` or `docs/findings/`. *(Outside this pass's write zone.)*
- [ ] **Unresolved contradiction: images vs vector `/Ink`.** Two measurements of the same file disagree
      about what the annotation layer *is*. M4's whole approach depends on the answer.
- [ ] **`electrical_notes/tmp.md`, `note.md`, `make_study_guide_master_prompt.md`** sit loose in the parent
      root. Parent-repo hygiene, noted not owned.

## E · Deliberately not done

- **`docs/research/` untouched.** A concurrent research pass owns it this session and will land
  `engine-landscape-2026-09.md`. Its `INDEX.md` is not this pass's to update.
- **Nothing under `src/` or `tests/` was written.** This pass is planning and documentation only.
- **No git operations.** Git is human-only in this doctrine; every git-shaped item above is a proposal.
- **Session records not relocated.** See § C, last item — the doctrine contradicts itself and the operator
  should settle it.

---

**Sources:** `~/llm-project-bootstrap/PROMPTS.md` § Initialize · `~/llm-project-bootstrap/directives/`
(scope-discipline, roadmap-and-plans, documentation-discipline, testing-discipline, research-docs,
question-discipline, automation-first) · `/home/devel/sys301_minesweeper/docs/` (exemplar)
