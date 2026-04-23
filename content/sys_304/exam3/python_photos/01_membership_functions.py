"""Generate fuzzy membership function diagrams for SYS 304 Exam 3 Q4.

Produces three PNGs:
  - 01a_position_membership.png
  - 01b_velocity_membership.png
  - 01c_force_membership.png
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ------------- Membership functions -------------

def mu_left(x):
    x = np.asarray(x, dtype=float)
    val = np.where((x >= -20) & (x <= 0), -x / 20.0, 0.0)
    return val


def mu_middle(x):
    x = np.asarray(x, dtype=float)
    val = np.zeros_like(x)
    mask1 = (x >= -10) & (x <= 0)
    mask2 = (x > 0) & (x <= 10)
    val[mask1] = (x[mask1] + 10) / 10.0
    val[mask2] = (10 - x[mask2]) / 10.0
    return val


def mu_right(x):
    x = np.asarray(x, dtype=float)
    val = np.where((x >= 0) & (x <= 20), x / 20.0, 0.0)
    return val


def mu_moving_left(v):
    v = np.asarray(v, dtype=float)
    val = np.where((v >= -1) & (v <= 0), -v, 0.0)
    return val


def mu_standing_still(v):
    v = np.asarray(v, dtype=float)
    val = np.zeros_like(v)
    mask1 = (v >= -0.5) & (v <= 0)
    mask2 = (v > 0) & (v <= 1)
    val[mask1] = 2.0 * (v[mask1] + 0.5)
    val[mask2] = 1.0 - v[mask2]
    return val


def mu_moving_right(v):
    v = np.asarray(v, dtype=float)
    val = np.where((v >= 0) & (v <= 2), v / 2.0, 0.0)
    return val


def mu_pull(F):
    F = np.asarray(F, dtype=float)
    val = np.where((F >= -1) & (F <= 0), -F, 0.0)
    return val


def mu_none(F):
    F = np.asarray(F, dtype=float)
    val = np.zeros_like(F)
    mask1 = (F >= -0.5) & (F <= 0)
    mask2 = (F > 0) & (F <= 0.5)
    val[mask1] = 2.0 * (F[mask1] + 0.5)
    val[mask2] = 2.0 * (0.5 - F[mask2])
    return val


def mu_push(F):
    F = np.asarray(F, dtype=float)
    val = np.where((F >= 0) & (F <= 1), F, 0.0)
    return val


# ------------- Plotters -------------

def plot_position():
    x = np.linspace(-20, 20, 200)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, mu_left(x),   label='Left',   color='tab:blue',   linewidth=2)
    ax.plot(x, mu_middle(x), label='Middle', color='tab:green',  linewidth=2)
    ax.plot(x, mu_right(x),  label='Right',  color='tab:red',    linewidth=2)

    # Evaluation point at x = 5
    x_eval = 5.0
    mid_val = float(mu_middle(np.array([x_eval])))
    right_val = float(mu_right(np.array([x_eval])))

    ax.axvline(x_eval, color='k', linestyle='--', alpha=0.6)
    ax.hlines(mid_val, -20, x_eval, colors='tab:green', linestyles=':', alpha=0.7)
    ax.hlines(right_val, -20, x_eval, colors='tab:red', linestyles=':', alpha=0.7)

    ax.plot([x_eval], [mid_val], 'o', color='tab:green')
    ax.plot([x_eval], [right_val], 'o', color='tab:red')
    ax.annotate(f'$\\mu_{{Middle}}(5) = {mid_val:.2f}$',
                xy=(x_eval, mid_val), xytext=(x_eval + 1.5, mid_val + 0.08),
                color='tab:green', fontsize=10)
    ax.annotate(f'$\\mu_{{Right}}(5) = {right_val:.2f}$',
                xy=(x_eval, right_val), xytext=(x_eval + 1.5, right_val + 0.08),
                color='tab:red', fontsize=10)

    ax.set_title('Position of Cart — Fuzzy Membership Functions')
    ax.set_xlabel('x (ft)')
    ax.set_ylabel('membership $\\mu$')
    ax.set_ylim(0, 1.05)
    ax.set_xlim(-20, 20)
    ax.grid(True, alpha=0.4)
    ax.legend(loc='upper center')

    out = os.path.join(OUT_DIR, '01a_position_membership.png')
    fig.savefig(out, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return out


def plot_velocity():
    v = np.linspace(-1.5, 2.5, 200)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(v, mu_moving_left(v),    label='Moving Left',    color='tab:blue',  linewidth=2)
    ax.plot(v, mu_standing_still(v), label='Standing Still', color='tab:green', linewidth=2)
    ax.plot(v, mu_moving_right(v),   label='Moving Right',   color='tab:red',   linewidth=2)

    v_eval = 0.8
    ss_val = float(mu_standing_still(np.array([v_eval])))
    mr_val = float(mu_moving_right(np.array([v_eval])))

    ax.axvline(v_eval, color='k', linestyle='--', alpha=0.6)
    ax.hlines(ss_val, -1.5, v_eval, colors='tab:green', linestyles=':', alpha=0.7)
    ax.hlines(mr_val, -1.5, v_eval, colors='tab:red',   linestyles=':', alpha=0.7)

    ax.plot([v_eval], [ss_val], 'o', color='tab:green')
    ax.plot([v_eval], [mr_val], 'o', color='tab:red')
    ax.annotate(f'$\\mu_{{StandingStill}}(0.8) = {ss_val:.2f}$',
                xy=(v_eval, ss_val), xytext=(v_eval + 0.15, ss_val + 0.08),
                color='tab:green', fontsize=10)
    ax.annotate(f'$\\mu_{{MovingRight}}(0.8) = {mr_val:.2f}$',
                xy=(v_eval, mr_val), xytext=(v_eval + 0.15, mr_val + 0.08),
                color='tab:red', fontsize=10)

    ax.set_title('Velocity of Cart — Fuzzy Membership Functions')
    ax.set_xlabel('v (ft/s)')
    ax.set_ylabel('membership $\\mu$')
    ax.set_ylim(0, 1.05)
    ax.set_xlim(-1.5, 2.5)
    ax.grid(True, alpha=0.4)
    ax.legend(loc='upper right')

    out = os.path.join(OUT_DIR, '01b_velocity_membership.png')
    fig.savefig(out, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return out


def plot_force():
    F = np.linspace(-1.2, 1.2, 200)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(F, mu_pull(F), label='Pull', color='tab:blue',  linewidth=2)
    ax.plot(F, mu_none(F), label='None', color='tab:green', linewidth=2)
    ax.plot(F, mu_push(F), label='Push', color='tab:red',   linewidth=2)

    ax.set_title('Control Force — Fuzzy Membership Functions')
    ax.set_xlabel('F (N)')
    ax.set_ylabel('membership $\\mu$')
    ax.set_ylim(0, 1.05)
    ax.set_xlim(-1.2, 1.2)
    ax.grid(True, alpha=0.4)
    ax.legend(loc='upper center')

    out = os.path.join(OUT_DIR, '01c_force_membership.png')
    fig.savefig(out, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return out


if __name__ == '__main__':
    p1 = plot_position()
    p2 = plot_velocity()
    p3 = plot_force()
    for p in (p1, p2, p3):
        print('wrote:', p)
