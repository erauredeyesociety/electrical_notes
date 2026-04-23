"""QFD House of Quality — Commuter Backpack (SYS 304 Exam 3 Q3).

Matches the exam worksheet format:
- Competitive Assessment columns labeled 1..5 (graphic assessment)
- Objective Measures block under the relationship matrix, label rotated 90°
"""

import matplotlib

matplotlib.use("Agg")

import os

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

CRS = [
    ("CR1 Comfort", 5),
    ("CR2 Protection", 5),
    ("CR3 Capacity", 4),
    ("CR4 Organization", 4),
    ("CR5 Affordability", 3),
]

TRS = [
    "TR1 Strap padding (mm)",
    "TR2 Laptop protection rating",
    "TR3 Usable volume (L)",
    "TR4 Quick-access compartments",
    "TR5 Manufacturing cost ($)",
]

# CR x TR relationship: 9 strong, 3 medium, 1 weak, 0 blank
REL = [
    [9, 1, 3, 1, 1],
    [1, 9, 1, 1, 1],
    [3, 1, 9, 3, 1],
    [1, 1, 3, 9, 1],
    [1, 1, 1, 1, 9],
]

TECH_IMPORTANCE = [69, 61, 71, 61, 45]

# Roof: upper triangular (i < j). "+", "-", or None.
ROOF = {
    (0, 1): "+",
    (0, 2): "-",
    (0, 3): None,
    (0, 4): "-",
    (1, 2): None,
    (1, 3): None,
    (1, 4): "-",
    (2, 3): None,
    (2, 4): "-",
    (3, 4): "-",
}

# Graphic competitive assessment: three competitors, rating 1..5 per CR
COMPETITORS = ["JanSport", "Borealis", "SwissGear"]
COMP = [
    [3, 5, 4],
    [2, 4, 5],
    [3, 4, 5],
    [2, 4, 5],
    [5, 2, 3],
]
COMP_MARKERS = ["o", "^", "s"]  # circle, triangle, square
COMP_COLORS = ["#c0392b", "#2874a6", "#1e8449"]

# Objective Measures block — 3 rows x N_TR cols
OBJ_MEAS_ROWS = ["Target value", "Direction of improvement", "Units"]
OBJ_MEAS = [
    ["≥ 14 mm", "5/5", "28–30 L", "4", "≤ $32"],
    ["↑", "↑", "↑", "↑", "↓"],
    ["mm", "1-5 rating", "L", "count", "$"],
]

# ---------------------------------------------------------------------------
# Layout constants (axis coordinates)
# ---------------------------------------------------------------------------

CR_X0 = 0.0
CR_W = 5.0

IMP_X0 = CR_X0 + CR_W
IMP_W = 1.2

REL_X0 = IMP_X0 + IMP_W
REL_CELL_W = 1.55
REL_CELL_H = 1.0
N_TR = len(TRS)
N_CR = len(CRS)
REL_W = REL_CELL_W * N_TR

COMP_GAP = 0.6
COMP_X0 = REL_X0 + REL_W + COMP_GAP
COMP_CELL_W = 0.85
COMP_CELL_H = REL_CELL_H
N_COMP_COLS = 5  # rating 1..5
COMP_W = COMP_CELL_W * N_COMP_COLS

TOTAL_RIGHT = COMP_X0 + COMP_W

# Y layout (bottom to top)
BAR_H = 1.4
OBJ_ROW_H = 0.75
N_OBJ_ROWS = len(OBJ_MEAS_ROWS)
OBJ_BLOCK_H = OBJ_ROW_H * N_OBJ_ROWS
TECH_H = 0.7

# Column for the rotated "Objective Measures" label on the LEFT side of the OM block
OBJ_LABEL_W = 1.0

REL_Y0 = BAR_H + OBJ_BLOCK_H + TECH_H
REL_H = REL_CELL_H * N_CR

TR_HEADER_H = 2.8
TR_HEADER_Y0 = REL_Y0 + REL_H

CR_HEADER_STRIP_H = 0.9
COMP_HEADER_STRIP_H = CR_HEADER_STRIP_H  # 1..5 column headers

ROOF_DIAG = REL_CELL_W
ROOF_ROW_H = ROOF_DIAG / 2
ROOF_Y0 = TR_HEADER_Y0 + TR_HEADER_H

ROOF_TOTAL_H = (N_TR - 1) * ROOF_ROW_H + ROOF_DIAG / 2 + 0.4

