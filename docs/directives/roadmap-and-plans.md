# Roadmap and Plans

**WHEN** a roadmap bullet needs a paragraph → **DON'T** write it in the roadmap →
**BECAUSE** the roadmap rots into a spec dump nobody reads. Put it in [`docs/plans/`](../plans/INDEX.md)
and link one line.

- **[../roadmap.md](../roadmap.md) is ONE lean file** — milestone bullets plus short path refs. No design
  specs, no findings, no inline plans, and **no semester schedule**. Due dates belong to the course, not
  to this repo; a roadmap that tracks them is out of date within a week.
- **The roadmap tracks the *repo*, not the *coursework*.** "Every course folder has an `_index.md`" is a
  roadmap item. "Finish HW3" is not — that lives in the course folder and in the operator's head.
- **Plans live in [../plans/](../plans/INDEX.md)**, tagged `ACTIVE-SPEC` (build-ready) or `FORWARD-PLAN`
  (future) in that folder's `INDEX.md`. Naming by **lifetime**: a point-in-time plan is dated
  `YYYY-MM-DD-<slug>.md`; a continuously-updated living document is named by concept only.
- **[../todo.md](../todo.md) is the session SSOT** — CURRENT STATE, NEXT ACTION, blocked items. It is an
  index, not a journal; the narrative goes in a session record.
- **Archive versioned, never erase.** A superseded roadmap becomes
  `docs/archives/roadmap_v{N}_{YYYY-MM-DD}.md` with a header saying what superseded it and why. Delivered
  plans move to [`docs/archives/plans/`](../archives/plans/INDEX.md).
- **Child-project roadmaps are separate and are not summarised here.** `ocr_handler/docs/roadmap.md`
  is linked by path from the root roadmap and never restated in it — restating it guarantees the two
  drift.

Hub: `~/llm-project-bootstrap/directives/roadmap-and-plans.md` → guide `ROADMAP_AND_PLANS.md`
