#!/usr/bin/env python3
"""Calculation audit for STAT 412 HW08."""

import math
import numpy as np
from scipy import stats


def pooled_t(xbar1, xbar2, s1, s2, n1, n2, mu0=0, alternative="two-sided"):
    sp = math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    se = sp * math.sqrt(1 / n1 + 1 / n2)
    t = ((xbar1 - xbar2) - mu0) / se
    df = n1 + n2 - 2
    if alternative == "greater":
        p = stats.t.sf(t, df)
    elif alternative == "less":
        p = stats.t.cdf(t, df)
    else:
        p = 2 * stats.t.sf(abs(t), df)
    return sp, t, df, p


def welch_t(x1, x2, mu0=0, alternative="two-sided"):
    n1, n2 = len(x1), len(x2)
    m1, m2 = np.mean(x1), np.mean(x2)
    s1, s2 = np.std(x1, ddof=1), np.std(x2, ddof=1)
    se = math.sqrt(s1**2 / n1 + s2**2 / n2)
    t = ((m1 - m2) - mu0) / se
    df = (s1**2 / n1 + s2**2 / n2) ** 2 / (
        (s1**2 / n1) ** 2 / (n1 - 1) + (s2**2 / n2) ** 2 / (n2 - 1)
    )
    if alternative == "greater":
        p = stats.t.sf(t, df)
    elif alternative == "less":
        p = stats.t.cdf(t, df)
    else:
        p = 2 * stats.t.sf(abs(t), df)
    return m1, m2, s1, s2, t, df, p


def chisq_gof(obs, props=None):
    obs = np.array(obs, dtype=float)
    if props is None:
        exp = np.repeat(obs.sum() / len(obs), len(obs))
    else:
        exp = obs.sum() * np.array(props, dtype=float)
    chi = ((obs - exp) ** 2 / exp).sum()
    p = stats.chi2.sf(chi, len(obs) - 1)
    return chi, len(obs) - 1, p, exp


def chisq_ind(obs):
    chi, p, df, exp = stats.chi2_contingency(np.array(obs, dtype=float), correction=False)
    return chi, df, p, exp


sp, t, df, p = pooled_t(34.5, 0, 10.3, 10.2, 25, 25, alternative="greater")
print(f"Q1: sp={sp:.4f}, t={t:.4f}, df={df}, p={p:.6g}")

sp, t, df, p = pooled_t(38400, 39700, 5200, 5800, 12, 12)
print(f"Q2: sp={sp:.4f}, t={t:.4f}, df={df}, p={p:.6g}")

x1 = np.array([105, 86, 95, 99, 84], dtype=float)
x2 = np.array([89, 156, 103, 141, 98, 79, 112], dtype=float)
m1, m2 = x1.mean(), x2.mean()
s1, s2 = x1.std(ddof=1), x2.std(ddof=1)
se = math.sqrt(s1**2 / len(x1) + s2**2 / len(x2))
t = ((m2 - m1) - 10) / se
df = (s1**2 / len(x1) + s2**2 / len(x2)) ** 2 / (
    (s1**2 / len(x1)) ** 2 / (len(x1) - 1) + (s2**2 / len(x2)) ** 2 / (len(x2) - 1)
)
p = stats.t.cdf(t, df)
print(f"Q3: means=({m1:.4f},{m2:.4f}), s=({s1:.4f},{s2:.4f}), t={t:.4f}, df={df:.4f}, left-tail p={p:.6g}")

se = math.sqrt(157**2 / 400 + 199**2 / 400)
ci = (40 - 1.96 * se, 40 + 1.96 * se)
print(f"Q9: SE={se:.4f}, 95% z CI=({ci[0]:.4f},{ci[1]:.4f})")

for name, obs in [
    ("Q11", [304, 316, 296, 286]),
    ("Q17", [39, 31, 45, 39, 47, 50, 48, 50, 50, 42, 38, 38]),
    ("Q18", [20, 19, 22, 36]),
    ("Q19", [44, 60, 57, 59, 57, 55, 36]),
]:
    props = [0.125, 0.25, 0.3125, 0.3125] if name == "Q18" else None
    chi, df, p, exp = chisq_gof(obs, props)
    print(f"{name}: chi={chi:.6f}, df={df}, p={p:.6g}, exp={np.round(exp,4).tolist()}")

chi, df, p, exp = chisq_ind([[23, 25], [222, 197]])
print(f"Q13 expected: {np.round(exp,4).tolist()}")

for name, obs in [
    ("Q14", [[123, 131], [52, 14]]),
    ("Q15", [[423, 59], [549, 13]]),
    ("Q16", [[246, 556], [475, 680]]),
]:
    chi, df, p, exp = chisq_ind(obs)
    print(f"{name}: chi={chi:.6f}, df={df}, p={p:.6g}, exp={np.round(exp,4).tolist()}")
