# STAT 412 Final Project Status

## Current state

- Original `.docx` and `.xlsx` files have not been edited.
- Source CSVs have been read successfully.
- Reproducible analysis script created:
  - `scripts/analyze_final_project.py`
- Working Markdown files created:
  - `project_instructions.md`
  - `project_setup_summary.md`
  - `analysis_results.md`
  - `final_report_draft.md`
- Clean generated CSV outputs created:
  - `outputs/final_project_random_sample_250.csv`
  - `outputs/final_project_calculations.csv`
  - `outputs/final_project_carrier_summary.csv`

## Random sample

- Seed: `412`
- Sample size: `250`
- Carrier counts in sample:
  - AA: 46
  - B6: 39
  - DL: 43
  - NK: 42
  - UA: 38
  - WN: 42

## Completed draft calculations

- Section 1, CI for mean:
  - sample mean arrival delay: `4.7` minutes
  - 95% CI: `(-0.5, 10.0)` minutes
- Section 2, CI for proportion:
  - late definition: `ARR_DELAY > 10`
  - late count: `61/250`
  - point estimate: `24.4%`
  - 95% CI: `(19.1%, 29.7%)`
- Section 3, one-sample mean test:
  - \(H_0:\mu\ge8\), \(H_1:\mu<8\)
  - \(t=-1.2\), p-value `0.1124`
  - decision: do not reject \(H_0\)
- Section 4, one-sample proportion test:
  - \(H_0:p\ge0.28\), \(H_1:p<0.28\)
  - \(z=-1.3\), p-value `0.1024`
  - decision: do not reject \(H_0\)

## Pending before final `.docx`

- Need the student's first and last initials, or explicit selected airline codes,
  for Section 5.
- After Section 5 is complete, create a copy of
  `STAT 412 Final Project Template.docx` with the final report filename and fill
  that copy only.
