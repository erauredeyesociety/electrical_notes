# STAT 412 MD5 Project — Exact Template Fill Map (Seed 41205)

This file follows the PDF template row order exactly. Use it to fill
`STAT_412_Midterm_Project_Template.docx`.

Do not paste this whole document into Word. Instead, copy each row's **Excel
command** into the template's middle column and each **response** into the
right column.

The values below use:

```text
tmp/sample_250_seed_41205.csv
```

Assumed Excel sheet/range after importing the sample:

```text
Sheet name: Sample_250
ARR_DELAY range: Sample_250!M2:M251
UNIQUE_CARRIER range: Sample_250!D2:D251
```

If your actual worksheet name is different, replace `Sample_250` in the formulas
with your sheet name.

## Page 1 — Section 2: Descriptive Statistics

| Row | Excel command used | Numeric result or text-based response |
|---|---|---|
| 2a Mean | `=AVERAGE(Sample_250!M2:M251)` | `3.9 minutes` |
| 2b Median | `=MEDIAN(Sample_250!M2:M251)` | `-6.0 minutes` |
| 2c Standard Deviation | `=STDEV.S(Sample_250!M2:M251)` | `38.1 minutes` |
| 2d Variance | `=VAR.S(Sample_250!M2:M251)` | `1449.9 minutes squared` |
| 2e Minimum | `=MIN(Sample_250!M2:M251)` | `-56.0 minutes` |
| 2f Maximum | `=MAX(Sample_250!M2:M251)` | `257.0 minutes` |
| 2g 1st Quartile | `=QUARTILE.INC(Sample_250!M2:M251,1)` | `-16.0 minutes` |
| 2h 3rd Quartile | `=QUARTILE.INC(Sample_250!M2:M251,3)` | `11.0 minutes` |
| 2i Compare mean results for Airline #1 vs Airline #2 | `=AVERAGEIF(Sample_250!D:D,"UA",Sample_250!M:M)` and `=AVERAGEIF(Sample_250!D:D,"WN",Sample_250!M:M)`; for SD use `=STDEV.S(FILTER(Sample_250!M:M,Sample_250!D:D="UA"))` and same for WN. | Airline #1 = UA; Airline #2 = WN. UA mean delay is `-0.8 minutes` with SD `34.9 minutes`. WN mean delay is `7.8 minutes` with SD `29.7 minutes`. UA has the better average arrival performance because its mean delay is lower, while WN is somewhat more consistent because its SD is smaller. |
| 2j Compare median results for Airline #1 vs Airline #2 | `=MEDIAN(FILTER(Sample_250!M:M,Sample_250!D:D="UA"))` and `=MEDIAN(FILTER(Sample_250!M:M,Sample_250!D:D="WN"))` | UA median delay is `-10.0 minutes`; WN median delay is `-1.0 minute`. A typical UA flight arrived earlier than a typical WN flight in this sample. |

If `FILTER` is not available in your Excel, make a small carrier summary table
instead by filtering/sorting the sample by `UNIQUE_CARRIER`, then apply
`AVERAGE`, `MEDIAN`, and `STDEV.S` to each carrier's `ARR_DELAY` values.

## Page 2 — Section 3: Trimmed Mean

| Row | Excel command used | Numeric result or text-based response |
|---|---|---|
| 3a Calculate a 20% trimmed mean | `=TRIMMEAN(Sample_250!M2:M251,0.2)` | `-4.3 minutes` |
| 3b Does this trimmed mean represent a significantly different result compared to the untrimmed mean? | Compare `=TRIMMEAN(Sample_250!M2:M251,0.2)` with `=AVERAGE(Sample_250!M2:M251)` | Yes. The trimmed mean is `-4.3 minutes`, compared with the untrimmed mean of `3.9 minutes`. The difference is about `8.2 minutes`, which is noticeable for arrival-delay data. |
| 3c Explain why the results were/weren't significantly different | N/A | The results differ because the sample has very large positive delay outliers, including a maximum of `257` minutes. Those unusually late flights pull the ordinary mean upward. The trimmed mean removes extreme values from both ends, so it better reflects the center of most flights. |
| 3d Why use a trimmed mean? | N/A | A trimmed mean is useful when data are skewed or contain outliers. It reduces the effect of extreme delays while still using more of the dataset than the median alone. |

