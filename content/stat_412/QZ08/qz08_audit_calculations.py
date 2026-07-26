#!/usr/bin/env python3
"""Calculation audit for STAT 412 QZ08."""

import math
import numpy as np
from scipy import stats


def chisq_gof(obs, props=None, estimated_params=0):
    obs = np.array(obs, dtype=float)
    if props is None:
        exp = np.repeat(obs.sum() / len(obs), len(obs))
    else:
        exp = obs.sum() * np.array(props, dtype=float)
    chi = ((obs - exp) ** 2 / exp).sum()
    df = len(obs) - 1 - estimated_params
    p = stats.chi2.sf(chi, df)
    return chi, df, p, exp


def chisq_ind(obs):
    chi, p, df, exp = stats.chi2_contingency(np.array(obs, dtype=float), correction=False)
    return chi, df, p, exp


def welch_t(m1, m2, s1, s2, n1, n2, alternative="two-sided"):
    se = math.sqrt(s1**2 / n1 + s2**2 / n2)
    t = (m1 - m2) / se
    df = (s1**2 / n1 + s2**2 / n2) ** 2 / (
        (s1**2 / n1) ** 2 / (n1 - 1) + (s2**2 / n2) ** 2 / (n2 - 1)
    )
    if alternative == "less":
        p = stats.t.cdf(t, df)
    elif alternative == "greater":
        p = stats.t.sf(t, df)
    else:
        p = 2 * stats.t.sf(abs(t), df)
    return se, t, df, p


def pooled_t(m1, m2, s1, s2, n1, n2):
    sp = math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    se = sp * math.sqrt(1 / n1 + 1 / n2)
    t = (m1 - m2) / se
    df = n1 + n2 - 2
    p = 2 * stats.t.sf(abs(t), df)
    return sp, se, t, df, p


for name, obs, props, estimated in [
    ("Q1", [36, 61, 65, 55, 57, 58, 43], None, 0),
    ("Q3", [19, 18, 21, 37], [2 / 16, 4 / 16, 5 / 16, 5 / 16], 0),
    ("Q4", [19, 13, 11, 14, 14, 8, 7, 13, 6, 10], None, 0),
]:
    chi, df, p, exp = chisq_gof(obs, props, estimated)
    print(f"{name}: chi={chi:.6f}, df={df}, p={p:.6g}, exp={np.round(exp,4).tolist()}")

heights = np.array(
    [
        171.99, 154.37, 155.68, 157.58, 168.59, 163.98, 159.51, 155.40,
        178.79, 155.61, 148.99, 155.58, 156.82, 154.77, 155.53, 155.01,
        154.92, 161.50, 160.02, 163.58, 164.67, 170.18, 154.63, 159.52,
        167.11, 156.79, 169.52, 170.88, 151.63, 159.72, 158.41, 173.60,
        160.09, 164.83, 172.10, 153.23, 134.47, 169.10, 160.19, 157.79,
        166.31, 158.38, 177.80, 152.38, 164.10, 160.59, 167.69, 158.78,
        156.49, 157.62, 169.72, 155.03, 170.60, 160.11, 156.40, 162.82,
        155.09, 166.09, 159.01, 148.67, 153.30, 175.12, 164.69, 154.82,
        161.18, 165.78, 165.57, 166.58, 168.90, 171.83, 159.99, 164.60,
        159.58, 160.91, 163.29, 151.99, 169.08, 159.41, 162.17, 170.91,
        162.49, 160.30, 181.40, 157.49, 165.61, 169.31, 154.11, 167.59,
        166.91, 156.62, 155.62, 162.92, 168.77, 157.43, 162.22, 157.32,
        162.60, 157.02, 161.42, 167.71, 166.98, 156.49, 156.51, 158.39,
        167.57, 144.41, 150.61, 160.32, 159.42, 162.52, 147.88, 164.41,
        166.11, 169.09, 149.49, 162.82, 165.10, 163.98, 165.21, 162.89,
        163.10, 163.29, 162.91, 166.10, 173.21, 169.81, 156.08, 167.99,
        163.01, 147.20, 176.10, 153.32, 165.41, 161.88, 166.88, 155.60,
        168.62, 177.32, 171.12, 163.10, 144.19, 156.31, 163.39, 162.50,
        175.63, 146.70, 162.17,
    ],
    dtype=float,
)
mu, s = heights.mean(), heights.std(ddof=1)
bounds = [-np.inf, 156.05, 162.15, 168.25, np.inf]
q2_obs = np.array(
    [
        (heights <= bounds[1]).sum(),
        ((heights > bounds[1]) & (heights <= bounds[2])).sum(),
        ((heights > bounds[2]) & (heights <= bounds[3])).sum(),
        (heights > bounds[3]).sum(),
    ]
)
q2_probs = [
    stats.norm.cdf(hi, mu, s) - stats.norm.cdf(lo, mu, s)
    for lo, hi in zip(bounds[:-1], bounds[1:])
]
q2_exp = len(heights) * np.array(q2_probs)
q2_chi = ((q2_obs - q2_exp) ** 2 / q2_exp).sum()
q2_df = 4 - 1 - 2
q2_p = stats.chi2.sf(q2_chi, q2_df)
print(f"Q2: n={len(heights)}, mean={mu:.6f}, s={s:.6f}, obs={q2_obs.tolist()}, probs={np.round(q2_probs,4).tolist()}, exp={np.round(q2_exp,4).tolist()}, chi={q2_chi:.6f}, df={q2_df}, p={q2_p:.6g}")

se, t, df, p = welch_t(18.14, 20.58, 1.46, 2.34, 25, 25, "less")
crit = stats.t.ppf(0.99, df)
diff = 18.14 - 20.58
print(f"Q5: t={t:.6f}, df={df:.6f}, p={p:.6g}, 98% CI=({diff-crit*se:.6f},{diff+crit*se:.6f})")

sp, se, t, df, p = pooled_t(38100, 40100, 5000, 5900, 12, 12)
print(f"Q8: sp={sp:.6f}, t={t:.6f}, df={df}, p={p:.6g}")

se, t, df, p = welch_t(2.32, 2.62, 0.91, 0.56, 35, 39)
crit = stats.t.ppf(0.995, df)
diff = 2.32 - 2.62
print(f"Q9: t={t:.6f}, df={df:.6f}, p={p:.6g}, 99% CI=({diff-crit*se:.6f},{diff+crit*se:.6f})")

for name, obs in [
    ("Q6", [[15, 49], [7, 9]]),
    ("Q7", [[357, 282, 117, 156], [380, 357, 202, 186]]),
    ("Q10", [[256, 720], [464, 962]]),
]:
    chi, df, p, exp = chisq_ind(obs)
    print(f"{name}: chi={chi:.6f}, df={df}, p={p:.6g}, exp={np.round(exp,4).tolist()}")
