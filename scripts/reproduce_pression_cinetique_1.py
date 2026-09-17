"""Reproduit le schema p.1 de pression-cinetique : element de paroi dS.

Figure d'origine (manuscrite, stylo bleu) : contour ferme = paroi d'un
recipient ; petit segment epaissi = element de surface dS, de normale
rentrante n ; trois fleches = vitesses des particules incidentes.

Style "stylo" : paroi et fleches bleues, element dS et normale rouges,
fond quadrille bleu.

Sortie : raw/physique/pression-cinetique/assets/schema-ds-normale.png

Usage :
  uv run scripts/reproduce_pression_cinetique_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_pression_cinetique_1.py
>>> # OK -> .../assets/schema-ds-normale.png (XXXXX o)
>>> # le rendu montre la paroi, dS, la normale n et les vitesses incidentes.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/pression-cinetique/assets/schema-ds-normale.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(7, 6))
ax.set_xlim(-5, 5)
ax.set_ylim(-4.5, 4.5)
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Paroi : contour ferme irregulier.
t = np.linspace(0, 2 * np.pi, 400)
wall_x = 3.4 * np.cos(t) + 0.5 * np.cos(2 * t + 0.6)
wall_y = 3.0 * np.sin(t) + 0.4 * np.sin(3 * t)
ax.plot(wall_x, wall_y, color=BLUE, linewidth=1.8)

# Element de surface dS : petit segment epaissi sur le flanc gauche.
ds_x = np.array([-3.55, -3.35])
ds_y = np.array([-0.5, 0.9])
ax.plot(ds_x, ds_y, color=RED, linewidth=4.0)
ax.text(-4.4, 0.2, "dS", color=RED, fontsize=14)

# Normale rentrante n (part du milieu de dS vers l'interieur).
mx, my = ds_x.mean(), ds_y.mean()
ax.annotate("", xy=(mx + 1.6, my), xytext=(mx, my),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.6))
ax.text(mx + 0.5, my - 0.55, "n", color=RED, fontsize=14)

# Particules incidentes : trois vitesses vers dS.
for i, (sx, sy) in enumerate([(-1.2, 1.6), (-0.9, 0.2), (-1.2, -1.2)]):
    ax.annotate("", xy=(mx + 0.15, my + (0.35 - 0.35 * i)),
                xytext=(sx, sy),
                arrowprops=dict(arrowstyle="->", color=BLUE,
                                linewidth=1.4))

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
