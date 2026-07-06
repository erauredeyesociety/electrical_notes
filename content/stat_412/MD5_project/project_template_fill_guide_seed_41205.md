# STAT 412 MD5 Project — Word Template Fill Guide

Use this as the copy/paste guide for `STAT_412_Midterm_Project_Template.docx`.
It is written to match the template's three main response columns:

- **Analysis to be performed**
- **Excel command used, if applicable**
- **Numeric result or text-based response**

These values use the reproducible seed-41205 sample:

```text
tmp/sample_250_seed_41205.csv
```

If you use a different Excel `RAND()` sample, recompute every numeric value.

## Section 1 — Sample selection note

The Word template starts at Section 2, but the project instructions require a
250-row sample. If there is any place to describe the sample method, use:

> I selected a random sample of 250 rows from the arrival-data CSV using a
> reproducible random seed of 41205. The analysis focuses on `ARR_DELAY`, where
> negative values indicate early arrivals and positive values indicate late
> arrivals.

## Section 2 — Descriptive statistics

Assume `ARR_DELAY` is in `Sample_250!M2:M251`.

| Analysis to be performed | Excel command used | Numeric result or text-based response |
|---|---|---|
| Mean | `=AVERAGE(Sample_250!M2:M251)` | `3.9 minutes` |
| Median | `=MEDIAN(Sample_250!M2:M251)` | `-6.0 minutes` |
| Standard Deviation | `=STDEV.S(Sample_250!M2:M251)` | `38.1 minutes` |
| Variance | `=VAR.S(Sample_250!M2:M251)` | `1449.9 minutes^2` |
| Minimum | `=MIN(Sample_250!M2:M251)` | `-56.0 minutes` |
| Maximum | `=MAX(Sample_250!M2:M251)` | `257.0 minutes` |
| 1st Quartile | `=QUARTILE.INC(Sample_250!M2:M251,1)` | `-16.0 minutes` |
| 3rd Quartile | `=QUARTILE.INC(Sample_250!M2:M251,3)` | `11.0 minutes` |
| Compare the mean on-time arrival results for AIRLINE #1 vs. AIRLINE #2 and state a conclusion. | Use carrier-filtered `AVERAGEIF`/summary table. Example: `=AVERAGEIF(Sample_250!D:D,"UA",Sample_250!M:M)` and `=AVERAGEIF(Sample_250!D:D,"WN",Sample_250!M:M)` | Compare UA vs WN. UA mean = `-0.8 minutes`, SD = `34.9 minutes`; WN mean = `7.8 minutes`, SD = `29.7 minutes`. UA had the lower average delay, while WN was somewhat more consistent because its standard deviation was smaller. |
| Compare the median on-time arrival results for AIRLINE #1 vs. AIRLINE #2 and state a conclusion. | Use filtered median or carrier summary. In modern Excel: `=MEDIAN(FILTER(Sample_250!M:M,Sample_250!D:D="UA"))` and same for WN. | UA median = `-10.0 minutes`; WN median = `-1.0 minute`. A typical UA flight arrived earlier than a typical WN flight in this sample. |

Carrier summary for the chosen comparison:

| Airline | Count | Mean delay | Median delay | Standard deviation |
|---|---:|---:|---:|---:|
| UA | 45 | -0.8 | -10.0 | 34.9 |
| WN | 45 | 7.8 | -1.0 | 29.7 |

## Section 3 — Trimmed mean

| Analysis to be performed | Excel command used | Numeric result or text-based response |
|---|---|---|
| Calculate a 20% trimmed mean. | `=TRIMMEAN(Sample_250!M2:M251,0.2)` | `-4.3 minutes` |
| Does this trimmed mean represent a significantly different result as compared to the untrimmed mean calculated in Step 2a? | Compare `TRIMMEAN` to `AVERAGE`. | Yes. The trimmed mean is `-4.3 minutes`, while the untrimmed mean is `3.9 minutes`, a difference of about `8.2 minutes`. |
| Explain why the results were significantly different or explain why the results were not significantly different. | Not applicable. | The difference occurs because the sample includes very large positive delays, including a maximum delay of `257` minutes. These extreme late flights pull the untrimmed mean upward. The trimmed mean removes the most extreme values on both ends, so it better reflects the center of the majority of flights. |
| Why would someone want to calculate a trimmed mean instead of using the untrimmed mean? | Not applicable. | A trimmed mean is useful when a dataset contains outliers or strong skewness. It reduces the effect of unusually early or unusually late flights while still using more information than the median alone. |

