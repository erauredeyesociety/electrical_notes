# HW08 Status

## Completed from visible screenshots/HTML

- Q1--Q3: two-sample \(t\) tests solved and re-audited against the visible dropdown orientation. Q3 must be entered in the platform's \(\mu_1-\mu_2\) form: \(H_0:\mu_1-\mu_2=-10\), \(H_1:\mu_1-\mu_2>-10\), \(t=-0.65\).
- Q4--Q5: Welch two-sample \(t\) tests solved from the provided data tables.
- Q6: TV time by gender chi-square independence test solved.
- Q7: technology-output confidence interval solved; assumptions dropdown/select-all is A, C, and D.
- Q8(a)--(c): parameter, hypotheses, and reported-P-value conclusion completed.
- Q9: confidence interval, interpretation choice, original \(z\)-test, and added test of \(H_0:\mu_1-\mu_2=26\) solved.
- Q11--Q12: goodness-of-fit tests solved using the expected/pie-chart distributions.
- Q13: marginal totals and expected frequencies solved.
- Q14--Q19: chi-square test quantities/conclusions solved from visible tables, including visible multiple-choice/dropdown hypothesis selections where shown.
- Q20: texting while driving by drinking-and-driving chi-square independence test solved.

## Verification notes

- Screenshots were normalized to `1.png` through `20.png`.
- The answer key now emphasizes platform/dropdown entries, not just the underlying calculations.
- Raw HTML in Q2 and Q7 was converted into clean markdown tables/output.
- Newly pasted platform HTML was stripped from the `q*.md` files during the cleanup pass.
- Q10 solved using pie-chart proportions \(0.12,0.02,0.03,0.14,0.10,0.31,0.28\): \(\chi^2=26.589\), P-value \(=0.000\) to three decimals.
- Q9 final comparison choice is **B**; assumptions choice is **D**.
- Q12 conclusion dropdowns from the pasted HTML are **Reject**, **is**, and **is different for teenagers and parents.**
- Q20 P-value is \(4.74\times10^{-126}\), so enter **0.000** if the platform asks for three decimals.
- `hw08_audit_calculations.py` reproduces all computed numeric results, including Q9 part (d) \(z=1.10,\ p=0.269\), Q12 \(\chi^2=29.664\), and Q20 \(\chi^2=570.34\) when rounded to two decimals.
- `tectonic` compiled the updated answer key and the changed solution PDFs successfully.
