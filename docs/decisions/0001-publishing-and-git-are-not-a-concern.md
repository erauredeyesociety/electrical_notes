# 0001 — Publishing and the git remote are not a concern for coursework

**Status:** Accepted · **Date:** 2026-09-01, re-affirmed 2026-09-04 · **Scope:** repo-wide

## Decision

**The publishing and git-repository aspects of this repo do not apply to the
coursework under `content/`.** Store student IDs and course material as
convenient. Do not add redaction steps. **Do not raise it again.**

This is an explicit operator decision, not an inference.

## Context

The repo has a GitHub remote and a `hugo.yaml` with
`baseURL: https://erauredeyesociety.github.io/electrical_notes/`, so everything
under `content/` would normally be treated as web-published. Worked solutions
are tracked as `.tex` sources. An agent encountering that for the first time
will reasonably flag it as an academic-integrity or privacy question.

It has now been flagged at least twice. The operator settled it on 2026-09-01:

> *"don't worry about this or publishing content at all, and the git repo aspect
> is not applicable for this project — and document this in the reference docs
> for later just in case there is any confusion."*

## Why this record exists at the repo root

The decision was originally recorded only in
[`content/cesc_410/labs_and_projects/reference_docs/submission_requirements.md`](../../content/cesc_410/labs_and_projects/reference_docs/submission_requirements.md)
(§ *Publishing and git — not a concern here*). That file is scoped to one course
folder, so a later reviewer looking at the repo as a whole did not see it and
re-raised the question repo-wide — exactly the confusion the operator asked to
prevent.

**A decision that governs the whole repo has to be recorded at the whole repo's
level.** That is the generalisable lesson here, and it applies beyond this
particular question.

## Consequences

- No redaction, obfuscation, or `ignoreFiles` change is to be proposed for
  `content/` on publishing grounds.
- `docs/scope.md` § Open questions #1 is **closed** by this record.
- Agents that notice the public `baseURL` should read this file and move on.
- This says nothing about *other* reasons to change what is published — e.g. the
  landing page indexing only 3 of 15 courses is a **navigation** question
  (scope.md #3), unrelated to this decision, and still open.

## Not covered by this decision

**Git mutations remain human-only.** That is a separate standing rule and is
unaffected: agents propose commands, the operator runs them.

---

**Related:** [`../scope.md`](../scope.md) ·
[`../../content/cesc_410/labs_and_projects/reference_docs/submission_requirements.md`](../../content/cesc_410/labs_and_projects/reference_docs/submission_requirements.md)
