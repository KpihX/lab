"""Reproduit le croquis p.7 de guldin-centres-masse : arc de cercle des centres.

Schema d'origine (cahier quadrille, coin superieur droit de la p.7) : les
points G et G1 obtenus par rotation d'angle alpha autour de (Ox) forment un
arc de cercle de rayon Gy ; petit repere (j, k) ; angle alpha annote au
sommet ; mention y = sqrt(Gy^2 - z^2).

Style "stylo" : arc bleu epais, rayons rouges, angle annote, fond quadrille.

Sortie : raw/geometrie/guldin-centres-masse/assets/arc-centres-g-g1.png

Usage :
  uv run scripts/reproduce_guldin-centres-masse_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_guldin-centres-masse_2.py
>>> # OK -> .../assets/arc-centres-g-g1.png (XXXXX o)
>>> # le rendu montre l'arc de cercle G...G1, l'angle alpha
>>> # et la relation y = sqrt(Gy^2 - z^2).
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/guldin-centres-masse/assets/arc-centres-g-g1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, INK = "#1a3fb5", "#d31f1f", "black"
ALPHA = np.deg2rad(50)  # angle de rotation alpha du croquis
GY = 2.0  # rayon de l'arc = distance Gy a l'axe (Ox)

fig, ax = plt.subplots(figsize=(5.2, 5.2))
ax.set_aspect("equal")
ax.set_xlim(-2.6, 2.6)
ax.set_ylim(-1.4, 3.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Petit repere (j, k) en haut a gauche du croquis.
ax.annotate("", xy=(-1.2, 2.2), xytext=(-2.0, 2.2),
            arrowprops=dict(arrowstyle="->", color=INK, linewidth=1.3))
ax.text(-1.05, 2.22, "j", color=INK, fontsize=12)
ax.annotate("", xy=(-2.0, 1.4), xytext=(-2.0, 2.2),
            arrowprops=dict(arrowstyle="->", color=INK, linewidth=1.3))
ax.text(-2.15, 1.3, "k", color=INK, fontsize=12)

# Rayons O->G et O->G1 (rouge) + arc de cercle G...G1 (bleu).
th = np.linspace(np.pi / 2 - ALPHA / 2, np.pi / 2 + ALPHA / 2, 200)
ax.plot([0, GY * np.cos(np.pi / 2 - ALPHA / 2)], [0, GY * np.sin(np.pi / 2 - ALPHA / 2)],
        color=RED, linewidth=1.6)
ax.plot([0, GY * np.cos(np.pi / 2 + ALPHA / 2)], [0, GY * np.sin(np.pi / 2 + ALPHA / 2)],
        color=RED, linewidth=1.6)
ax.plot(GY * np.cos(th), GY * np.sin(th), color=BLUE, linewidth=2.2)
ax.plot(0, 0, marker="o", color=INK, markersize=5)

xg = GY * np.cos(np.pi / 2 - ALPHA / 2)
yg = GY * np.sin(np.pi / 2 - ALPHA / 2)
xg1 = GY * np.cos(np.pi / 2 + ALPHA / 2)
yg1 = GY * np.sin(np.pi / 2 + ALPHA / 2)
ax.text(xg + 0.12, yg + 0.05, "G", color=INK, fontsize=13)
ax.text(xg1 - 0.35, yg1 + 0.05, "G1", color=INK, fontsize=13)
ax.text(0.08, -0.25, "O", color=INK, fontsize=12)

# Angle alpha annote au sommet.
ax.add_patch(Arc((0, 0), 1.1, 1.1, theta1=90 - 25, theta2=90 + 25,
                 color=INK, linewidth=1.2))
ax.text(0.02, 0.78, "α", color=INK, fontsize=13, ha="center")

ax.text(-2.4, -1.0, "y = √(Gy² − z²)", color=BLUE, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
