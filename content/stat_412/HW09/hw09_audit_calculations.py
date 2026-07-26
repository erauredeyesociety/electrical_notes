#!/usr/bin/env python3
"""Calculation audit for STAT 412 HW09."""

import math
from statistics import NormalDist

N = NormalDist()


def ztest(x1, n1, x2, n2, alt):
    p1 = x1 / n1
    p2 = x2 / n2
    phat = (x1 + x2) / (n1 + n2)
    se = math.sqrt(phat * (1 - phat) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se
    if alt == ">":
        p = 1 - N.cdf(z)
    elif alt == "<":
        p = N.cdf(z)
    else:
        p = 2 * (1 - N.cdf(abs(z)))
    return p1, p2, phat, z, p


def ci(x1, n1, x2, n2, conf):
    p1 = x1 / n1
    p2 = x2 / n2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    zcrit = N.inv_cdf(1 - (1 - conf) / 2)
    diff = p1 - p2
    return diff - zcrit * se, diff + zcrit * se


def fmt_ci(bounds):
    lo, hi = bounds
    return f"({lo:.4f},{hi:.4f})"


questions = [
    ("Q1", 53, 80, 59, 100, "!="),
    ("Q2", 251, 300, 308, 400, ">"),
    ("Q3", None, None, None, None, ">"),
    ("Q4", 421, 1405, 227, 775, "!="),
    ("Q5", 63, 286, 132, 312, ">"),
    ("Q6", 31, 2876, 17, 7647, ">"),
    ("Q7", 35, 40, 96, 113, "!="),
    ("Q8", 15, 334, 27, 276, "<"),
    ("Q9", 245, 2120, 56, 375, "<"),
    ("Q10", 312, 904, 407, 1106, "!="),
]

for name, x1, n1, x2, n2, alt in questions:
    if name == "Q3":
        print("Q3: use platform technology output: pooled=0.36, z=11.2997, p=0.0000, 80% CI=(0.4458,0.5418)")
        continue
    p1, p2, phat, z, p = ztest(x1, n1, x2, n2, alt)
    print(f"{name}: p1={p1:.6f}, p2={p2:.6f}, pooled={phat:.6f}, z={z:.6f}, p={p:.6g}")
    if name == "Q4":
        print(f"  95% CI={fmt_ci(ci(x1,n1,x2,n2,0.95))}")
    if name == "Q5":
        print(f"  90% CI={fmt_ci(ci(x1,n1,x2,n2,0.90))}")
        print("  Q5 platform answer unresolved; prior attempted entries were incorrect")
    if name == "Q6":
        print(f"  98% CI={fmt_ci(ci(x1,n1,x2,n2,0.98))}")
    if name == "Q7":
        print(f"  99% CI={fmt_ci(ci(x1,n1,x2,n2,0.99))}")
    if name == "Q8":
        print(f"  90% CI={fmt_ci(ci(x1,n1,x2,n2,0.90))}")
    if name == "Q9":
        print(f"  98% CI={fmt_ci(ci(x1,n1,x2,n2,0.98))}")
    if name == "Q10":
        print(f"  99% CI={fmt_ci(ci(x1,n1,x2,n2,0.99))}")
