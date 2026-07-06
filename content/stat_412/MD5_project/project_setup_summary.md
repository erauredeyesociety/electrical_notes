# STAT 412 MD5 Project — Setup Summary and Work Plan

## Current folder status

Original files preserved:

- `STAT 412 Printable Midterm Project Instructions.docx`
- `Dataset_STAT412_Project_Final.xlsx`
- `STAT_412_Midterm_Project_Template.docx`

Safe working files available:

- `project_instructions.md` — clean Markdown conversion of the project
  instructions.
- `project_completion_guide.md` — project-control document: what complete
  looks like, what is automatable, and what the human still needs to do in
  Word/Excel.
- `project_answer_draft_seed_41205.md` — copy-ready draft answers using the
  reproducible seed-41205 sample.
- `project_template_fill_guide_seed_41205.md` — table-aligned Markdown guide for
  filling the Word template without editing the DOCX from Codex.
- `project_template_exact_fill_seed_41205.md` — tighter row-by-row fill map
  based on the PDF version of the Word template.
- `build_midterm_submission.py` — repeatable builder for the completed Excel
  workbook and completed Word template.
- `STAT412_MD5_Project_Workbook_seed_41205.xlsx` — generated workbook with the
  sample, formulas, calculations, chart support, and template-answer sheet.
- `STAT412_MD5_Project_Workbook_seed_41205_SAFE.xlsx` — same workbook rebuilt
  in a safer Excel-compatible form after Excel reported repair/#NAME issues.
  The non-`SAFE` workbook filename now also contains this safe rebuilt content.
- `STAT412_MD5_Project_Workbook_seed_41205_VALUES_ONLY.xlsx` — most compatible
  workbook: no live formulas, only formula text plus fixed computed results.
  The non-`SAFE` workbook filename now contains this values-only version.
- `STAT412_MD5_Project_Template_Completed_seed_41205.docx` — generated completed
  Word template with answers and chart images.
- `STAT412_MD5_Project_Template_Completed_placeholders_seed_41205.docx` —
  generated completed Word template with text placeholders for manual chart
  insertion.
- `md5_boxplot_UA_WN_seed_41205.png` and
  `md5_pareto_airline_avg_delay_seed_41205.png` — standalone chart images for
  drag/drop insertion if desired.
- `Dataset_STAT412_Project_Final(ArrivalData).csv` — exported arrival-data sheet.
- `Dataset_STAT412_Project_Final(Data Dictionary).csv` — exported data
  dictionary.
- `project05_helper.py` — optional read-only Python helper that writes scratch
  outputs to `tmp/`.
- `tmp/` — disposable generated outputs; ignored except for `tmp/.gitignore`.

The arrival-data CSV has 1,756 rows and 17 columns. There are no missing
`ARR_DELAY` values in the exported CSV.

Carrier counts in the full exported data:

| Carrier | Rows |
|---|---:|
| AA | 298 |
| B6 | 291 |
| DL | 296 |
| NK | 287 |
| UA | 296 |
| WN | 288 |

## What you need to submit

Submit both:

1. The completed Word template.
2. An Excel workbook showing the sample, formulas, calculations, and graphs.

The safest workflow is to keep the original XLSX untouched and make a working
copy for the submitted Excel file.

## Big picture checklist

1. Make a working Excel copy.
2. Randomly select 250 rows.
3. Compute descriptive statistics for `ARR_DELAY`.
4. Choose two airlines and compare their center/spread.
5. Compute and interpret the 20% trimmed mean.
6. Build side-by-side boxplots for the two chosen airlines.
7. Build a Pareto-style chart of average arrival delay by airline.
8. Use the sample mean and sample standard deviation for normal-distribution
   probability questions.
9. Use inverse normal formulas for percentile cutoff questions.
10. Compare Chebyshev's theorem with normal-distribution probabilities.

## Recommended Excel formulas

Assume the 250 sampled `ARR_DELAY` values are in `M2:M251`. Adjust the range if
your working sheet differs.

| Task | Excel formula |
|---|---|
| Mean | `=AVERAGE(M2:M251)` |
| Median | `=MEDIAN(M2:M251)` |
| Sample standard deviation | `=STDEV.S(M2:M251)` |
| Sample variance | `=VAR.S(M2:M251)` |
| Minimum | `=MIN(M2:M251)` |
| Maximum | `=MAX(M2:M251)` |
| 1st quartile | `=QUARTILE.INC(M2:M251,1)` |
| 3rd quartile | `=QUARTILE.INC(M2:M251,3)` |
| 20% trimmed mean | `=TRIMMEAN(M2:M251,0.2)` |

