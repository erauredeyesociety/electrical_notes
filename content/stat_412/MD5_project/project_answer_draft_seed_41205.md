# STAT 412 MD5 Project — Answer Draft Using Seed 41205

This draft uses the reproducible 250-row sample saved at:

```text
tmp/sample_250_seed_41205.csv
```

Use these answers only if that exact sample is used in the official Excel
workbook. If a different Excel `RAND()` sample is used, recompute all numeric
answers from that sample.

## Section 1 — Sample selection

Copy-ready wording:

> I selected a random sample of 250 rows from the arrival-data CSV using a
> reproducible random seed of 41205. The analysis focuses on `ARR_DELAY`, the
> difference in minutes between scheduled and actual arrival time. Negative
> values indicate early arrivals and positive values indicate late arrivals.

## Section 2 — Descriptive statistics

For the 250 sampled `ARR_DELAY` values:

| Item | Value |
|---|---:|
| Mean | 3.9 minutes |
| Median | -6.0 minutes |
| Standard deviation | 38.1 minutes |
| Variance | 1449.9 minutes² |
| Minimum | -56.0 minutes |
| Maximum | 257.0 minutes |
| 1st quartile | -16.0 minutes |
| 3rd quartile | 11.0 minutes |

Excel formulas, assuming `ARR_DELAY` is in `M2:M251`:

| Item | Excel formula |
|---|---|
| Mean | `=AVERAGE(M2:M251)` |
| Median | `=MEDIAN(M2:M251)` |
| Standard deviation | `=STDEV.S(M2:M251)` |
| Variance | `=VAR.S(M2:M251)` |
| Minimum | `=MIN(M2:M251)` |
| Maximum | `=MAX(M2:M251)` |
| 1st quartile | `=QUARTILE.INC(M2:M251,1)` |
| 3rd quartile | `=QUARTILE.INC(M2:M251,3)` |

### Section 2(i) — Airline #1 vs. Airline #2 mean and standard deviation

Suggested airline comparison: UA vs. WN. These were the two largest carrier
groups in the seed-41205 sample, with 45 rows each.

| Airline | Count | Mean delay | Standard deviation |
|---|---:|---:|---:|
| UA | 45 | -0.8 minutes | 34.9 minutes |
| WN | 45 | 7.8 minutes | 29.7 minutes |

Copy-ready conclusion:

> UA had the lower average arrival delay, with a mean of -0.8 minutes compared
> with WN's mean of 7.8 minutes. This means UA flights in this sample arrived
> slightly early on average, while WN flights arrived late by about 7.8 minutes
> on average. WN had the smaller standard deviation, so its arrival-delay values
> were somewhat more consistent than UA's.

### Section 2(j) — Median comparison

| Airline | Median delay |
|---|---:|
| UA | -10.0 minutes |
| WN | -1.0 minutes |

Copy-ready conclusion:

> The median delay for UA was -10.0 minutes, while the median delay for WN was
> -1.0 minute. Based on the median, a typical UA flight in this sample arrived
> earlier than a typical WN flight.

## Section 3 — Trimmed mean

20% trimmed mean:

```text
-4.3 minutes
```

Excel formula:

```excel
=TRIMMEAN(M2:M251,0.2)
```

Copy-ready answers:

> The 20% trimmed mean is -4.3 minutes.

> The trimmed mean is noticeably different from the untrimmed mean of 3.9
> minutes. The difference is about 8.2 minutes.

> The difference occurs because the data include very large positive delays,
> such as the maximum delay of 257 minutes. These extreme late flights pull the
> ordinary mean upward. The 20% trimmed mean removes the most extreme values on
> both ends, so it better reflects the center of the majority of flights.

> A trimmed mean is useful when a dataset contains outliers or strong skewness.
> It reduces the effect of unusually early or unusually late flights while still
> using more information than the median alone.

## Section 4 — Side-by-side boxplots

Chart preview:

```text
tmp/boxplot_seed_41205.png
```

Suggested airline comparison: UA vs. WN.

Boxplot diagnostics:

| Airline | Q1 | Median | Q3 | IQR | Outliers by 1.5×IQR rule |
|---|---:|---:|---:|---:|---|
| UA | -22.0 | -10.0 | 6.0 | 28.0 | 52, 56, 57, 110, 117 |
| WN | -11.0 | -1.0 | 16.0 | 27.0 | 83, 93, 110 |

Copy-ready answers:

> Both UA and WN appear right-skewed. In both cases, most flights were near
> on-time or early, but a few very late flights stretch the upper tail.

> Both boxplots show high positive outliers. These outliers represent flights
> that arrived much later than the typical flight for that airline. The airline
> should be concerned because even a small number of very late flights can hurt
> customer satisfaction and increase the average delay.

> UA has a lower median delay (-10.0 minutes) than WN (-1.0 minute), which
> suggests UA performed better for a typical flight in this sample. WN has a
> slightly smaller spread by standard deviation, but both airlines show high
> late-arrival outliers.

