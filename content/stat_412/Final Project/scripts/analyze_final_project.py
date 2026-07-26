#!/usr/bin/env python3
"""Reproducible analysis for STAT 412 Final Project.

This script intentionally works from CSV files and writes CSV/Markdown outputs.
It does not modify the instructor's Excel or Word template files.
"""

from __future__ import annotations

import argparse
import csv
import math
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, stdev

from scipy import stats


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_CSV = BASE_DIR / "Dataset_STAT412_Project_Final(ArrivalData).csv"
OUTPUT_DIR = BASE_DIR / "outputs"


AIRLINE_NAMES = {
    "AA": "American Airlines",
    "B6": "JetBlue Airways",
    "DL": "Delta Air Lines",
    "NK": "Spirit Airlines",
    "UA": "United Airlines",
    "WN": "Southwest Airlines",
}


@dataclass
class MeanCi:
    n: int
    sample_mean: float
    sample_stdev: float
    margin_error: float
    lower: float
    upper: float


@dataclass
class PropCi:
    n: int
    count_late: int
    phat: float
    margin_error: float
    lower: float
    upper: float


@dataclass
class OneSampleMeanTest:
    hypothesized_mean: float
    t_stat: float
    df: int
    p_value: float
    reject: bool


@dataclass
class OneSamplePropTest:
    hypothesized_prop: float
    z_stat: float
    p_value: float
    reject: bool


