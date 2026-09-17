"""Reproduit le schema p.1 de ressort-frottements : masse sur ressort horizontal.

Croquis d'origine (stylo bleu) : axe x horizontal ; ressort a gauche
attache a un mur, masse (pave) a droite ; forces : poids P vers le bas,
reaction R vers le haut, tension T du ressort vers la gauche, frottement
fd ; origine O et vecteur vitesse v.

Style "stylo" : ressort et pave bleus, forces et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/physique/ressort-frottements/assets/masse-ressort-frottement.png

Usage :
  uv run scripts/reproduce_ressort_frottements_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_ressort_frottements_1.py
>>> # OK -> .../assets/masse-ressort-frottement.png (XXXXX o)
>>> # le rendu montre le ressort, la masse et les forces P, R, T, fd.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/ressort-frottements/assets/masse-ressort-frottement.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(8, 4))
ax.set_aspect("equal")
ax.set_xlim(-1, 11)
ax.set_ylim(-2.5, 3.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Mur et sol.
ax.plot([0, 0], [-2, 2], color=BLUE, linewidth=2.5)
ax.plot([0, 10.5], [-1.4, -1.4], color=BLUE, linewidth=1.5)

# Ressort (zigzag).
import numpy as np

zx = np.linspace(0.2, 4.0, 40)
zy = np.where((np.arange(40) % 2 == 0), 0.3, -0.3)
zy[0] = zy[-1] = 0
ax.plot(zx, zy, color=BLUE, linewidth=1.6)

# Masse (pave).
ax.add_patch(Rectangle((4.0, -1.4), 2.0, 1.6, fill=False, edgecolor=BLUE,
                       linewidth=1.8))
ax.text(5.0, -1.75, "m", color=BLUE, fontsize=13, ha="center")

# Axe x.
ax.annotate("", xy=(10.3, -0.6), xytext=(4.0, -0.6),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.text(10.4, -0.6, "x", color=BLUE, fontsize=13)
ax.text(4.6, -0.35, "O", color=BLUE, fontsize=11)

# Forces : P (bas), R (haut), T (gauche), fd (gauche), v (droite).
ax.annotate("", xy=(5.0, -2.6), xytext=(5.0, -1.4),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.6))
ax.text(5.25, -2.45, "P", color=RED, fontsize=12)
ax.annotate("", xy=(5.0, 2.2), xytext=(5.0, 0.2),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.6))
ax.text(5.3, 1.9, "R", color=RED, fontsize=12)
ax.annotate("", xy=(2.6, 0.9), xytext=(4.0, 0.9),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.6))
ax.text(3.0, 1.2, "T", color=RED, fontsize=12)
ax.annotate("", xy=(3.2, -0.6), xytext=(4.0, -0.6),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.2,
                            linestyle=(0, (4, 3))))
ax.text(2.55, -0.55, "fd", color=RED, fontsize=11)
ax.annotate("", xy=(7.5, 0.6), xytext=(6.0, 0.6),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.text(6.6, 0.9, "v", color=BLUE, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
