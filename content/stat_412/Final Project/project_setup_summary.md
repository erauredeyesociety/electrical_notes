# STAT 412 Final Project Setup Summary

## Working files

- Source dataset: `Dataset_STAT412_Project_Final(ArrivalData).csv`
- Data dictionary: `Dataset_STAT412_Project_Final(Data Dictionary).csv`
- Original template: `STAT 412 Final Project Template.docx`
- Original printable instructions: `STAT 412 Printable Final Project Instructions.pdf`
- Analysis script: `scripts/analyze_final_project.py`

## Generated outputs

The analysis script writes:

- `outputs/final_project_random_sample_250.csv`
- `outputs/final_project_calculations.csv`
- `outputs/final_project_carrier_summary.csv`
- `outputs/final_project_airline_samples.csv` if two airline codes are supplied
- `analysis_results.md`
- `final_report_draft.md`

## Reproducible sample

The random sample uses seed `412` by default. This creates a stable 250-row
sample and stores each row's generated `RANDOM_VALUE`, which mimics the Excel
`=RAND()` + paste-values + sort workflow without the sample changing later.

Run the base analysis:

```bash
python3 scripts/analyze_final_project.py
```

Run the base analysis with airline codes:

```bash
python3 scripts/analyze_final_project.py --airline-1 AA --airline-2 DL
```

Replace `AA` and `DL` with the selected airline codes after the student's first
and last initials are known.

## Rounding convention

The instructions say to round all answers to one decimal place unless otherwise
specified. This project therefore reports:

- mean delays and confidence interval endpoints to one decimal place;
- proportions as percentages to one decimal place;
- p-values to four decimals for clarity.

## Completion rule

Do not edit the original `.docx` or `.xlsx`. Once all analyses are final and the
airline selection is confirmed, make a copy of the Word template with the final
report filename, then fill that copy.
