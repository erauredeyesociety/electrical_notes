# Quizzes — CPSC 462

One folder per quiz: `qzNN/`, same shape as `hw/hwNN/`.

```sh
mkdir -p content/cpsc_462/qz/qz01
docs/latex/new_tex.sh content/cpsc_462/qz/qz01 1 some-slug --pts "5 pts"
docs/latex/new_tex.sh content/cpsc_462/qz/qz01 --solutions
docs/latex/build_tex.sh content/cpsc_462/qz/qz01
docs/latex/flatten_tex.sh content/cpsc_462/qz/qz01
```

The macros resolve to [`../reference_docs/cpsc462_macros.tex`](../reference_docs/cpsc462_macros.tex)
automatically — `new_tex.sh` computes the path, so don't write it by hand.

**Quizzes are named by topic, not numbered** (Quiz Application, Quiz Transport,
Quiz Network 1, Quiz Network 2, Quiz Link Layer, Quiz Wireless). Record which
topic a `qzNN` is in that folder's `README.md`.

Everything else — the two-document rule, citations, verification — is in
[`../hw/prompt.md`](../hw/prompt.md) and the
[doctrine](../../../docs/directives/coursework-solutions.md).
