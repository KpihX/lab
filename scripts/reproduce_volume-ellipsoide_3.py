"""Reproduit la figure p.2 du Volume d'un ellipsoide : coupe elliptique et rectangle.

Schema d'origine (stylo bleu sur papier) : une ellipse horizontale (coupe
de l'ellipsoide a abscisse x0 fixee) avec ses axes ; un rectangle vertical
hachure represente l'ensemble des points (y, z) avec y dans [y0, y1] et
z dans [z0, z1] ; annotations x0, y0, y1 autour.

Style "stylo" : ellipse/axes/rectangle bleus, annotations rouges,
fond quadrille bleu.

Sortie : raw/analyse-integrales/volume-ellipsoide/assets/coupe-ellipsoide.png

Usage :
  uv run scripts/reproduce_volume-ellipsoide_3.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_volume-ellipsoide_3.py
>>> # OK -> .../assets/coupe-ellipsoide.png (NNNNN o)
>>> # le rendu montre l'ellipse, ses axes, le rectangle [y0,y1]x[z0,z1] hachure.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-integrales"
    "/volume-ellipsoide/assets/coupe-ellipsoide.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6, 5))
ax.set_aspect("equal")
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-2.4, 2.4)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Ellipse de coupe (demi-axes a=3, b=2).
ax.add_patch(Ellipse((0, 0), 6.0, 4.0, fill=False, color=BLUE, linewidth=1.5))
# Axes de l'ellipse.
ax.plot([-3.2, 3.2], [0, 0], color=BLUE, linewidth=1.0)
ax.plot([0, 0], [-2.4, 2.4], color=BLUE, linewidth=1.0)

# Rectangle des points (y dans [y0, y1], z dans [z0, z1]) : hachures.
rect = Rectangle((-1.2, -0.8), 2.4, 1.6, fill=False, color=BLUE, linewidth=1.5, hatch="///")
ax.add_patch(rect)

# Abscisse x0 fixee (point de coupe) et annotations.
ax.plot(1.8, 0, "o", color=BLUE, markersize=5)
ax.text(1.8, -0.25, "x0", color=BLUE, fontsize=12, ha="center")
ax.text(-1.2, -1.05, "y0", color=BLUE, fontsize=12, ha="center")
ax.text(1.2, 1.05, "y1", color=BLUE, fontsize=12, ha="center")
ax.text(1.45, -0.8, "z0", color=BLUE, fontsize=12)
ax.text(1.45, 0.8, "z1", color=BLUE, fontsize=12)
ax.text(0, 2.5 - 2.4 + 2.15, "coupe a x0 fixee", color=RED, fontsize=12, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