For Section 6, let:

- `mean` = Section 2(a)
- `sd` = Section 2(c)
- `Q1` = Section 2(g)
- `Q3` = Section 2(h)

Normal distribution formulas:

| Question | Formula idea |
|---|---|
| P(arrives early) | `=NORM.DIST(0, mean, sd, TRUE)` |
| P(arrives late) | `=1-NORM.DIST(0, mean, sd, TRUE)` |
| P(Q1 < X < Q3) | `=NORM.DIST(Q3, mean, sd, TRUE)-NORM.DIST(Q1, mean, sd, TRUE)` |
| P(mean-2sd < X < mean+2sd) | `=NORM.DIST(mean+2*sd, mean, sd, TRUE)-NORM.DIST(mean-2*sd, mean, sd, TRUE)` |
| Top 10% cutoff | `=NORM.INV(0.90, mean, sd)` |
| Bottom 15% cutoff | `=NORM.INV(0.15, mean, sd)` |
| Within 3 sd, normal | `=NORM.DIST(mean+3*sd, mean, sd, TRUE)-NORM.DIST(mean-3*sd, mean, sd, TRUE)` |

Note: the instruction document says `INV.NORM`, but modern Excel uses
`NORM.INV`.

Chebyshev for within 3 standard deviations:

\[
P(|X-\mu|<3\sigma)\ge 1-\frac{1}{3^2}=\frac{8}{9}\approx0.889.
\]

For a normal distribution, the area within 3 standard deviations is about
`0.997`.

## Interpretation notes to keep handy

- `ARR_DELAY < 0`: early arrival.
- `ARR_DELAY = 0`: exactly on time.
- `ARR_DELAY > 0`: late arrival.
- Higher mean/median delay means worse on-time performance.
- Larger standard deviation means less consistent arrival performance.
- A right-skewed distribution usually means most flights are early/on-time, but
  a few very late flights pull the mean upward.
- A trimmed mean is useful when outliers or extreme delays distort the regular
  mean.
- A Pareto chart is useful because it orders categories by impact, making the
  worst performers immediately visible.
- Chebyshev works for any distribution, so it gives a conservative lower bound.
  The normal rule is more specific and usually gives a much tighter probability.

## Optional Python preview helper

Run from the repository root:

```bash
python3 content/stat_412/MD5_project/project05_helper.py --seed 41205
```

Outputs go to:

```text
content/stat_412/MD5_project/tmp/
```

The helper creates:

- `sample_250_seed_41205.csv`
- `descriptive_stats_seed_41205.csv`
- `airline_summary_seed_41205.csv`
- `boxplot_diagnostics_seed_41205.csv`
- `normal_calculations_seed_41205.csv`
- `boxplot_seed_41205.png`
- `pareto_seed_41205.png`

Preview results from seed `41205`:

| Statistic | Value |
|---|---:|
| Mean | 3.9 min |
| Median | -6.0 min |
| Standard deviation | 38.1 min |
| Variance | 1449.9 min² |
| Minimum | -56.0 min |
| Maximum | 257.0 min |
| 1st quartile | -16.0 min |
| 3rd quartile | 11.0 min |
| 20% trimmed mean | -4.3 min |

Those numbers are now written up in `project_answer_draft_seed_41205.md`. Use
them as the official project numbers only if you use the exact saved sample
`tmp/sample_250_seed_41205.csv` in the submitted Excel workbook. If Excel's
`RAND()` produces a different 250-row sample, your submitted numbers should
differ.

For the preview seed, the helper selected UA and WN for the side-by-side boxplot
because they were the two largest groups in that sample.

## Suggested next step

Recommended: review the generated completed files:

- `STAT412_MD5_Project_Workbook_seed_41205.xlsx`
- `STAT412_MD5_Project_Template_Completed_seed_41205.docx`
- `STAT412_MD5_Project_Template_Completed_placeholders_seed_41205.docx` if you
  prefer manual chart insertion.

Alternative: choose a new official sample with Excel's `RAND()` method:

- Use Excel's `RAND()` method exactly as described in the instructions.
- Recompute every value from the new sample.
- Keep the written explanations from the draft, but update the numbers and
  carrier conclusions.

Once the official sample is chosen, all numerical answers in the Word template
and Excel workbook must come from that exact 250-row sample.
