"""Reproduit le pont de Wheatstone p.2 de associations-resistances.

Schema d'origine (stylo bleu) : losange A (gauche), D (haut), B (droite),
F/E (bas) ; R1 (A-D), R2 (D-B), R3 (A-F), R4 (F-B), R5 en diagonale
(galvanometre) ; source E en bas ; fleches de courants I, I1, I2 et
tensions U1..U4.

Style "stylo" : branches bleues, source et galvanometre rouges,
fond quadrille bleu.

Sortie : raw/physique/associations-resistances/assets/pont-wheatstone.png

Usage :
  uv run scripts/reproduce_associations_resistances_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_associations_resistances_2.py
>>> # OK -> .../assets/pont-wheatstone.png (XXXXX o)
>>> # le rendu montre le losange, la diagonale R5 et la source E.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/associations-resistances/assets/pont-wheatstone.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1, 11)
ax.set_ylim(-1.5, 11)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Sommets du losange : A gauche, D haut, B droite, F bas.
A, D, B, F = (1, 5), (5, 9), (9, 5), (5, 1)

branches = [(A, D, "R1"), (D, B, "R2"), (A, F, "R3"), (F, B, "R4")]
for (x1, y1), (x2, y2), label in branches:
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.plot([x1, mx - 0.5], [y1, my - 0.35], color=BLUE, linewidth=1.6)
    ax.plot([mx + 0.5, x2], [my + 0.35, y2], color=BLUE, linewidth=1.6)
    ax.add_patch(Rectangle((mx - 0.5, my - 0.35), 1.0, 0.7, fill=False,
                           edgecolor=BLUE, linewidth=1.6))
    ax.text(mx, my, label, color=BLUE, fontsize=10, ha="center", va="center")

# Diagonale A-B : galvanometre R5.
ax.plot([A[0], 4.2], [A[1], 5], color=RED, linewidth=1.4)
ax.plot([5.8, B[0]], [5, B[1]], color=RED, linewidth=1.4)
ax.add_patch(Circle((5, 5), 0.8, fill=False, edgecolor=RED, linewidth=1.6))
ax.text(5, 5, "R5", color=RED, fontsize=10, ha="center", va="center")

# Source E sous le pont (entre F et la masse).
ax.plot([F[0], F[0]], [F[1], -0.3], color=BLUE, linewidth=1.6)
ax.add_patch(Circle((5, -0.3), 0.55, fill=False, edgecolor=RED, linewidth=1.6))
ax.text(5, -0.3, "E", color=RED, fontsize=11, ha="center", va="center")

for (x, y), name in [(A, "A"), (D, "D"), (B, "B"), (F, "F")]:
    ax.plot(x, y, "o", color=BLUE, markersize=5)
    ax.text(x - 0.45, y + 0.35, name, color=BLUE, fontsize=12)

ax.text(2.2, 8.2, "I1", color=BLUE, fontsize=11)
ax.text(7.8, 8.2, "I2", color=BLUE, fontsize=11)
ax.text(0.6, 3.0, "I", color=BLUE, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
