"""Reproduit la figure p.2 de marees : bourrelets de maree et axe Lune-Terre.

Schema d'origine (stylo bleu) : Terre (centre O) entouree d'une ellipse
(bourrelets) avec A a droite (cote Lune), D a gauche ; etiquettes JOUR
(cote nuit/jour), NUIT, AUBE ; forces FUA, FUB, FUC, FUD, FUO ; axe L-T
jusqu'a la Lune (L) a droite avec fleche de revolution.

Style "stylo" : Terre et bourrelet bleus, Lune et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/physique/marees/assets/bourrelets-maree.png

Usage :
  uv run scripts/reproduce_marees_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_marees_2.py
>>> # OK -> .../assets/bourrelets-maree.png (XXXXX o)
>>> # le rendu montre la Terre, les bourrelets, l'axe L-T et la Lune.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/marees/assets/bourrelets-maree.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_aspect("equal")
ax.set_xlim(-4, 11)
ax.set_ylim(-3.5, 3.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Bourrelet de maree (ellipse) puis Terre.
ax.add_patch(Ellipse((0, 0), 5.2, 3.4, fill=False, edgecolor=BLUE, linewidth=1.6))
ax.add_patch(Circle((0, 0), 1.5, fill=False, edgecolor=BLUE, linewidth=1.8))
ax.plot(0, 0, "o", color=BLUE, markersize=5)
ax.text(0.15, -0.4, "O", color=BLUE, fontsize=12)

# Points A (cote Lune) et D, B, C.
ax.plot(1.5, 0, "o", color=RED, markersize=4)
ax.text(1.65, 0.2, "A", color=RED, fontsize=12)
ax.plot(-1.5, 0, "o", color=RED, markersize=4)
ax.text(-1.85, 0.2, "D", color=RED, fontsize=12)
ax.text(-0.2, 2.2, "B", color=BLUE, fontsize=12)
ax.text(-0.2, -2.5, "C", color=BLUE, fontsize=12)

# Forces differentielles.
ax.annotate("", xy=(3.4, 0), xytext=(1.5, 0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.text(2.2, 0.35, "FUA", color=BLUE, fontsize=11)
ax.annotate("", xy=(-3.6, 0), xytext=(-1.5, 0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.text(-3.0, 0.35, "FUD", color=BLUE, fontsize=11)

# Axe L-T jusqu'a la Lune.
ax.plot([1.5, 8.3], [0, 0], color=BLUE, linewidth=1.2)
ax.text(4.5, 0.35, "L-T", color=BLUE, fontsize=11)
ax.add_patch(Circle((9, 0), 0.7, fill=False, edgecolor=RED, linewidth=1.8))
ax.text(9, -1.2, "L", color=RED, fontsize=13)
ax.annotate("", xy=(9.9, 1.3), xytext=(9.6, 0.7),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4))

# Etiquettes jour/nuit/aube.
ax.text(3.2, 1.1, "NUIT", color=RED, fontsize=11)
ax.text(3.2, -0.9, "NUIT", color=RED, fontsize=11)
ax.text(-3.9, 1.1, "JOUR", color=RED, fontsize=11)
ax.text(-3.9, -0.9, "JOUR", color=RED, fontsize=11)
ax.text(-0.4, -3.1, "AUBE", color=RED, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
