"""Reproduit la figure PB p.1 de parcours-graphes.

Figure d'origine (notes manuscrites) : graphe a 4 sommets
A (haut-gauche), B (haut-droite), D (bas-gauche), C (bas-droite) ;
K4 (6 aretes entre les 4 sommets) + 1 boucle par sommet, d'ou
deg(A) = deg(B) = deg(C) = deg(D) = 5.

Sortie : raw/informatique/parcours-graphes/assets/parcours-graphes-1.png

Usage :
  uv run scripts/reproduce_parcours-graphes_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/parcours-graphes/assets/parcours-graphes-1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

POS = {
    "A": (0.0, 1.0),
    "B": (1.0, 1.0),
    "C": (1.0, 0.0),
    "D": (0.0, 0.0),
}
EDGES = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C"), ("B", "D")]
LOOPS = {"A": (-0.18, 0.18), "B": (0.18, 0.18), "C": (0.18, -0.18), "D": (-0.18, -0.18)}

LABELS = {"A": (-0.10, 0.10), "B": (0.10, 0.10), "C": (0.12, -0.06), "D": (-0.10, -0.02)}

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.6, 1.6)
ax.set_ylim(-0.6, 1.6)
ax.set_aspect("equal")
ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

for u, v in EDGES:
    x1, y1 = POS[u]
    x2, y2 = POS[v]
    ax.plot([x1, x2], [y1, y2], color=BLUE, linewidth=1.6)

for node, (dx, dy) in LOOPS.items():
    x, y = POS[node]
    loop = Circle((x + dx, y + dy), 0.16, fill=False, edgecolor=RED, linewidth=1.6)
    ax.add_patch(loop)

for node, (x, y) in POS.items():
    ax.plot([x], [y], marker="o", color=BLUE, markersize=9)
    dx, dy = LABELS[node]
    ax.text(x + dx, y + dy, node, ha="center", va="center", fontsize=13, color=BLUE,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.0})

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
