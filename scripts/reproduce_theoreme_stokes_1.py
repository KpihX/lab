"""Reproduit la figure p.1 de theoreme-stokes : surface (S) bordee par (C).

Croquis d'origine (stylo) : nappe (S) vue en perspective, quadrillee par
le reseau des coordonnees (u, v), bordee par le parcours ferme (C) ;
en marge, le parallelogramme elementaire engendre par dOM/du et dOM/dv ;
en bas de p.2, un petit schema d'orientation du contour.

Style "stylo" : nappe et contour bleus, vecteurs et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/physique/theoreme-stokes/assets/surface-contour-stokes.png

Usage :
  uv run scripts/reproduce_theoreme_stokes_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_theoreme_stokes_1.py
>>> # OK -> .../assets/surface-contour-stokes.png (XXXXX o)
>>> # le rendu montre la nappe (S), son contour (C) et le pavelet (u, v).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/theoreme-stokes/assets/surface-contour-stokes.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_aspect("equal")
ax.set_xlim(-0.5, 8.5)
ax.set_ylim(-0.5, 7.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Nappe (S) : grille curviligne (u horizontal, v vertical).
u = np.linspace(1.0, 7.0, 9)
v = np.linspace(1.0, 5.6, 8)
for vv in v:
    xs = u + 0.35 * (vv - 1)
    ys = vv + 0.25 * np.sin(0.9 * u)
    ax.plot(xs, ys, color=BLUE, linewidth=0.9)
for uu in u:
    xs = uu + 0.35 * (v - 1)
    ys = v + 0.25 * np.sin(0.9 * uu) * np.ones_like(v)
    ax.plot(xs, ys, color=BLUE, linewidth=0.9)

# Contour (C) : bord de la nappe avec sens de parcours.
edge_u = np.linspace(1.0, 7.0, 60)
bot_x = edge_u + 0.35 * (1.0 - 1)
bot_y = np.full_like(edge_u, 1.0) + 0.25 * np.sin(0.9 * edge_u)
top_x = edge_u + 0.35 * (5.6 - 1)
top_y = np.full_like(edge_u, 5.6) + 0.25 * np.sin(0.9 * edge_u)
ax.plot(edge_u, bot_y, color=BLUE, linewidth=2.0)
ax.plot(edge_u, top_y, color=BLUE, linewidth=2.0)
ax.plot([bot_x[0], top_x[0]], [bot_y[0], top_y[0]], color=BLUE, linewidth=2.0)
ax.plot([bot_x[-1], top_x[-1]], [bot_y[-1], top_y[-1]], color=BLUE,
        linewidth=2.0)
ax.annotate("", xy=(4.2, bot_y[22]), xytext=(3.0, bot_y[15]),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.8))
ax.text(7.9, 0.7, "(C)", color=BLUE, fontsize=13)
ax.text(6.9, 6.1, "(S)", color=BLUE, fontsize=13)

# Pavelet elementaire dS : parallelogramme (dOM/du, dOM/dv).
px, py = 2.6, 2.6
ax.annotate("", xy=(px + 1.1, py + 0.15), xytext=(px, py),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.5))
ax.text(px + 0.5, py + 0.35, "dOM/du", color=RED, fontsize=10)
ax.annotate("", xy=(px + 0.25, py + 1.0), xytext=(px, py),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.5))
ax.text(px - 0.55, py + 0.7, "dOM/dv", color=RED, fontsize=10)
ax.text(px + 0.35, py - 0.45, "dS", color=BLUE, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
