# Features — INDEX

Specifications for **shipped-stable** capabilities: what it does, its interface, how to use it.

**EMPTY, deliberately — and it may stay that way.** This repo's deliverable is documents, not software.
It has no API and no user-facing feature surface; what it has is a build pipeline and a workflow, and
both are already covered:

- The **coursework workflow** is a standing rule, so it is a directive —
  [../directives/coursework-solutions.md](../directives/coursework-solutions.md).
- The **build commands** are operator procedures, so they belong in
  [../runbooks/INDEX.md](../runbooks/INDEX.md).
- The **child projects** have real interfaces and document them themselves —
  [`ocr_handler/docs/features/INDEX.md`](../../ocr_handler/docs/features/INDEX.md).

**Populate this folder only if** the root repo grows something with a stable, reusable interface — a
generalised submission packager, say, or a shared figure pipeline — *after* it has shipped and settled.
Writing a spec against a workflow still being invented produces a doc that is wrong on arrival
([../directives/documentation-discipline.md](../directives/documentation-discipline.md)).
