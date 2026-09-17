"""Reproduit la figure p.128 de quatrieme-bloc-notes : triangle BB'C et cevienne.

Figure d'origine (manuscrite) : grand triangle de sommet B' en haut,
base BC horizontale (B a gauche, C a droite), point A' interieur sur
la base, cevienne B'A', sous-triangle gauche d'aire A1, hauteurs h1 h2,
angle alpha en A' entre la base et la cevienne.

Style "stylo" : triangle et cevienne bleus, lettres et cotes rouges,
fond quadrille bleu.

Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/triangle-hauteurs.png

Usage :
  uv run scripts/reproduce_triangle_hauteurs.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/triangle-hauteurs.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, 10.5)
ax.set_ylim(-1.5, 8.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

B = np.array([0.0, 0.0])
C = np.array([9.0, 0.0])
Bp = np.array([2.5, 7.0])
Ap = np.array([4.0, 0.0])

ax.plot([B[0], C[0]], [B[1], C[1]], color=BLUE, linewidth=1.8)
ax.plot([B[0], Bp[0]], [B[1], Bp[1]], color=BLUE, linewidth=1.8)
ax.plot([C[0], Bp[0]], [C[1], Bp[1]], color=BLUE, linewidth=1.8)
ax.plot([Bp[0], Ap[0]], [Bp[1], Ap[1]], color=BLUE, linewidth=1.6)

for pt in (B, C, Bp, Ap):
    ax.plot(pt[0], pt[1], "o", color=BLUE, markersize=5)

ax.text(B[0] - 0.55, -0.35, "B", color=RED, fontsize=14)
ax.text(C[0] + 0.2, -0.35, "C", color=RED, fontsize=14)
ax.text(Bp[0] - 0.7, Bp[1] + 0.25, "B'", color=RED, fontsize=14)
ax.text(Ap[0] - 0.15, -0.75, "A'", color=RED, fontsize=14)
ax.text(2.0, 1.6, "A1", color=RED, fontsize=13)
ax.text(1.0, 4.2, "h1", color=RED, fontsize=13)
ax.text(3.7, 3.6, "h2", color=RED, fontsize=13)

# Angle alpha en A' entre la base (direction B) et la cevienne (direction B').
v1 = B - Ap
v2 = Bp - Ap
a1 = np.degrees(np.arctan2(v1[1], v1[0]))
a2 = np.degrees(np.arctan2(v2[1], v2[0]))
ax.add_patch(Arc(Ap, 1.7, 1.7, theta1=a2, theta2=a1, color=RED, linewidth=1.3))
ax.text(Ap[0] - 1.35, Ap[1] + 0.55, "\u03b1", color=RED, fontsize=15)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
