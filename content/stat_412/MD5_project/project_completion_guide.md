# STAT 412 MD5 Project — Completion Guide

This is the project-control document for finishing the Module 5 midterm without
touching the original Word or Excel downloads.

Original files to preserve:

- `STAT 412 Printable Midterm Project Instructions.docx`
- `Dataset_STAT412_Project_Final.xlsx`
- `STAT_412_Midterm_Project_Template.docx`

Safe working files:

- `Dataset_STAT412_Project_Final(ArrivalData).csv`
- `Dataset_STAT412_Project_Final(Data Dictionary).csv`
- `project_instructions.md`
- `project_setup_summary.md`
- `project05_helper.py`
- `project_answer_draft_seed_41205.md`
- `project_template_fill_guide_seed_41205.md`
- `project_template_exact_fill_seed_41205.md`
- `build_midterm_submission.py`

Generated completed files:

- `STAT412_MD5_Project_Workbook_seed_41205.xlsx`
- `STAT412_MD5_Project_Workbook_seed_41205_SAFE.xlsx`
- `STAT412_MD5_Project_Workbook_seed_41205_VALUES_ONLY.xlsx`
- `STAT412_MD5_Project_Template_Completed_seed_41205.docx`
- `STAT412_MD5_Project_Template_Completed_placeholders_seed_41205.docx`
- `md5_boxplot_UA_WN_seed_41205.png`
- `md5_pareto_airline_avg_delay_seed_41205.png`

## Recommended working decision

Use the reproducible Python sample with seed `41205` as the official 250-row
sample unless the instructor specifically requires Excel's volatile `RAND()`
method. The instructions allow any random selection method, and this method is
auditable because the exact sample is saved as:

```text
tmp/sample_250_seed_41205.csv
```

If you instead choose an Excel `RAND()` sample, the written interpretations and
Excel workflow still apply, but every numeric answer must be recalculated from
that different sample.

## What “complete” looks like

The submission should contain two files:

1. A completed Word template with answers for Sections 2--8 and embedded chart
   images:
   `STAT412_MD5_Project_Template_Completed_seed_41205.docx`.
   If you prefer to drag/drop charts manually, use the placeholder version:
   `STAT412_MD5_Project_Template_Completed_placeholders_seed_41205.docx`.
2. An Excel workbook showing calculations, formula text, fixed results, and
   chart support:
   `STAT412_MD5_Project_Workbook_seed_41205.xlsx`.
   This file has been rebuilt as a values-only workbook after Excel reported
   compatibility issues with live formulas. Formula columns are plain text and
   result columns are fixed computed values, so there are zero live formulas to
   break. The identical values-only copy is
   `STAT412_MD5_Project_Workbook_seed_41205_VALUES_ONLY.xlsx`.

The generated Excel workbook includes:
   - The 250-row sample.
   - Descriptive statistics for `ARR_DELAY`.
   - Airline comparison calculations.
   - Side-by-side boxplot.
   - Pareto-style average-delay chart.
   - Normal-distribution and inverse-normal formulas.
   - Chebyshev calculation.

## Automatable work already done

- Converted project instructions to Markdown.
- Preserved the original Word and Excel files untouched.
- Read the CSV export of the arrival data.
- Built a reproducible 250-row sample using seed `41205`.
- Computed descriptive statistics, trimmed mean, carrier summaries, normal
  probabilities, inverse-normal cutoffs, Chebyshev values, and boxplot outlier
  diagnostics.
- Generated preview charts:
  - `tmp/boxplot_seed_41205.png`
  - `tmp/pareto_seed_41205.png`
- Drafted copy-ready answers in `project_answer_draft_seed_41205.md`.

## Human-required work

The generated files are ready for review. Before submitting:

1. Open the completed Word document and completed workbook.
2. Check that the chart images and tables display correctly on your machine.
3. If chart formatting is awkward, use the placeholder Word version and manually
   insert:
   - `md5_boxplot_UA_WN_seed_41205.png`
   - `md5_pareto_airline_avg_delay_seed_41205.png`
4. If your instructor requires Excel-native charts instead of inserted images,
   recreate the side-by-side boxplot from `Boxplot_Data` and the Pareto chart
   from `Carrier_Comparison`, then paste those Excel charts into Word.
5. Save both files using the required course naming convention with your first
   and last name and the activity number/description, with no punctuation or
   special characters.
6. Submit both the Word document and Excel workbook.

## Recommended workbook layout

Use separate sheets in the working workbook:

| Sheet | Purpose |
|---|---|
| `Sample_250` | Paste/import `tmp/sample_250_seed_41205.csv`. |
| `Descriptive_Stats` | Section 2 and Section 3 formulas. |
| `Carrier_Comparison` | Mean/median/standard deviation by carrier. |
| `Charts` | Side-by-side boxplot and Pareto chart. |
| `Normal_Calcs` | Sections 6--8 formulas. |

## Reproducibility note for the Word template

Use wording like this in Section 1:

> I selected a random sample of 250 rows from the arrival-data CSV using a
> reproducible random seed of 41205. The sample was then used for all
> calculations and charts.

This makes the sample method clear and auditable.

## If numbers disagree between Python and Excel

Check these first:

- Excel should use `STDEV.S` and `VAR.S`, not population versions.
- Quartiles should use `QUARTILE.INC`.
- The 20% trimmed mean should use `TRIMMEAN(range,0.2)`.
- The sample must contain exactly the same 250 rows as
  `tmp/sample_250_seed_41205.csv`.
- The `ARR_DELAY` column must be numeric and must not include the header row in
  formula ranges.
