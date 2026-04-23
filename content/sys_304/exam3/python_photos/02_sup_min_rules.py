"""Sup-Min Inference visualization for SYS 304 Exam 3 Question 4(c).

For input x = 5 ft, v = 0.8 ft/s, plots the four active rules as a 4x3 grid:
  Col 1: position membership (Middle or Right) with x=5 evaluation
  Col 2: velocity membership (Standing Still or Moving Right) with v=0.8 evaluation
  Col 3: consequent (None or Pull) clipped at firing strength
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


# --- Membership functions ---
def mu_left(x):
    x = np.asarray(x, dtype=float)
    return np.where((x >= -20) & (x <= 0), -x / 20.0, 0.0)


def mu_middle(x):
    x = np.asarray(x, dtype=float)
    left = np.where((x >= -10) & (x <= 0), (x + 10) / 10.0, 0.0)
    right = np.where((x > 0) & (x <= 10), (10 - x) / 10.0, 0.0)
    return left + right


def mu_right(x):
    x = np.asarray(x, dtype=float)
    return np.where((x >= 0) & (x <= 20), x / 20.0, 0.0)


def mu_moving_left(v):
    v = np.asarray(v, dtype=float)
    return np.where((v >= -1) & (v <= 0), -v, 0.0)


def mu_standing_still(v):
    v = np.asarray(v, dtype=float)
    left = np.where((v >= -0.5) & (v <= 0), 2.0 * (v + 0.5), 0.0)
    right = np.where((v > 0) & (v <= 1), 1.0 - v, 0.0)
    return left + right


def mu_moving_right(v):
    v = np.asarray(v, dtype=float)
    return np.where((v >= 0) & (v <= 2), v / 2.0, 0.0)


def mu_pull(F):
    F = np.asarray(F, dtype=float)
    return np.where((F >= -1) & (F <= 0), -F, 0.0)


def mu_none(F):
    F = np.asarray(F, dtype=float)
    left = np.where((F >= -0.5) & (F <= 0), 2.0 * (F + 0.5), 0.0)
    right = np.where((F > 0) & (F <= 0.5), 2.0 * (0.5 - F), 0.0)
    return left + right


def mu_push(F):
    F = np.asarray(F, dtype=float)
    return np.where((F >= 0) & (F <= 1), F, 0.0)


# --- Evaluation point ---
X_EVAL = 5.0
V_EVAL = 0.8

# --- Rule table: (rule_label, pos_name, pos_fn, vel_name, vel_fn, cons_name, cons_fn) ---
RULES = [
    (5, "Middle", mu_middle, "Standing Still", mu_standing_still, "None", mu_none),
    (6, "Middle", mu_middle, "Moving Right",   mu_moving_right,   "Pull", mu_pull),
    (7, "Right",  mu_right,  "Moving Right",   mu_moving_right,   "Pull", mu_pull),
    (8, "Right",  mu_right,  "Standing Still", mu_standing_still, "Pull", mu_pull),
]


def main():
    x_range = np.linspace(-20, 20, 801)
    v_range = np.linspace(-1, 2, 601)
    F_range = np.linspace(-1, 1, 801)

    fig, axes = plt.subplots(4, 3, figsize=(14, 12))

    for i, (rule_num, pos_name, pos_fn, vel_name, vel_fn, cons_name, cons_fn) in enumerate(RULES):
        mu_pos = float(pos_fn(X_EVAL))
        mu_vel = float(vel_fn(V_EVAL))
        fire = min(mu_pos, mu_vel)
        # TeX-safe name (spaces -> \,)
        vel_tex = vel_name.replace(' ', r'\,')

        # --- Column 1: position ---
        ax = axes[i, 0]
        ax.plot(x_range, pos_fn(x_range), color='tab:blue', linewidth=2,
                label=f"$\\mu_{{{pos_name}}}(x)$")
        ax.axvline(X_EVAL, color='gray', linestyle='--', linewidth=1)
        ax.hlines(mu_pos, -20, X_EVAL, color='tab:red', linestyle=':', linewidth=1.5)
        ax.plot([X_EVAL], [mu_pos], 'o', color='tab:red')
        ax.annotate(f"$\\mu_{{{pos_name}}}(5) = {mu_pos:.2f}$",
                    xy=(X_EVAL, mu_pos), xytext=(X_EVAL + 1, mu_pos + 0.08),
                    fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.85))
        ax.set_xlim(-20, 20)
        ax.set_ylim(0, 1.05)
        ax.set_title(f"Rule {rule_num}: position ({pos_name})", fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper left', fontsize=9)
        if i == 3:
            ax.set_xlabel("x (ft)")
        ax.set_ylabel("membership")

        # --- Column 2: velocity ---
        ax = axes[i, 1]
        ax.plot(v_range, vel_fn(v_range), color='tab:green', linewidth=2,
                label=f"$\\mu_{{{vel_tex}}}(v)$")
        ax.axvline(V_EVAL, color='gray', linestyle='--', linewidth=1)
        ax.hlines(mu_vel, -1, V_EVAL, color='tab:red', linestyle=':', linewidth=1.5)
        ax.plot([V_EVAL], [mu_vel], 'o', color='tab:red')
        ax.annotate(f"$\\mu_{{{vel_tex}}}(0.8) = {mu_vel:.2f}$",
                    xy=(V_EVAL, mu_vel), xytext=(V_EVAL - 0.1, mu_vel + 0.12),
                    fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.85))
        ax.set_xlim(-1, 2)
        ax.set_ylim(0, 1.05)
        ax.set_title(f"Rule {rule_num}: velocity ({vel_name})", fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper right', fontsize=9)
        if i == 3:
            ax.set_xlabel("v (ft/s)")

        # --- Column 3: consequent clipped ---
        ax = axes[i, 2]
        cons_unclipped = cons_fn(F_range)
        cons_clipped = np.minimum(cons_unclipped, fire)
        ax.plot(F_range, cons_unclipped, color='tab:orange', linestyle='--',
                linewidth=1.2, alpha=0.6, label=f"$\\mu_{{{cons_name}}}(F)$")
        ax.plot(F_range, cons_clipped, color='tab:purple', linewidth=2,
                label=f"clipped at {fire:.2f}")
        ax.fill_between(F_range, 0, cons_clipped, color='tab:purple', alpha=0.3)
        ax.axhline(fire, color='tab:red', linestyle=':', linewidth=1.2)
        ax.annotate(f"firing = min({mu_pos:.2f}, {mu_vel:.2f}) = {fire:.2f}",
                    xy=(0.02, 0.92), xycoords='axes fraction',
                    fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.85))
        ax.set_xlim(-1, 1)
        ax.set_ylim(0, 1.05)
        ax.set_title(f"Rule {rule_num}: consequent ({cons_name})", fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper right', fontsize=9)
        if i == 3:
            ax.set_xlabel("F (N)")

        # Row label on the leftmost axis
        axes[i, 0].text(-0.22, 0.5,
                        f"Rule {rule_num}:\n{pos_name} $\\wedge$ {vel_name}\n$\\to$ {cons_name}\n(fire {fire:.2f})",
                        transform=axes[i, 0].transAxes,
                        rotation=90, va='center', ha='center',
                        fontsize=10, fontweight='bold')

    fig.suptitle("Sup-Min Inference — Active Rules at x = 5 ft, v = 0.8 ft/s",
                 fontsize=14, fontweight='bold')
    fig.tight_layout(rect=[0.03, 0, 1, 0.97])

    out_path = "/home/devel/electrical_notes/content/sys_304/exam3/python_photos/02_sup_min_rule_grid.png"
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
