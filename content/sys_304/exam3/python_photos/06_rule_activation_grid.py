"""
Question 4(b) - Rule Activation Grid for x = 5 ft, v = 0.8 ft/s.

Visualizes the 3x3 rule table with eliminated rules struck through and active
rules highlighted, colored by consequent.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---------------------------------------------------------------
# Inputs and memberships
# ---------------------------------------------------------------
# Position memberships at x = 5 ft
mu_pos = {"Left": 0.0, "Middle": 0.5, "Right": 0.25}
# Velocity memberships at v = 0.8 ft/s
mu_vel = {"Moving Left": 0.0, "Standing Still": 0.2, "Moving Right": 0.4}

pos_order = ["Left", "Middle", "Right"]           # rows (top -> bottom)
vel_order = ["Moving Left", "Standing Still", "Moving Right"]  # cols (left -> right)

# Rule table: (row_position, col_velocity) -> (rule_number, consequent)
rule_table = {
    ("Left",   "Moving Left"):     (1, "Push"),
    ("Left",   "Standing Still"):  (2, "Push"),
    ("Left",   "Moving Right"):    (3, "None"),
    ("Middle", "Moving Left"):     (4, "Push"),
    ("Middle", "Standing Still"):  (5, "None"),
    ("Middle", "Moving Right"):    (6, "Pull"),
    ("Right",  "Moving Left"):     (9, "None"),
    ("Right",  "Standing Still"):  (8, "Pull"),
    ("Right",  "Moving Right"):    (7, "Pull"),
}

# Colors by consequent (active)
active_colors = {
    "Push": "#cfe3ff",   # light blue
    "None": "#d2f0d2",   # light green
    "Pull": "#fcd0c8",   # salmon
}
eliminated_color = "#e6e6e6"  # light gray

# ---------------------------------------------------------------
# Figure & layout geometry
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 7))
ax.set_xlim(0, 11)
ax.set_ylim(0, 7)
ax.set_aspect("equal")
ax.axis("off")

# Grid cell size
cell_w = 1.7
cell_h = 1.3

# Origin of the 3x3 grid (lower-left of bottom-left cell)
grid_x0 = 2.8
grid_y0 = 1.6  # leave room for summary below

# Row y-coordinates: row 0 = Left (top), row 2 = Right (bottom)
def cell_bbox(row_idx, col_idx):
    x = grid_x0 + col_idx * cell_w
    # row_idx 0 -> top row
    y = grid_y0 + (2 - row_idx) * cell_h
    return x, y, cell_w, cell_h

# ---------------------------------------------------------------
# Faint band highlighting: nonzero rows and columns
# ---------------------------------------------------------------
grid_left = grid_x0
grid_right = grid_x0 + 3 * cell_w
grid_bottom = grid_y0
grid_top = grid_y0 + 3 * cell_h

band_color_vel = "#fff4cc"  # faint yellow for velocity columns
band_color_pos = "#e0ecff"  # faint blue for position rows

# Extend bands slightly above/left so they include the header strips
band_extra_top = 1.0   # above the grid into the velocity header strip
band_extra_left = 1.8  # to the left into the position header strip

for col_idx, vname in enumerate(vel_order):
    if mu_vel[vname] > 0:
        x = grid_x0 + col_idx * cell_w
        ax.add_patch(Rectangle(
            (x, grid_bottom),
            cell_w,
            3 * cell_h + band_extra_top,
            facecolor=band_color_vel, edgecolor="none", zorder=0,
        ))

for row_idx, pname in enumerate(pos_order):
    if mu_pos[pname] > 0:
        y = grid_y0 + (2 - row_idx) * cell_h
        ax.add_patch(Rectangle(
            (grid_left - band_extra_left, y),
            3 * cell_w + band_extra_left,
            cell_h,
            facecolor=band_color_pos, edgecolor="none", zorder=0,
        ))

# ---------------------------------------------------------------
# Column headers (velocity)
# ---------------------------------------------------------------
header_y = grid_top + 0.25
for col_idx, vname in enumerate(vel_order):
    x_center = grid_x0 + col_idx * cell_w + cell_w / 2
    ax.text(
        x_center, header_y + 0.45,
        vname,
        ha="center", va="center",
        fontsize=11, fontweight="bold",
    )
    ax.text(
        x_center, header_y + 0.1,
        rf"$\mu$ = {mu_vel[vname]:.1f}",
        ha="center", va="center",
        fontsize=10,
    )

# ---------------------------------------------------------------
# Row headers (position)
# ---------------------------------------------------------------
for row_idx, pname in enumerate(pos_order):
    y_center = grid_y0 + (2 - row_idx) * cell_h + cell_h / 2
    ax.text(
        grid_x0 - 0.15, y_center + 0.15,
        pname,
        ha="right", va="center",
        fontsize=11, fontweight="bold",
    )
    ax.text(
        grid_x0 - 0.15, y_center - 0.2,
        rf"$\mu$ = {mu_pos[pname]:.2f}" if mu_pos[pname] not in (0.0, 0.5) else rf"$\mu$ = {mu_pos[pname]:.1f}",
        ha="right", va="center",
        fontsize=10,
    )

# Axis label (position axis only; velocity label would collide with the title)
ax.text(
    grid_x0 - 1.7, grid_y0 + 1.5 * cell_h,
    "Position\n(rows)",
    ha="center", va="center",
    fontsize=10, fontstyle="italic", color="#555555",
    rotation=90,
)

# ---------------------------------------------------------------
# Draw cells
# ---------------------------------------------------------------
for row_idx, pname in enumerate(pos_order):
    for col_idx, vname in enumerate(vel_order):
        rule_num, consequent = rule_table[(pname, vname)]
        mp = mu_pos[pname]
        mv = mu_vel[vname]
        active = (mp > 0) and (mv > 0)

        x, y, w, h = cell_bbox(row_idx, col_idx)

        if active:
            fill = active_colors[consequent]
            edge = "#333333"
            lw = 1.8
        else:
            fill = eliminated_color
            edge = "#888888"
            lw = 1.0

        ax.add_patch(Rectangle(
            (x, y), w, h,
            facecolor=fill, edgecolor=edge, linewidth=lw, zorder=2,
        ))

        # Text positions within the cell
        cx = x + w / 2
        y_line1 = y + h - 0.25
        y_line2 = y + h / 2 + 0.05
        y_line3 = y + 0.25

        # Line 1: "Rule k"
        label_rule = f"Rule {rule_num}"
        t1 = ax.text(
            cx, y_line1, label_rule,
            ha="center", va="center",
            fontsize=10, fontweight="bold",
            color="#444444" if not active else "#111111",
            zorder=3,
        )

        # Line 2: "→ <consequent>"
        arrow_text = f"→ {consequent}"
        t2 = ax.text(
            cx, y_line2, arrow_text,
            ha="center", va="center",
            fontsize=12,
            color="#444444" if not active else "#111111",
            fontweight="bold" if active else "normal",
            zorder=3,
        )

        # Line 3: firing strength or eliminated tag
        if active:
            fire = min(mp, mv)
            line3a = f"fire = min({mp:.2f}, {mv:.2f})"
            line3b = f"     = {fire:.2f}"
            ax.text(
                cx, y_line3 + 0.15, line3a,
                ha="center", va="center",
                fontsize=7.5, color="#222222",
                zorder=3,
            )
            ax.text(
                cx, y_line3 - 0.12, line3b,
                ha="center", va="center",
                fontsize=7.5, color="#222222",
                fontweight="bold",
                zorder=3,
            )
        else:
            # Mark eliminated: strikethrough t1 and t2, and add an "eliminated" note
            # Draw strikethrough lines through the rule label and arrow text.
            # Use the approximate horizontal extent of the text (cell width minus padding).
            strike_pad = 0.25
            ax.plot(
                [x + strike_pad, x + w - strike_pad],
                [y_line1, y_line1],
                color="#666666", linewidth=1.2, zorder=4,
            )
            ax.plot(
                [x + strike_pad, x + w - strike_pad],
                [y_line2, y_line2],
                color="#666666", linewidth=1.2, zorder=4,
            )
            ax.text(
                cx, y_line3, "✗ eliminated",
                ha="center", va="center",
                fontsize=9, color="#a33",
                fontstyle="italic",
                zorder=3,
            )

# ---------------------------------------------------------------
# Summary box below grid
# ---------------------------------------------------------------
summary_x = grid_x0 - band_extra_left
summary_y = 0.25
summary_w = 3 * cell_w + band_extra_left + 0.2
summary_h = 1.1

ax.add_patch(Rectangle(
    (summary_x, summary_y), summary_w, summary_h,
    facecolor="#fafafa", edgecolor="#555555", linewidth=1.0, zorder=1,
))

ax.text(
    summary_x + 0.15, summary_y + summary_h - 0.3,
    "Active rules: 5, 6, 7, 8.",
    ha="left", va="center",
    fontsize=11, fontweight="bold", color="#073",
    zorder=2,
)
ax.text(
    summary_x + 0.15, summary_y + summary_h - 0.75,
    r"Eliminated ($\mu$ = 0 in at least one antecedent): 1, 2, 3, 4, 9.",
    ha="left", va="center",
    fontsize=10, color="#444444",
    zorder=2,
)

# ---------------------------------------------------------------
# Title
# ---------------------------------------------------------------
ax.text(
    5.5, 6.75,
    "Question 4(b) — Rule Activation at x = 5 ft, v = 0.8 ft/s",
    ha="center", va="center",
    fontsize=13, fontweight="bold",
)

# ---------------------------------------------------------------
# Small legend for consequent colors (top-right)
# ---------------------------------------------------------------
legend_items = [
    ("Push (active)", active_colors["Push"]),
    ("None (active)", active_colors["None"]),
    ("Pull (active)", active_colors["Pull"]),
    ("Eliminated",    eliminated_color),
]
legend_x0 = 9.1
legend_y0 = 6.2
swatch_w = 0.35
swatch_h = 0.22
row_gap = 0.32

for i, (label, color) in enumerate(legend_items):
    ly = legend_y0 - i * row_gap
    ax.add_patch(Rectangle(
        (legend_x0, ly), swatch_w, swatch_h,
        facecolor=color, edgecolor="#333333", linewidth=0.8, zorder=2,
    ))
    ax.text(
        legend_x0 + swatch_w + 0.1, ly + swatch_h / 2,
        label,
        ha="left", va="center",
        fontsize=9, zorder=2,
    )

# ---------------------------------------------------------------
# Save
# ---------------------------------------------------------------
out_path = (
    "/home/devel/electrical_notes/content/sys_304/exam3/"
    "python_photos/06_rule_activation_grid.png"
)
plt.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Wrote {out_path}")
