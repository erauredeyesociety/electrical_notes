#!/usr/bin/env python3
"""Build completed STAT 412 Module 5 project workbook and Word document.

This script preserves the original downloaded Word/Excel files. It reads the
reproducible seed-41205 CSV/sample outputs and creates new completed working
files:

- STAT412_MD5_Project_Workbook_seed_41205_SAFE.xlsx
- STAT412_MD5_Project_Template_Completed_seed_41205.docx
"""

from __future__ import annotations

import math
from pathlib import Path

import pandas as pd
import xlsxwriter
from docx import Document
from docx.shared import Inches, Pt


ROOT = Path(__file__).resolve().parent
TMP = ROOT / "tmp"
SAMPLE = TMP / "sample_250_seed_41205.csv"
BOXPLOT = TMP / "boxplot_seed_41205.png"
PARETO = TMP / "pareto_seed_41205.png"
TEMPLATE = ROOT / "STAT_412_Midterm_Project_Template.docx"
OUT_XLSX = ROOT / "STAT412_MD5_Project_Workbook_seed_41205_SAFE.xlsx"
OUT_DOCX = ROOT / "STAT412_MD5_Project_Template_Completed_seed_41205.docx"


def build_excel() -> None:
    df = pd.read_csv(SAMPLE)

    workbook = xlsxwriter.Workbook(OUT_XLSX, {"strings_to_formulas": False})
    workbook.set_properties(
        {
            "title": "STAT 412 Module 5 Midterm Project Workbook",
            "subject": "Seed 41205 reproducible sample and calculations",
            "author": "Gatlin Nelson",
        }
    )

    fmt_header = workbook.add_format({"bold": True, "bg_color": "#D9EAF7", "border": 1})
    fmt_subheader = workbook.add_format({"bold": True, "bg_color": "#E2F0D9", "border": 1})
    fmt_cell = workbook.add_format({"border": 1})
    fmt_num1 = workbook.add_format({"border": 1, "num_format": "0.0"})
    fmt_num3 = workbook.add_format({"border": 1, "num_format": "0.000"})
    fmt_num = workbook.add_format({"border": 1, "num_format": "0.000000"})
    fmt_note = workbook.add_format({"text_wrap": True, "valign": "top"})
    fmt_wrap = workbook.add_format({"border": 1, "text_wrap": True, "valign": "top"})

    # Sample data.
    ws = workbook.add_worksheet("Sample_250")
    for c, name in enumerate(df.columns):
        ws.write(0, c, name, fmt_header)
    for r, row in enumerate(df.itertuples(index=False), start=1):
        for c, value in enumerate(row):
            ws.write(r, c, value, fmt_cell)
    ws.freeze_panes(1, 0)
    ws.autofilter(0, 0, len(df), len(df.columns) - 1)
    ws.set_column(0, len(df.columns) - 1, 12)
    ws.set_column(3, 3, 16)
    ws.set_column(12, 12, 12)

    # Descriptive statistics and trimmed mean.
    ws = workbook.add_worksheet("Descriptive_Stats")
    ws.write_row(0, 0, ["Statistic", "Excel formula", "Result"], fmt_header)
    desc_rows = [
        ("Mean", '=AVERAGE(Sample_250!M2:M251)', 3.876, "0.0"),
        ("Median", '=MEDIAN(Sample_250!M2:M251)', -6.0, "0.0"),
        ("Standard Deviation", '=STDEV.S(Sample_250!M2:M251)', 38.07723898228516, "0.0"),
        ("Variance", '=VAR.S(Sample_250!M2:M251)', 1449.8761285140563, "0.0"),
        ("Minimum", '=MIN(Sample_250!M2:M251)', -56.0, "0.0"),
        ("Maximum", '=MAX(Sample_250!M2:M251)', 257.0, "0.0"),
        ("1st Quartile", '=QUARTILE.INC(Sample_250!M2:M251,1)', -16.0, "0.0"),
        ("3rd Quartile", '=QUARTILE.INC(Sample_250!M2:M251,3)', 11.0, "0.0"),
        ("20% Trimmed Mean", '=TRIMMEAN(Sample_250!M2:M251,0.2)', -4.3133333333333335, "0.0"),
    ]
    for r, (label, formula, value, _) in enumerate(desc_rows, start=1):
        ws.write(r, 0, label, fmt_cell)
        ws.write_string(r, 1, formula, fmt_cell)
        ws.write_formula(r, 2, formula, fmt_num1, value)
    ws.set_column(0, 0, 24)
    ws.set_column(1, 1, 42)
    ws.set_column(2, 2, 16)
    ws.write(12, 0, "Notes", fmt_subheader)
    ws.write(
        13,
        0,
        "ARR_DELAY is in minutes. Negative values mean early arrivals; positive values mean late arrivals.",
        fmt_note,
    )
    ws.set_column(0, 2, 28)

    # Carrier comparison / Pareto support.
    ws = workbook.add_worksheet("Carrier_Comparison")
    ws.write_row(0, 0, ["Carrier", "Count", "Mean Delay", "Median Delay", "Std Dev", "Min", "Max"], fmt_header)
    carriers = ["AA", "B6", "DL", "NK", "UA", "WN"]
    cached = {
        "AA": (36, -2.4166666666666665, -10.0, 21.909391332746523, -30, 60),
        "B6": (36, 11.277777777777779, -4.5, 62.29543028923256, -56, 257),
        "DL": (44, 8.204545454545455, -5.5, 42.033530107248374, -42, 194),
        "NK": (44, -0.5454545454545454, -7.5, 27.724101298542386, -35, 92),
        "UA": (45, -0.8444444444444444, -10.0, 34.924565173030466, -55, 117),
        "WN": (45, 7.8, -1.0, 29.742531530086374, -29, 110),
    }
    for r, carrier in enumerate(carriers, start=1):
        count, mean, median, sd, mn, mx = cached[carrier]
        ws.write(r, 0, carrier, fmt_cell)
        ws.write_formula(r, 1, f'=COUNTIF(Sample_250!D:D,A{r+1})', fmt_cell, count)
        ws.write_formula(r, 2, f'=AVERAGEIF(Sample_250!D:D,A{r+1},Sample_250!M:M)', fmt_num1, mean)
        # Median/std/min/max formulas reference the carrier-specific helper
        # columns written farther right on this same sheet. This avoids the
        # newer FILTER() function, which causes #NAME? in older Excel versions.
        helper_col = 9 + (r - 1)
        helper_letter = xlsxwriter.utility.xl_col_to_name(helper_col)
        ws.write_formula(r, 3, f'=MEDIAN({helper_letter}2:{helper_letter}251)', fmt_num1, median)
        ws.write_formula(r, 4, f'=STDEV.S({helper_letter}2:{helper_letter}251)', fmt_num1, sd)
        ws.write_formula(r, 5, f'=MIN({helper_letter}2:{helper_letter}251)', fmt_num1, mn)
        ws.write_formula(r, 6, f'=MAX({helper_letter}2:{helper_letter}251)', fmt_num1, mx)

    # Carrier-specific helper columns for compatible median/std-dev formulas.
    for idx, carrier in enumerate(carriers, start=9):
        ws.write(0, idx, f"{carrier} ARR_DELAY", fmt_header)
        vals = df.loc[df["UNIQUE_CARRIER"] == carrier, "ARR_DELAY"].reset_index(drop=True)
        for r, value in enumerate(vals, start=1):
            ws.write(r, idx, float(value), fmt_cell)

    ws.write(9, 0, "Chosen airlines for boxplot", fmt_subheader)
    ws.write(10, 0, "Airline #1", fmt_cell)
    ws.write(10, 1, "UA", fmt_cell)
    ws.write(11, 0, "Airline #2", fmt_cell)
    ws.write(11, 1, "WN", fmt_cell)

    ws.write(14, 0, "Pareto support table (sorted worst to best)", fmt_subheader)
    ws.write_row(15, 0, ["Carrier", "Average Delay"], fmt_header)
    for idx, (carrier, avg) in enumerate(
        [("B6", 11.277777777777779), ("DL", 8.204545454545455), ("WN", 7.8), ("NK", -0.5454545454545454), ("UA", -0.8444444444444444), ("AA", -2.4166666666666665)],
        start=16,
    ):
        ws.write(idx, 0, carrier, fmt_cell)
        ws.write_formula(idx, 1, f'=AVERAGEIF(Sample_250!D:D,A{idx+1},Sample_250!M:M)', fmt_num1, avg)

    chart = workbook.add_chart({"type": "column"})
    chart.add_series(
        {
            "name": "Average Arrival Delay",
            "categories": ["Carrier_Comparison", 16, 0, 21, 0],
            "values": ["Carrier_Comparison", 16, 1, 21, 1],
            "fill": {"color": "#4472C4"},
        }
    )
    chart.set_title({"name": "Average Arrival Delay by Airline"})
    chart.set_x_axis({"name": "Airline"})
    chart.set_y_axis({"name": "Average delay (minutes)"})
    chart.set_legend({"none": True})
    ws.insert_chart("D15", chart, {"x_scale": 1.25, "y_scale": 1.15})
    ws.set_column(0, 6, 16)

    # Boxplot data support. Excel workbook includes the generated image plus raw
    # per-airline values for recreating the official box-and-whisker chart.
    ws = workbook.add_worksheet("Boxplot_Data")
    ua = df.loc[df["UNIQUE_CARRIER"] == "UA", "ARR_DELAY"].reset_index(drop=True)
    wn = df.loc[df["UNIQUE_CARRIER"] == "WN", "ARR_DELAY"].reset_index(drop=True)
    ws.write_row(0, 0, ["UA ARR_DELAY", "WN ARR_DELAY"], fmt_header)
    for i in range(max(len(ua), len(wn))):
        if i < len(ua):
            ws.write(i + 1, 0, float(ua.iloc[i]), fmt_cell)
        if i < len(wn):
            ws.write(i + 1, 1, float(wn.iloc[i]), fmt_cell)
    ws.write(0, 3, "Boxplot preview image", fmt_header)
    if BOXPLOT.exists():
        ws.insert_image("D2", str(BOXPLOT), {"x_scale": 0.85, "y_scale": 0.85})
    ws.write(20, 3, "Outlier diagnostics", fmt_subheader)
    diagnostics = [
        ["Carrier", "Q1", "Median", "Q3", "IQR", "Outliers"],
        ["UA", -22.0, -10.0, 6.0, 28.0, "52, 56, 57, 110, 117"],
        ["WN", -11.0, -1.0, 16.0, 27.0, "83, 93, 110"],
    ]
    for r, row in enumerate(diagnostics, start=21):
        for c, value in enumerate(row, start=3):
            ws.write(r, c, value, fmt_header if r == 21 else fmt_cell)
    ws.set_column(0, 1, 14)
    ws.set_column(3, 8, 16)

    # Normal calculations.
    ws = workbook.add_worksheet("Normal_Calcs")
    ws.write_row(0, 0, ["Calculation", "Excel formula", "Result"], fmt_header)
    normal_rows = [
        ("P arrives early", '=NORM.DIST(0,3.876,38.0772389823,TRUE)', 0.4594604533390443),
        ("P arrives late", '=1-NORM.DIST(0,3.876,38.0772389823,TRUE)', 0.5405395466609557),
        ("P between Q1 and Q3", '=NORM.DIST(11,3.876,38.0772389823,TRUE)-NORM.DIST(-16,3.876,38.0772389823,TRUE)', 0.27336821798702626),
        ("P within 2 SD", '=NORM.DIST(3.876+2*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-2*38.0772389823,3.876,38.0772389823,TRUE)', 0.9544997361036416),
        ("Top 10% cutoff", '=NORM.INV(0.90,3.876,38.0772389823)', 52.673945175886075),
        ("Bottom 15% cutoff", '=NORM.INV(0.15,3.876,38.0772389823)', -35.58852190522189),
        ("Chebyshev within 3 SD", '=1-1/3^2', 0.8888888888888888),
        ("Normal within 3 SD", '=NORM.DIST(3.876+3*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-3*38.0772389823,3.876,38.0772389823,TRUE)', 0.9973002039367398),
    ]
    for r, (label, formula, value) in enumerate(normal_rows, start=1):
        ws.write(r, 0, label, fmt_cell)
        ws.write_string(r, 1, formula, fmt_wrap)
        ws.write_formula(r, 2, formula, fmt_num3 if abs(value) < 2 else fmt_num1, value)
    ws.write(11, 0, "Input values", fmt_subheader)
    for r, row in enumerate(
        [("Mean", 3.876), ("Standard deviation", 38.07723898228516), ("Q1", -16.0), ("Q3", 11.0)],
        start=12,
    ):
        ws.write(r, 0, row[0], fmt_cell)
        ws.write(r, 1, row[1], fmt_num)
    ws.set_column(0, 0, 28)
    ws.set_column(1, 1, 110)
    ws.set_column(2, 2, 14)

    # Word-template support text.
    ws = workbook.add_worksheet("Template_Answers")
    ws.write_row(0, 0, ["Template row", "Excel command", "Response"], fmt_header)
    for r, (label, formula, response) in enumerate(template_rows(), start=1):
        ws.write(r, 0, label, fmt_cell)
        ws.write_string(r, 1, formula, fmt_wrap)
        ws.write(r, 2, response, fmt_wrap)
    ws.set_column(0, 0, 38)
    ws.set_column(1, 1, 60)
    ws.set_column(2, 2, 80)

    workbook.close()


