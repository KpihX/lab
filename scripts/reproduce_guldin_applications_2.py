"""Reproduit la figure 2 p.1 de guldin-applications : surface (S) et axe (Ox).

Schema d'origine (stylo bleu) : l'axe (Ox) vertical, l'axe y horizontal ;
une surface fermee (S) (patate verticale) avec son centre de gravite G et
un element dS (petit carre) ; des hachures horizontales a droite suggerent
le volume de revolution autour de (Ox).

Style "stylo" : axes et contour bleus, G et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/geometrie/guldin-applications/assets/surface-rotation-ox.png

Usage :
  uv run scripts/reproduce_guldin_applications_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_guldin_applications_2.py
>>> # OK -> .../assets/surface-rotation-ox.png (XXXXX o)
>>> # le rendu montre la surface (S), G, dS, l'axe (Ox) et les hachures.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/guldin-applications/assets/surface-rotation-ox.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, GRAY = "#1a3fb5", "red", "gray"

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-2.6, 2.6)
ax.set_ylim(-0.5, 5.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Axes : (Ox) vertical, y horizontal.
ax.annotate("", xy=(0, 5.2), xytext=(0, 0), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.5))
ax.annotate("", xy=(-2.4, 0), xytext=(0, 0), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.5))
ax.text(0.15, 5.0, "x", color=BLUE, fontsize=13)
ax.text(-2.4, -0.35, "y", color=BLUE, fontsize=13)
ax.text(-0.2, -0.3, "O", color=BLUE, fontsize=12)

# Surface fermee (S) : contour de type "patate" vertical.
t = np.linspace(0, 2 * np.pi, 300)
xc = -1.3 + 0.45 * np.cos(t) + 0.15 * np.cos(2 * t)
yc = 2.5 + 1.3 * np.sin(t) + 0.1 * np.sin(3 * t)
ax.plot(xc, yc, color=BLUE, linewidth=1.8)
ax.text(-2.1, 3.2, "(S)", color=BLUE, fontsize=12)

# Centre de gravite G et element dS (petit carre).
ax.plot(-1.3, 2.7, "o", color=BLUE, markersize=5)
ax.text(-1.1, 2.8, "G", color=RED, fontsize=13)
ax.add_patch(Rectangle((-1.5, 1.6), 0.25, 0.25, facecolor="none",
                       edgecolor=BLUE, linewidth=1.4))
ax.text(-1.45, 1.3, "dS", color=BLUE, fontsize=11)

# Hachures horizontales suggerant le volume de revolution.
for y0 in np.arange(1.4, 4.0, 0.3):
    ax.plot([0.1, 2.4], [y0, y0], color=GRAY, linewidth=0.8)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
