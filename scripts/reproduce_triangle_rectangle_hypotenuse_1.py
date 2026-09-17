"""Reproduit la figure p.2 de triangle-rectangle-hypotenuse : croquis du triangle.

Figure d'origine (manuscrite) : segment horizontal BC (hypotenuse de
longueur h), point H entre B et C avec BH = e, hauteur HA abaisee sur A
(sommet de l'angle droit sous le segment), angle droit marque en H,
segments BA et AC.

Style "stylo" : triangle et hauteur bleus, cotes et lettres rouges,
fond quadrille bleu.

Sortie : raw/geometrie/triangle-rectangle-hypotenuse/assets/triangle-bhc.png

Usage :
  uv run scripts/reproduce_triangle_rectangle_hypotenuse_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_triangle_rectangle_hypotenuse_1.py
>>> # OK -> .../assets/triangle-bhc.png (XXXXX o)
>>> # le rendu montre BC horizontal, H, la hauteur HA et l'angle droit.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/triangle-rectangle-hypotenuse/assets/triangle-bhc.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-4.5, 1.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

# Hypotenuse BC horizontale (h quelconque), H entre B et C, A sous H.
B = np.array([0.0, 0.0])
C = np.array([9.0, 0.0])
H = np.array([3.0, 0.0])
A = np.array([3.0, -3.2])

ax.plot([B[0], C[0]], [B[1], C[1]], color=BLUE, linewidth=1.8)
ax.plot([B[0], A[0]], [B[1], A[1]], color=BLUE, linewidth=1.8)
ax.plot([C[0], A[0]], [C[1], A[1]], color=BLUE, linewidth=1.8)
ax.plot([H[0], A[0]], [H[1], A[1]], color=BLUE, linewidth=1.4,
        linestyle=(0, (4, 3)))

# Marque d'angle droit en H.
s = 0.45
ax.plot([H[0], H[0] + s], [H[1], H[1]], color=RED, linewidth=1.2)
ax.plot([H[0] + s, H[0] + s], [H[1], H[1] - s], color=RED, linewidth=1.2)
ax.plot([H[0], H[0] + s], [H[1] - s, H[1] - s], color=RED, linewidth=1.2)

for pt in (B, H, C, A):
    ax.plot(pt[0], pt[1], "o", color=BLUE, markersize=5)

ax.text(B[0] - 0.35, 0.35, "B", color=RED, fontsize=14)
ax.text(H[0] - 0.1, 0.35, "H", color=RED, fontsize=14)
ax.text(C[0] + 0.15, 0.35, "C", color=RED, fontsize=14)
ax.text(A[0] + 0.2, A[1] - 0.2, "A", color=RED, fontsize=14)
ax.text(1.5, 0.35, "e", color=RED, fontsize=14)
ax.annotate("", xy=(H[0] - 0.15, 0.0), xytext=(B[0] + 0.15, 0.0),
            arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.2))

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
