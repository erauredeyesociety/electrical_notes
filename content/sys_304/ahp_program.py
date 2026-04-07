"""
SYS 304 Homework 5 - Part III
AHP (Analytic Hierarchy Process) Calculator

Usage:
    python3 ahp_program.py

    Runs the AHP analysis with the current pairwise comparison inputs
    and prints all results (criteria weights, alternative weights,
    overall priorities, consistency ratios, and the selected alternative).

    No command-line arguments needed. To change inputs, edit the numpy
    arrays below (criteria_matrix, alt_A through alt_E).

How to modify inputs:
    1. Find the comparison matrices starting around line 40.
    2. Each matrix is a numpy array of Saaty pairwise comparison values.
    3. The diagonal is always 1 (anything vs itself = equally preferred).
    4. Upper triangle: if the ROW item is preferred over the COLUMN item,
       enter the Saaty scale value (1-9).
    5. Lower triangle: enter the reciprocal (e.g., if upper is 5, lower is 1/5).
    6. Save and re-run. All outputs update automatically.

Saaty scale quick reference:
    1 = Equally preferred
    3 = Moderately preferred
    5 = Strongly preferred
    7 = Very strongly preferred
    9 = Extremely preferred
    2, 4, 6, 8 = Intermediate values

Decision problem (from Lecture Slide 8):
    Goal: Select best overall automated system
    Criteria (Level II): A=CIMS goals, B=Net present worth, C=Serviceability,
                          D=Management/eng effort, E=Lack of riskiness
    Alternatives (Level III): P-1, P-2, P-3

Requires: numpy (pip install numpy)
"""

import numpy as np

# ============================================================
# SAATY SCALE REFERENCE
# 1 = Equally preferred
# 3 = Moderately preferred
# 5 = Strongly preferred
# 7 = Very strongly preferred
# 9 = Extremely preferred
# 2,4,6,8 = Intermediate values
# Reciprocals (1/3, 1/5, etc.) for reverse preference
# ============================================================

# Random Index table for consistency ratio
RI_TABLE = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12,
            6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}

# ============================================================
# USER INPUTS: Pairwise comparison matrices
# Modify these to change the analysis
# ============================================================

# Level II: Criteria comparison (5x5)
# Order: A(CIMS), B(NPW), C(Serviceability), D(Mgmt effort), E(Riskiness)
criteria_matrix = np.array([
    [1,   1/3, 5,   6,   5],    # A vs all
    [3,   1,   6,   7,   6],    # B vs all
    [1/5, 1/6, 1,   3,   1],    # C vs all
    [1/6, 1/7, 1/3, 1,   1/4],  # D vs all
    [1/5, 1/6, 1,   4,   1],    # E vs all
])

# Level III: Alternative comparisons for each criterion (3x3 each)
# Order: P-1, P-2, P-3

# A. CIMS Goals (subjective)
alt_A = np.array([
    [1,   1/3, 1],
    [3,   1,   2],
    [1,   1/2, 1],
])

# B. Net Present Worth (from performance data: 300M, 350M, 400M)
# Proportional: P1=300/1050, P2=350/1050, P3=400/1050
# Using pairwise ratios:
alt_B = np.array([
    [1,     300/350, 300/400],
    [350/300, 1,     350/400],
    [400/300, 400/350, 1],
])

# C. Serviceability (subjective)
alt_C = np.array([
    [1,   2,   2],
    [1/2, 1,   1],
    [1/2, 1,   1],
])

# D. Management/Engineering Effort (from performance data: 500, 700, 1100 hrs)
# Lower is better, so invert: 1/500, 1/700, 1/1100
# Pairwise ratios:
alt_D = np.array([
    [1,       700/500,   1100/500],
    [500/700, 1,         1100/700],
    [500/1100, 700/1100, 1],
])

# E. Lack of Riskiness (subjective)
alt_E = np.array([
    [1,   3,   4],
    [1/3, 1,   2],
    [1/4, 1/2, 1],
])

# ============================================================
# AHP COMPUTATION FUNCTIONS
# ============================================================

def compute_ahp(matrix, name=""):
    """Compute priority weights and consistency ratio for a pairwise comparison matrix."""
    n = matrix.shape[0]

    # Step 1: Normalize columns
    col_sums = matrix.sum(axis=0)
    normalized = matrix / col_sums

    # Step 2: Compute priority weights (row averages of normalized matrix)
    weights = normalized.mean(axis=1)

    # Step 3: Consistency check
    # Multiply original matrix by weight vector
    weighted_sum = matrix @ weights
    # Divide element-wise by weights
    consistency_vector = weighted_sum / weights
    lambda_max = consistency_vector.mean()

    if n > 2:
        CI = (lambda_max - n) / (n - 1)
        RI = RI_TABLE.get(n, 1.49)
        CR = CI / RI if RI > 0 else 0.0
    else:
        CI = 0.0
        CR = 0.0
        RI = RI_TABLE.get(n, 0.0)

    return weights, CI, CR, RI, lambda_max


