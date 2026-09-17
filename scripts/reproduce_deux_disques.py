"""Reproduit la figure p.151 de quatrieme-bloc-notes : paradoxe des deux disques.

Figure d'origine (manuscrite, bas de page) : grand disque (D') de centre
O' et rayon R', petit disque (D) de centre O et rayon R tangent
exterieurement, angle alpha balaye le long de la circonference.

Style "stylo" : cercles et rayons bleus, centres et annotations rouges,
fond quadrille bleu.

Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/deux-disques.png

Usage :
  uv run scripts/reproduce_deux_disques.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/deux-disques.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-3.2, 3.8)
ax.set_ylim(-3.2, 3.8)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

Rp, R = 2.0, 0.7
Op = np.array([0.0, 0.0])
alpha = np.radians(45.0)
direction = np.array([np.cos(alpha), np.sin(alpha)])
P = Op + Rp * direction
O = P + R * direction

ax.add_patch(Circle(Op, Rp, fill=False, color=BLUE, linewidth=1.8))
ax.add_patch(Circle(O, R, fill=False, color=BLUE, linewidth=1.8))
ax.plot([Op[0], O[0]], [Op[1], O[1]], color=BLUE, linewidth=1.2)
ax.plot(Op[0], Op[1], "o", color=BLUE, markersize=5)
ax.plot(O[0], O[1], "o", color=BLUE, markersize=5)
ax.plot(P[0], P[1], "o", color=RED, markersize=5)

# Rayon R' (centre O' -> contact) et R (contact -> centre O).
ax.text(*(Op + 0.45 * Rp * direction + [-0.35, 0.1]), "R'", color=RED, fontsize=14)
ax.text(*(P + 0.45 * R * direction + [0.05, 0.1]), "R", color=RED, fontsize=14)
ax.text(Op[0] - 0.45, Op[1] - 0.35, "O'", color=RED, fontsize=14)
ax.text(O[0] + 0.15, O[1] + 0.15, "O", color=RED, fontsize=14)
ax.text(Op[0] - 1.3, Op[1] - 0.4, "(D')", color=RED, fontsize=14)
ax.text(O[0] - 0.25, O[1] + 0.1, "(D)", color=RED, fontsize=14)

# Angle alpha balaye depuis l'axe horizontal.
ax.add_patch(Arc(Op, 1.2, 1.2, theta1=0, theta2=np.degrees(alpha),
                 color=RED, linewidth=1.3))
ax.text(0.75, 0.25, "\u03b1", color=RED, fontsize=15)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