PAD = 0.6
X_MIN = CR_X0 - PAD
X_MAX = TOTAL_RIGHT + PAD

LEGEND_H = 1.6
LEGEND_Y_TOP = -0.4
LEGEND_Y_BOTTOM = LEGEND_Y_TOP - LEGEND_H

Y_MIN = LEGEND_Y_BOTTOM - PAD
Y_MAX = ROOF_Y0 + ROOF_TOTAL_H + 1.2

# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
COLOR_CR_BG = "#f5f0e6"
COLOR_IMP_BG = "#fff6d6"
COLOR_TR_HEADER_BG = "#eaf2fb"
COLOR_REL_BG = "#ffffff"
COLOR_COMP_HEADER_BG = "#e8f5ec"
COLOR_COMP_BG = "#f2faf4"
COLOR_TECH_BG = "#fde7e1"
COLOR_OBJ_BG = "#f1e6fa"
COLOR_OBJ_LABEL_BG = "#d9c8ea"
COLOR_BAR_BG = "#fafafa"
COLOR_ROOF_BG = "#fbfbfb"
COLOR_LEGEND_BG = "#fafafa"
COLOR_BAR = "#e08a3e"
COLOR_STRONG = "#1f3c63"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def tr_col_x(i):
    return REL_X0 + (i + 0.5) * REL_CELL_W


def comp_col_x(j):
    """j is 0..4 => rating 1..5"""
    return COMP_X0 + (j + 0.5) * COMP_CELL_W


def cr_row_y(i):
    return REL_Y0 + REL_H - (i + 0.5) * REL_CELL_H


def draw_region(ax, x0, y0, w, h, color, zorder=0.5):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=color, edgecolor="none", zorder=zorder))


def draw_grid(ax, x0, y0, w, h, nx, ny, color="#b9b9b9", lw=0.9, zorder=1.5):
    ax.add_patch(
        Rectangle((x0, y0), w, h, facecolor="none", edgecolor=color, linewidth=lw, zorder=zorder)
    )
    dx = w / nx
    dy = h / ny
    for i in range(1, nx):
        ax.plot([x0 + i * dx, x0 + i * dx], [y0, y0 + h], color=color, linewidth=lw, zorder=zorder)
    for j in range(1, ny):
        ax.plot([x0, x0 + w], [y0 + j * dy, y0 + j * dy], color=color, linewidth=lw, zorder=zorder)


def draw_rel_symbol(ax, cx, cy, strength):
    if strength == 9:
        ax.add_patch(Circle((cx - 0.3, cy), 0.22, facecolor=COLOR_STRONG,
                            edgecolor="black", linewidth=0.8, zorder=3))
    elif strength == 3:
        ax.add_patch(Circle((cx - 0.3, cy), 0.22, facecolor="white",
                            edgecolor="black", linewidth=1.1, zorder=3))
    elif strength == 1:
        tri = Polygon(
            [
                (cx - 0.3, cy + 0.22),
                (cx - 0.3 - 0.22, cy - 0.17),
                (cx - 0.3 + 0.22, cy - 0.17),
            ],
            closed=True, facecolor="white", edgecolor="black", linewidth=1.0, zorder=3,
        )
        ax.add_patch(tri)
    else:
        return
    ax.text(cx + 0.32, cy, str(strength), ha="center", va="center",
            fontsize=9, zorder=4)


def draw_diamond(ax, cx, cy, diag, symbol):
    half = diag / 2
    pts = [(cx, cy + half), (cx + half, cy), (cx, cy - half), (cx - half, cy)]
    face = "#ffffff"
    if symbol == "+":
        face = "#e8f1fb"
    elif symbol == "-":
        face = "#fbeaea"
    ax.add_patch(Polygon(pts, closed=True, facecolor=face, edgecolor="#7a7a7a",
                         linewidth=0.8, zorder=2))
    if symbol in ("+", "-"):
        disp = "+" if symbol == "+" else "−"
        ax.text(cx, cy, disp, ha="center", va="center", fontsize=14,
                fontweight="bold",
                color=("#234f8c" if symbol == "+" else "#9b2d2d"),
                zorder=3)


