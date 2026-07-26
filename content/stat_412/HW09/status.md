# HW09 Status

## Current pass

- Timestamp screenshots were normalized to `1.png` through `10.png` in question order.
- The standard-normal table files originally named `q1.md` and `q2.md` were preserved as reference tables `1.md` and `2.md`.
- Clean prompts were created for Q1--Q10.
- Raw MyStatLab technology HTML in Q3 was replaced with clean Markdown technology results.
- Newly pasted conclusion/dropdown HTML was cleaned from Q1, Q2, Q3, Q5, Q6, Q7, Q8, Q9, and Q10 and replaced with explicit platform dropdown selections.
- Q4 was corrected from the mismatched right-tailed platform choice to **Choice C**: \(H_0:p_1=p_2\), \(H_a:p_1\ne p_2\).
- Q5 now shows the pooled-proportion calculation for the test statistic \(z=-5.28\).
- The missing conclusion selection-list words were added to `platform_answers.md`, the relevant `qN.md` files, and the consolidated answer-key PDF.
- For Q5, the added pasted HTML was an incorrect-answer feedback dialog for the \(z\) calculation rather than an expanded conclusion dropdown; the recorded conclusion selections follow the same MyStatLab conclusion template used by the neighboring questions.
- New HW09 context added CI follow-ups: Q4 conclusion dropdowns were added; Q5 is now explicitly marked **unresolved / not platform-confirmed** after prior attempted platform entries were incorrect. Screenshot hypothesis choice is **D**; direct calculation from the visible prompt gives \(z=-5.28\) and 90% CI \(-0.2640 < p_1-p_2 < -0.1416\), but those should not be treated as accepted platform fields. Q6/Q7 now include appropriate CI checks; Q8/Q9/Q10 CI conclusion dropdowns/wording were expanded.
- Appropriate CI levels used here: one-tailed \(\alpha\) tests use two-sided \(1-2\alpha\) intervals; two-tailed \(\alpha\) tests use \(1-\alpha\) intervals.
- `hw09_audit_calculations.py` reproduces all non-technology-output calculations.

## Notes

- Q3 uses the platform's own technology-output values because the prompt gives percentages and the popup gives the accepted downstream statistics.
- Several values needed zoomed screenshot verification: Q2 is \(251/300\) and \(308/400\); Q5 is \(63/286\); Q6 uses \(17/7647\); Q9 is \(245/2120\); Q10 is \(312/904\) and \(407/1106\).
