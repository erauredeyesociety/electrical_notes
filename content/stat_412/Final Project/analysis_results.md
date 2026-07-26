# STAT 412 Final Project Analysis Results

Random sample seed: `412`. Sample size: `250` rows.

## Section 1: Confidence Interval for Mean

- Point estimate: mean arrival delay = **4.7 minutes**.
- Sample standard deviation = **42.4 minutes**.
- 95% CI = **(-0.5, 10.0) minutes**.
- Interpretation: We are 95% confident that the true mean arrival delay for all U.S. flights is between **-0.5** and **10.0** minutes.

## Section 2: Confidence Interval for Proportion

- Late flight definition: `ARR_DELAY > 10` minutes.
- Late count = **61** out of **250**.
- Point estimate: **24.4%**.
- 95% CI = **(19.1%, 29.7%)**.
- Interpretation: We are 95% confident that the true proportion of flights arriving more than 10 minutes late is between **19.1%** and **29.7%**.

## Section 3: One-Sample Mean Hypothesis Test

- Claim: the average flight arrival delay is less than 8 minutes.
- Hypotheses: `H0: μ ≥ 8`; `H1: μ < 8`.
- Test statistic: **t = -1.2**, df = **249**.
- P-value: **0.1124**.
- Decision: **do not reject H0** at α = 0.05.

## Section 4: One-Sample Proportion Hypothesis Test

- Claim: less than 28% of flights are late.
- Hypotheses: `H0: p ≥ 0.28`; `H1: p < 0.28`.
- Test statistic: **z = -1.3**.
- P-value: **0.1024**.
- Decision: **do not reject H0** at α = 0.05.

## Section 5: Two-Sample Mean Hypothesis Test

Pending: provide first/last initials or explicit airline codes to select the two airlines.