def draw_comp_marker(ax, cx, cy, marker, color):
    size = 90
    ax.scatter([cx], [cy], marker=marker, s=size, facecolor=color,
               edgecolor="black", linewidths=0.8, zorder=4)


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def build():
    fig, ax = plt.subplots(figsize=(18, 15))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(Y_MIN, Y_MAX)

    ax.text(
        (X_MIN + X_MAX) / 2,
        Y_MAX - 0.35,
        "House of Quality — Commuter Backpack for Engineering Students",
        ha="center", va="top", fontsize=15, fontweight="bold",
    )

    # ---- Region backgrounds --------------------------------------------
    cr_header_y = REL_Y0 + REL_H
    draw_region(ax, CR_X0, cr_header_y, CR_W, CR_HEADER_STRIP_H, COLOR_CR_BG)
    draw_region(ax, IMP_X0, cr_header_y, IMP_W, CR_HEADER_STRIP_H, COLOR_IMP_BG)
    draw_region(ax, CR_X0, REL_Y0, CR_W, REL_H, COLOR_CR_BG)
    draw_region(ax, IMP_X0, REL_Y0, IMP_W, REL_H, COLOR_IMP_BG)
    draw_region(ax, REL_X0, REL_Y0, REL_W, REL_H, COLOR_REL_BG)
    draw_region(ax, COMP_X0, REL_Y0, COMP_W, REL_H, COLOR_COMP_BG)
    draw_region(ax, REL_X0, TR_HEADER_Y0, REL_W, TR_HEADER_H, COLOR_TR_HEADER_BG)

    # Competitive Assessment header strip (1..5 columns)
    draw_region(ax, COMP_X0, cr_header_y, COMP_W, COMP_HEADER_STRIP_H, COLOR_COMP_HEADER_BG)

    # "Competitive Assessment" title bar ABOVE the 1..5 strip
    comp_title_y = cr_header_y + COMP_HEADER_STRIP_H
    comp_title_h = 0.7
    draw_region(ax, COMP_X0, comp_title_y, COMP_W, comp_title_h, COLOR_COMP_HEADER_BG)
    ax.add_patch(Rectangle((COMP_X0, comp_title_y), COMP_W, comp_title_h,
                           facecolor="none", edgecolor="#7a7a7a", linewidth=1.0, zorder=1.5))
    ax.text(COMP_X0 + COMP_W / 2, comp_title_y + comp_title_h / 2,
            "Competitive Assessment", ha="center", va="center",
            fontsize=11, fontweight="bold")

    tech_y0 = REL_Y0 - TECH_H
    draw_region(ax, CR_X0, tech_y0, REL_X0 + REL_W - CR_X0, TECH_H, COLOR_TECH_BG)

    # Objective Measures block + label column
    obj_y0 = tech_y0 - OBJ_BLOCK_H
    obj_label_x0 = CR_X0
    obj_label_w = OBJ_LABEL_W
    obj_body_x0 = obj_label_x0 + obj_label_w
    obj_body_w = REL_X0 + REL_W - obj_body_x0

    # sub-label column (row labels for the OM rows)
    obj_rowlabel_w = CR_W + IMP_W - obj_label_w
    obj_rowlabel_x0 = obj_body_x0
    obj_grid_x0 = REL_X0
    obj_grid_w = REL_W

    draw_region(ax, obj_label_x0, obj_y0, obj_label_w, OBJ_BLOCK_H, COLOR_OBJ_LABEL_BG)
    draw_region(ax, obj_rowlabel_x0, obj_y0, obj_rowlabel_w, OBJ_BLOCK_H, COLOR_OBJ_BG)
    draw_region(ax, obj_grid_x0, obj_y0, obj_grid_w, OBJ_BLOCK_H, COLOR_OBJ_BG)

    bar_y0 = obj_y0 - BAR_H
    draw_region(ax, CR_X0, bar_y0, REL_X0 + REL_W - CR_X0, BAR_H, COLOR_BAR_BG)

    draw_region(ax, REL_X0 - 0.2, ROOF_Y0 - 0.05, REL_W + 0.4, ROOF_TOTAL_H, COLOR_ROOF_BG)

    # ---- Headers -------------------------------------------------------
    ax.text(CR_X0 + CR_W / 2, cr_header_y + CR_HEADER_STRIP_H / 2,
            "Customer Requirement", ha="center", va="center",
            fontsize=11, fontweight="bold")
    # "Importance" rotated 90° in its header strip
    ax.text(IMP_X0 + IMP_W / 2, cr_header_y + CR_HEADER_STRIP_H / 2,
            "Importance", ha="center", va="center", fontsize=10,
            fontweight="bold", rotation=90)

    # borders on CR/Imp header strips
    ax.add_patch(Rectangle((CR_X0, cr_header_y), CR_W, CR_HEADER_STRIP_H,
                           facecolor="none", edgecolor="#7a7a7a", linewidth=1.0, zorder=1.5))
    ax.add_patch(Rectangle((IMP_X0, cr_header_y), IMP_W, CR_HEADER_STRIP_H,
                           facecolor="none", edgecolor="#7a7a7a", linewidth=1.0, zorder=1.5))

    # 1..5 rating scale column headers
    ax.add_patch(Rectangle((COMP_X0, cr_header_y), COMP_W, COMP_HEADER_STRIP_H,
                           facecolor="none", edgecolor="#7a7a7a", linewidth=1.0, zorder=1.5))
    for j in range(N_COMP_COLS):
        cx = comp_col_x(j)
        ax.text(cx, cr_header_y + COMP_HEADER_STRIP_H / 2, str(j + 1),
                ha="center", va="center", fontsize=12, fontweight="bold")
        if j > 0:
            ax.plot([COMP_X0 + j * COMP_CELL_W, COMP_X0 + j * COMP_CELL_W],
                    [cr_header_y, cr_header_y + COMP_HEADER_STRIP_H],
                    color="#7a7a7a", linewidth=0.8, zorder=1.6)

    # ---- CR rows / Importance ------------------------------------------
    draw_grid(ax, CR_X0, REL_Y0, CR_W, REL_H, 1, N_CR)
    draw_grid(ax, IMP_X0, REL_Y0, IMP_W, REL_H, 1, N_CR)
    for i, (name, imp) in enumerate(CRS):
        y = cr_row_y(i)
        ax.text(CR_X0 + 0.25, y, name, ha="left", va="center", fontsize=10)
        ax.text(IMP_X0 + IMP_W / 2, y, str(imp), ha="center", va="center",
                fontsize=11, fontweight="bold")

    # ---- Relationship matrix -------------------------------------------
    draw_grid(ax, REL_X0, REL_Y0, REL_W, REL_H, N_TR, N_CR)
    for i in range(N_CR):
        for j in range(N_TR):
            draw_rel_symbol(ax, tr_col_x(j), cr_row_y(i), REL[i][j])

    # ---- TR header strip -----------------------------------------------
    ax.add_patch(Rectangle((REL_X0, TR_HEADER_Y0), REL_W, TR_HEADER_H,
                           facecolor="none", edgecolor="#7a7a7a", linewidth=1.0, zorder=1.5))
    tr_code_band_h = 0.45
    ax.add_patch(Rectangle((REL_X0, TR_HEADER_Y0), REL_W, tr_code_band_h,
                           facecolor="#d6e3f3", edgecolor="#7a7a7a", linewidth=0.8, zorder=1.6))

    # "Design Characteristics" banner above TR labels
    dc_y = TR_HEADER_Y0 + TR_HEADER_H - 0.45
    ax.add_patch(Rectangle((REL_X0, dc_y), REL_W, 0.45,
                           facecolor="#c7dbf1", edgecolor="#7a7a7a",
                           linewidth=0.8, zorder=1.6))
    ax.text(REL_X0 + REL_W / 2, dc_y + 0.225,
            "Design Characteristics", ha="center", va="center",
            fontsize=11, fontweight="bold")

    for j, tr in enumerate(TRS):
        code, _, rest = tr.partition(" ")
        cx = tr_col_x(j)
        ax.text(cx, TR_HEADER_Y0 + tr_code_band_h / 2, code,
                ha="center", va="center", fontsize=11, fontweight="bold")
        ax.text(
            cx - 0.1,
            TR_HEADER_Y0 + tr_code_band_h + 0.15,
            rest,
            ha="left", va="bottom",
            rotation=45, rotation_mode="anchor",
            fontsize=10,
        )
        if j > 0:
            ax.plot(
                [REL_X0 + j * REL_CELL_W, REL_X0 + j * REL_CELL_W],
                [TR_HEADER_Y0, TR_HEADER_Y0 + TR_HEADER_H],
                color="#b9b9b9", linewidth=0.8, zorder=1.55,
            )

    # ---- Competitive Assessment body (graphic) -------------------------
    ax.add_patch(Rectangle((COMP_X0, REL_Y0), COMP_W, REL_H,
                           facecolor="none", edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.5))
    draw_grid(ax, COMP_X0, REL_Y0, COMP_W, REL_H, N_COMP_COLS, N_CR)

    # markers + connecting profile lines per competitor
    for c_idx in range(len(COMPETITORS)):
        xs = []
        ys = []
        for i in range(N_CR):
            rating = COMP[i][c_idx]
            cx = comp_col_x(rating - 1)
            cy = cr_row_y(i)
            xs.append(cx)
            ys.append(cy)
        ax.plot(xs, ys, color=COMP_COLORS[c_idx], linewidth=1.2,
                alpha=0.55, zorder=3.5)
        for x, y in zip(xs, ys):
            draw_comp_marker(ax, x, y, COMP_MARKERS[c_idx], COMP_COLORS[c_idx])

    # ---- Tech importance row -------------------------------------------
    ax.add_patch(Rectangle((CR_X0, tech_y0), CR_W + IMP_W, TECH_H,
                           facecolor=COLOR_TECH_BG, edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.5))
    ax.text(CR_X0 + 0.25, tech_y0 + TECH_H / 2, "Technical importance",
            ha="left", va="center", fontsize=11, fontweight="bold")
    draw_grid(ax, REL_X0, tech_y0, REL_W, TECH_H, N_TR, 1)
    for j, v in enumerate(TECH_IMPORTANCE):
        ax.text(tr_col_x(j), tech_y0 + TECH_H / 2, str(v),
                ha="center", va="center", fontsize=11, fontweight="bold")

    # ---- Objective Measures block --------------------------------------
    # Left label column (rotated 90°)
    ax.add_patch(Rectangle((obj_label_x0, obj_y0), obj_label_w, OBJ_BLOCK_H,
                           facecolor=COLOR_OBJ_LABEL_BG, edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.5))
    ax.text(obj_label_x0 + obj_label_w / 2, obj_y0 + OBJ_BLOCK_H / 2,
            "Objective Measures", ha="center", va="center",
            fontsize=11, fontweight="bold", rotation=90)

    # Row labels column
    ax.add_patch(Rectangle((obj_rowlabel_x0, obj_y0), obj_rowlabel_w, OBJ_BLOCK_H,
                           facecolor=COLOR_OBJ_BG, edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.5))
    draw_grid(ax, obj_rowlabel_x0, obj_y0, obj_rowlabel_w, OBJ_BLOCK_H, 1, N_OBJ_ROWS)

    # Value grid (aligned with TR columns)
    draw_grid(ax, obj_grid_x0, obj_y0, obj_grid_w, OBJ_BLOCK_H, N_TR, N_OBJ_ROWS)
    ax.add_patch(Rectangle((obj_grid_x0, obj_y0), obj_grid_w, OBJ_BLOCK_H,
                           facecolor="none", edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.55))

    for r, label in enumerate(OBJ_MEAS_ROWS):
        # rows from top to bottom: r=0 is top
        row_y = obj_y0 + OBJ_BLOCK_H - (r + 0.5) * OBJ_ROW_H
        ax.text(obj_rowlabel_x0 + 0.2, row_y, label,
                ha="left", va="center", fontsize=10, fontweight="bold")
        for j in range(N_TR):
            val = OBJ_MEAS[r][j]
            fs = 11 if r == 1 else 10
            fw = "bold" if r == 1 else "normal"
            ax.text(tr_col_x(j), row_y, val,
                    ha="center", va="center", fontsize=fs, fontweight=fw)

    # ---- Importance bar chart row --------------------------------------
    ax.add_patch(Rectangle((CR_X0, bar_y0), CR_W + IMP_W, BAR_H,
                           facecolor=COLOR_BAR_BG, edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.5))
    ax.text(CR_X0 + 0.25, bar_y0 + BAR_H / 2, "Tech. importance bar",
            ha="left", va="center", fontsize=11, fontweight="bold")
    ax.add_patch(Rectangle((REL_X0, bar_y0), REL_W, BAR_H,
                           facecolor="none", edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.5))
    max_imp = max(TECH_IMPORTANCE)
    bar_max_h = BAR_H - 0.55
    for j, v in enumerate(TECH_IMPORTANCE):
        cx = tr_col_x(j)
        h = bar_max_h * (v / max_imp)
        bw = REL_CELL_W * 0.55
        ax.add_patch(
            Rectangle((cx - bw / 2, bar_y0 + 0.1), bw, h,
                      facecolor=COLOR_BAR, edgecolor="#7a4a1e",
                      linewidth=0.8, zorder=2)
        )
        ax.text(cx, bar_y0 + 0.1 + h + 0.08, str(v),
                ha="center", va="bottom", fontsize=9, fontweight="bold")

    # ---- Roof ----------------------------------------------------------
    for k in range(1, N_TR):
        for i in range(N_TR - k):
            j = i + k
            cx = (tr_col_x(i) + tr_col_x(j)) / 2
            cy = ROOF_Y0 + (k - 0.5) * ROOF_ROW_H + ROOF_DIAG / 2
            sym = ROOF.get((i, j))
            draw_diamond(ax, cx, cy, ROOF_DIAG, sym)

    # "Tradeoff Matrix" caption near the roof apex
    roof_top = ROOF_Y0 + ROOF_TOTAL_H
    ax.text(REL_X0 + REL_W / 2, roof_top - 0.15, "Tradeoff Matrix",
            ha="center", va="top", fontsize=10, style="italic", color="#555")

    # ---- Legend --------------------------------------------------------
    legend_x0 = CR_X0
    legend_y0 = LEGEND_Y_BOTTOM
    legend_w = TOTAL_RIGHT - CR_X0
    ax.add_patch(Rectangle((legend_x0, legend_y0), legend_w, LEGEND_H,
                           facecolor=COLOR_LEGEND_BG, edgecolor="#7a7a7a",
                           linewidth=1.0, zorder=1.5))
    ax.text(legend_x0 + 0.25, legend_y0 + LEGEND_H - 0.25, "Legend",
            ha="left", va="top", fontsize=11, fontweight="bold")

    row1_y = legend_y0 + LEGEND_H - 0.65
    row2_y = legend_y0 + 0.40

    def legend_dot(x, y, kind):
        if kind == "strong":
            ax.add_patch(Circle((x, y), 0.18, facecolor=COLOR_STRONG,
                                edgecolor="black", linewidth=0.8, zorder=3))
        elif kind == "medium":
            ax.add_patch(Circle((x, y), 0.18, facecolor="white",
                                edgecolor="black", linewidth=1.1, zorder=3))
        elif kind == "weak":
            tri = Polygon(
                [(x, y + 0.2), (x - 0.2, y - 0.15), (x + 0.2, y - 0.15)],
                closed=True, facecolor="white", edgecolor="black",
                linewidth=1.0, zorder=3,
            )
            ax.add_patch(tri)

    # Row 1: relationship symbols + roof correlations
    items_row1 = [
        ("strong", "Strong (9)"),
        ("medium", "Medium (3)"),
        ("weak", "Weak (1)"),
    ]
    x = legend_x0 + 1.3
    for kind, label in items_row1:
        legend_dot(x, row1_y, kind)
        ax.text(x + 0.35, row1_y, label, ha="left", va="center", fontsize=10)
        x += 2.4

    ax.text(x, row1_y, "+", ha="center", va="center", fontsize=14,
            fontweight="bold", color="#234f8c")
    ax.text(x + 0.3, row1_y, "Positive corr.", ha="left", va="center", fontsize=10)
    x += 2.7
    ax.text(x, row1_y, "−", ha="center", va="center", fontsize=14,
            fontweight="bold", color="#9b2d2d")
    ax.text(x + 0.3, row1_y, "Negative corr.", ha="left", va="center", fontsize=10)
    x += 2.8
    ax.text(x, row1_y, "↑ higher better   ↓ lower better",
            ha="left", va="center", fontsize=10)

    # Row 2: competitors
    ax.text(legend_x0 + 0.25, row2_y, "Competitors:", ha="left", va="center",
            fontsize=10, fontweight="bold")
    x = legend_x0 + 2.4
    for c_idx, name in enumerate(COMPETITORS):
        draw_comp_marker(ax, x, row2_y, COMP_MARKERS[c_idx], COMP_COLORS[c_idx])
        ax.text(x + 0.3, row2_y, name, ha="left", va="center", fontsize=10)
        x += 2.4

    # Importance bar swatch
    ax.add_patch(Rectangle((x - 0.18, row2_y - 0.22), 0.36, 0.44,
                           facecolor=COLOR_BAR, edgecolor="#7a4a1e",
                           linewidth=0.8, zorder=3))
    ax.text(x + 0.3, row2_y, "Technical importance bar",
            ha="left", va="center", fontsize=10)

    return fig


def main():
    fig = build()
    out = "/home/devel/electrical_notes/content/sys_304/exam3/python_photos/04_qfd_house_of_quality.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    size = os.path.getsize(out)
    print(f"wrote {out} ({size} bytes)")


if __name__ == "__main__":
    main()
