# QZ08 Status

Updated from the QZ08 screenshot wave added on 2026-07-23 and normalized on 2026-07-23/24.

## Complete Work Captured

- Clean prompts and answers: `q1.md` through `q10.md`.
- Platform entry sheet: `platform_answers.md`.
- Table/blank-entry sheet: `table_entries.md`.
- Worked standalone LaTeX partials: `solutions/q01.tex` through `solutions/q10.tex`.
- Concise answer key: `stat412_qz08_answer_key.tex`.
- Calculation audit: `qz08_audit_calculations.py`.

## Screenshot Map

- `1.png`: Q1 births by day.
- `2.png`: Q2 female-height normality GOF, later parts.
- `3.png`: Q3 best-of-seven games.
- `4.png`: Q4 horse-race post positions.
- `5.png`: Q5 candy and tips.
- `6.png`: Q6 polygraph independence.
- `7.png`: Q7 gender and eye color.
- `8.png`: Q8 tire wear.
- `8-2.png`: Q8 experiment-results popup.
- `9.png`: Q9 treatment/placebo.
- `10.png`: Q10 tennis challenges.

## Preserved Legacy/Unmapped Material

- The older July 18 screenshot wave was moved to `legacy_unmapped_2026-07-18/`
  because it does not match the active QZ08 `q1.md`--`q10.md` prompts.

## Verification

- The audit script runs successfully.
- `tectonic` compiled the answer key and all solution TeX files successfully.
- Latest compile check after screenshot renaming: answer key compiles with only a harmless underfull-box warning.
- Latest table-entry pass: Q2 expected-frequency cells, Q5/Q9 confidence-interval blanks, and expected-count check tables for Q3/Q4/Q6/Q7/Q10 are explicitly written out.
- Latest worked-solution expansion: `solutions/q01.tex`--`solutions/q10.tex` now include calculation details such as chi-square formulas, expected-count substitutions, degrees of freedom, Welch/pooled standard errors, and confidence-interval margin calculations.
