# STAT 412 Final Project Instructions

This is a faithful working summary of the final project source files in this
folder. It preserves the instructor's workflow while translating it into the
CSV/Python workflow used here.

## Required submission files

The course instructions require two submitted files:

1. A completed Word template.
2. An Excel workbook showing the random sample, formulas, calculations, and any
   graphs.

For this repository workflow, the original Word/Excel files are preserved. The
analysis is done with Python and CSV files first. A completed copy of the Word
template should be created only after all calculations and choices are final.
Clean CSV files are produced instead of editing or creating an Excel workbook.

## Data

Use `Dataset_STAT412_Project_Final(ArrivalData).csv`.

The project focuses on `ARR_DELAY`, the arrival delay in minutes:

- negative value = arrived early;
- positive value = arrived late.

Late-flight definition for proportion work:

```text
ARR_DELAY > 10 minutes
```

## Random sample

Randomly select 250 rows from the dataset. The Excel instructions suggest
generating random numbers with `=RAND()`, freezing them as values, sorting by
the random numbers, and keeping the first 250 rows.

The Python workflow mirrors that process with a fixed random seed so the sample
is reproducible. The output sample CSV includes `SOURCE_ROW` and `RANDOM_VALUE`
columns for auditability.

## Section 1: Confidence interval for the mean

Question: What is the average arrival delay for all U.S. flights?

Required:

- point estimate: sample mean of `ARR_DELAY`;
- 95% confidence interval for the population mean;
- one-sentence plain-language interpretation.

Round answers to one decimal place unless otherwise specified.

## Section 2: Confidence interval for the proportion

Question: What proportion of flights are late?

Required:

- point estimate: sample proportion with `ARR_DELAY > 10`;
- 95% confidence interval for the population proportion;
- one-sentence plain-language interpretation.

Round answers to one decimal place unless otherwise specified.

## Section 3: One-sample hypothesis test for the mean

Manager's claim: the average flight arrival delay is less than 8 minutes.

Use:

```text
alpha = 0.05
H0: mu >= 8
H1: mu < 8
```

Required:

- hypotheses;
- test statistic;
- p-value;
- reject/do-not-reject decision with rationale;
- email to the manager explaining the method and result.

## Section 4: One-sample hypothesis test for the proportion

Manager's claim: less than 28% of flights are late.

Use:

```text
late = ARR_DELAY > 10
alpha = 0.05
H0: p >= 0.28
H1: p < 0.28
```

Required:

- hypotheses;
- test statistic;
- p-value;
- reject/do-not-reject decision with rationale;
- email to the manager explaining the method and result.

## Section 5: Two-sample hypothesis test for airline mean delays

Question: Is the selected airline better than a competitor airline?

Better means lower average arrival delay.

Airline selection rule:

- use the first letter of the student's first name to select the first/employer
  airline;
- use the first letter of the student's last name to select the competitor
  airline;
- if no airline begins with that letter, select the closest available airline
  following instructor guidance.

Use:

```text
alpha = 0.05
H0: mu1 >= mu2
H1: mu1 < mu2
```

Required:

- hypotheses;
- test statistic from a two-sample t-test assuming unequal variances;
- p-value;
- reject/do-not-reject decision with rationale;
- email to the CEO explaining whether the selected airline appears better than
  the competitor.

## Current unresolved input

The two-sample airline comparison needs the student's first and last initials,
or explicit airline codes, before the final report can be completed.
