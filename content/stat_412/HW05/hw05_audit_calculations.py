#!/usr/bin/env python3
"""Recompute HW05 numerical answers from the visible prompts.

This is an audit helper only. It does not modify files. Values use the same
standard-normal table convention as the solution files where MyStatLab links
the normal table.
"""

from __future__ import annotations

import math
import statistics as st


ZT = {
    -1.81: 0.0351,
    -1.50: 0.0668,
    -1.41: 0.0793,
    -1.33: 0.0918,
    -1.30: 0.0968,
    -0.61: 0.2709,
    -0.20: 0.4207,
    0.00: 0.5000,
    0.17: 0.5675,
    0.22: 0.5871,
    0.53: 0.7019,
    0.65: 0.7422,
    0.74: 0.7704,
    0.76: 0.7764,
    0.85: 0.8023,
    1.00: 0.8413,
    1.63: 0.9484,
    1.78: 0.9625,
    2.00: 0.9772,
    2.18: 0.9854,
    2.24: 0.9875,
    2.25: 0.9878,
    3.00: 0.9987,
}


def main() -> None:
    q1 = [9, 16, 13, 10, 4, 68, 20, 9, 14]
    print("Q1 mean/median/mode:", round(st.mean(q1), 2), st.median(q1), st.multimode(q1))

    q2 = [53, 50, 47, 47, 44, 36, 31, 29, 26, 26, 26, 22]
    print("Q2 mean/median/mode:", round(st.mean(q2), 2), st.median(q2), st.multimode(q2))

    q3 = [5, 7, 7, 8, 13, 7, 16, 15, 15, 15]
    print("Q3 range/s:", max(q3) - min(q3), round(st.stdev(q3), 2))

    q4 = [11.6, 11.4, 8.6, 13.8, 12.4, 14.6, 12.3, 9.7]
    print("Q4 mean/sample variance:", round(st.mean(q4), 2), round(st.variance(q4), 2))

    q5 = [2.5, 3.5, 3.4, 2.9, 1.7, 2.1, 2.9, 1.8, 2.6, 2.5,
          2.7, 2.4, 3.2, 2.5, 1.9, 2.4, 3.6, 2.3, 2.5, 3.5]
    print("Q5 s:", round(st.stdev(q5), 2))

    print("Q6:", round(ZT[-0.20] - ZT[-1.30], 4))
    print("Q7:", int(round(49 * (4 / 3.5) ** 2)))
    print("Q8:", 5.4**2 / 36, 5.4**2 / 324, 5.4**2 / 900, 5.4**2 / 81)
    print("Q9:", round(ZT[2.18] - ZT[0.53], 4))
    print("Q10:", 178.7, 6.2 / math.sqrt(25),
          "expected count b", round(300 * (ZT[0.85] - ZT[-1.33])),
          "expected count c", round(300 * ZT[-1.41]))
    print("Q11:", 4.7, 0.81, "xbar", 4.7, 0.81 / 64, "part c", ZT[1.78])
    print("Q12:", round(1 - ZT[1.00], 4))
    print("Q13:", ZT[-1.50], round(1 - ZT[1.00], 4), round(ZT[2.00] - ZT[0.00], 4))
    print("Q14:", round(ZT[0.74] - ZT[-1.81], 4))
    print("Q15:", ZT[-0.61])
    print("Q16:", round(2 * (1 - ZT[1.63]), 4), round(2 * (ZT[0.65] - ZT[0.22]), 4))
    print("Q17:", round(1 - ZT[0.76], 4))
    print("Q18:", 0.5000, round(1 - ZT[3.00], 4))
    print("Q19:", round(1 - ZT[3.00], 4))
    print("Q20:", math.ceil((2.24 / 0.05) ** 2))


if __name__ == "__main__":
    main()
