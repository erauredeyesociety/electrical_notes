# Homework 

## Question 2

### Problem Statement

We apply Bayes' Theorem to update the belief about product success after observing a favorable survey result.

**Step 1: Identify Prior Probabilities**

- P(Success) = 0.40
- P(Unsuccessful) = 1 − 0.40 = 0.60

**Step 2: Identify Conditional Probabilities (Survey Reliability)**

- P(Favorable | Success) = 0.90
- P(Unfavorable | Unsuccessful) = 0.80
- P(Favorable | Unsuccessful) = 1 − 0.80 = 0.20 (false positive rate)

**Step 3: Calculate Joint Probabilities**

P(Success AND Favorable) = P(Favorable | Success) × P(Success) = 0.90 × 0.40 = **0.36**

P(Unsuccessful AND Favorable) = P(Favorable | Unsuccessful) × P(Unsuccessful) = 0.20 × 0.60 = **0.12**

**Step 4: Calculate Marginal Probability of a Favorable Survey**

P(Favorable) = P(Success AND Favorable) + P(Unsuccessful AND Favorable)

P(Favorable) = 0.36 + 0.12 = **0.48**

**Step 5: Apply Bayes' Theorem for Posterior Probability**

P(Success | Favorable) = P(Success AND Favorable) / P(Favorable)

P(Success | Favorable) = 0.36 / 0.48

**P(Success | Favorable) = 0.75 = 75%**

### Answer

Given a favorable result from the marketing survey, the probability that the product will be successful is **75%**.

---

## Question 3

We compare two strategies: (A) decide immediately without a pilot study, or (B) conduct the pilot study first then decide based on the result.

#### Part 1: Prior Decision (Without Pilot Study)

**Given:**

- P(Favorable Market) = 0.60
- P(Unfavorable Market) = 0.40

**EMV Calculations:**

EMV(Large) = (0.60)($90,000) + (0.40)(−$30,000) = $54,000 − $12,000 = **$42,000**

EMV(Small) = (0.60)($60,000) + (0.40)(−$20,000) = $36,000 − $8,000 = **$28,000**

EMV(None) = **$0**

**Best prior decision: Build Large Facility (EMV = $42,000)**

#### Part 2: Pilot Study Conditional Probabilities

- P(Successful Pilot) = 0.50, P(Unsuccessful Pilot) = 0.50
- P(Favorable Market | Successful Pilot) = 0.80
- P(Unfavorable Market | Successful Pilot) = 1 − 0.80 = 0.20
- P(Unfavorable Market | Unsuccessful Pilot) = 0.90
- P(Favorable Market | Unsuccessful Pilot) = 1 − 0.90 = 0.10

#### Part 3: EMVs Given Pilot Results (Including $10,000 Study Cost)

**If Pilot Study is Successful:**

EMV(Large | Success) = (0.80)($90,000) + (0.20)(−$30,000) − $10,000 = $72,000 − $6,000 − $10,000 = **$56,000**

EMV(Small | Success) = (0.80)($60,000) + (0.20)(−$20,000) − $10,000 = $48,000 − $4,000 − $10,000 = **$34,000**

EMV(None | Success) = $0 − $10,000 = **−$10,000**

**Best action if pilot successful: Build Large Facility (EMV = $56,000)**

**If Pilot Study is Unsuccessful:**

EMV(Large | Unsuccessful) = (0.10)($90,000) + (0.90)(−$30,000) − $10,000 = $9,000 − $27,000 − $10,000 = **−$28,000**

EMV(Small | Unsuccessful) = (0.10)($60,000) + (0.90)(−$20,000) − $10,000 = $6,000 − $18,000 − $10,000 = **−$22,000**

EMV(None | Unsuccessful) = $0 − $10,000 = **−$10,000**

**Best action if pilot unsuccessful: Build None (EMV = −$10,000)**

#### Part 4: Total Expected Value with Pilot Study

EMV(With Pilot) = P(Success) × EMV(Best | Success) + P(Unsuccessful) × EMV(Best | Unsuccessful)

EMV(With Pilot) = (0.50)($56,000) + (0.50)(−$10,000)

EMV(With Pilot) = $28,000 − $5,000

**EMV(With Pilot) = $23,000**

#### Part 5: Comparison and Recommendation

| Strategy                | Expected Value |
|------------------------|---------------|
| No Pilot — Build Large | $42,000       |
| Conduct Pilot Study    | $23,000       |

Expected Value of Sample Information (EVSI) = $23,000 − $42,000 = **−$9,000**

### Recommendation

**Do not conduct the pilot study. Build the large manufacturing facility immediately.**

The EMV of deciding now ($42,000) significantly exceeds the EMV of conducting the pilot study first ($23,000). The EVSI is negative (−$9,000), meaning the information gained from the pilot study is not worth its $10,000 cost. The prior probability of a favorable market (0.60) is already strong enough to justify the large facility investment without further testing.