## Section 4 — Side-by-side boxplots

Paste the side-by-side boxplot into the template from:

```text
tmp/boxplot_seed_41205.png
```

Recommended official Excel action: recreate this chart in Excel using the
seed-41205 sample, then paste the Excel chart into Word.

| Analysis to be performed | Excel command used | Numeric result or text-based response |
|---|---|---|
| Copy and paste the side-by-side boxplot here. | Excel chart: Insert → Statistic Chart → Box and Whisker, using UA and WN `ARR_DELAY` values. | Paste chart. |
| Examine each boxplot separately and comment on the shape of the distribution with respect to symmetric or skewed for each airline. | Not applicable. | Both UA and WN appear right-skewed. In both cases, most flights were near on-time or early, but a few very late flights stretch the upper tail. |
| Are there any outliers shown on the boxplots? If there are any outliers shown on the boxplot, comment on what this indicates with respect to on-time arrivals. Should the airline be concerned? | Not applicable. | Yes. UA has high-delay outliers at `52, 56, 57, 110, 117` minutes. WN has high-delay outliers at `83, 93, 110` minutes. These represent unusually late flights. The airlines should be concerned because even a few very late flights can hurt customers and pull average delay upward. |
| Compare the boxplots for AIRLINE #1 versus AIRLINE #2. Do you observe any significant differences? | Not applicable. | UA has a lower median delay (`-10.0`) than WN (`-1.0`), suggesting better typical performance. WN has a slightly smaller standard deviation, suggesting somewhat more consistency. Both airlines have high positive outliers. |
| Assume you are a manager at AIRLINE #1. State a conclusion based on your analysis of the side-by-side boxplots. | Not applicable. | As a UA manager, I would conclude that typical arrival performance is good because the median flight arrived 10 minutes early. However, the high positive outliers show that UA should investigate the causes of very late flights, especially delays above 100 minutes. |

Boxplot diagnostic table:

| Airline | Q1 | Median | Q3 | IQR | Outliers |
|---|---:|---:|---:|---:|---|
| UA | -22.0 | -10.0 | 6.0 | 28.0 | 52, 56, 57, 110, 117 |
| WN | -11.0 | -1.0 | 16.0 | 27.0 | 83, 93, 110 |

## Section 5 — Pareto chart

Paste the Pareto-style average-delay chart into the template from:

```text
tmp/pareto_seed_41205.png
```

Recommended official Excel action: recreate this as an ordered bar chart in
Excel from the carrier average-delay table, then paste the Excel chart into
Word.

| Analysis to be performed | Excel command used | Numeric result or text-based response |
|---|---|---|
| Copy and paste the Pareto chart. | Build a carrier summary table, sort average `ARR_DELAY` from largest to smallest, then Insert → Bar/Column Chart. | Paste chart. |
| Based on the Pareto chart, which is the worst-performing airline for average on-time arrivals? | `=AVERAGEIF(...)` by carrier, sorted descending. | `B6`, with an average delay of `11.3 minutes`. |
| Based on the Pareto chart, which is the best-performing airline for average on-time arrivals? | `=AVERAGEIF(...)` by carrier, sorted descending. | `AA`, with an average delay of `-2.4 minutes`. |
| What is the benefit of creating a Pareto chart versus a bar chart? | Not applicable. | A Pareto chart orders categories from largest to smallest impact, making the worst-performing airlines easy to identify quickly. |
| Assume you are a manager at the airline with the worst performance. What steps would you investigate to improve on-time arrival? What factors might be within/outside the airline's control? | Not applicable. | As a B6 manager, I would investigate scheduling, turnaround time, staffing, maintenance availability, boarding procedures, and whether certain routes or airports drive most delays. Within-control factors include staffing, scheduling, aircraft readiness, gate operations, and boarding efficiency. Less-controllable factors include weather, air traffic control restrictions, airport congestion, and security disruptions. |

