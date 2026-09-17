"""Reproduit la figure 1 p.1 de guldin-applications : courbe (C) et axe (Ox).

Schema d'origine (stylo bleu) : l'axe (Ox) vertical (fleche vers le haut),
l'axe y horizontal ; une courbe ouverte (C) ondulee (verticale) avec son
centre de gravite G ; des arcs en pointilles a droite suggerent la surface
de revolution engendree autour de (Ox).

Style "stylo" : axes et courbe bleus, G et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/geometrie/guldin-applications/assets/courbe-rotation-ox.png

Usage :
  uv run scripts/reproduce_guldin_applications_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_guldin_applications_1.py
>>> # OK -> .../assets/courbe-rotation-ox.png (XXXXX o)
>>> # le rendu montre la courbe (C), G, l'axe (Ox) et les arcs pointilles.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/guldin-applications/assets/courbe-rotation-ox.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, GRAY = "#1a3fb5", "red", "gray"

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-2.2, 3.2)
ax.set_ylim(-0.5, 5.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Axes : (Ox) vertical, y horizontal partant de O.
ax.annotate("", xy=(0, 5.2), xytext=(0, 0), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.5))
ax.annotate("", xy=(-2.0, 0), xytext=(0, 0), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.5))
ax.text(0.15, 5.0, "x", color=BLUE, fontsize=13)
ax.text(-2.0, -0.35, "y", color=BLUE, fontsize=13)
ax.text(-0.15, -0.3, "O", color=BLUE, fontsize=12)

# Courbe ouverte (C), ondulee, a gauche de l'axe.
t = np.linspace(0, 1, 200)
xc = -1.1 + 0.25 * np.sin(2 * np.pi * 1.5 * t)
yc = 1.0 + 3.0 * t
ax.plot(xc, yc, color=BLUE, linewidth=1.8)
ax.text(-1.7, 1.3, "(C)", color=BLUE, fontsize=12)

# Centre de gravite G sur la courbe.
ax.plot(-1.1, 2.5, "o", color=BLUE, markersize=5)
ax.text(-0.9, 2.6, "G", color=RED, fontsize=13)

# Arcs pointilles de la surface de revolution (a droite de l'axe).
for y0, w in [(1.6, 3.4), (2.5, 4.2), (3.4, 3.4)]:
    ax.add_patch(Arc((0, y0), w, 0.9, theta1=270, theta2=90,
                     color=GRAY, linewidth=1.1, linestyle=(0, (4, 3))))

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
