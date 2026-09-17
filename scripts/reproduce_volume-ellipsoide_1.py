"""Reproduit le premier croquis p.2 du Volume d'un ellipsoide (lot B0).

Croquis d'origine (stylo bleu sur papier) : un ellipsoide vu en
perspective, traverse par un pave (boite) interieur et une diagonale
qui le coupe ; annotations "a" (en haut) et "b" (a droite).

Style "stylo" : ellipsoide, pave et diagonale bleus, annotations
rouges, fond quadrille bleu.

Sortie : raw/analyse-integrales/volume-ellipsoide/assets/ellipsoide-pave.png

Usage :
  uv run scripts/reproduce_volume-ellipsoide_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_volume-ellipsoide_1.py
>>> # OK -> .../assets/ellipsoide-pave.png (NNNNN o)
>>> # le rendu montre l'ellipsoide, le pave interieur et la diagonale.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-integrales"
    "/volume-ellipsoide/assets/ellipsoide-pave.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")

# Ellipsoide (a=3, b=2, c=1.5) : maillage filaire bleu.
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 25)
xs = 3.0 * np.outer(np.cos(u), np.sin(v))
ys = 2.0 * np.outer(np.sin(u), np.sin(v))
zs = 1.5 * np.outer(np.ones_like(u), np.cos(v))
ax.plot_wireframe(xs, ys, zs, color=BLUE, linewidth=0.5, rstride=3, cstride=3)

# Pave interieur (boite) : 12 aretes bleues.
x0, y0, z0 = 1.4, 1.0, 0.7
corners = np.array([[sx * x0, sy * y0, sz * z0]
                    for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)])
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7),
         (0, 4), (1, 5), (2, 6), (3, 7)]
for i, j in edges:
    ax.plot([corners[i][0], corners[j][0]],
            [corners[i][1], corners[j][1]],
            [corners[i][2], corners[j][2]], color=BLUE, linewidth=1.2)

# Diagonale qui coupe l'ellipsoide.
ax.plot([-3.4, 3.4], [-2.3, 2.3], [-1.8, 1.8], color=BLUE, linewidth=1.0)

ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.5, 2.5)
ax.set_zlim(-2.0, 2.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)

# Annotations : "a" en haut, "b" a droite.
ax.text(0, 0, 2.1, "a", color=RED, fontsize=13)
ax.text(3.2, 1.2, 0, "b", color=RED, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