Carrier averages, worst to best:

| Airline | Average delay |
|---|---:|
| B6 | 11.3 |
| DL | 8.2 |
| WN | 7.8 |
| NK | -0.5 |
| UA | -0.8 |
| AA | -2.4 |

## Section 6 — Applying normal distribution

Use:

- Mean = `3.876`
- Standard deviation = `38.0772389823`
- Q1 = `-16.0`
- Q3 = `11.0`

| Analysis to be performed | Excel command used | Numeric result or text-based response |
|---|---|---|
| Calculate the probability that a flight arrives early. | `=NORM.DIST(0,3.876,38.0772389823,TRUE)` | `0.459` |
| Calculate the probability that a flight arrives late. | `=1-NORM.DIST(0,3.876,38.0772389823,TRUE)` | `0.541` |
| Calculate the probability that the on-time arrival of a flight falls between the 1st quartile and 3rd quartile. | `=NORM.DIST(11,3.876,38.0772389823,TRUE)-NORM.DIST(-16,3.876,38.0772389823,TRUE)` | `0.273` |
| Is the result from part (c) reasonable? What is the expected area under the normal curve between the 1st and 3rd quartile? How does your actual numeric result compare? | Not applicable. | For an actual dataset, Q1 to Q3 contains the middle 50%. Under this fitted normal model, the area is only `0.273`, much less than `0.500`. This suggests the arrival-delay data are not very normal and are affected by skewness/outliers. |
| Calculate the probability that the on-time arrival of a flight falls between 2 standard deviations below and above the mean. | `=NORM.DIST(3.876+2*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-2*38.0772389823,3.876,38.0772389823,TRUE)` | `0.954` |
| Is the result from part (e) reasonable? What is the expected area under the normal curve between 2 standard deviations below and above the mean? How does your actual numeric result compare? | Not applicable. | Yes. For a normal distribution, about 95% of values fall within two standard deviations. The computed value, `0.954`, is very close to the expected `0.950`/`0.9545` normal-rule value. |

## Section 7 — Inverse normal distribution

| Analysis to be performed | Excel command used | Numeric result or text-based response |
|---|---|---|
| What on-time arrival delay cuts off the top 10% of the distribution? | `=NORM.INV(0.90,3.876,38.0772389823)` | `52.7 minutes` |
| What on-time arrival delay cuts off the bottom 15% of the distribution? | `=NORM.INV(0.15,3.876,38.0772389823)` | `-35.6 minutes` |

Template note: the instructions may say `INV.NORM`; modern Excel uses
`NORM.INV`.

## Section 8 — Chebyshev's theorem

The Word template says "age of aircraft" in this section, but the Canvas
instructions and project context say this section is about on-time arrival
data. Use on-time-arrival wording in your response unless the instructor tells
you otherwise.

| Analysis to be performed | Excel command used | Numeric result or text-based response |
|---|---|---|
| Using Chebyshev's Theorem, find the probability that the on-time arrival data falls within 3 standard deviations of the mean. Show details. | Not applicable. | Chebyshev: `P(|X - mu| < 3sigma) >= 1 - 1/3^2 = 1 - 1/9 = 8/9 = 0.889`. So at least `0.889` of the data fall within 3 standard deviations. |
| Using the normal distribution, find the probability within 3 standard deviations of the mean. Include Excel command. | `=NORM.DIST(3.876+3*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-3*38.0772389823,3.876,38.0772389823,TRUE)` | `0.997` |
| Compare your results. What do you conclude about Chebyshev's Theorem? | Not applicable. | Chebyshev gives a conservative lower bound that works for any distribution with a finite mean and variance. The normal result is much tighter because it assumes a specific distribution shape. Here Chebyshev guarantees at least `0.889`, while the normal model gives `0.997`. |

## Final human checklist

- Fill in your name at the top of the Word template.
- Paste/recreate the boxplot and Pareto chart.
- Make sure the Excel workbook contains the 250-row sample and formulas.
- Save the Word and Excel files using the course naming convention with your
  first and last name and the activity number/description, with no punctuation
  or special characters.

