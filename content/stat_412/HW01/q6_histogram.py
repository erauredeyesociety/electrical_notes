#!/usr/bin/env python3
"""Construct the relative-frequency histogram for Q6 (teacher salaries).
Charts are built in Python/matplotlib (not LaTeX) — see lessons-learned note.
Run:  python3 q6_histogram.py   ->  writes q6_histogram.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

salaries = [3.94, 2.91, 2.82, 2.83, 3.05, 1.77, 2.46, 3.12, 2.36, 2.07,
            2.73, 2.57, 2.76, 2.70, 3.66, 3.82, 3.33, 2.04, 2.89, 2.85,
            3.24, 2.44, 2.09, 3.73, 3.07, 3.53, 2.30, 2.59, 3.59, 3.34]

edges = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]          # class width 0.5
n = len(salaries)
counts = [0] * (len(edges) - 1)
for v in salaries:
    for i in range(len(edges) - 1):
        if edges[i] <= v < edges[i + 1]:
            counts[i] += 1
            break
rel = [c / n for c in counts]

fig, ax = plt.subplots(figsize=(5.2, 3.2))
ax.bar([(edges[i] + edges[i + 1]) / 2 for i in range(len(rel))], rel,
       width=0.5, edgecolor="black", color="#9ecae1", align="center")
ax.set_xlabel("Salary ($ per pupil)")
ax.set_ylabel("Relative frequency")
ax.set_xticks(edges)
ax.set_ylim(0, 0.40)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="0.85", linewidth=0.6)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
fig.tight_layout()
fig.savefig("q6_histogram.png", dpi=150)
print("counts:", counts, "rel:", [round(r, 4) for r in rel])
