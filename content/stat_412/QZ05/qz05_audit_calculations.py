#!/usr/bin/env python3
"""Audit calculations for STAT 412 QZ05.

This script does not modify files. It recomputes the numerical answers used in
the QZ05 Markdown/LaTeX artifacts. Table-based answers are printed using the
same rounded z-table convention as the quiz.
"""

from __future__ import annotations

import math
import statistics as st
from collections import Counter


ZT = {
    -2.20: 0.0139,
    -1.95: 0.0256,
    -1.80: 0.0359,
    -1.46: 0.0721,
    -0.34: 0.3669,
    0.00: 0.5000,
    0.14: 0.5557,
    0.34: 0.6331,
    0.77: 0.7794,
    0.85: 0.8023,
    1.46: 0.9279,
    1.60: 0.9452,
    2.00: 0.9772,
    2.40: 0.9918,
}


def phi(z: float) -> float:
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def main() -> None:
    sd1 = math.sqrt(60**2 / 48 + 60**2 / 60)
    q1a = 2 * (1 - ZT[1.46])
    q1b = 2 * (ZT[0.77] - ZT[0.34])
    print("Q1:", sd1, q1a, q1b)

    print("Q2:", ZT[-2.20], 1 - ZT[1.60], ZT[2.00] - ZT[0.00])

    sd3 = math.sqrt(11**2 / 64 + 5**2 / 100)
    print("Q3:", sd3, (44.2 - 44) / sd3, ZT[0.14])

    print("Q4:", 1 - ZT[2.00])

    se5 = 6.8 / math.sqrt(25)
    q5b = round(200 * (ZT[0.85] - ZT[-1.80]))
    q5c = round(200 * ZT[-1.95])
    print("Q5:", 172.1, se5, q5b, q5c)

    q6a = ZT[2.40] - (1 - ZT[2.40])
    n6 = math.ceil(((1.6448536269514722 * 200) / 30) ** 2)
    print("Q6:", q6a, n6)

    q7 = [7, 11, 10, 3, 19, 11, 3, 11, 3, 6]
    print("Q7:", st.mean(q7), st.median(q7), Counter(q7))

    q8 = [3.2, 2.7, 2.3, 3.6, 4.9, 4.2, 4.8, 2.6, 4.1]
    print("Q8:", max(q8) - min(q8), st.variance(q8))

    q9 = [61000, 52000, 69000, 44000, 59000, 54000, 62000, 68000, 53000, 67000]
    transformed = [x / 500 - 125 for x in q9]
    print("Q9:", st.variance(transformed), math.sqrt(st.variance(transformed) * 500**2), st.stdev(q9))


if __name__ == "__main__":
    main()

