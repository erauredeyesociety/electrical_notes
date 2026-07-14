# HW07 Status

Generated from the initial 20 screenshots and loose reference tables on 2026-07-13.

## Complete / visible work captured

- Clean prompts: `q1.md` through `q20.md`.
- Worked standalone LaTeX partials: `solutions/q01.tex` through `solutions/q20.tex`.
- Concise standalone answer key: `stat412_hw07_answer_key.tex`.
- Calculation audit script: `hw07_audit_calculations.py`.

## Current open review items

- Q4: the visible screenshot values give `t=-2.43` and P-value about `0.009`, but a raw platform dump showed `-2.43` marked incorrect and a P-value range of `0.005 <= P-value < 0.0075`. This is inconsistent with the screenshot values (`n=68`, `xbar=40`, `s=3.4`). If the platform still rejects Q4, recapture the active prompt before changing the math.
- Q12: re-read the screenshot as sample mean `18,330` (not `18,230`), so the correct visible-prompt statistic is `t=0.94`.
- Q15 visible screenshot still has 55.0%, which gives `z=1.19`, P-value about `0.235`, and **does not reject** H0 at alpha 0.05. If platform expects rejection, get the later/revised screenshot because the visible values do not support rejection.

## Notes to review on platform

- Q9 uses the two-sided alternative because the expert's claim is exactly 40%. If a later screen explicitly asks for evidence of increase or decrease, update `q9.md`, `solutions/q09.tex`, and the answer key together.
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
- Q9 exact binomial two-sided P-value is about `0.1075`; do not reject at `alpha=0.08`.
- Q10 platform-confirmed P-value is `0.718`; fail to reject.
- Q11 alternative is right-tailed from the visible prompt: `H1: mu > 10` (greater-than, not not-equal).
- Q13 statistic is negative: `z=-0.30`; keep the minus sign.
- If Q13 platform rejects exact `z=-0.30`, try `z=-0.33`; that comes from using rounded `phat=0.094` in the test-statistic formula.
- Q14 conclusion choice is A: reject H0 with sufficient evidence.
- Q18 conclusion choice is B.
- Cleaned all remaining pasted HTML out of `q1.md`--`q20.md`; inventory reports no markdown files containing HTML.
