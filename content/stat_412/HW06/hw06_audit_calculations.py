#!/usr/bin/env python3
"""Audit calculations for STAT 412 HW06."""

from __future__ import annotations

import math
import statistics as st

from scipy.stats import chi2, norm, t


def ci_mean_z(xbar: float, sigma: float, n: int, c: float) -> tuple[float, float, float]:
    z = norm.ppf(1 - (1 - c) / 2)
    e = z * sigma / math.sqrt(n)
    return e, xbar - e, xbar + e


def ci_mean_t(xbar: float, s: float, n: int, c: float) -> tuple[float, float, float]:
    crit = t.ppf(1 - (1 - c) / 2, n - 1)
    e = crit * s / math.sqrt(n)
    return e, xbar - e, xbar + e


def ci_prop(x: int, n: int, c: float) -> tuple[float, float, float, float]:
    phat = x / n
    z = norm.ppf(1 - (1 - c) / 2)
    e = z * math.sqrt(phat * (1 - phat) / n)
    return phat, e, phat - e, phat + e


def ci_var(s2: float, n: int, c: float) -> tuple[float, float, float, float]:
    df = n - 1
    alpha = 1 - c
    lo = df * s2 / chi2.ppf(1 - alpha / 2, df)
    hi = df * s2 / chi2.ppf(alpha / 2, df)
    return lo, hi, math.sqrt(lo), math.sqrt(hi)


def main() -> None:
    print("Q1", 26.23 - 24.88)
    print("Q2", (5.1 - 4.5) / 2, (5.1 + 4.5) / 2)
    print("Q3", ci_mean_z(82.38, 13.78, 59, .90), ci_mean_z(82.38, 13.78, 59, .95))
    q5 = [21.53, 22.52, 15.23, 22.79, 21.96, 20.92, 17.19, 15.45,
          19.16, 21.56, 16.17, 22.52, 22.88, 19.46, 17.81, 22.68]
    print("Q5 mean", st.mean(q5), "90/99", ci_mean_z(st.mean(q5), 2.73, len(q5), .90), ci_mean_z(st.mean(q5), 2.73, len(q5), .99))
    print("Q6", ci_mean_t(31.7, 7.2, 26, .80))
    print("Q7", ci_mean_t(416, 190, 11, .90))
    print("Q8", ci_mean_t(75, 14, 4, .99))
    q9 = [10.30, 29.80, 27.10, 16.51, 11.90, 8.81, 14.00, 20.46, 14.90, 33.67,
          30.91, 14.86, 22.49, 15.35, 9.72, 19.80, 14.86, 8.09, 5.30, 18.30]
    print("Q9", st.mean(q9), st.stdev(q9))
    print("Q9 98", ci_mean_t(st.mean(q9), st.stdev(q9), len(q9), .98))
    print("Q10", ci_mean_t(28.2, 6.14, 43, .90))
    print("Q11", (.787 - .761) / 2, (.787 + .761) / 2)
    for label, args in [
        ("Q12 90", (717, 2029, .90)), ("Q12 95", (717, 2029, .95)),
        ("Q13", (1420, 3183, .99)), ("Q14", (382, 688, .90)),
        ("Q15 90", (1321, 2549, .90)), ("Q15 95", (1321, 2549, .95)),
    ]:
        print(label, ci_prop(*args))
    print("Q16", chi2.ppf(.005, 27), chi2.ppf(.995, 27))
    print("Q17", ci_var(5.76, 26, .95))
    q18 = [4.471, 4.422, 4.024, 4.322, 4.005, 3.766, 3.811, 3.769, 4.246,
           3.934, 4.163, 4.528, 3.938, 3.747, 3.849, 3.834, 4.435]
    print("Q18", st.variance(q18), ci_var(st.variance(q18), len(q18), .95))
    q19 = [1.75, 1.84, 1.58, 1.65, 1.73, 1.95, 1.36, 1.56, 1.46, 2.05]
    print("Q19", st.variance(q19), ci_var(st.variance(q19), len(q19), .99))
    print("Q20", ci_mean_t(182.7, 6.9, 60, .98))


if __name__ == "__main__":
    main()
