"""Reproduit la figure p.1 de marees : Terre (O, A, B, C, D) face a la Lune.

Schema d'origine (stylo bleu) : cercle terrestre de centre O avec A a
droite (cote Lune), D a gauche, B en haut, C en bas ; fleches de forces
d'attraction lunaire ; la Lune (L) a droite avec les constantes
(RL, G, ML, D, RT) rappelees en haut a droite.

Style "stylo" : cercle et fleches bleus, points et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/physique/marees/assets/terre-lune-points.png

Usage :
  uv run scripts/reproduce_marees_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_marees_1.py
>>> # OK -> .../assets/terre-lune-points.png (XXXXX o)
>>> # le rendu montre la Terre, ses points A-D et la Lune L.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/marees/assets/terre-lune-points.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_aspect("equal")
ax.set_xlim(-4, 10)
ax.set_ylim(-3.5, 3.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Terre.
ax.add_patch(Circle((0, 0), 1.5, fill=False, edgecolor=BLUE, linewidth=1.8))
ax.plot(0, 0, "o", color=BLUE, markersize=5)
ax.text(0.15, -0.35, "O", color=BLUE, fontsize=12)

pts = {"A": (1.5, 0), "D": (-1.5, 0), "B": (0, 1.5), "C": (0, -1.5)}
for name, (x, y) in pts.items():
    ax.plot(x, y, "o", color=RED, markersize=4)
    ax.text(x + 0.15, y + 0.15, name, color=RED, fontsize=12)

# Fleches d'attraction vers la Lune.
for (x, y) in [(1.5, 0), (0, 1.0), (0, -1.0)]:
    ax.annotate("", xy=(x + 1.2, y), xytext=(x, y),
                arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.text(2.0, 0.35, "FUA", color=BLUE, fontsize=11)

# Lune.
ax.add_patch(Circle((8, 0), 0.7, fill=False, edgecolor=BLUE, linewidth=1.8))
ax.text(8, -1.2, "L", color=BLUE, fontsize=13)
ax.plot([1.5, 7.3], [0, 0], color=BLUE, linewidth=1.0, linestyle=(0, (4, 3)))

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
