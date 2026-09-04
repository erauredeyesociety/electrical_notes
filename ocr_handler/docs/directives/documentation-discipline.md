# Documentation Discipline

**WHEN** you learn something worth keeping → **DON'T** leave it in `todo.md` →
**BECAUSE** `todo.md` is a volatile index and gets re-leaned. Five real decisions were nearly lost that
way; they are now ADRs.

**Route by type — the load-bearing split is INTERNAL vs EXTERNAL:**

| Content | Folder |
| --- | --- |
| Discoveries about **our own** code or our own corpus (file:line, measurements, audits) | `docs/findings/` |
| Teardowns of things **outside** this repo (models, libraries, upstream projects) | `docs/research/` |
| Prescriptive rules distilled from our own experience, WHEN→DON'T→BECAUSE | `docs/lessons_learned/` |
| Why a choice was made | `docs/decisions/` — immutable ADRs; supersede with a new one, never edit |
| Tactical how-to for work not yet done | `docs/plans/` |
| Repeatable operator procedures | `docs/runbooks/` |
| Shipped-stable capability specs and APIs | `docs/features/` |
| Dated per-session narrative | `docs/archives/session_records/` |

- **Never the repo root.** `electrical_notes/tmp_ocr_child.md` is durable project knowledge in a repo root
  and holds measurements found nowhere else. That is the anti-pattern.
- **Supersede in place; name by concept, not by date.** Before writing a new doc, grep for a near-duplicate
  and update it at its existing path. Dated siblings guarantee bloat. Exceptions that stay dated and
  immutable: ADRs, session records, archived roadmaps, and point-in-time plans.
- **Cite, don't recopy.** A plan cites `docs/research/` and `docs/findings/` by path. `todo.md` used to
  restate the research verdict in full — that is the bloat loop, and it drifts.
- **Every docs folder has an `INDEX.md`.** All eleven do; keep it that way.
- **Contradictions are recorded, not resolved by preference.** Two measurements disagree about whether the
  annotation ink is embedded images or vector `/Ink` objects. Both are written down until one is disproved.

Hub: `~/llm-project-bootstrap/directives/documentation-discipline.md` → guide `DOCUMENTATION_STANDARDS.md`
