"""Reproduit la figure p.35 du 4e Bloc-Notes : longueur d'une spire.

En haut : cylindre (C) — silhouette + 2 spires (arcs pleins devant,
pointilles derriere), ellipse d'embout, longueur l. En bas : prisme (T) a
base polygonale — zigzag (onde triangulaire) + cache en pointilles,
losange d'embout, meme longueur l.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/ressort-spire.png
Usage : uv run scripts/reproduce_ressort_spire.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/ressort-spire.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

L, R = 10.0, 1.0  # longueur et rayon

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
for ax in (ax1, ax2):
    ax.set_xlim(-0.6, L + 1.2)
    ax.set_ylim(-1.8, 1.8)
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    ax.set_axisbelow(True)

# ---- (C) : cylindre + helice sinusoidale ----
x = np.linspace(0, L, 600)
y = R * np.sin(2 * np.pi * 2 * x / L)
front = np.cos(2 * np.pi * 2 * x / L) > 0
ax1.plot(x[front], y[front], color="black", linewidth=1.3)
ax1.plot(x[~front], y[~front], color="dimgray", linewidth=1.0,
         linestyle=(0, (4, 3)))
ax1.plot([0, L], [R, R], color="black", linewidth=1.0)
ax1.plot([0, L], [-R, -R], color="black", linewidth=1.0)
ax1.add_patch(Ellipse((L, 0), 0.5, 2 * R, fill=False,
                      edgecolor="black", linewidth=1.3))
ax1.annotate("", xy=(L, -1.45), xytext=(0, -1.45),
             arrowprops=dict(arrowstyle="<->", color="black"))
ax1.text(L / 2 - 0.1, -1.7, "l", fontsize=13)
ax1.text(L + 0.6, 0.0, "(C)", fontsize=14, color="darkblue")

# ---- (T) : prisme + spire en zigzag ----
xp = np.linspace(0, L, 9)
yp = R * np.tile([1, -1], 5)[:9]
ax2.plot(xp, yp, color="black", linewidth=1.3)  # face avant
ax2.plot(xp + 0.35, yp * 0.55 + 0.35, color="dimgray", linewidth=1.0,
         linestyle=(0, (4, 3)))  # arete cachee
ax2.plot([0, L], [R, R], color="black", linewidth=1.0)
ax2.plot([0, L], [-R, -R], color="black", linewidth=1.0)
ax2.add_patch(Polygon([[L, R], [L + 0.5, 0.4], [L, -R], [L - 0.2, 0.0]],
                      closed=True, fill=False, edgecolor="black", linewidth=1.3))
ax2.annotate("", xy=(L, -1.45), xytext=(0, -1.45),
             arrowprops=dict(arrowstyle="<->", color="black"))
ax2.text(L / 2 - 0.1, -1.7, "l", fontsize=13)
ax2.text(L + 0.8, 0.0, "(T)", fontsize=14, color="darkblue")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
