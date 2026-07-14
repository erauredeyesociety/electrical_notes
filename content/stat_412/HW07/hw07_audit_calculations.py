#!/usr/bin/env python3
import math
from scipy.stats import binom, chi2, norm, t
checks = {
    "q2_alpha": binom.cdf(2, 15, 0.4) + binom.sf(9, 15, 0.4),
    "q2_beta_p_0_3": binom.cdf(9, 15, 0.3) - binom.cdf(2, 15, 0.3),
    "q2_beta_p_0_5": binom.cdf(9, 15, 0.5) - binom.cdf(2, 15, 0.5),
    "q3_alpha": 2 * (1 - norm.cdf((219 - 210) / (15 / math.sqrt(9)))),
    "q3_beta_mu_195": norm.cdf((219 - 195) / (15 / math.sqrt(9))) - norm.cdf((201 - 195) / (15 / math.sqrt(9))),
    "q4_t": (40 - 41) / (3.4 / math.sqrt(68)),
    "q4_p_left": t.cdf((40 - 41) / (3.4 / math.sqrt(68)), 67),
    "q5_z": (781 - 800) / (37 / math.sqrt(33)),
    "q5_p_two": 2 * norm.cdf((781 - 800) / (37 / math.sqrt(33))),
    "q6_z": (165.8 - 162.8) / (6.8 / math.sqrt(48)),
    "q6_p_two": 2 * norm.sf(abs((165.8 - 162.8) / (6.8 / math.sqrt(48)))),
    "q7_n_raw": ((norm.ppf(0.90) + norm.ppf(0.95)) * 7.2 / 3.3) ** 2,
    "q7_n_ceil": math.ceil(((norm.ppf(0.90) + norm.ppf(0.95)) * 7.2 / 3.3) ** 2),
    "q8_n_raw": ((norm.ppf(0.90) + norm.ppf(0.99)) ** 2 * (6.28**2 + 5.68**2)) / (12 - 6) ** 2,
    "q8_n_ceil": math.ceil(((norm.ppf(0.90) + norm.ppf(0.99)) ** 2 * (6.28**2 + 5.68**2)) / (12 - 6) ** 2),
    "q9_p_two_exact": binom.sf(11, 20, 0.4) + binom.cdf(4, 20, 0.4),
    "q10_chi_square": 48 * 4.35 / 4.1,
    "q10_p_two": 2 * min(chi2.cdf(48 * 4.35 / 4.1, 48), chi2.sf(48 * 4.35 / 4.1, 48)),
    "q11_t": (10.5 - 10) / (2.22 / math.sqrt(240)),
    "q11_p_right": t.sf((10.5 - 10) / (2.22 / math.sqrt(240)), 239),
    "q12_t": (18330 - 18000) / (3700 / math.sqrt(110)),
    "q12_p_right": t.sf((18330 - 18000) / (3700 / math.sqrt(110)), 109),
    "q13_z": (99 / 1050 - 0.097) / math.sqrt(0.097 * 0.903 / 1050),
    "q13_z_if_phat_rounded_3dp": (0.094 - 0.097) / math.sqrt(0.097 * 0.903 / 1050),
    "q13_p_left": norm.cdf((99 / 1050 - 0.097) / math.sqrt(0.097 * 0.903 / 1050)),
    "q14_z": (0.42 - 0.50) / math.sqrt(0.5 * 0.5 / 1011),
    "q15_z": (0.55 - 0.54) / math.sqrt(0.54 * 0.46 / 3500),
    "q16_z": (0.52 - 0.50) / math.sqrt(0.5 * 0.5 / 280000),
    "q17_p": norm.cdf(-2.2),
    "q18_p": 2 * norm.sf(2.6),
}
for name, value in checks.items():
    print(f"{name}: {value:.8f}")
