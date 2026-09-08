# Session records — INDEX

Dated per-session narrative, `YYYY-MM-DD_<description>.md`. **Immutable** — written once, not revised.
Records rotate to [../archives/session_records/](../archives/session_records/INDEX.md) when stale.

| Date | Session | Outcome |
| --- | --- | --- |
| [2026-09-08](./2026-09-08_lab01-and-the-human-task-standard.md) | CESC 410 Lab 1 delivered, and the human-task standard that came out of it | Lab 1 complete, demoed and down to **one file** to upload. Three *silent* failures closed — a GUI window blocking an unattended run, a stale Overleaf copy that compiles and looks right, and a "code" archive that is 93% dependency lockfile. New repo-wide directive `human-task-instructions.md`; all 19 source `.tex` files now say in their own first six lines that they cannot go to Overleaf. |
| [2026-09-06](./2026-09-06_rag-staleness-and-lessons.md) | The RAG index only grows; lessons distilled | A live correctness defect found in docs-rag — a re-ingest inserts rather than replaces, so **28 stale documents / 145 chunks were live in search**, including superseded homework solutions. Purged, made executable as `purge_stale.sh`, verified against a restored backup. `lessons_learned/` filled in both trees. M2 confirmed complete. |
| [2026-09-04](./2026-09-04_catch-up.md) | First bootstrap of the root `docs/` tree | Scope, roadmap, todo, README, five directives and eleven indexes created. Ten drift items found, none acted on outside `docs/`. |

---

## ✅ The `session_records/` vs `archives/session_records/` question — settled 2026-09-06

Both trees flagged this as an open operator call. It is **resolved in favour of this folder**, and the
disagreement turns out to sit in the bootstrap itself, not in our projects:

| Bootstrap document | Says |
| --- | --- |
| `guides/DOCUMENTATION_STANDARDS.md` line 35, 252–253 | live records in `docs/session_records/`, **rotating into** `archives/session_records/` |
| `PROMPTS.md` § Save Progress | write directly into `docs/archives/session_records/` |

The lifecycle version wins on two grounds: the Save Progress prompt **names
`DOCUMENTATION_STANDARDS.md` as its own reference** for archives structure, and writing straight to
`archives/` makes the word meaningless — nothing would ever be live.

**Applied to both trees.** This project was already correct. The child project
[`ocr_handler/`](../../ocr_handler/docs/session_records/INDEX.md) now writes here too; its 2026-09-02
record stays in `archives/` where it legitimately rotated to.

> ⚠ **Upstream:** `~/llm-project-bootstrap/PROMPTS.md` § Save Progress steps 1–2 contradict its own
> cited guide. Worth fixing there so the next project does not re-derive this. Operator call — that repo
> is outside this one's scope.
