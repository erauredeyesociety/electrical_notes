# Scope Discipline

**WHEN** you want a capability that is not in `docs/scope.md` § In scope → **DON'T** build it →
**BECAUSE** the blacklist only works if it is read before acting. Re-opening a blacklist row needs an ADR
in `docs/decisions/`, not a commit message.

- **One file: [../scope.md](../scope.md).** It carries the mission, the in-scope list, and the mandatory
  Out-of-Scope blacklist, tiered *permanent* / *yes* / *maybe later*.
- **The permanent rows are enforced constraints, not deferrals.** Chief among them: never run a model over
  a page whose text layer is already good, and never silently repair extracted text.
- **This project has two problems of very different size** — the 430-document extractor and the
  2-document annotated-lecture path. Work on the small one is not automatically in scope just because it
  is more interesting. Check which problem a task serves before starting it.
- **The CLI rule is a verb count, not a flag count.** Three verbs: `inspect`, `extract`, `version`. New
  capability arrives as a new *value* of `--mode` / `--format` / `--engine`. A capability that needs a
  fourth verb is a scope question.
- **Uncertain about the operator's intent → write it into `scope.md` § Open decisions**, don't invent an
  answer. Six are open right now.

Hub: `~/llm-project-bootstrap/directives/scope-discipline.md` → guide `PROJECT_SETUP.md`