## Page 2–3 — Section 4: Side-by-Side Boxplots

Use Airline #1 = UA and Airline #2 = WN.

Chart file generated for preview:

```text
tmp/boxplot_seed_41205.png
```

Best submission practice: recreate the boxplot in Excel from the sample, then
paste that Excel chart into the Word template. The PNG is a visual reference.

| Row | Excel command used | Numeric result or text-based response |
|---|---|---|
| 4a Copy and paste the side-by-side boxplot | Excel chart menu: Insert → Statistic Chart → Box and Whisker. Use UA and WN `ARR_DELAY` values. | Paste the side-by-side boxplot here. |
| 4b Shape of each airline's distribution | N/A | Both UA and WN appear right-skewed. Most flights are near on-time or early, but a few very late flights create long upper tails. |
| 4c Outliers and concern | N/A | Yes. UA has high-delay outliers at `52, 56, 57, 110, 117` minutes. WN has high-delay outliers at `83, 93, 110` minutes. These are unusually late flights. The airlines should be concerned because even a few very late flights can hurt customers and raise average delay. |
| 4d Significant differences between distributions | N/A | UA has a lower median delay (`-10.0 minutes`) than WN (`-1.0 minute`), so UA has better typical performance. WN has slightly less spread by SD (`29.7` vs. `34.9`), so WN is somewhat more consistent. Both distributions have high positive outliers. |
| 4e Manager conclusion for Airline #1 | N/A | As a UA manager, I would conclude that typical performance is good because the median UA flight arrived 10 minutes early. However, the high-delay outliers show that UA should investigate causes of very late flights, especially delays above 100 minutes. |

Diagnostic values:

| Airline | Q1 | Median | Q3 | IQR | Outliers |
|---|---:|---:|---:|---:|---|
| UA | -22.0 | -10.0 | 6.0 | 28.0 | 52, 56, 57, 110, 117 |
| WN | -11.0 | -1.0 | 16.0 | 27.0 | 83, 93, 110 |

## Page 3–4 — Section 5: Pareto Chart

Chart file generated for preview:

```text
tmp/pareto_seed_41205.png
```

Best submission practice: recreate this in Excel as a sorted bar chart of
average arrival delay by carrier.

| Row | Excel command used | Numeric result or text-based response |
|---|---|---|
| 5a Copy and paste the Pareto chart | Create carrier average-delay table using `AVERAGEIF`; sort largest to smallest; Insert → Column/Bar Chart. | Paste the Pareto chart here. |
| 5b Worst-performing airline | Use sorted carrier averages. | `B6` is worst, with average delay `11.3 minutes`. |
| 5c Best-performing airline | Use sorted carrier averages. | `AA` is best, with average delay `-2.4 minutes`. |
| 5d Benefit of Pareto chart vs bar chart | N/A | A Pareto chart orders categories from largest to smallest impact, making the worst performers easy to identify quickly. |
| 5e Manager response for worst airline | N/A | As a B6 manager, I would investigate scheduling, aircraft turnaround time, staffing, maintenance availability, boarding procedures, and whether particular routes or airports drive most delays. Within-control factors include staffing, scheduling, aircraft readiness, gate operations, and boarding efficiency. Less-controllable factors include weather, air traffic control restrictions, airport congestion, and security disruptions. |

Carrier averages, worst to best:

| Airline | Average delay |
|---|---:|
| B6 | 11.3 |
| DL | 8.2 |
| WN | 7.8 |
| NK | -0.5 |
| UA | -0.8 |
| AA | -2.4 |

