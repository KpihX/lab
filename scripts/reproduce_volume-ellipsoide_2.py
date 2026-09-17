"""Reproduit la figure (A) p.2 du Volume d'un ellipsoide (lot B0).

Figure d'origine (stylo bleu sur papier), notee "(A)" : un ellipsoide
avec ses trois axes (annotations a, b, c), un point courant M
d'abscisse x, et le rectangle des points de meme abscisse
(ordonnees y0, y1, cotes z0, z1).

Style "stylo" : ellipsoide, axes et rectangle bleus, annotations
rouges, fond quadrille bleu.

Sortie : raw/analyse-integrales/volume-ellipsoide/assets/ellipsoide-coupe-rectangle.png

Usage :
  uv run scripts/reproduce_volume-ellipsoide_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_volume-ellipsoide_2.py
>>> # OK -> .../assets/ellipsoide-coupe-rectangle.png (NNNNN o)
>>> # le rendu montre l'ellipsoide, ses axes a/b/c et le rectangle [y0,y1]x[z0,z1].
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-integrales"
    "/volume-ellipsoide/assets/ellipsoide-coupe-rectangle.png"
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

# Axes de l'ellipsoide.
ax.plot([-3.5, 3.5], [0, 0], [0, 0], color=BLUE, linewidth=1.0)
ax.plot([0, 0], [-2.5, 2.5], [0, 0], color=BLUE, linewidth=1.0)
ax.plot([0, 0], [0, 0], [-2.0, 2.0], color=BLUE, linewidth=1.0)

# Rectangle des points d'abscisse x fixee (y dans [y0, y1], z dans [z0, z1]).
x1, ya, yb, za, zb = 1.2, -1.0, 1.0, -0.7, 0.7
rect = [(x1, ya, za), (x1, yb, za), (x1, yb, zb), (x1, ya, zb), (x1, ya, za)]
rx, ry, rz = zip(*rect)
ax.plot(rx, ry, rz, color=BLUE, linewidth=1.5)

# Point courant M sur l'axe des x.
ax.scatter([x1], [0], [0], color=BLUE, s=25)

ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.5, 2.5)
ax.set_zlim(-2.0, 2.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)

# Annotations.
ax.text(3.6, 0, 0, "a", color=RED, fontsize=13)
ax.text(0, 2.6, 0, "b", color=RED, fontsize=13)
ax.text(0, 0, 2.1, "c", color=RED, fontsize=13)
ax.text(x1, -0.2, -0.3, "M", color=RED, fontsize=11)
ax.text(x1, ya - 0.25, 0, "y0", color=RED, fontsize=10)
ax.text(x1, yb + 0.1, 0, "y1", color=RED, fontsize=10)
ax.text(x1, 0.1, za - 0.2, "z0", color=RED, fontsize=10)
ax.text(x1, 0.1, zb + 0.05, "z1", color=RED, fontsize=10)
ax.text(-3.4, -2.4, 1.9, "(A)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
