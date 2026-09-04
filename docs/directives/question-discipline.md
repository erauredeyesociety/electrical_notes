# Question Discipline

**WHEN** you hit a call only the operator can make → **DON'T** guess it, and **DON'T** drip it →
**BECAUSE** the calls in this repo are about **what gets submitted for a grade** and **what gets published
to a public website**. Both are hard to walk back, and neither has a safe default an agent can pick.

- **The open questions are enumerated** in [../scope.md](../scope.md) § Open questions. Read ahead and ask
  them in **one round**, each led by a recommendation and a default so it is a one-tap approval.
- **Highest-impact first:** does a course get retrofitted to the new doctrine · does a solution PDF get
  published publicly · does a loose root file get moved. Those three change outcomes. The rest change
  values.
- **Never retrofit a course on your own judgment.** The operator was explicit that `cesc_470`, `cesc_410`
  and `cpsc_462` are the doctrine courses and the other twelve are not to be touched. "It would be more
  consistent" is not a reason; it is the exact thing the rule forbids.
- **Never move or delete a file under `content/`.** Say where it *should* go, in a report, and let the
  operator move it. Coursework paths are referenced from submission scripts, per-course READMEs and the
  Hugo site; a silent move breaks all three.
- **Proceed on a defensible default; ask only when the answer changes the outcome.** Adding an `INDEX.md`
  to a docs folder needs no approval — the doctrine requires it. Deciding whether worked solutions belong
  on a public site does.
- **"Defer until X" is a command, not a dismissal.** Record the re-raise trigger in
  [../todo.md](../todo.md) and carry it forward.
- **Halt only the blocked item.** An open publishing question blocks the publishing decision; it blocks
  nothing about the docs skeleton.
- **Git is human-only.** Every `add`, `commit`, `push`, `checkout`, `reset` and hook installation is
  *proposed as a command* for the operator to run — never executed. Reads (`status`, `diff`, `log`) are
  fine, and `.gitignore` may be edited. This repo had **49 uncommitted paths** on 2026-09-04; that is
  the operator's to resolve, not an agent's.

Hub: `~/llm-project-bootstrap/directives/question-discipline.md` → guide `ASKING_QUESTIONS.md`
