# Roadmap and Plans

**WHEN** a roadmap bullet needs a paragraph → **DON'T** write it in the roadmap →
**BECAUSE** the roadmap rots into a spec dump nobody reads. Put it in `docs/plans/` and link one line.

- **[../roadmap.md](../roadmap.md) is ONE lean file, ~40 lines** — milestone bullets plus short path refs.
  No design specs, no findings, no inline plans.
- **Plans live in [../plans/](../plans/INDEX.md)**, tagged `ACTIVE-SPEC` (build-ready) or `FORWARD-PLAN`
  (future) in that folder's `INDEX.md`. Naming by **lifetime**: a point-in-time plan is dated
  `YYYY-MM-DD-<slug>.md`; a continuously-updated living document is named by concept only
  (`text-layer-first.md`), because a date in a filename that never stops changing invites a near-duplicate.
- **Re-sequence by leverage, and say why in one line.** Milestone order here is not append-only. The
  2026-09-04 re-sequence moved the ink path behind the extractor because one serves 2 documents and the
  other serves 430; the reason is stated in the roadmap header, not applied silently.
- **Archive versioned, never erase.** A superseded roadmap becomes
  `docs/archives/roadmap_v{N}_{YYYY-MM-DD}.md` carrying a header saying what superseded it and why.
  Delivered plans move to `docs/archives/plans/`.
- **Tag must-not-break paths on the milestone**, and give each one a test in `tests/persistent/`.
- Distinct from execution discipline: this is the strategic *what*; `plan-first` is *how you execute*.

Hub: `~/llm-project-bootstrap/directives/roadmap-and-plans.md` → guide `ROADMAP_AND_PLANS.md`
