"""
SYS 304 Exam 3 - Question 2 Solution Diagram
Payoff matrix with row minima, column maxima, and saddle points highlighted.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np

# Payoff matrix
payoff = np.array([
    [2, 3, 1, 4],
    [3, 4, 3, 5],
    [1, 3, 0, 3],
    [2, 5, 2, 3],
])
n_rows, n_cols = payoff.shape

row_mins = payoff.min(axis=1)   # [1, 3, 0, 2]
col_maxes = payoff.max(axis=0)  # [3, 5, 3, 5]
maximin = row_mins.max()        # 3
minimax = col_maxes.min()       # 3

# Determine cell categories
row_min_cells = set()
for i in range(n_rows):
    for j in range(n_cols):
        if payoff[i, j] == row_mins[i]:
            row_min_cells.add((i, j))

col_max_cells = set()
for j in range(n_cols):
    for i in range(n_rows):
        if payoff[i, j] == col_maxes[j]:
            col_max_cells.add((i, j))

saddle_cells = row_min_cells & col_max_cells

# Colors
COLOR_HEADER = "#dcdcdc"
COLOR_ROW_MIN = "#b5d8f2"   # light blue
COLOR_COL_MAX = "#ffd7a8"   # light orange
COLOR_SADDLE = "#b8e6a8"    # light green
COLOR_SUMMARY = "#f0f0f0"   # light gray for corner

# Geometry: use a grid with origin at top-left
# Columns: [row-label] [C1 C2 C3 C4] [Row min]   -> 6 columns total
# Rows:    [col-label] [R1 R2 R3 R4] [Col max]   -> 6 rows total
cell_w = 1.4
cell_h = 1.0

# We will draw with (0,0) in top-left; invert y by negating.
def xy(col, row):
    """col, row are grid indices starting at 0 (top-left)."""
    x = col * cell_w
    y = -row * cell_h
    return x, y

fig, ax = plt.subplots(figsize=(9, 6))
ax.axis("off")

total_cols = 6  # 1 row-header + 4 payoff + 1 row-min
total_rows = 6  # 1 col-header + 4 payoff + 1 col-max

def draw_cell(col, row, text, facecolor="white", edgecolor="black",
              linewidth=1.0, fontsize=12, fontweight="normal", text_color="black"):
    x, y = xy(col, row)
    rect = Rectangle((x, y - cell_h), cell_w, cell_h,
                     facecolor=facecolor, edgecolor=edgecolor,
                     linewidth=linewidth)
    ax.add_patch(rect)
    if text is not None:
        ax.text(x + cell_w / 2, y - cell_h / 2, text,
                ha="center", va="center",
                fontsize=fontsize, fontweight=fontweight, color=text_color)

# Top-left empty corner
draw_cell(0, 0, "", facecolor=COLOR_HEADER)

# Column headers (C1..C4) in row 0, cols 1..4
for j in range(n_cols):
    draw_cell(1 + j, 0, f"C{j+1}", facecolor=COLOR_HEADER,
              fontsize=13, fontweight="bold")

# "Row min" header at top-right (row 0, col 5)
draw_cell(5, 0, "Row min", facecolor=COLOR_HEADER,
          fontsize=11, fontweight="bold")

# Row headers (R1..R4) in col 0, rows 1..4
for i in range(n_rows):
    draw_cell(0, 1 + i, f"R{i+1}", facecolor=COLOR_HEADER,
              fontsize=13, fontweight="bold")

# "Col max" header at bottom-left (row 5, col 0)
draw_cell(0, 5, "Col max", facecolor=COLOR_HEADER,
          fontsize=11, fontweight="bold")

# Payoff cells
for i in range(n_rows):
    for j in range(n_cols):
        val = payoff[i, j]
        is_rmin = (i, j) in row_min_cells
        is_cmax = (i, j) in col_max_cells
        is_saddle = (i, j) in saddle_cells

        if is_saddle:
            facecolor = COLOR_SADDLE
            edgecolor = "black"
            linewidth = 2.8
            fontweight = "bold"
        elif is_rmin:
            facecolor = COLOR_ROW_MIN
            edgecolor = "black"
            linewidth = 1.0
            fontweight = "normal"
        elif is_cmax:
            facecolor = COLOR_COL_MAX
            edgecolor = "black"
            linewidth = 1.0
            fontweight = "normal"
        else:
            facecolor = "white"
            edgecolor = "black"
            linewidth = 1.0
            fontweight = "normal"

        draw_cell(1 + j, 1 + i, str(val),
                  facecolor=facecolor, edgecolor=edgecolor,
                  linewidth=linewidth, fontsize=14, fontweight=fontweight)

        # Add a star for saddle cells
        if is_saddle:
            x, y = xy(1 + j, 1 + i)
            ax.text(x + cell_w - 0.12, y - 0.18, "★",
                    ha="right", va="top", fontsize=14,
                    color="#b8860b", fontweight="bold")

# Row min column (col 5, rows 1..4)
for i in range(n_rows):
    text = str(row_mins[i])
    # Bold if this row's min equals the maximin
    fw = "bold" if row_mins[i] == maximin else "normal"
    fc = COLOR_ROW_MIN if row_mins[i] == maximin else "white"
    draw_cell(5, 1 + i, text, facecolor=fc, fontsize=13, fontweight=fw)

# Col max row (row 5, cols 1..4)
for j in range(n_cols):
    text = str(col_maxes[j])
    fw = "bold" if col_maxes[j] == minimax else "normal"
    fc = COLOR_COL_MAX if col_maxes[j] == minimax else "white"
    draw_cell(1 + j, 5, text, facecolor=fc, fontsize=13, fontweight=fw)

# Bottom-right corner cell — show maximin and minimax
x_c, y_c = xy(5, 5)
rect = Rectangle((x_c, y_c - cell_h), cell_w, cell_h,
                 facecolor=COLOR_SUMMARY, edgecolor="black", linewidth=1.5)
ax.add_patch(rect)
ax.text(x_c + cell_w / 2, y_c - cell_h / 2 + 0.18,
        f"maximin = {maximin}", ha="center", va="center",
        fontsize=10, fontweight="bold", color="#0b5394")
ax.text(x_c + cell_w / 2, y_c - cell_h / 2 - 0.18,
        f"minimax = {minimax}", ha="center", va="center",
        fontsize=10, fontweight="bold", color="#b45f06")

# Title
ax.set_title("Question 2 — Payoff Matrix with Row Mins, Col Maxes, and Saddle Points",
             fontsize=13, fontweight="bold", pad=14)

# Legend (drawn below the table)
legend_y = -total_rows * cell_h - 0.6
legend_entries = [
    (COLOR_ROW_MIN, "Row min cell"),
    (COLOR_COL_MAX, "Col max cell"),
    (COLOR_SADDLE, "Saddle point (row min AND col max)"),
]
legend_x = 0.0
box_w = 0.45
box_h = 0.35
spacing = 0.1

entry_widths = [2.6, 2.6, 5.5]  # pre-sized slots (in data units)
x_cursor = legend_x
for (color, label), slot_w in zip(legend_entries, entry_widths):
    rect = Rectangle((x_cursor, legend_y - box_h), box_w, box_h,
                     facecolor=color, edgecolor="black", linewidth=1.0)
    ax.add_patch(rect)
    ax.text(x_cursor + box_w + 0.15, legend_y - box_h / 2, label,
            ha="left", va="center", fontsize=10)
    x_cursor += slot_w

# Caption below legend
caption_y = legend_y - box_h - 0.7
ax.text(0.0, caption_y,
        f"Saddle points at (R2, C1) and (R2, C3), value = {maximin}.",
        ha="left", va="top", fontsize=11, fontweight="bold")
ax.text(0.0, caption_y - 0.5,
        "Since maximin = minimax, a saddle point exists (pure-strategy equilibrium).",
        ha="left", va="top", fontsize=10, style="italic")

# Set limits with margin
ax.set_xlim(-0.3, total_cols * cell_w + 0.3)
ax.set_ylim(caption_y - 1.5, 0.8)
ax.set_aspect("equal")

out_path = "/home/devel/electrical_notes/content/sys_304/exam3/python_photos/05_game_theory_payoff_saddle.png"
plt.savefig(out_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {out_path}")
