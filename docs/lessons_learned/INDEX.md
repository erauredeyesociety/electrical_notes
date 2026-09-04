# Lessons Learned — INDEX

**PRESCRIPTIVE** rules future sessions must obey, in `WHEN → DON'T → BECAUSE` form, each carrying the
specific failure that earned it. A [finding](../findings/INDEX.md) that hardens into a rule graduates here.

**EMPTY — and that is a gap, not a state of nature.** At least three lessons are already earned and
recorded elsewhere as *findings*. The distillation is the missing step; it is
[../roadmap.md](../roadmap.md) § M6.

| Lesson owed | The failure that earned it | Where the evidence is |
| --- | --- | --- |
| **Never read mathematics out of a PDF text layer** — render the region and look at it | `pdftotext` turned $\cos(\tfrac{\pi}{6}n)$ into `cos( 6π n)`, a constant signal, and dropped a $\sqrt{\ }$ that decided whether a signal was periodic. **Neither raised an error.** | [`content/cesc_410/hw/reference_docs/findings.md`](../../content/cesc_410/hw/reference_docs/findings.md) HW-01 |
| **Never let a tooling reference into a submitted document** | Script names and flags reached a report that was zipped for submission | [`content/cesc_410/labs_and_projects/reference_docs/known_issues.md`](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md) KI-09 — already promoted into [../directives/coursework-solutions.md](../directives/coursework-solutions.md) § Repo hygiene |
| **A silent success is worse than a failure** | The docs-rag ingester has no `.tex` handler: it logs a warning, indexes **zero** files, and reports success. Every LaTeX-sourced answer it gives is unreliable, and nothing says so. | [`docs-rag/FINDINGS.md`](../../docs-rag/FINDINGS.md) F-01 |

## The distinction that keeps this folder from becoming a second directives folder

A **directive** is a standing rule for how to work here. A **lesson** is a rule *plus the specific
failure that earned it*. If you cannot name the incident, it is a directive, not a lesson.

## Format

One bullet per lesson — no prose essay:

```
- **<the rule, stated so it applies next time>** — e.g. <the concrete failure that taught it>. (YYYY-MM-DD)
  Source: <path>
```

Split at ~400 lines into `lessons_2.md` and index the parts.
