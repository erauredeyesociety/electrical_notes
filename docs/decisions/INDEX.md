# Decisions — ADRs

One-screen records of *why*. **ADRs are immutable** — write a new one to supersede, never edit an old
one. A wrong idea is kept together with the reason it lost, so nobody re-attempts it.

Format: `NNNN-<slug>.md`, with **Status / Context / Decision / Consequences**.

**EMPTY — and three real decisions were made on 2026-09-04 that are currently recorded only in prose.**
Writing them up is [../roadmap.md](../roadmap.md) work; they are named here so they are not lost the way
`ocr_handler` nearly lost five decisions to its `todo.md`.

| ADR owed | The decision | Currently recorded in |
| --- | --- | --- |
| Older courses are not retrofitted | The coursework doctrine applies to `cesc_470`, `cesc_410`, `cpsc_462` and courses started after 2026-09-04. The other twelve are frozen. **Explicit operator ruling**, and the consequence — permanent inconsistency across the repo — was accepted deliberately. | [../directives/coursework-solutions.md](../directives/coursework-solutions.md) header · [../scope.md](../scope.md) § blacklist |
| One shared LaTeX toolchain, not one per course | `docs/latex/coursework_preamble.tex` is shared; only *notation* lives in a per-course `<course>_macros.tex`. The alternative — a preamble per course — was rejected because three preambles drift apart. Carried out the same day: all 18 problem files across `cesc_410` and `cesc_470` were re-pointed and the old course-local preamble was left in place as a documented tombstone rather than deleted. | [../directives/coursework-solutions.md](../directives/coursework-solutions.md) § Every file is standalone · [../DRIFT_REPORT.md](../DRIFT_REPORT.md) § 2 |
| The two-document rule | Derivations in per-problem `.tex`; final answers only in the assembled solutions document. Consequence accepted: more files, and an assembly step. | [../directives/coursework-solutions.md](../directives/coursework-solutions.md) § The two-document rule |

**Child-project ADRs are separate and are not restated here:**
[`ocr_handler/docs/decisions/INDEX.md`](../../ocr_handler/docs/decisions/INDEX.md) — five accepted ADRs
covering the PDF library, the imaging stack, text-layer-first, the deferred engine choice, and a
reopened intermediate representation.