> As a manager at UA, I would conclude that typical arrival performance is good
> because the median flight arrived 10 minutes early. However, the high positive
> outliers show that UA should still investigate the causes of very late flights,
> especially delays of 110 minutes or more.

## Section 5 — Pareto chart

Chart preview:

```text
tmp/pareto_seed_41205.png
```

Average arrival delay by airline, ordered worst to best:

| Airline | Average delay |
|---|---:|
| B6 | 11.3 minutes |
| DL | 8.2 minutes |
| WN | 7.8 minutes |
| NK | -0.5 minutes |
| UA | -0.8 minutes |
| AA | -2.4 minutes |

Copy-ready answers:

> The worst-performing airline by average arrival delay is B6, with an average
> delay of 11.3 minutes.

> The best-performing airline by average arrival delay is AA, with an average
> delay of -2.4 minutes.

> A Pareto chart is useful because it orders categories from largest to smallest
> impact. This makes it easier to identify the worst-performing airlines quickly
> compared with a regular unordered bar chart.

> As a manager at B6, I would investigate delay causes such as scheduling,
> turnaround time, staffing, maintenance availability, boarding procedures, and
> whether certain routes or airports are responsible for most of the delays.
> Factors more directly within the airline's control include staffing,
> scheduling, aircraft readiness, gate operations, and boarding efficiency.
> Factors less directly within the airline's control include weather, air
> traffic control restrictions, airport congestion, and security disruptions.

## Section 6 — Applying the normal distribution

Use:

- Mean = 3.876 minutes
- Standard deviation = 38.0772389823 minutes
- Q1 = -16.0 minutes
- Q3 = 11.0 minutes

Rounded answers:

| Part | Question | Value |
|---|---|---:|
| a | Probability flight arrives early, `P(X < 0)` | 0.459 |
| b | Probability flight arrives late, `P(X > 0)` | 0.541 |
| c | Probability between Q1 and Q3 | 0.273 |
| e | Probability within 2 standard deviations of mean | 0.954 |

Excel formulas:

```excel
=NORM.DIST(0,3.876,38.0772389823,TRUE)
=1-NORM.DIST(0,3.876,38.0772389823,TRUE)
=NORM.DIST(11,3.876,38.0772389823,TRUE)-NORM.DIST(-16,3.876,38.0772389823,TRUE)
=NORM.DIST(3.876+2*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-2*38.0772389823,3.876,38.0772389823,TRUE)
```

Copy-ready reasoning:

> The probability of arriving early is 0.459, and the probability of arriving
> late is 0.541 under the normal model.

> The probability of falling between the sample first and third quartiles is
> 0.273. For an actual dataset, the first and third quartiles contain the middle
> 50% of observations. Under this fitted normal model, however, the sample
> quartile cutoffs are much closer to the mean than the theoretical normal first
> and third quartiles would be, so the normal-model area is only 0.273. This
> suggests the arrival-delay data are not very normal and are affected by
> skewness/outliers.

> The probability of falling within two standard deviations of the mean is
> 0.954. This is reasonable because for any normal distribution the empirical
> rule gives about 95% within two standard deviations.

## Section 7 — Inverse normal distribution

Rounded answers:

| Part | Question | Value |
|---|---|---:|
| a | Delay cutoff for the top 10% | 52.7 minutes |
| b | Delay cutoff for the bottom 15% | -35.6 minutes |

Excel formulas:

```excel
=NORM.INV(0.90,3.876,38.0772389823)
=NORM.INV(0.15,3.876,38.0772389823)
```

Copy-ready wording:

> The top 10% cutoff is 52.7 minutes. Under the normal model, about 10% of
> flights are expected to have arrival delays greater than 52.7 minutes.

> The bottom 15% cutoff is -35.6 minutes. Under the normal model, about 15% of
> flights are expected to arrive earlier than 35.6 minutes before the scheduled
> arrival time.

## Section 8 — Chebyshev's theorem

Chebyshev calculation for within 3 standard deviations:

\[
P(|X-\mu|<3\sigma)\ge 1-\frac{1}{3^2}
=1-\frac{1}{9}
=\frac{8}{9}
\approx 0.889.
\]

Normal-distribution calculation:

```excel
=NORM.DIST(3.876+3*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-3*38.0772389823,3.876,38.0772389823,TRUE)
```

Normal result:

```text
0.997
```

Copy-ready comparison:

> Chebyshev's theorem says that at least 0.889 of the data must fall within
> three standard deviations of the mean, regardless of distribution shape. The
> normal model gives a much larger probability, 0.997, within three standard
> deviations. This shows that Chebyshev's theorem is very general but
> conservative. It is useful when the distribution shape is unknown or skewed,
> but it does not give as tight of a result as the normal model when a normal
> assumption is used.

