#!/usr/bin/env python3
"""Read-only helper for STAT 412 Module 5 project.

This script never modifies the original XLSX/DOCX/CSV files. It reads the
exported ArrivalData CSV and writes optional working outputs to ./tmp:

- sample_250_seed_<seed>.csv
- descriptive_stats_seed_<seed>.csv
- airline_summary_seed_<seed>.csv
- boxplot_diagnostics_seed_<seed>.csv
- normal_calculations_seed_<seed>.csv
- boxplot_seed_<seed>.png
- pareto_seed_<seed>.png

Use the same seed if you want reproducible Python results. If you instead use
Excel's RAND() workflow for the submitted workbook, expect different numeric
answers because the 250-row sample will be different.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "Dataset_STAT412_Project_Final(ArrivalData).csv"
TMP = ROOT / "tmp"


def sample_quantile(series: pd.Series, q: float) -> float:
    """Match Excel QUARTILE.INC / PERCENTILE.INC style quantiles."""

    return float(series.quantile(q, interpolation="linear"))


def norm_cdf(x: float, mean: float, sd: float) -> float:
    """Normal CDF without requiring scipy."""

    z = (x - mean) / sd
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def inv_norm_standard(p: float) -> float:
    """Acklam inverse standard-normal approximation."""

    a = [
        -3.969683028665376e01,
        2.209460984245205e02,
        -2.759285104469687e02,
        1.383577518672690e02,
        -3.066479806614716e01,
        2.506628277459239e00,
    ]
    b = [
        -5.447609879822406e01,
        1.615858368580409e02,
        -1.556989798598866e02,
        6.680131188771972e01,
        -1.328068155288572e01,
    ]
    c = [
        -7.784894002430293e-03,
        -3.223964580411365e-01,
        -2.400758277161838e00,
        -2.549732539343734e00,
        4.374664141464968e00,
        2.938163982698783e00,
    ]
    d = [
        7.784695709041462e-03,
        3.224671290700398e-01,
        2.445134137142996e00,
        3.754408661907416e00,
    ]
    plow = 0.02425
    phigh = 1 - plow
    if not 0 < p < 1:
        raise ValueError("p must be between 0 and 1")
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (
            (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5])
            / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
        )
    if p <= phigh:
        q = p - 0.5
        r = q * q
        return (
            (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5])
            * q
            / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)
        )
    q = math.sqrt(-2 * math.log(1 - p))
    return -(
        (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5])
        / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    )


def build_outputs(seed: int, airlines: list[str] | None) -> None:
    TMP.mkdir(exist_ok=True)
    df = pd.read_csv(DATA)
    sample = df.sample(n=250, random_state=seed).reset_index(drop=True)
    sample_path = TMP / f"sample_250_seed_{seed}.csv"
    sample.to_csv(sample_path, index=False)

    arr = sample["ARR_DELAY"]
    stats = pd.DataFrame(
        [
            ("Mean", arr.mean(), "minutes"),
            ("Median", arr.median(), "minutes"),
            ("Standard Deviation", arr.std(ddof=1), "minutes"),
            ("Variance", arr.var(ddof=1), "minutes^2"),
            ("Minimum", arr.min(), "minutes"),
            ("Maximum", arr.max(), "minutes"),
            ("1st Quartile", sample_quantile(arr, 0.25), "minutes"),
            ("3rd Quartile", sample_quantile(arr, 0.75), "minutes"),
            ("20% Trimmed Mean", arr.sort_values().iloc[50:200].mean(), "minutes"),
        ],
        columns=["statistic", "value", "units"],
    )
    stats.to_csv(TMP / f"descriptive_stats_seed_{seed}.csv", index=False)

    summary = (
        sample.groupby("UNIQUE_CARRIER")["ARR_DELAY"]
        .agg(count="count", mean="mean", median="median", std="std", min="min", max="max")
        .reset_index()
        .sort_values("mean", ascending=False)
    )
    summary.to_csv(TMP / f"airline_summary_seed_{seed}.csv", index=False)

    if airlines is None:
        # Pick the two largest airline groups in the sample, which usually gives
        # steadier boxplots than choosing tiny groups.
        airlines = (
            sample["UNIQUE_CARRIER"].value_counts().head(2).index.to_list()
        )
    chosen = sample[sample["UNIQUE_CARRIER"].isin(airlines)]

    diagnostics = []
    for carrier in airlines:
        carrier_delays = sample.loc[sample["UNIQUE_CARRIER"] == carrier, "ARR_DELAY"]
        q1 = sample_quantile(carrier_delays, 0.25)
        q3 = sample_quantile(carrier_delays, 0.75)
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        outliers = carrier_delays[
            (carrier_delays < lower_fence) | (carrier_delays > upper_fence)
        ].sort_values()
        diagnostics.append(
            {
                "carrier": carrier,
                "count": int(carrier_delays.count()),
                "mean": carrier_delays.mean(),
                "median": carrier_delays.median(),
                "std": carrier_delays.std(ddof=1),
                "q1": q1,
                "q3": q3,
                "iqr": iqr,
                "lower_fence": lower_fence,
                "upper_fence": upper_fence,
                "skew": carrier_delays.skew(),
                "outliers": "; ".join(str(int(v)) for v in outliers),
            }
        )
    pd.DataFrame(diagnostics).to_csv(
        TMP / f"boxplot_diagnostics_seed_{seed}.csv", index=False
    )

    mean = arr.mean()
    sd = arr.std(ddof=1)
    q1 = sample_quantile(arr, 0.25)
    q3 = sample_quantile(arr, 0.75)
    normal_rows = [
        ("P(arrives early), P(X<0)", norm_cdf(0, mean, sd)),
        ("P(arrives late), P(X>0)", 1 - norm_cdf(0, mean, sd)),
        ("P(Q1<X<Q3)", norm_cdf(q3, mean, sd) - norm_cdf(q1, mean, sd)),
        (
            "P(mean-2sd<X<mean+2sd)",
            norm_cdf(mean + 2 * sd, mean, sd) - norm_cdf(mean - 2 * sd, mean, sd),
        ),
        ("Top 10 percent cutoff", mean + sd * inv_norm_standard(0.90)),
        ("Bottom 15 percent cutoff", mean + sd * inv_norm_standard(0.15)),
        ("Chebyshev lower bound within 3sd", 1 - 1 / 9),
        (
            "Normal P(mean-3sd<X<mean+3sd)",
            norm_cdf(mean + 3 * sd, mean, sd) - norm_cdf(mean - 3 * sd, mean, sd),
        ),
    ]
    pd.DataFrame(normal_rows, columns=["calculation", "value"]).to_csv(
        TMP / f"normal_calculations_seed_{seed}.csv", index=False
    )

    fig, ax = plt.subplots(figsize=(7, 4.5))
    chosen.boxplot(column="ARR_DELAY", by="UNIQUE_CARRIER", ax=ax)
    ax.set_title("Arrival Delay by Airline")
    ax.set_xlabel("Airline")
    ax.set_ylabel("Arrival delay (minutes)")
    fig.suptitle("")
    fig.tight_layout()
    fig.savefig(TMP / f"boxplot_seed_{seed}.png", dpi=180)
    plt.close(fig)

    pareto = summary.sort_values("mean", ascending=False)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(pareto["UNIQUE_CARRIER"], pareto["mean"])
    ax.set_title("Average Arrival Delay by Airline")
    ax.set_xlabel("Airline")
    ax.set_ylabel("Average arrival delay (minutes)")
    fig.tight_layout()
    fig.savefig(TMP / f"pareto_seed_{seed}.png", dpi=180)
    plt.close(fig)

    print(f"Wrote sample and summaries to {TMP}")
    print(f"Sample: {sample_path}")
    print(f"Normal calculations: {TMP / f'normal_calculations_seed_{seed}.csv'}")
    print(f"Boxplot diagnostics: {TMP / f'boxplot_diagnostics_seed_{seed}.csv'}")
    print("Airline choices for boxplot:", ", ".join(airlines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=41205)
    parser.add_argument(
        "--airlines",
        nargs=2,
        metavar=("AIRLINE1", "AIRLINE2"),
        help="Optional two airline carrier codes for the side-by-side boxplot.",
    )
    args = parser.parse_args()
    build_outputs(args.seed, args.airlines)


if __name__ == "__main__":
    main()
