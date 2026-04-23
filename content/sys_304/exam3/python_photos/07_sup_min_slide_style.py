"""
Q4(c) Sup-Min Control Action Rules in the style of the class
"Fuzzy Theory in Decision Analysis" slides 39-40.

Top row:  three small panels, one per consequent (Pull, None, Push),
          each showing the original triangle (dashed) and the clipped
          membership function (solid + fill) at the aggregated firing
          strength.
Bottom:   a single wide panel showing all clipped consequents overlaid
          on one F axis, with the union envelope drawn in bold black
          and the centroid F* marked with a vertical line.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# ---------------------------------------------------------------------------
# Output membership functions on F (N)
# ---------------------------------------------------------------------------
F = np.linspace(-1.1, 1.1, 4001)


def mu_pull(f):
    return np.where((f >= -1.0) & (f <= 0.0), -f, 0.0)


def mu_none(f):
    left = np.where((f >= -0.5) & (f <= 0.0), 2.0 * (f + 0.5), 0.0)
    right = np.where((f > 0.0) & (f <= 0.5), 2.0 * (0.5 - f), 0.0)
    return left + right


def mu_push(f):
    return np.where((f >= 0.0) & (f <= 1.0), f, 0.0)


# Aggregated firing strengths per consequent
alpha_pull = 0.4
alpha_none = 0.2
alpha_push = 0.0

full_pull = mu_pull(F)
full_none = mu_none(F)
full_push = mu_push(F)

clip_pull = np.minimum(full_pull, alpha_pull)
clip_none = np.minimum(full_none, alpha_none)
clip_push = np.minimum(full_push, alpha_push)  # all zeros

# Union envelope
mu_agg = np.maximum.reduce([clip_pull, clip_none, clip_push])

# Centroid of the union
area = np.trapezoid(mu_agg, F)
centroid = np.trapezoid(F * mu_agg, F) / area if area > 0 else 0.0

# ---------------------------------------------------------------------------
# Figure setup
# ---------------------------------------------------------------------------
fig = plt.figure(figsize=(12, 8))
gs = GridSpec(
    2,
    3,
    figure=fig,
    height_ratios=[1.0, 1.4],
    hspace=0.55,
    wspace=0.28,
    left=0.07,
    right=0.97,
    top=0.90,
    bottom=0.08,
)

# Colors
C_PULL = "tab:red"
C_NONE = "tab:green"
C_PUSH = "tab:blue"
C_DASH = "0.55"
C_UNION = "black"


def style_small_panel(ax):
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(0.0, 1.05)
    ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
    ax.set_yticks([0.0, 0.5, 1.0])
    ax.set_xlabel("F (N)", fontsize=9)
    ax.set_ylabel(r"$\mu$", fontsize=10)
    ax.grid(True, alpha=0.25)
    ax.tick_params(axis="both", labelsize=8)


# ---------------------------------------------------------------------------
# Top-row panel: Pull
# ---------------------------------------------------------------------------
ax_pull = fig.add_subplot(gs[0, 0])
ax_pull.plot(F, full_pull, linestyle="--", color=C_DASH, linewidth=1.2,
             label="Full MF")
ax_pull.plot(F, clip_pull, color=C_PULL, linewidth=2.2, label="Clipped")
ax_pull.fill_between(F, 0, clip_pull, color=C_PULL, alpha=0.35)
ax_pull.axhline(alpha_pull, color=C_PULL, linestyle=":", linewidth=1.0,
                alpha=0.7)
ax_pull.text(-0.98, alpha_pull + 0.03, r"$\alpha = 0.40$",
             color=C_PULL, fontsize=8)
ax_pull.set_title("Pull (rules 6 & 7)\n" r"$\alpha = 0.40$ (clipped)",
                  fontsize=10)
style_small_panel(ax_pull)

# ---------------------------------------------------------------------------
# Top-row panel: None
# ---------------------------------------------------------------------------
ax_none = fig.add_subplot(gs[0, 1])
ax_none.plot(F, full_none, linestyle="--", color=C_DASH, linewidth=1.2,
             label="Full MF")
ax_none.plot(F, clip_none, color=C_NONE, linewidth=2.2, label="Clipped")
ax_none.fill_between(F, 0, clip_none, color=C_NONE, alpha=0.35)
ax_none.axhline(alpha_none, color=C_NONE, linestyle=":", linewidth=1.0,
                alpha=0.7)
ax_none.text(-0.48, alpha_none + 0.03, r"$\alpha = 0.20$",
             color=C_NONE, fontsize=8)
ax_none.set_title("None (rule 5)\n" r"$\alpha = 0.20$ (clipped)",
                  fontsize=10)
style_small_panel(ax_none)

# ---------------------------------------------------------------------------
# Top-row panel: Push
# ---------------------------------------------------------------------------
ax_push = fig.add_subplot(gs[0, 2])
ax_push.plot(F, full_push, linestyle="--", color=C_DASH, linewidth=1.2,
             label="Full MF")
ax_push.text(0.5, 0.55, "not activated", ha="center", va="center",
             color=C_PUSH, fontsize=11, style="italic",
             bbox=dict(boxstyle="round,pad=0.3", fc="white",
                       ec=C_PUSH, alpha=0.85))
ax_push.set_title("Push (no rules)\n" r"$\alpha = 0$ (inactive)",
                  fontsize=10)
style_small_panel(ax_push)

# ---------------------------------------------------------------------------
# Bottom: union panel
# ---------------------------------------------------------------------------
ax_u = fig.add_subplot(gs[1, :])

# Unclipped reference triangles
ax_u.plot(F, full_pull, linestyle="--", color=C_DASH, linewidth=1.1,
          label="Full MF (unclipped)")
ax_u.plot(F, full_none, linestyle="--", color=C_DASH, linewidth=1.1)
ax_u.plot(F, full_push, linestyle="--", color=C_DASH, linewidth=1.1)

# Clipped consequents with fill
ax_u.fill_between(F, 0, clip_pull, color=C_PULL, alpha=0.30)
ax_u.plot(F, clip_pull, color=C_PULL, linewidth=2.0,
          label=r"Pull clipped ($\alpha=0.40$)")

ax_u.fill_between(F, 0, clip_none, color=C_NONE, alpha=0.30)
ax_u.plot(F, clip_none, color=C_NONE, linewidth=2.0,
          label=r"None clipped ($\alpha=0.20$)")

# Union envelope on top
ax_u.plot(F, mu_agg, color=C_UNION, linewidth=3.0,
          label="Union envelope (max)")

# Centroid marker
ax_u.axvline(centroid, color="purple", linestyle="-.", linewidth=1.6)
ax_u.plot([centroid], [0.02], marker="v", color="purple", markersize=10)
ax_u.text(
    centroid + 0.02,
    0.95,
    f"F* = {centroid:.2f} N",
    color="purple",
    fontsize=10,
    fontweight="bold",
)

# Arrow to Pull flat top
ax_u.annotate(
    r"Pull dominates ($\alpha = 0.4$)",
    xy=(-0.8, 0.40),
    xytext=(-0.2, 0.80),
    fontsize=10,
    color=C_PULL,
    arrowprops=dict(arrowstyle="->", color=C_PULL, lw=1.4,
                    connectionstyle="arc3,rad=-0.2"),
)

# "Push: not activated" note
ax_u.text(0.75, 0.15, "Push: not activated", ha="center", va="center",
          color=C_PUSH, fontsize=9, style="italic",
          bbox=dict(boxstyle="round,pad=0.25", fc="white",
                    ec=C_PUSH, alpha=0.85))

ax_u.set_xlim(-1.1, 1.1)
ax_u.set_ylim(0.0, 1.05)
ax_u.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
ax_u.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax_u.set_xlabel("F (N)", fontsize=11)
ax_u.set_ylabel(r"$\mu(F)$", fontsize=11)
ax_u.set_title("Control action rules (union of all clipped MFs)",
               fontsize=12)
ax_u.grid(True, alpha=0.25)
ax_u.legend(loc="upper right", fontsize=8.5, framealpha=0.9)

fig.suptitle(
    "Q4(c) - Sup-Min Control Action Rules (Slide 39-40 style)",
    fontsize=13,
    fontweight="bold",
)

out_path = (
    "/home/devel/electrical_notes/content/sys_304/exam3/"
    "python_photos/07_sup_min_slide_style.png"
)
fig.savefig(out_path, dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"Saved: {out_path}")
print(f"Centroid F* = {centroid:.4f} N  (rounded: {centroid:.2f} N)")
