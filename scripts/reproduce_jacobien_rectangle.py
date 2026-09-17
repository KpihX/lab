"""Reproduit le schema p.119 du 4e Bloc-Notes : Jacobien cartesien dx*dy.

Axes (x, y) au crayon, petit rectangle dx x dy en (x, y),
annotations rouges dA (encadre), dx, dy.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/jacobien-rectangle.png
Usage : uv run scripts/reproduce_jacobien_rectangle.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/jacobien-rectangle.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

x0, y0 = 1.0, 1.0
dx, dy = 1.2, 0.9

fig, ax = plt.subplots(figsize=(6, 5))
ax.set_aspect("equal")
ax.set_xlim(-0.5, 4.2)
ax.set_ylim(-0.5, 3.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

# axes crayon (gris) avec fleches
ax.annotate("", xy=(4.0, 0.15), xytext=(-0.3, 0.15),
            arrowprops=dict(arrowstyle="->", color="dimgray", linewidth=1.0))
ax.annotate("", xy=(0.15, 3.4), xytext=(0.15, -0.3),
            arrowprops=dict(arrowstyle="->", color="dimgray", linewidth=1.0))
ax.text(3.85, -0.15, "x", fontsize=13, color="dimgray")
ax.text(-0.15, 3.25, "y", fontsize=13, color="dimgray")
ax.text(0.0, -0.05, "O", fontsize=11, color="dimgray")

# rectangle dx x dy
rect = Rectangle((x0, y0), dx, dy, facecolor="none",
                 edgecolor="dimgray", linewidth=1.2)
ax.add_patch(rect)
# projections en pointilles sur les axes (style manuscrit)
for xx, lab in ((x0, "x"), (x0 + dx, "x+dx")):
    ax.plot([xx, xx], [0.15, y0 + (dy if xx > x0 else 0)], color="dimgray",
            linewidth=0.8, linestyle=(0, (3, 3)))
    ax.text(xx - 0.12, -0.18, lab, fontsize=11, color="dimgray")
for yy, lab in ((y0, "y"), (y0 + dy, "y+dy")):
    ax.plot([0.15, x0 + (dx if yy > y0 else 0)], [yy, yy], color="dimgray",
            linewidth=0.8, linestyle=(0, (3, 3)))
    ax.text(-0.35, yy - 0.08, lab, fontsize=11, color="dimgray")

# annotations rouges : dA encadre, dx, dy
ax.text(x0 + dx / 2 - 0.12, y0 + dy / 2 - 0.1, "dA", fontsize=13,
        color="red", bbox=dict(boxstyle="square,pad=0.25",
                               edgecolor="red", facecolor="none", linewidth=1.2))
ax.text(x0 + dx / 2 - 0.1, y0 - 0.32, "dx", fontsize=12, color="red")
ax.text(x0 + dx + 0.08, y0 + dy / 2 - 0.1, "dy", fontsize=12, color="red")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
