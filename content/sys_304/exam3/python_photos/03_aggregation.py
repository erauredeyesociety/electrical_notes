"""
SYS 304 Exam 3, Question 4(c): Sup-Min aggregation and centroid defuzzification.

Produces:
  03a_output_aggregation.png -- clipped consequent sets, aggregated output,
                                and centroid defuzzification.
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def mu_pull(F):
    F = np.asarray(F, dtype=float)
    out = np.zeros_like(F)
    mask = (F >= -1.0) & (F <= 0.0)
    out[mask] = -F[mask]
    return out


def mu_none(F):
    F = np.asarray(F, dtype=float)
    out = np.zeros_like(F)
    m1 = (F >= -0.5) & (F <= 0.0)
    m2 = (F >= 0.0) & (F <= 0.5)
    out[m1] = 2.0 * (F[m1] + 0.5)
    out[m2] = 2.0 * (0.5 - F[m2])
    return out


def mu_push(F):
    F = np.asarray(F, dtype=float)
    out = np.zeros_like(F)
    mask = (F >= 0.0) & (F <= 1.0)
    out[mask] = F[mask]
    return out


def make_aggregation_figure(out_path):
    F = np.linspace(-1.2, 1.2, 1000)

    pull = mu_pull(F)
    none = mu_none(F)
    push = mu_push(F)

    clip_pull = 0.4
    clip_none = 0.2
    clip_push = 0.0

    pull_c = np.minimum(pull, clip_pull)
    none_c = np.minimum(none, clip_none)
    push_c = np.minimum(push, clip_push)

    agg = np.maximum.reduce([pull_c, none_c, push_c])

    num = np.trapezoid(F * agg, F)
    den = np.trapezoid(agg, F)
    F_star = num / den

    print(f"Computed centroid F* = {F_star:.4f} N  (rounded: {F_star:.2f} N)")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    color_pull = "tab:red"
    color_none = "tab:green"
    color_push = "tab:blue"

    ax1.plot(F, pull, "--", color=color_pull, alpha=0.5, linewidth=1.2,
             label="μ_Pull (unclipped)")
    ax1.plot(F, none, "--", color=color_none, alpha=0.5, linewidth=1.2,
             label="μ_None (unclipped)")
    ax1.plot(F, push, "--", color=color_push, alpha=0.5, linewidth=1.2,
             label="μ_Push (unclipped)")

    ax1.plot(F, pull_c, color=color_pull, linewidth=2.4,
             label=f"μ_Pull clipped @ {clip_pull}")
    ax1.fill_between(F, 0, pull_c, color=color_pull, alpha=0.30)

    ax1.plot(F, none_c, color=color_none, linewidth=2.4,
             label=f"μ_None clipped @ {clip_none}")
    ax1.fill_between(F, 0, none_c, color=color_none, alpha=0.30)

    ax1.plot(F, push_c, color=color_push, linewidth=2.4,
             label="μ_Push clipped @ 0 (no rules)")

    ax1.axhline(clip_pull, color=color_pull, linestyle=":", linewidth=1.0)
    ax1.axhline(clip_none, color=color_none, linestyle=":", linewidth=1.0)
    ax1.text(1.18, clip_pull + 0.015, f"α = {clip_pull}",
             color=color_pull, ha="right", va="bottom", fontsize=9)
    ax1.text(1.18, clip_none + 0.015, f"α = {clip_none}",
             color=color_none, ha="right", va="bottom", fontsize=9)

    ax1.set_title("Clipped Consequent Sets (per rule)")
    ax1.set_xlabel("F (N)")
    ax1.set_ylabel("membership μ")
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(0, 1.05)
    ax1.grid(True, alpha=0.4)
    ax1.legend(loc="upper right", fontsize=8, ncol=2)

    ax2.plot(F, agg, color="black", linewidth=2.6, label="μ_agg(F) = max(clipped)")
    ax2.fill_between(F, 0, agg, color="tab:purple", alpha=0.30,
                     label="aggregated region")

    ax2.axvline(F_star, color="tab:orange", linewidth=2.0, linestyle="--",
                label=f"F* ≈ {F_star:.2f} N")
    ax2.annotate(f"F* ≈ {F_star:.2f} N",
                 xy=(F_star, 0.55),
                 xytext=(F_star + 0.35, 0.80),
                 fontsize=11, color="tab:orange",
                 arrowprops=dict(arrowstyle="->", color="tab:orange", lw=1.2))

    ax2.set_title("Aggregated Output μ_agg(F) and Centroid Defuzzification")
    ax2.set_xlabel("F (N)")
    ax2.set_ylabel("membership μ")
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(0, 1.05)
    ax2.grid(True, alpha=0.4)
    ax2.legend(loc="upper right", fontsize=9)

    fig.suptitle("Sup-Min Aggregation and Centroid Defuzzification",
                 fontsize=13, y=0.995)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

    return F_star


if __name__ == "__main__":
    base = "/home/devel/electrical_notes/content/sys_304/exam3/python_photos"
    agg_path = f"{base}/03a_output_aggregation.png"

    F_star = make_aggregation_figure(agg_path)

    print(f"Wrote: {agg_path}")
    print(f"Centroid F* = {F_star:.2f} N")
