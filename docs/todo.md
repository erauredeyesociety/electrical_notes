# TODO — single source of truth

> Last updated: 2026-09-08 · **MODE: maintenance**
> Index, not an essay. Detail lives behind the links.

## CURRENT STATE

**Governance is populated and now has an enforcement layer.**
[directives/](./directives/INDEX.md) gained
[human-task-instructions.md](./directives/human-task-instructions.md) — how a task handed to the human
must be written — and the LaTeX toolchain gained `flatten_tex.sh --check`, which catches a stale
Overleaf copy before it is uploaded.
[lessons_learned/lessons.md](./lessons_learned/lessons.md) carries 15 lessons.

**CESC 410L Lab 1 is complete and demoed.** Submission is one file,
`content/cesc_410/labs_and_projects/lab01/lab01-artifacts-nelson-gatlin.pdf`; only the Canvas upload
remains. CESC 470 and CPSC 462 have no labs yet but now inherit the standard.

**docs-rag serves 16 per-course KBs**, all healthy; `purge_stale.sh` is a required step after any
re-ingest. **ResearchHub is down** — pwnstar unreachable, not a VPN or wifi fault.

Last session: [session_records/2026-09-08_lab01-and-the-human-task-standard.md](./session_records/2026-09-08_lab01-and-the-human-task-standard.md).

## NEXT ACTION

**1. Upload Lab 1** — `content/cesc_410/labs_and_projects/lab01/lab01-artifacts-nelson-gatlin.pdf`,
one file, due a week from assignment. The demo is signed off. Nothing else about this lab is open.

**2. Then the docs-rag chunking work** carried over from 2026-09-06 and still not done:
strip the `\input` preamble block in `prepare_corpus.py` (every converted problem file wastes its
first chunk on boilerplate), then re-examine `chunk_size` 256/50. Purge and re-ingest, in that order
([`docs-rag/RUN.md`](../docs-rag/RUN.md)).

**3. Then [roadmap.md](./roadmap.md) § M3** (loose root `.md`, operator moves) and § M4
(`scripts/check.sh`, pin `hugo-version`).

## Blocked / awaiting operator

Six named calls, all in [scope.md](./scope.md) § Open questions. Batch them; none should be guessed.
Highest-impact first:

- **#1 — are worked solutions published publicly?** `content/cesc_410/hw/hw01/` tracks six solution `.tex`
  files that Hugo publishes to a site under the institution's GitHub org. This also gates § M7.
- **#2 — where do the four loose root `.md` files go?** Recommendations in
  [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 3. `tmp_ocr_child.md` is the urgent one.
- **#4 — pin `hugo-version` in CI?** It is `latest`, so an upstream release can break the public site.

## Known issues

- **`scripts/refactor_standard_equations.sh` is a destructive, undocumented, repo-wide in-place rewrite.**
  Running it today would rewrite twelve frozen course folders. § 5.
- **docs-rag re-ingest is not idempotent** — it inserts rather than replaces, and exclusions are not
  retroactive, so the index only grows ([`docs-rag/FINDINGS.md`](../docs-rag/FINDINGS.md) F-06).
  `purge_stale.sh` closes it, but it must actually be run.
- **LaTeX-derived chunks open with `\input` boilerplate** that matches nothing — a wasted chunk per
  converted problem file at `chunk_size` 256.
- **Four `ocr_handler` modules are untracked** — `crops.py`, `latex_repair.py`, `structure.py`,
  `validity.py`, plus `tools/` and `tests/fixtures/`. `textlayer.py` is now tracked. Repeated here
  because they are one `git clean` from gone. **Git is human-only** — reported, never resolved.
- **Many uncommitted paths across the repo.** Git is human-only — the state is reported, never resolved.
  Git is human-only — the count is reported, never resolved.
- **`.github/workflows/pages.yml` runs `git submodule update`** against a repo with no `.gitmodules`.
  Harmless no-op, misleading to read.

## Doctrine gaps

- `docs-rag/` is a child project with no bootstrap and no git tracking. [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 9.
  It now carries `FINDINGS.md`, `RUN.md` and `purge_stale.sh`, but not the doctrine tree.

**Closed 2026-09-06:** ~~`docs/latex/` has no `INDEX.md`~~ · ~~`lessons_learned/` is empty~~ (14 lessons
written) · ~~`decisions/` is empty~~ (two ADRs) · ~~the `session_records/` vs `archives/` convention is
unsettled~~ ([session_records/INDEX.md](./session_records/INDEX.md) — the contradiction was in the
bootstrap, not here).

---

**See:** [roadmap.md](./roadmap.md) · [scope.md](./scope.md) · [DRIFT_REPORT.md](./DRIFT_REPORT.md) · [directives/INDEX.md](./directives/INDEX.md)
