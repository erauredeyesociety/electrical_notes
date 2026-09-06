# Exams — CPSC 462

One folder per exam: `examNN/`, same shape as `hw/hwNN/`.

```sh
mkdir -p content/cpsc_462/exam/exam01
docs/latex/new_tex.sh content/cpsc_462/exam/exam01 1 some-slug --pts "20 pts"
docs/latex/new_tex.sh content/cpsc_462/exam/exam01 --solutions
docs/latex/build_tex.sh content/cpsc_462/exam/exam01
docs/latex/flatten_tex.sh content/cpsc_462/exam/exam01
```

The macros resolve to [`../reference_docs/cpsc462_macros.tex`](../reference_docs/cpsc462_macros.tex)
automatically — `new_tex.sh` computes the path, so don't write it by hand.

Two exams are scheduled: **Exam 1** 9/30/26 and **Exam 2** 11/6/26. Each covers
the material since the previous exam, so `exam01/README.md` should record the
coverage range as well as the problem inventory.

Everything else — the two-document rule, citations, verification — is in
[`../hw/prompt.md`](../hw/prompt.md) and the
[doctrine](../../../docs/directives/coursework-solutions.md).