## Page 4–5 — Section 6: Applying Normal Distribution

Use these values from Section 2:

```text
mean = 3.876
standard deviation = 38.0772389823
Q1 = -16.0
Q3 = 11.0
```

The template asks for probabilities rounded to three decimal places.

| Row | Excel command used | Numeric result or text-based response |
|---|---|---|
| 6a Probability that a flight arrives early | `=NORM.DIST(0,3.876,38.0772389823,TRUE)` | `0.459` |
| 6b Probability that a flight arrives late | `=1-NORM.DIST(0,3.876,38.0772389823,TRUE)` | `0.541` |
| 6c Probability arrival delay falls between Q1 and Q3 | `=NORM.DIST(11,3.876,38.0772389823,TRUE)-NORM.DIST(-16,3.876,38.0772389823,TRUE)` | `0.273` |
| 6d Is result from 6c reasonable? | N/A | For the actual sample, Q1 to Q3 contains the middle 50% of observations. Under this fitted normal model, the area is only `0.273`, much less than `0.500`. This suggests the arrival-delay data are not very normal and are affected by skewness/outliers. |
| 6e Probability arrival delay falls within 2 SD of the mean | `=NORM.DIST(3.876+2*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-2*38.0772389823,3.876,38.0772389823,TRUE)` | `0.954` |
| 6f Is result from 6e reasonable? | N/A | Yes. For a normal distribution, about 95% of values fall within two standard deviations of the mean. The computed value `0.954` is very close to the expected normal-rule area. |

## Page 5 — Section 7: Inverse Normal Distribution

The template/instructions may call this `INV.NORM`, but modern Excel uses
`NORM.INV`.

| Row | Excel command used | Numeric result or text-based response |
|---|---|---|
| 7a Arrival delay cutting off top 10% | `=NORM.INV(0.90,3.876,38.0772389823)` | `52.7 minutes`. Under the normal model, about 10% of flights have delays greater than this. |
| 7b Arrival delay cutting off bottom 15% | `=NORM.INV(0.15,3.876,38.0772389823)` | `-35.6 minutes`. Under the normal model, about 15% of flights arrive more than 35.6 minutes early. |

## Page 6 — Section 8: Chebyshev's Theorem

Important wording note: the PDF template says "age of aircraft" in Section 8,
but the Canvas instructions and the rest of the project say the analysis is
about on-time arrival delay. If you want to follow the template literally, you
can leave "age of aircraft" in the prompt row, but the response should be based
on the Section 2 mean and standard deviation for arrival delay.

Recommended wording below uses "arrival delay" because that matches the project
instructions.

| Row | Excel command used | Numeric result or text-based response |
|---|---|---|
| 8a Chebyshev probability within 3 SD | N/A | Chebyshev's theorem gives `P(|X - mu| < 3sigma) >= 1 - 1/3^2 = 1 - 1/9 = 8/9 = 0.889`. Therefore, at least `0.889` of the arrival-delay values fall within 3 standard deviations of the mean. |
| 8b Normal probability within 3 SD | `=NORM.DIST(3.876+3*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-3*38.0772389823,3.876,38.0772389823,TRUE)` | `0.997` |
| 8c Compare Chebyshev and normal results | N/A | Chebyshev gives a conservative lower bound that works for any distribution with finite mean and variance. The normal result is much tighter because it assumes a specific normal shape. Here Chebyshev guarantees at least `0.889`, while the normal model gives `0.997`. |

## Final check before submission

- Name is already visible in the PDF version as `Gatlin Nelson`; confirm it is
  filled in correctly in the editable DOCX.
- Make sure the Excel workbook includes the seed-41205 250-row sample.
- Make sure formulas are visible in the workbook or can be checked from formula
  cells.
- Paste/recreate both required charts:
  - side-by-side boxplot for UA vs WN
  - Pareto-style ordered carrier average-delay chart
- Submit both the completed Word document and Excel workbook.