def print_matrix(matrix, labels_row, labels_col, title=""):
    """Print a matrix with labels."""
    if title:
        print(f"\n  {title}")
    header = "          " + "".join(f"{c:>10}" for c in labels_col)
    print(header)
    for i, row_label in enumerate(labels_row):
        row_str = f"  {row_label:<8}" + "".join(f"{matrix[i,j]:>10.4f}" for j in range(matrix.shape[1]))
        print(row_str)


# ============================================================
# MAIN COMPUTATION
# ============================================================

criteria_names = ["A.CIMS", "B.NPW", "C.Serv", "D.Mgmt", "E.Risk"]
alt_names = ["P-1", "P-2", "P-3"]
alt_matrices = [alt_A, alt_B, alt_C, alt_D, alt_E]

print("=" * 65)
print("  AHP ANALYSIS: Best Overall Automated System")
print("=" * 65)

# --- Level II: Criteria Weights ---
print("\n" + "-" * 65)
print("  LEVEL II: CRITERIA WEIGHTS")
print("-" * 65)

print_matrix(criteria_matrix, criteria_names, criteria_names, "Pairwise Comparison Matrix:")

criteria_weights, criteria_CI, criteria_CR, criteria_RI, criteria_lambda = compute_ahp(criteria_matrix, "Criteria")

print(f"\n  Priority Weights:")
for name, w in zip(criteria_names, criteria_weights):
    print(f"    {name:<10} = {w:.4f}")

print(f"\n  lambda_max = {criteria_lambda:.4f}")
print(f"  CI = {criteria_CI:.4f}")
print(f"  RI = {criteria_RI:.4f}")
print(f"  CR = {criteria_CR:.4f}", end="")
print("  <-- INCONSISTENT!" if criteria_CR > 0.10 else "  (acceptable)")

# --- Level III: Alternative Weights per Criterion ---
print("\n" + "-" * 65)
print("  LEVEL III: ALTERNATIVE WEIGHTS PER CRITERION")
print("-" * 65)

alt_weight_matrix = np.zeros((len(alt_names), len(criteria_names)))
alt_CIs = []
alt_CRs = []
alt_RIs = []

for j, (crit_name, alt_mat) in enumerate(zip(criteria_names, alt_matrices)):
    weights, CI, CR, RI, lam = compute_ahp(alt_mat)
    alt_weight_matrix[:, j] = weights
    alt_CIs.append(CI)
    alt_CRs.append(CR)
    alt_RIs.append(RI)

    print(f"\n  Criterion: {crit_name}")
    print_matrix(alt_mat, alt_names, alt_names, "Comparison Matrix:")
    print(f"  Weights: {', '.join(f'{w:.4f}' for w in weights)}")
    print(f"  CR = {CR:.4f}", end="")
    print("  <-- INCONSISTENT!" if CR > 0.10 else "  (acceptable)")

# --- Overall Priority Weights ---
print("\n" + "-" * 65)
print("  OVERALL PRIORITY WEIGHTS (Slide 26 format)")
print("-" * 65)

header = "          " + "".join(f"{c:>10}" for c in criteria_names) + "    Overall"
print(header)
wt_line = "  Weights " + "".join(f"{w:>10.4f}" for w in criteria_weights)
print(wt_line)
print()

overall_weights = alt_weight_matrix @ criteria_weights

for i, alt_name in enumerate(alt_names):
    row_str = f"  {alt_name:<8}" + "".join(f"{alt_weight_matrix[i,j]:>10.4f}" for j in range(len(criteria_names)))
    row_str += f"    {overall_weights[i]:.4f}"
    print(row_str)

# --- Selected Alternative ---
best_idx = np.argmax(overall_weights)
print(f"\n  >>> SELECTED ALTERNATIVE: {alt_names[best_idx]} (weight = {overall_weights[best_idx]:.4f}) <<<")

# --- Consistency Summary ---
print("\n" + "-" * 65)
print("  CONSISTENCY SUMMARY")
print("-" * 65)

print(f"\n  {'Matrix':<20} {'CI':>8} {'CR':>8} {'Status':>14}")
print(f"  {'Criteria':<20} {criteria_CI:>8.4f} {criteria_CR:>8.4f} {'INCONSISTENT' if criteria_CR > 0.10 else 'OK':>14}")
for j, crit_name in enumerate(criteria_names):
    status = "INCONSISTENT" if alt_CRs[j] > 0.10 else "OK"
    print(f"  {crit_name:<20} {alt_CIs[j]:>8.4f} {alt_CRs[j]:>8.4f} {status:>14}")

# --- Global Consistency Ratio (C.R.H.) ---
print(f"\n  Global Consistency Ratio (C.R.H.):")
M_CI = criteria_CI + criteria_weights @ np.array(alt_CIs)
M_RI = criteria_RI + criteria_weights @ np.array(alt_RIs)
CRH = M_CI / M_RI if M_RI > 0 else 0.0
print(f"  M_CI = {M_CI:.4f}")
print(f"  M_RI = {M_RI:.4f}")
print(f"  C.R.H. = {CRH:.4f}", end="")
print("  <-- INCONSISTENT!" if CRH > 0.10 else "  (acceptable)")

print("\n" + "=" * 65)
