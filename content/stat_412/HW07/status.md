# HW07 Status

Generated from the initial 20 screenshots and loose reference tables on 2026-07-13.

## Complete / visible work captured

- Clean prompts: `q1.md` through `q20.md`.
- Worked standalone LaTeX partials: `solutions/q01.tex` through `solutions/q20.tex`.
- Concise standalone answer key: `stat412_hw07_answer_key.tex`.
- Calculation audit script: `hw07_audit_calculations.py`.

## Current open review items

- Q12: re-read the screenshot as sample mean `18,330` (not `18,230`), so the correct visible-prompt statistic is `t=0.94`.
- Q15 visible screenshot still has 55.0%, which gives `z=1.19`, P-value about `0.235`, and **does not reject** H0 at alpha 0.05. If platform expects rejection, get the later/revised screenshot because the visible values do not support rejection.

## Notes to review on platform

- Q9 uses the two-sided alternative because the expert's claim is exactly 40%.
- Q12 sample mean is transcribed as 18,330 kilometers.

## 2026-07-14 correction pass

- Merged/deleted duplicate raw markdown snippets `1.md`, `10.md`, and `11.md`.
- Cleaned pasted HTML out of reference-table files `4.md`, `5.md`, and `9.md`; useful context was moved into the matching `qN.md` files.
- Corrected Q2 non-rejection region to 3 through 9, so `alpha = 0.0609`.
- Added Q2 beta/power from newly exposed prompt text: beta `0.8695` for `p=0.3`, beta `0.8454` for `p=0.5`; powers `0.1305` and `0.1546`.
- Corrected Q3 standard deviation to 15 mL, so type I error probability is `0.0718`.
- Added Q3 type II probability when `mu=195`: beta `0.1151`.
- Q5 conclusion dropdowns: reject H0; there is sufficient evidence; reject for significance levels greater than the P-value.
- Q6 P-value is two-tailed and exact value is `0.0022389`; the prompt asks for three decimals, so enter `0.002` rather than `0.0022`.
- Q9 MyStatLab feedback uses the doubled one-tail exact binomial rule for the two-sided test: `2P(X >= 12) = 0.1131`; do not reject at `alpha=0.05`.
- Q10 platform-confirmed P-value is `0.718`; fail to reject.
- Q11 alternative is right-tailed from the visible prompt: `H1: mu > 10` (greater-than, not not-equal).
- Q13 statistic is negative: `z=-0.30`; keep the minus sign.
- Q14 conclusion choice is A: reject H0 with sufficient evidence.
- Q18 conclusion choice is B.
- Cleaned all remaining pasted HTML out of `q1.md`--`q20.md`; inventory reports no markdown files containing HTML.

## 2026-07-18 HTML catch-up

- Q1(a) corrected from user feedback: Type I fill-ins are `31% or more`; `less than 31%`. Type II is the reverse: `less than 31%`; `31% or more`.
- Q2(c) is not a good test because alpha is relatively small while both beta values are large.
- Q6 platform-confirmed values remain `z=3.06` and P-value `0.002`.
- Q11 confirms `t=3.49`; its P-value field is still blank, so `0.000` is computed but not platform-confirmed.
- Removed all newly pasted HTML from Q1, Q2, Q4, Q6, Q9, and Q11.
- Inventory reports no Markdown files containing pasted HTML.
- `tectonic` compiled `stat412_hw07_answer_key.tex` and `solutions/q01.tex` successfully after the Q1 correction.

## 2026-07-19 correction pass

- Q4 conclusion from newly added content: reject H0; there is sufficient evidence; less than 41 months. The exact P-value is about `0.009`, and the table range is `0.0075 < P-value < 0.01`.
- Q6 and Q11 both use `greater` for "rejected for significance levels ___ than the P-value."
- Q9 screenshot uses `alpha=0.05`; MyStatLab feedback corrected the P-value method to `2P(X >= 12) = 0.1131`, not `0.1075`.
- Q11 newly added HTML confirms the conclusion dropdowns `Reject` and `is`; use `greater` for the final significance-level comparison.
- Q12 P-value rechecked: exact right-tail P-value is about `0.1758`, so enter `0.176` if a numeric field is shown; from the t table, use `0.15 < P-value < 0.20` if a range dropdown is shown.
- Q13 user confirmed the correct z statistic is `-0.30`; P-value from the found statistic is `0.3821`.
- Removed newly pasted HTML from Q4, Q9, Q11, and Q13.

## 2026-07-19 later added-content pass

- Q9 added conclusion choices. Correct conclusion choice is B: do not reject H0; there is not sufficient evidence that the percentage differs from 40%.
- Q12 added final conclusion dropdowns. Fill-ins are `Do not reject`, `is not`, and `greater`.
- Q13 added final conclusion choices. Correct conclusion choice is C: do not reject H0; insufficient evidence to support the claim.
- Inventory reports no Markdown files containing pasted HTML after this pass.
- `tectonic` compiled `stat412_hw07_answer_key.tex`, `solutions/q09.tex`, `solutions/q12.tex`, and `solutions/q13.tex` successfully.