def template_rows() -> list[tuple[str, str, str]]:
    n_a = "N/A"
    return [
        ("2a Mean", "=AVERAGE(Sample_250!M2:M251)", "3.9 minutes"),
        ("2b Median", "=MEDIAN(Sample_250!M2:M251)", "-6.0 minutes"),
        ("2c Standard Deviation", "=STDEV.S(Sample_250!M2:M251)", "38.1 minutes"),
        ("2d Variance", "=VAR.S(Sample_250!M2:M251)", "1449.9 minutes squared"),
        ("2e Minimum", "=MIN(Sample_250!M2:M251)", "-56.0 minutes"),
        ("2f Maximum", "=MAX(Sample_250!M2:M251)", "257.0 minutes"),
        ("2g 1st Quartile", "=QUARTILE.INC(Sample_250!M2:M251,1)", "-16.0 minutes"),
        ("2h 3rd Quartile", "=QUARTILE.INC(Sample_250!M2:M251,3)", "11.0 minutes"),
        (
            "2i Mean comparison",
            '=AVERAGEIF(Sample_250!D:D,"UA",Sample_250!M:M); =AVERAGEIF(Sample_250!D:D,"WN",Sample_250!M:M); use STDEV.S with filtered carrier data.',
            "Airline #1 = UA; Airline #2 = WN. UA mean delay is -0.8 minutes with SD 34.9 minutes. WN mean delay is 7.8 minutes with SD 29.7 minutes. UA has the better average arrival performance because its mean delay is lower, while WN is somewhat more consistent because its SD is smaller.",
        ),
        (
            "2j Median comparison",
            '=MEDIAN(FILTER(Sample_250!M:M,Sample_250!D:D="UA")); =MEDIAN(FILTER(Sample_250!M:M,Sample_250!D:D="WN"))',
            "UA median delay is -10.0 minutes; WN median delay is -1.0 minute. A typical UA flight arrived earlier than a typical WN flight in this sample.",
        ),
        ("3a 20% trimmed mean", "=TRIMMEAN(Sample_250!M2:M251,0.2)", "-4.3 minutes"),
        (
            "3b Trimmed vs untrimmed",
            "Compare TRIMMEAN with AVERAGE",
            "Yes. The trimmed mean is -4.3 minutes, compared with the untrimmed mean of 3.9 minutes. The difference is about 8.2 minutes, which is noticeable for arrival-delay data.",
        ),
        (
            "3c Explain trimmed mean difference",
            n_a,
            "The results differ because the sample has very large positive delay outliers, including a maximum of 257 minutes. Those unusually late flights pull the ordinary mean upward. The trimmed mean removes extreme values from both ends, so it better reflects the center of most flights.",
        ),
        (
            "3d Why trimmed mean",
            n_a,
            "A trimmed mean is useful when data are skewed or contain outliers. It reduces the effect of unusually early or unusually late flights while still using more of the dataset than the median alone.",
        ),
        ("4a Boxplot", "Insert -> Statistic Chart -> Box and Whisker using UA and WN ARR_DELAY values.", "Boxplot inserted."),
        ("4b Boxplot shape", n_a, "Both UA and WN appear right-skewed. Most flights are near on-time or early, but a few very late flights create long upper tails."),
        (
            "4c Boxplot outliers",
            n_a,
            "Yes. UA has high-delay outliers at 52, 56, 57, 110, 117 minutes. WN has high-delay outliers at 83, 93, 110 minutes. These are unusually late flights. The airlines should be concerned because even a few very late flights can hurt customers and raise average delay.",
        ),
        (
            "4d Boxplot comparison",
            n_a,
            "UA has a lower median delay (-10.0 minutes) than WN (-1.0 minute), so UA has better typical performance. WN has slightly less spread by SD (29.7 vs. 34.9), so WN is somewhat more consistent. Both distributions have high positive outliers.",
        ),
        (
            "4e Manager conclusion",
            n_a,
            "As a UA manager, I would conclude that typical performance is good because the median UA flight arrived 10 minutes early. However, the high-delay outliers show that UA should investigate causes of very late flights, especially delays above 100 minutes.",
        ),
        ("5a Pareto chart", "AVERAGEIF by carrier, sort largest to smallest, then Insert -> Column/Bar Chart.", "Pareto chart inserted."),
        ("5b Worst airline", "Sorted carrier averages", "B6 is worst, with average delay 11.3 minutes."),
        ("5c Best airline", "Sorted carrier averages", "AA is best, with average delay -2.4 minutes."),
        ("5d Pareto benefit", n_a, "A Pareto chart orders categories from largest to smallest impact, making the worst performers easy to identify quickly."),
        (
            "5e Worst-airline manager response",
            n_a,
            "As a B6 manager, I would investigate scheduling, aircraft turnaround time, staffing, maintenance availability, boarding procedures, and whether particular routes or airports drive most delays. Within-control factors include staffing, scheduling, aircraft readiness, gate operations, and boarding efficiency. Less-controllable factors include weather, air traffic control restrictions, airport congestion, and security disruptions.",
        ),
        ("6a Arrives early", "=NORM.DIST(0,3.876,38.0772389823,TRUE)", "0.459"),
        ("6b Arrives late", "=1-NORM.DIST(0,3.876,38.0772389823,TRUE)", "0.541"),
        ("6c Between Q1 and Q3", "=NORM.DIST(11,3.876,38.0772389823,TRUE)-NORM.DIST(-16,3.876,38.0772389823,TRUE)", "0.273"),
        (
            "6d Reasonableness of 6c",
            n_a,
            "For the actual sample, Q1 to Q3 contains the middle 50% of observations. Under this fitted normal model, the area is only 0.273, much less than 0.500. This suggests the arrival-delay data are not very normal and are affected by skewness/outliers.",
        ),
        (
            "6e Within 2 SD",
            "=NORM.DIST(3.876+2*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-2*38.0772389823,3.876,38.0772389823,TRUE)",
            "0.954",
        ),
        (
            "6f Reasonableness of 6e",
            n_a,
            "Yes. For a normal distribution, about 95% of values fall within two standard deviations of the mean. The computed value 0.954 is very close to the expected normal-rule area.",
        ),
        ("7a Top 10% cutoff", "=NORM.INV(0.90,3.876,38.0772389823)", "52.7 minutes. Under the normal model, about 10% of flights have delays greater than this."),
        ("7b Bottom 15% cutoff", "=NORM.INV(0.15,3.876,38.0772389823)", "-35.6 minutes. Under the normal model, about 15% of flights arrive more than 35.6 minutes early."),
        (
            "8a Chebyshev",
            n_a,
            "Chebyshev's theorem gives P(|X - mu| < 3sigma) >= 1 - 1/3^2 = 1 - 1/9 = 8/9 = 0.889. Therefore, at least 0.889 of the arrival-delay values fall within 3 standard deviations of the mean.",
        ),
        (
            "8b Normal within 3 SD",
            "=NORM.DIST(3.876+3*38.0772389823,3.876,38.0772389823,TRUE)-NORM.DIST(3.876-3*38.0772389823,3.876,38.0772389823,TRUE)",
            "0.997",
        ),
        (
            "8c Chebyshev comparison",
            n_a,
            "Chebyshev gives a conservative lower bound that works for any distribution with finite mean and variance. The normal result is much tighter because it assumes a specific normal shape. Here Chebyshev guarantees at least 0.889, while the normal model gives 0.997.",
        ),
    ]


