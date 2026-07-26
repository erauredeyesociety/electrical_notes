# STAT 412 Final Project Student Guide

## Sources Reviewed
- STAT 412 Printable Final Project Instructions.docx
- STAT 412 Final Project Template.docx
- Dataset_STAT412_Project_Final.xlsx

---

# What You Must Submit

You must submit **two files**:

## 1. Completed Word Template
- Enter all answers into the provided template.
- Include formulas, calculations, interpretations, hypothesis tests, and email responses.

## 2. Excel Workbook
- Show your random sample selection.
- Show all formulas and calculations.
- Include any graphs you create.

**Important:** Both the Word document and Excel workbook must be submitted to receive full credit.

---

# Step 1: Create Your Random Sample

Use the dataset and focus on:

**Column M = ARR_DELAY**

Meaning:
- Negative value = Flight arrived early
- Positive value = Flight arrived late

## Random Sample Selection Process

1. Add a new column and enter:

```excel
=RAND()
```

2. Fill the formula down through the dataset.

3. Copy the RAND column and paste as values so the numbers stop changing.

4. Sort by the frozen random numbers.

5. Keep only the first **250 rows**.

This 250-row sample will be used for all remaining sections.

---

# Step 2: Confidence Interval for the Mean (15 Points)

Question:

> What is the average arrival delay for all U.S. flights?

## A. Point Estimate

Calculate the sample mean:

```excel
=AVERAGE(range)
```

This is your estimate of the population mean arrival delay.

## B. 95% Confidence Interval for the Mean

Calculate:

```excel
=AVERAGE(range)
=STDEV.S(range)
=COUNT(range)
```

Margin of Error:

```excel
=CONFIDENCE.T(0.05, stdev, n)
```

Confidence Interval:

```text
Lower Limit = Mean - Margin of Error
Upper Limit = Mean + Margin of Error
```

## C. Interpretation

Example:

> We are 95% confident that the true average arrival delay for all U.S. airline flights lies between X and Y minutes.

---

# Step 3: Confidence Interval for a Proportion (15 Points)

Question:

> What proportion of flights are late?

A flight is considered late if:

```text
ARR_DELAY > 10 minutes
```

## A. Point Estimate

Count flights greater than 10 minutes:

```excel
=COUNTIF(range,">10")
```

Then:

```excel
=count_late/250
```

This gives the sample proportion (p̂).

## B. 95% Confidence Interval for the Proportion

Formula:

```text
p̂ ± z × √[(p̂(1-p̂))/n]
```

Use:

```text
z = 1.96
n = 250
```

## C. Interpretation

Example:

> We are 95% confident that the true proportion of flights arriving more than 10 minutes late is between X% and Y%.

---

# Step 4: One-Sample Hypothesis Test for Mean (20 Points)

Manager's Claim:

> The average flight arrival delay is less than 8 minutes.

Significance Level:

```text
α = 0.05
```

## A. Hypotheses

```text
H0: μ ≥ 8
H1: μ < 8
```

## B. Test Statistic

```text
t = (x̄ - 8)/(s/√n)
```

## C. P-Value

Excel:

```excel
=T.DIST(test_statistic, df, TRUE)
```

This is a left-tailed test.

## D. Decision Rule

If:

```text
p-value < 0.05
```

Reject H0.

Otherwise:

```text
Do not reject H0.
```

## E. Email to Manager

Explain:

- Random sample selection
- One-sample t-test method
- Test statistic and p-value
- Decision
- Whether evidence supports the claim

Use plain language.

---

# Step 5: One-Sample Hypothesis Test for Proportion (20 Points)

Manager's Claim:

> Less than 28% of flights are late.

Late means:

```text
ARR_DELAY > 10
```

## A. Hypotheses

```text
H0: p ≥ 0.28
H1: p < 0.28
```

## B. Test Statistic

```text
z = (p̂ - 0.28) / √[(0.28)(0.72)/250]
```

## C. P-Value

Excel:

```excel
=NORM.S.DIST(z,TRUE)
```

## D. Decision

Compare the p-value to:

```text
0.05
```

## E. Email to Manager

Explain:

- How the proportion was calculated
- Hypothesis test process
- Whether evidence supports the claim

Use non-technical language.

---

# Step 6: Two-Sample Mean Hypothesis Test (30 Points)

Question:

> Is your airline better than a competitor airline?

"Better" means lower average arrival delay.

## Airline Selection

Use the first letter of your first name to select your airline.

Use the first letter of your last name to select the competitor airline.

If no airline starts with the correct letter, follow the instructor's guidance and choose the closest available airline.

## Build Two Samples

Filter ARR_DELAY by the two selected airlines.

Common airline codes in the dataset include:

```text
AA
B6
DL
NK
UA
```

## A. Hypotheses

Because a lower delay is better:

```text
H0: μ1 ≥ μ2
H1: μ1 < μ2
```

Where:

- μ1 = Your airline
- μ2 = Competitor airline

## B. Test Statistic

Use Excel Data Analysis ToolPak:

```text
t-Test: Two-Sample Assuming Unequal Variances
```

## C. P-Value

Obtain from Excel test output.

## D. Decision

If:

```text
p-value < 0.05
```

Reject H0.

Otherwise:

```text
Do not reject H0.
```

## E. Email to CEO

Include:

- Goal of analysis
- Airlines compared
- Test used
- P-value
- Final decision
- Whether the airline appears better than the competitor

Write for a business executive rather than a statistician.

---

# What Goes Into the Word Template

For every section include:

## Excel Formula Used

Example:

```excel
=AVERAGE(M2:M251)
```

## Numeric Result

Example:

```text
Mean = 7.4
```

## Interpretation

Provide a plain English explanation.

## Hypothesis Tests

Include:

- H₀
- H₁
- Test statistic
- P-value
- Decision
- Supporting explanation

## Required Emails

You will write:

1. Email to the DOT Manager
2. Email to the Airline CEO

---

# Recommended Workflow

1. Create random sample of 250 rows.
2. Complete confidence interval for mean.
3. Complete confidence interval for proportion.
4. Complete one-sample mean hypothesis test.
5. Complete one-sample proportion hypothesis test.
6. Complete two-sample airline comparison test.
7. Fill in Word template.
8. Verify formulas and calculations remain in Excel.
9. Submit both Word and Excel files.

---

# Quick Checklist Before Submission

- [ ] Random sample contains exactly 250 rows.
- [ ] ARR_DELAY column used correctly.
- [ ] All answers rounded appropriately.
- [ ] Confidence interval calculations shown.
- [ ] Hypothesis test calculations shown.
- [ ] P-values provided.
- [ ] Decision statements included.
- [ ] Manager email completed.
- [ ] CEO email completed.
- [ ] Word template completed.
- [ ] Excel workbook attached.
- [ ] Both files submitted.