@dataclass
class WelchTest:
    airline_1: str
    airline_2: str
    n1: int
    n2: int
    mean1: float
    mean2: float
    stdev1: float
    stdev2: float
    t_stat: float
    df: float
    p_value: float
    reject: bool


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_rows(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def as_float(row: dict[str, str], key: str) -> float:
    return float(row[key])


def random_sample(rows: list[dict[str, str]], n: int, seed: int) -> list[dict[str, object]]:
    rng = random.Random(seed)
    augmented: list[dict[str, object]] = []
    for index, row in enumerate(rows, start=1):
        copied: dict[str, object] = dict(row)
        copied["SOURCE_ROW"] = index
        copied["RANDOM_VALUE"] = rng.random()
        augmented.append(copied)
    augmented.sort(key=lambda r: float(r["RANDOM_VALUE"]))
    return augmented[:n]


def confidence_interval_mean(values: list[float], confidence: float = 0.95) -> MeanCi:
    n = len(values)
    xbar = mean(values)
    s = stdev(values)
    alpha = 1 - confidence
    tcrit = stats.t.ppf(1 - alpha / 2, df=n - 1)
    me = tcrit * s / math.sqrt(n)
    return MeanCi(n, xbar, s, me, xbar - me, xbar + me)


def confidence_interval_prop(late_count: int, n: int, confidence: float = 0.95) -> PropCi:
    phat = late_count / n
    zcrit = stats.norm.ppf(1 - (1 - confidence) / 2)
    me = zcrit * math.sqrt(phat * (1 - phat) / n)
    return PropCi(n, late_count, phat, me, phat - me, phat + me)


def one_sample_mean_test(values: list[float], mu0: float = 8.0, alpha: float = 0.05) -> OneSampleMeanTest:
    n = len(values)
    xbar = mean(values)
    s = stdev(values)
    t_stat = (xbar - mu0) / (s / math.sqrt(n))
    p_value = stats.t.cdf(t_stat, df=n - 1)
    return OneSampleMeanTest(mu0, t_stat, n - 1, p_value, p_value < alpha)


def one_sample_prop_test(late_count: int, n: int, p0: float = 0.28, alpha: float = 0.05) -> OneSamplePropTest:
    phat = late_count / n
    se0 = math.sqrt(p0 * (1 - p0) / n)
    z_stat = (phat - p0) / se0
    p_value = stats.norm.cdf(z_stat)
    return OneSamplePropTest(p0, z_stat, p_value, p_value < alpha)


def welch_left_tail(values_1: list[float], values_2: list[float], code_1: str, code_2: str, alpha: float = 0.05) -> WelchTest:
    n1, n2 = len(values_1), len(values_2)
    if n1 < 2 or n2 < 2:
        raise ValueError(f"Need at least two rows for each airline; got {code_1}={n1}, {code_2}={n2}.")
    m1, m2 = mean(values_1), mean(values_2)
    s1, s2 = stdev(values_1), stdev(values_2)
    se2 = s1 * s1 / n1 + s2 * s2 / n2
    t_stat = (m1 - m2) / math.sqrt(se2)
    df = se2 * se2 / ((s1 * s1 / n1) ** 2 / (n1 - 1) + (s2 * s2 / n2) ** 2 / (n2 - 1))
    p_value = stats.t.cdf(t_stat, df=df)
    return WelchTest(code_1, code_2, n1, n2, m1, m2, s1, s2, t_stat, df, p_value, p_value < alpha)


def fmt(x: float, digits: int = 1) -> str:
    return f"{x:.{digits}f}"


def pct(x: float, digits: int = 1) -> str:
    return f"{100*x:.{digits}f}%"


def excel_formula_notes() -> dict[str, str]:
    return {
        "sample_mean": "=AVERAGE(M2:M251)",
        "sample_stdev": "=STDEV.S(M2:M251)",
        "sample_n": "=COUNT(M2:M251)",
        "mean_ci_margin": "=CONFIDENCE.T(0.05, STDEV.S(M2:M251), COUNT(M2:M251))",
        "late_count": '=COUNTIF(M2:M251,">10")',
        "late_prop": '=COUNTIF(M2:M251,">10")/COUNT(M2:M251)',
        "prop_ci_margin": "=1.96*SQRT(phat*(1-phat)/250)",
        "mean_test_t": "=(AVERAGE(M2:M251)-8)/(STDEV.S(M2:M251)/SQRT(COUNT(M2:M251)))",
        "mean_test_p": "=T.DIST(t_statistic,249,TRUE)",
        "prop_test_z": "=(phat-0.28)/SQRT(0.28*(1-0.28)/250)",
        "prop_test_p": "=NORM.S.DIST(z_statistic,TRUE)",
        "two_sample_test": "Excel Data Analysis ToolPak: t-Test: Two-Sample Assuming Unequal Variances",
    }


def write_calculation_csv(
    path: Path,
    mean_ci: MeanCi,
    prop_ci: PropCi,
    mean_test: OneSampleMeanTest,
    prop_test: OneSamplePropTest,
    welch: WelchTest | None,
) -> None:
    rows: list[dict[str, object]] = []
    formulas = excel_formula_notes()

    def add(section: str, item: str, value: object, formula: str = "") -> None:
        rows.append({"section": section, "item": item, "value": value, "excel_formula_or_method": formula})

    add("sample", "sample_size", mean_ci.n, formulas["sample_n"])
    add("section_1_mean_ci", "point_estimate_mean", fmt(mean_ci.sample_mean), formulas["sample_mean"])
    add("section_1_mean_ci", "sample_stdev", fmt(mean_ci.sample_stdev), formulas["sample_stdev"])
    add("section_1_mean_ci", "margin_of_error", fmt(mean_ci.margin_error), formulas["mean_ci_margin"])
    add("section_1_mean_ci", "lower_limit", fmt(mean_ci.lower))
    add("section_1_mean_ci", "upper_limit", fmt(mean_ci.upper))
    add("section_2_prop_ci", "late_count_arr_delay_gt_10", prop_ci.count_late, formulas["late_count"])
    add("section_2_prop_ci", "point_estimate_late_proportion", pct(prop_ci.phat), formulas["late_prop"])
    add("section_2_prop_ci", "margin_of_error", pct(prop_ci.margin_error), formulas["prop_ci_margin"])
    add("section_2_prop_ci", "lower_limit", pct(prop_ci.lower))
    add("section_2_prop_ci", "upper_limit", pct(prop_ci.upper))
    add("section_3_mean_test", "hypotheses", "H0: mu >= 8; H1: mu < 8")
    add("section_3_mean_test", "test_statistic_t", fmt(mean_test.t_stat), formulas["mean_test_t"])
    add("section_3_mean_test", "df", mean_test.df)
    add("section_3_mean_test", "p_value", f"{mean_test.p_value:.4f}", formulas["mean_test_p"])
    add("section_3_mean_test", "decision", "reject H0" if mean_test.reject else "do not reject H0")
    add("section_4_prop_test", "hypotheses", "H0: p >= 0.28; H1: p < 0.28")
    add("section_4_prop_test", "test_statistic_z", fmt(prop_test.z_stat), formulas["prop_test_z"])
    add("section_4_prop_test", "p_value", f"{prop_test.p_value:.4f}", formulas["prop_test_p"])
    add("section_4_prop_test", "decision", "reject H0" if prop_test.reject else "do not reject H0")
    if welch:
        add("section_5_two_sample", "airline_1", f"{welch.airline_1} ({AIRLINE_NAMES.get(welch.airline_1, 'unknown')})")
        add("section_5_two_sample", "airline_2", f"{welch.airline_2} ({AIRLINE_NAMES.get(welch.airline_2, 'unknown')})")
        add("section_5_two_sample", "hypotheses", "H0: mu1 >= mu2; H1: mu1 < mu2")
        add("section_5_two_sample", "n1", welch.n1)
        add("section_5_two_sample", "n2", welch.n2)
        add("section_5_two_sample", "mean1", fmt(welch.mean1))
        add("section_5_two_sample", "mean2", fmt(welch.mean2))
        add("section_5_two_sample", "stdev1", fmt(welch.stdev1))
        add("section_5_two_sample", "stdev2", fmt(welch.stdev2))
        add("section_5_two_sample", "test_statistic_t", fmt(welch.t_stat), formulas["two_sample_test"])
        add("section_5_two_sample", "df", fmt(welch.df))
        add("section_5_two_sample", "p_value", f"{welch.p_value:.4f}")
        add("section_5_two_sample", "decision", "reject H0" if welch.reject else "do not reject H0")
    else:
        add("section_5_two_sample", "status", "pending: provide first/last initials or airline codes")
    write_rows(path, rows, ["section", "item", "value", "excel_formula_or_method"])


def write_carrier_summary(path: Path, sample_rows: list[dict[str, object]]) -> None:
    grouped: dict[str, list[float]] = defaultdict(list)
    for row in sample_rows:
        grouped[str(row["UNIQUE_CARRIER"])].append(float(row["ARR_DELAY"]))
    rows = []
    for code in sorted(grouped):
        values = grouped[code]
        rows.append(
            {
                "UNIQUE_CARRIER": code,
                "AIRLINE_NAME": AIRLINE_NAMES.get(code, ""),
                "n": len(values),
                "mean_arr_delay": fmt(mean(values)),
                "stdev_arr_delay": fmt(stdev(values)) if len(values) > 1 else "",
                "late_count_arr_delay_gt_10": sum(1 for v in values if v > 10),
                "late_percent_arr_delay_gt_10": pct(sum(1 for v in values if v > 10) / len(values)),
            }
        )
    write_rows(path, rows, list(rows[0].keys()))


def write_markdown(
    path: Path,
    seed: int,
    mean_ci: MeanCi,
    prop_ci: PropCi,
    mean_test: OneSampleMeanTest,
    prop_test: OneSamplePropTest,
    welch: WelchTest | None,
) -> None:
    lines: list[str] = []
    lines.append("# STAT 412 Final Project Analysis Results")
    lines.append("")
    lines.append(f"Random sample seed: `{seed}`. Sample size: `{mean_ci.n}` rows.")
    lines.append("")
    lines.append("## Section 1: Confidence Interval for Mean")
    lines.append("")
    lines.append(f"- Point estimate: mean arrival delay = **{fmt(mean_ci.sample_mean)} minutes**.")
    lines.append(f"- Sample standard deviation = **{fmt(mean_ci.sample_stdev)} minutes**.")
    lines.append(f"- 95% CI = **({fmt(mean_ci.lower)}, {fmt(mean_ci.upper)}) minutes**.")
    lines.append(f"- Interpretation: We are 95% confident that the true mean arrival delay for all U.S. flights is between **{fmt(mean_ci.lower)}** and **{fmt(mean_ci.upper)}** minutes.")
    lines.append("")
    lines.append("## Section 2: Confidence Interval for Proportion")
    lines.append("")
    lines.append(f"- Late flight definition: `ARR_DELAY > 10` minutes.")
    lines.append(f"- Late count = **{prop_ci.count_late}** out of **{prop_ci.n}**.")
    lines.append(f"- Point estimate: **{pct(prop_ci.phat)}**.")
    lines.append(f"- 95% CI = **({pct(prop_ci.lower)}, {pct(prop_ci.upper)})**.")
    lines.append(f"- Interpretation: We are 95% confident that the true proportion of flights arriving more than 10 minutes late is between **{pct(prop_ci.lower)}** and **{pct(prop_ci.upper)}**.")
    lines.append("")
    lines.append("## Section 3: One-Sample Mean Hypothesis Test")
    lines.append("")
    lines.append("- Claim: the average flight arrival delay is less than 8 minutes.")
    lines.append("- Hypotheses: `H0: μ ≥ 8`; `H1: μ < 8`.")
    lines.append(f"- Test statistic: **t = {fmt(mean_test.t_stat)}**, df = **{mean_test.df}**.")
    lines.append(f"- P-value: **{mean_test.p_value:.4f}**.")
    lines.append(f"- Decision: **{'reject H0' if mean_test.reject else 'do not reject H0'}** at α = 0.05.")
    lines.append("")
    lines.append("## Section 4: One-Sample Proportion Hypothesis Test")
    lines.append("")
    lines.append("- Claim: less than 28% of flights are late.")
    lines.append("- Hypotheses: `H0: p ≥ 0.28`; `H1: p < 0.28`.")
    lines.append(f"- Test statistic: **z = {fmt(prop_test.z_stat)}**.")
    lines.append(f"- P-value: **{prop_test.p_value:.4f}**.")
    lines.append(f"- Decision: **{'reject H0' if prop_test.reject else 'do not reject H0'}** at α = 0.05.")
    lines.append("")
    lines.append("## Section 5: Two-Sample Mean Hypothesis Test")
    lines.append("")
    if welch:
        lines.append(f"- Airline 1: **{welch.airline_1} ({AIRLINE_NAMES.get(welch.airline_1, 'unknown')})**.")
        lines.append(f"- Airline 2: **{welch.airline_2} ({AIRLINE_NAMES.get(welch.airline_2, 'unknown')})**.")
        lines.append("- Hypotheses: `H0: μ1 ≥ μ2`; `H1: μ1 < μ2`.")
        lines.append(f"- Sample sizes: n1 = **{welch.n1}**, n2 = **{welch.n2}**.")
        lines.append(f"- Means: airline 1 = **{fmt(welch.mean1)}**, airline 2 = **{fmt(welch.mean2)}** minutes.")
        lines.append(f"- Test statistic: **t = {fmt(welch.t_stat)}**, df ≈ **{fmt(welch.df)}**.")
        lines.append(f"- P-value: **{welch.p_value:.4f}**.")
        lines.append(f"- Decision: **{'reject H0' if welch.reject else 'do not reject H0'}** at α = 0.05.")
    else:
        lines.append("Pending: provide first/last initials or explicit airline codes to select the two airlines.")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report_draft(
    path: Path,
    mean_ci: MeanCi,
    prop_ci: PropCi,
    mean_test: OneSampleMeanTest,
    prop_test: OneSamplePropTest,
    welch: WelchTest | None,
) -> None:
    mean_claim_result = "support" if mean_test.reject else "do not support"
    prop_claim_result = "support" if prop_test.reject else "do not support"
    lines = [
        "# Draft Text for Word Template",
        "",
        "This Markdown file is a staging draft. The final `.docx` should be filled only after all selections are confirmed.",
        "",
        "## Section 1: Confidence Interval for Mean",
        "",
        f"Point estimate: The sample mean arrival delay is {fmt(mean_ci.sample_mean)} minutes.",
        f"95% CI: The 95% confidence interval is ({fmt(mean_ci.lower)}, {fmt(mean_ci.upper)}) minutes.",
        f"Interpretation: We are 95% confident that the true average arrival delay for all U.S. flights is between {fmt(mean_ci.lower)} and {fmt(mean_ci.upper)} minutes.",
        "",
        "## Section 2: Confidence Interval for Proportion",
        "",
        f"Point estimate: {prop_ci.count_late} of {prop_ci.n} sampled flights were late, so the sample proportion is {pct(prop_ci.phat)}.",
        f"95% CI: The 95% confidence interval is ({pct(prop_ci.lower)}, {pct(prop_ci.upper)}).",
        f"Interpretation: We are 95% confident that the true proportion of flights arriving more than 10 minutes late is between {pct(prop_ci.lower)} and {pct(prop_ci.upper)}.",
        "",
        "## Section 3: Email to DOT Manager — Mean Delay Claim",
        "",
        "Subject: Arrival Delay Hypothesis Test Results",
        "",
        "Hello,",
        "",
        f"I reviewed a random sample of 250 U.S. flights to evaluate the claim that the true average arrival delay is less than 8 minutes. I used a one-sample t-test because we are comparing one sample mean to the claimed benchmark of 8 minutes. The sample mean was {fmt(mean_ci.sample_mean)} minutes, the test statistic was t = {fmt(mean_test.t_stat)}, and the p-value was {mean_test.p_value:.4f}. Since the p-value is {'less' if mean_test.reject else 'greater'} than 0.05, I {'rejected' if mean_test.reject else 'did not reject'} the null hypothesis. Based on this sample, I {mean_claim_result} the claim that the true average arrival delay is less than 8 minutes.",
        "",
        "## Section 4: Email to DOT Manager — Late-Flight Proportion Claim",
        "",
        "Subject: Late Flight Proportion Hypothesis Test Results",
        "",
        "Hello,",
        "",
        f"I evaluated the claim that less than 28% of U.S. flights are late, where late means arriving more than 10 minutes after the scheduled arrival time. In the random sample, {prop_ci.count_late} of {prop_ci.n} flights were late, giving a sample proportion of {pct(prop_ci.phat)}. I used a one-sample proportion z-test. The test statistic was z = {fmt(prop_test.z_stat)}, and the p-value was {prop_test.p_value:.4f}. Since the p-value is {'less' if prop_test.reject else 'greater'} than 0.05, I {'rejected' if prop_test.reject else 'did not reject'} the null hypothesis. Based on this sample, I {prop_claim_result} the claim that less than 28% of flights are late.",
        "",
        "## Section 5: Email to Airline CEO",
        "",
    ]
    if welch:
        ceo_result = "appears better" if welch.reject else "does not show enough evidence of being better"
        lines.extend(
            [
                f"Subject: Arrival Delay Comparison for {welch.airline_1} vs. {welch.airline_2}",
                "",
                "Hello,",
                "",
                f"I compared the average arrival delay for {welch.airline_1} ({AIRLINE_NAMES.get(welch.airline_1, 'selected airline')}) with {welch.airline_2} ({AIRLINE_NAMES.get(welch.airline_2, 'competitor airline')}) using a two-sample t-test assuming unequal variances. Lower average arrival delay is considered better. In the random sample, {welch.airline_1} had a mean delay of {fmt(welch.mean1)} minutes and {welch.airline_2} had a mean delay of {fmt(welch.mean2)} minutes. The test statistic was t = {fmt(welch.t_stat)}, and the p-value was {welch.p_value:.4f}. Since the p-value is {'less' if welch.reject else 'greater'} than 0.05, I {'rejected' if welch.reject else 'did not reject'} the null hypothesis. Based on this sample, {welch.airline_1} {ceo_result} than {welch.airline_2} in terms of mean arrival delay.",
            ]
        )
    else:
        lines.append("Pending: provide first/last initials or airline codes before writing the CEO email.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="STAT 412 final project analysis")
    parser.add_argument("--seed", type=int, default=412, help="Random seed used for sample selection.")
    parser.add_argument("--sample-size", type=int, default=250)
    parser.add_argument("--airline-1", help="Selected/employer airline code, e.g. AA.")
    parser.add_argument("--airline-2", help="Competitor airline code, e.g. DL.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = read_rows(DATA_CSV)
    sample_rows = random_sample(rows, args.sample_size, args.seed)
    arr_delay = [float(row["ARR_DELAY"]) for row in sample_rows]
    late_count = sum(1 for value in arr_delay if value > 10)

    mean_ci = confidence_interval_mean(arr_delay)
    prop_ci = confidence_interval_prop(late_count, len(arr_delay))
    mean_test = one_sample_mean_test(arr_delay)
    prop_test = one_sample_prop_test(late_count, len(arr_delay))

    welch: WelchTest | None = None
    if args.airline_1 and args.airline_2:
        code1 = args.airline_1.upper()
        code2 = args.airline_2.upper()
        vals1 = [float(row["ARR_DELAY"]) for row in sample_rows if str(row["UNIQUE_CARRIER"]).upper() == code1]
        vals2 = [float(row["ARR_DELAY"]) for row in sample_rows if str(row["UNIQUE_CARRIER"]).upper() == code2]
        welch = welch_left_tail(vals1, vals2, code1, code2)
        airline_rows = [row for row in sample_rows if str(row["UNIQUE_CARRIER"]).upper() in {code1, code2}]
        write_rows(
            OUTPUT_DIR / "final_project_airline_samples.csv",
            airline_rows,
            list(sample_rows[0].keys()),
        )

    write_rows(OUTPUT_DIR / "final_project_random_sample_250.csv", sample_rows, list(sample_rows[0].keys()))
    write_carrier_summary(OUTPUT_DIR / "final_project_carrier_summary.csv", sample_rows)
    write_calculation_csv(OUTPUT_DIR / "final_project_calculations.csv", mean_ci, prop_ci, mean_test, prop_test, welch)
    write_markdown(BASE_DIR / "analysis_results.md", args.seed, mean_ci, prop_ci, mean_test, prop_test, welch)
    write_report_draft(BASE_DIR / "final_report_draft.md", mean_ci, prop_ci, mean_test, prop_test, welch)

    carrier_counts = Counter(row["UNIQUE_CARRIER"] for row in sample_rows)
    print(f"Wrote outputs using seed={args.seed}, sample_size={args.sample_size}.")
    print("Sample carrier counts:", ", ".join(f"{k}={v}" for k, v in sorted(carrier_counts.items())))
    print(f"Mean CI: ({fmt(mean_ci.lower)}, {fmt(mean_ci.upper)})")
    print(f"Proportion CI: ({pct(prop_ci.lower)}, {pct(prop_ci.upper)})")
    if welch:
        print(f"Welch test {welch.airline_1} vs {welch.airline_2}: t={fmt(welch.t_stat)}, p={welch.p_value:.4f}")
    else:
        print("Two-sample airline comparison pending airline codes.")


if __name__ == "__main__":
    main()