def set_cell_text(cell, text: str) -> None:
    cell.text = text
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(8)


def add_picture_to_cell(cell, image_path: Path, width: float) -> None:
    cell.text = ""
    paragraph = cell.paragraphs[0]
    run = paragraph.add_run()
    run.add_picture(str(image_path), width=Inches(width))


def build_docx() -> None:
    doc = Document(TEMPLATE)
    table = doc.tables[0]
    rows = template_rows()
    if len(rows) != 35:
        raise RuntimeError(f"Expected 35 response rows, got {len(rows)}")

    for idx, (_, formula, response) in enumerate(rows, start=1):
        row = table.rows[idx]
        # Put formulas in column 3 and responses in column 4.
        set_cell_text(row.cells[2], formula)
        set_cell_text(row.cells[3], response)

    # Insert chart images in the chart rows. Merge formula/result columns for
    # more space in the completed copy.
    if BOXPLOT.exists():
        merged = table.rows[15].cells[2].merge(table.rows[15].cells[3])
        add_picture_to_cell(merged, BOXPLOT, 3.6)
    if PARETO.exists():
        merged = table.rows[20].cells[2].merge(table.rows[20].cells[3])
        add_picture_to_cell(merged, PARETO, 3.6)

    # Add a short appendix note to clarify the Section 8 template typo.
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.add_run("Note on Section 8 wording: ").bold = True
    p.add_run(
        "The template says \"age of aircraft,\" but the project instructions and dataset "
        "are about on-time arrival delay. The Section 8 calculations use the Section 2 "
        "arrival-delay mean and standard deviation."
    )

    doc.save(OUT_DOCX)


def main() -> None:
    if not SAMPLE.exists():
        raise SystemExit(f"Missing sample CSV: {SAMPLE}")
    build_excel()
    build_docx()
    print(f"Wrote {OUT_XLSX}")
    print(f"Wrote {OUT_DOCX}")


if __name__ == "__main__":
    main()
