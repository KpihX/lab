"""Reproduit la figure 3 p.1 de guldin-applications : demi-disque et sphere.

Schema d'origine (stylo bleu) : axe x horizontal avec origine O ; un
demi-disque (S) de rayon r (hachures verticales), borde par le demi-cercle
(C) ; un rayon fleche annote r ; la rotation autour de (Ox) engendre une
sphere (resp. boule).

Style "stylo" : contour bleu, hachures grises, r et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/geometrie/guldin-applications/assets/demi-disque-sphere.png

Usage :
  uv run scripts/reproduce_guldin_applications_3.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_guldin_applications_3.py
>>> # OK -> .../assets/demi-disque-sphere.png (XXXXX o)
>>> # le rendu montre le demi-disque hachure, O, r et (C).
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/guldin-applications/assets/demi-disque-sphere.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, GRAY = "#1a3fb5", "red", "gray"
R = 1.0

fig, ax = plt.subplots(figsize=(6, 4.5))
ax.set_aspect("equal")
ax.set_xlim(-0.4, 1.6)
ax.set_ylim(-0.5, 1.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Demi-disque hachure (hachures verticales grises).
for x0 in np.arange(0.05, R, 0.1):
    h = np.sqrt(max(R**2 - x0**2, 0))
    ax.plot([x0, x0], [0, h], color=GRAY, linewidth=0.8)

# Demi-cercle (C) et diametre sur l'axe x.
t = np.linspace(0, np.pi, 200)
ax.plot(R * np.cos(t), R * np.sin(t), color=BLUE, linewidth=1.8)
ax.plot([0, R], [0, 0], color=BLUE, linewidth=1.5)

# Axe x horizontal.
ax.annotate("", xy=(1.55, 0), xytext=(-0.3, 0), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2))
ax.text(1.5, -0.18, "x", color=BLUE, fontsize=13)

# Origine O, rayon r et etiquettes.
ax.plot(0, 0, "o", color=BLUE, markersize=5)
ax.text(-0.08, -0.22, "O", color=BLUE, fontsize=12)
ax.annotate("", xy=(R * np.cos(0.7), R * np.sin(0.7)), xytext=(0, 0), color=BLUE,
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2))
ax.text(0.55, 0.55, "r", color=RED, fontsize=13)
ax.text(1.05, 0.75, "(C)", color=BLUE, fontsize=12)
ax.text(-0.3, -0.05, "(S)", color=BLUE, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
