# HW06 Status Notes

## Screenshot wave

The initial timestamp screenshot wave was normalized chronologically to `1.png`
through `20.png`. OCR drafts and a contact sheet are in ignored `tmp/`.

## Captured parts

Some initial screenshots showed only the first answer field even when the prompt
had later parts. The inferable later parts have now been filled into the
question markdown, worked solutions, and answer key.

Resolved from the latest material:

- Q5 now includes 99% CI, interpretation, and width comparison.
- Q3 final parts: 95% interval is wider; interpretation choice B.
- Q6 final parts: margin of error is 1.9 minutes; interpretation choice C.
- Q7 margin of error was visible/confirmed as 103.83, the unit is dollars, and CI is computed.
- Q7 interpretation choice is C with fill-in 90; confidence intervals for means describe the population mean, not most individual phones.
- Q8 interpretation choice is D.
- Q9 part (b) asks for the sample standard deviation, $s=8.01$.
- Q9 part (c) asks for a 98% CI; answer is $(12.81,21.91)$.
- Q10 interpretation choice is A.
- Q12 now includes interpretation fill-ins and width comparison.
- Q13 interpretation choice is B; Q14 interpretation choice is C.
- Q15 screenshot count is **1321**, not 1221; intervals were corrected.
- Q15 interpretation/width comparison resolved: population proportion; between the endpoints; 95% interval is wider.
- Q18 variance interpretation choice is D; standard-deviation interpretation choice is C with values 0.207 and 0.422. A raw HTML dump showed choice D selected for the SD interpretation, but it says 5% confidence and is not correct for the 95% interval.
- Q19 variance interpretation choice is B with between-values 0.018 and 0.240 (not 24).
- Q20 part (b) fill-ins are $\bar x$ and $\mu$, with maximum error 2.13 cm.
- Added explicit final-answer blocks to sparse question files so Q1--Q20 no longer look partially unanswered from the markdown layer.

## Method notes

- Known population standard deviation: use $z_{\alpha/2}\sigma/\sqrt n$.
- Unknown population standard deviation: use $t_{\alpha/2,df}s/\sqrt n$.
- Population proportion: use $\hat p\pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$.
- Variance/standard deviation intervals require normality and chi-square
  critical values:
  \[
  \frac{(n-1)s^2}{\chi^2_R}<\sigma^2<\frac{(n-1)s^2}{\chi^2_L}.
  \]
