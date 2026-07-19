# QZ07 Status

Updated from the full screenshot wave added on 2026-07-18.

## Complete work captured

- Numbered screenshots: `1.png` through `8.png`.
- Reference tables: `2.md`, `6.md`, and `8.md`.
- Clean prompts: `q1.md` through `q8.md`.
- Worked standalone LaTeX partials: `solutions/q01.tex` through `solutions/q08.tex`.
- Concise standalone answer key: `stat412_qz07_answer_key.tex`.

## Screenshot map

- `1.png`: Q1 mean-height known-sigma z test.
- `2.png`: Q2 soft-drink type I/type II error probabilities.
- `3.png`: Q3 illegal-drug-use one-proportion test.
- `4.png`: Q4 Type I/Type II wording.
- `5.png`: Q5 aflatoxin variance test.
- `6.png`: Q6 mouse-life-span t test.
- `7.png`: Q7 malpractice-lawsuit one-proportion test.
- `8.png`: Q8 thread-strength sample-size problem.

## Answers / review notes

- Q1: two-sided known-sigma mean test. `z=2.43`, P-value `0.015`.
- Q2: type I error probability `0.0244`; type II error probability at `mu=178` is `0.2266`.
- Q3: one-proportion left-tailed test. Choice B, `z=-0.46`, P-value `0.3225`, conclusion choice C.
- Q4: Type I/II wording choice C.
- Q5: variance test. `chi-square=48.57`, P-value `0.900`; do not reject.
- Q6: left-tailed one-sample t test. Choice F, `t=-2.46`, uses the reference table in `6.md`; table range `0.0075 < P-value < 0.01`.
- Q7: one-proportion right-tailed test. Choice B, `z=7.75`, P-value `0.000`, decision choice B, final conclusion choice D.
- Q8: two-sample known-sigma sample-size problem. Minimum sample size is `20` for each sample.

## Platform notes

- Q6 asks for a P-value range from a t table. The exact one-tailed P-value is about `0.0082`; if the dropdown does not include `0.0075 < P-value < 0.01`, use the broader range that contains it, usually `0.005 < P-value < 0.01`.
- Q7 screenshot did not display a numeric alpha, but the P-value rounds to `0.000`, so the rejection decision is stable for normal significance levels.

## Verification

- Material inventory reports no unassigned screenshots and no Markdown files containing pasted HTML.
- `tectonic` compiled `stat412_qz07_answer_key.tex` and `solutions/q01.tex` through `solutions/q08.tex` successfully.
