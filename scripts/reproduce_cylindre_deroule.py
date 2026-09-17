"""Reproduit les schemas p.123 du 4e Bloc-Notes : cylindre creux deroule.

A gauche : cylindre creux de rayon r, epaisseur dr, hauteur e^{-r^2}.
A droite (=>) : rectangle deroule de largeur 2(pi)r.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/cylindre-deroule.png
Usage : uv run scripts/reproduce_cylindre_deroule.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle, FancyArrowPatch
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/cylindre-deroule.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_aspect("equal")
ax.set_xlim(-1.5, 9.5)
ax.set_ylim(-0.5, 4.2)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

# --- cylindre creux (crayon gris) ---
cx, top, h = 1.2, 3.2, 2.2
rx, ry = 0.9, 0.28
ax.add_patch(Ellipse((cx, top), 2 * rx, 2 * ry, facecolor="none",
                     edgecolor="dimgray", linewidth=1.1))
ax.add_patch(Ellipse((cx, top - h), 2 * rx, 2 * ry, facecolor="none",
                     edgecolor="dimgray", linewidth=1.1))
ax.plot([cx - rx, cx - rx], [top - h, top], color="dimgray", linewidth=1.1)
ax.plot([cx + rx, cx + rx], [top - h, top], color="dimgray", linewidth=1.1)

def dbl_arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                 arrowstyle="<->", color="red", linewidth=1.2,
                 mutation_scale=10, shrinkA=0, shrinkB=0))

# rayon r (haut du cylindre), epaisseur dr (bord), hauteur e^{-r2}
dbl_arrow(cx, top + 0.05, cx + rx, top + 0.05)
ax.text(cx + 0.35, top + 0.28, "r", fontsize=12, color="red")
dbl_arrow(cx + rx - 0.02, top + 0.02, cx + rx + 0.22, top + 0.02)
ax.text(cx + rx + 0.28, top + 0.05, "dr", fontsize=11, color="red")
dbl_arrow(cx - rx - 0.35, top, cx - rx - 0.35, top - h)
ax.text(cx - rx - 0.75, top - h / 2 - 0.1, "e⁻ʳ²", fontsize=12, color="red")

# implication =>
ax.text(2.9, 2.0, "⇒", fontsize=20, color="dimgray")

# --- rectangle deroule (crayon gris) ---
rx0, ry0, rw, rh = 4.2, 1.0, 4.0, 2.2
ax.add_patch(Rectangle((rx0, ry0), rw, rh, facecolor="none",
                       edgecolor="dimgray", linewidth=1.2))
dbl_arrow(rx0, ry0 - 0.3, rx0 + rw, ry0 - 0.3)
ax.text(rx0 + rw / 2 - 0.3, ry0 - 0.65, "2πr", fontsize=12, color="red")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
