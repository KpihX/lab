"""Reproduit la figure p.2 de guldin-applications : cercle et tore.

Schema d'origine (stylo bleu) : axe vertical (fleche vers le haut) et axe
y horizontal avec origine O ; un cercle (C) de centre G et de rayon r,
a distance R de l'axe ; des ellipses en pointilles (haut et bas) et un
second cercle a droite suggerent le tore engendre par rotation autour
de (Oy).

Style "stylo" : cercles bleus, ellipses grises pointillees, R, r et
etiquettes rouges, fond quadrille bleu.

Sortie : raw/geometrie/guldin-applications/assets/cercle-tore.png

Usage :
  uv run scripts/reproduce_guldin_applications_4.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_guldin_applications_4.py
>>> # OK -> .../assets/cercle-tore.png (XXXXX o)
>>> # le rendu montre le cercle (C), G, R, r et les ellipses du tore.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/guldin-applications/assets/cercle-tore.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, GRAY = "#1a3fb5", "red", "gray"
R_BIG, R_SMALL = 2.0, 0.5  # distance a l'axe, rayon du cercle

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_aspect("equal")
ax.set_xlim(-1.2, 4.2)
ax.set_ylim(-1.4, 1.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Axe vertical et axe y avec origine O.
ax.annotate("", xy=(0, 1.5), xytext=(0, -1.2), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.5))
ax.annotate("", xy=(-1.0, 0), xytext=(0, 0), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2))
ax.text(-0.15, -0.3, "O", color=BLUE, fontsize=12)
ax.text(-1.0, -0.3, "y", color=BLUE, fontsize=13)

# Ellipses du tore (haut et bas, pointilles gris).
for yc in (R_SMALL + 0.12, -R_SMALL - 0.12):
    ax.add_patch(Ellipse((R_BIG, yc), 2 * (R_BIG + R_SMALL + 0.3), 0.35,
                         facecolor="none", edgecolor=GRAY, linewidth=1.0,
                         linestyle=(0, (4, 3))))

# Cercle (C) de centre G et de rayon r, a distance R de l'axe.
ax.add_patch(Circle((R_BIG, 0), R_SMALL, facecolor="none",
                    edgecolor=BLUE, linewidth=1.8))
ax.plot(R_BIG, 0, "o", color=BLUE, markersize=4)
ax.text(R_BIG - 0.05, -0.28, "G", color=RED, fontsize=12)
ax.text(R_BIG - 1.05, 0.62, "(C)", color=BLUE, fontsize=12)
ax.text(-0.75, 0.35, "(S)", color=BLUE, fontsize=12)

# Second cercle (cote oppose du tore).
ax.add_patch(Circle((R_BIG + 1.6, 0.05), R_SMALL * 0.9, facecolor="none",
                    edgecolor=GRAY, linewidth=1.0))

# Cotes R (axe -> G) et r (G -> cercle).
ax.annotate("", xy=(R_BIG, 0), xytext=(0, 0), color=BLUE,
            arrowprops=dict(arrowstyle="<->", color=BLUE, linewidth=1.1))
ax.text(R_BIG / 2 - 0.1, 0.1, "R", color=RED, fontsize=13)
ax.annotate("", xy=(R_BIG + R_SMALL * 0.7, R_SMALL * 0.7), xytext=(R_BIG, 0),
            color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.1))
ax.text(R_BIG + 0.28, 0.28, "r", color=RED, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
