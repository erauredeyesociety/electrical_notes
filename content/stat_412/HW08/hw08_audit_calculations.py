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
t = ((m1 - m2) - (-10)) / se
df = (s1**2 / len(x1) + s2**2 / len(x2)) ** 2 / (
    (s1**2 / len(x1)) ** 2 / (len(x1) - 1) + (s2**2 / len(x2)) ** 2 / (len(x2) - 1)
)
p = stats.t.sf(t, df)
print(f"Q3: means=({m1:.4f},{m2:.4f}), s=({s1:.4f},{s2:.4f}), platform t={t:.4f}, df={df:.4f}, right-tail p={p:.6g}")

q4_nonsmokers = [
    0.97,
    0.72,
    1.00,
    0.81,
    0.62,
    1.32,
    1.24,
    0.99,
    0.90,
    0.74,
    0.88,
    0.94,
    1.16,
    0.86,
    0.85,
    0.58,
    0.64,
    0.98,
    1.09,
    0.92,
    0.78,
    1.24,
    1.18,
]
q4_smokers = [0.48, 0.71, 0.68, 1.18, 1.36, 0.78, 1.64]
m1, m2, s1, s2, t, df, p = welch_t(q4_nonsmokers, q4_smokers)
print(f"Q4: n=({len(q4_nonsmokers)},{len(q4_smokers)}), means=({m1:.4f},{m2:.4f}), s=({s1:.4f},{s2:.4f}), t={t:.4f}, df={df:.4f}, p={p:.6g}")

q5_station1 = [5030, 13700, 10730, 11400, 860, 2200, 4250, 15040, 4980, 8130, 26850, 17660, 22800, 1130, 1690]
q5_station2 = [2800, 4670, 6890, 7720, 7030, 7330, 2810, 1330, 3320, 1230, 2190]
m1, m2, s1, s2, t, df, p = welch_t(q5_station1, q5_station2)
print(f"Q5: n=({len(q5_station1)},{len(q5_station2)}), means=({m1:.4f},{m2:.4f}), s=({s1:.4f},{s2:.4f}), t={t:.4f}, df={df:.4f}, p={p:.6g}")

se = math.sqrt(157**2 / 400 + 199**2 / 400)
ci = (40 - 1.96 * se, 40 + 1.96 * se)
z = 40 / se
p = 2 * stats.norm.sf(abs(z))
print(f"Q9: SE={se:.4f}, 95% z CI=({ci[0]:.4f},{ci[1]:.4f}), z={z:.4f}, p={p:.6g}")
z = (40 - 26) / se
p = 2 * stats.norm.sf(abs(z))
print(f"Q9 part d: H0 diff=26, z={z:.4f}, p={p:.6g}")

for name, obs, props in [
    ("Q10", [42, 17, 25, 49, 41, 165, 150], [0.12, 0.02, 0.03, 0.14, 0.10, 0.31, 0.28]),
    ("Q11", [304, 316, 296, 286], None),
    ("Q12", [88, 60, 35, 15, 2], [0.52, 0.29, 0.08, 0.07, 0.04]),
    ("Q17", [39, 31, 45, 39, 47, 50, 48, 50, 50, 42, 38, 38], None),
    ("Q18", [20, 19, 22, 36], [0.125, 0.25, 0.3125, 0.3125]),
    ("Q19", [44, 60, 57, 59, 57, 55, 36], None),
]:
    chi, df, p, exp = chisq_gof(obs, props)
    print(f"{name}: chi={chi:.6f}, df={df}, p={p:.6g}, exp={np.round(exp,4).tolist()}")

chi, df, p, exp = chisq_ind([[23, 25], [222, 197]])
print(f"Q13 expected: {np.round(exp,4).tolist()}")

for name, obs in [
    ("Q6", [[15, 28], [28, 19]]),
    ("Q14", [[123, 131], [52, 14]]),
    ("Q15", [[423, 59], [549, 13]]),
    ("Q16", [[246, 556], [475, 680]]),
    ("Q20", [[725, 3024], [159, 4563]]),
]:
    chi, df, p, exp = chisq_ind(obs)
    print(f"{name}: chi={chi:.6f}, df={df}, p={p:.6g}, exp={np.round(exp,4).tolist()}")
