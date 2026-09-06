# Quizzes — CESC 470

Nothing here yet. One folder per quiz: `qzNN/`, same shape as `hw/hwNN/` — the
doctrine treats `hw`, `qz` and `exam` identically.

```sh
mkdir -p content/cesc_470/qz/qz01
docs/latex/new_tex.sh   content/cesc_470/qz/qz01 1 some-slug --pts "5 pts"
docs/latex/new_tex.sh   content/cesc_470/qz/qz01 --solutions
docs/latex/build_tex.sh content/cesc_470/qz/qz01
docs/latex/flatten_tex.sh content/cesc_470/qz/qz01
```

The macros resolve to [`../reference_docs/cesc470_macros.tex`](../reference_docs/cesc470_macros.tex)
automatically — `new_tex.sh` computes the path, so don't write it by hand. Use
the three-argument `\problemheader{n}{pts}{title}`: CESC 470 states no learning
outcomes.

Verified end to end on a throwaway `qz99/` (since deleted) on 2026-09-05: both
files scaffolded with no warning, built, flattened, and the flattened copies
compiled standalone with `CESC 470` in the running head.

Build products are handled by the course-level
[`../.gitignore`](../.gitignore) — no per-kind copy, and the instructor's quiz
PDF is kept whatever it is called.

Everything else — the two-document rule, citations, verification — is in
[`../hw/prompt.md`](../hw/prompt.md), the course traps are in
[`../reference_docs/findings.md`](../reference_docs/findings.md), and the rules
are in the [doctrine](../../../docs/directives/coursework-solutions.md).
