"""Reproduit le graphe d'application G p.7 de parcours-graphes.

Figure d'origine (notes manuscrites) : sommets S1 (haut-gauche),
S2 (haut-droite), S4 (bas-gauche), S3 (bas-droite) ; 9 aretes :
d2 (droit haut S1-S2), d1 (boucle haut S1-S2), d4 (droit droite
S2-S3), d3 (boucle droite S2-S3), d7 (bas S4-S3), d8 (droit gauche
S4-S1), d9 (boucle gauche S4-S1), d6 (diagonale S1-S3),
d5 (diagonale S2-S4). S1, S2 impairs ; S3, S4 pairs.

Sortie : raw/informatique/parcours-graphes/assets/parcours-graphes-2.png

Usage :
  uv run scripts/reproduce_parcours-graphes_2.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/parcours-graphes/assets/parcours-graphes-2.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

POS = {
    "S1": (0.0, 1.0),
    "S2": (1.0, 1.0),
    "S3": (1.0, 0.0),
    "S4": (0.0, 0.0),
}
STRAIGHT = {
    "d2": ("S1", "S2"),
    "d4": ("S2", "S3"),
    "d7": ("S4", "S3"),
    "d8": ("S4", "S1"),
}
DIAG = {"d6": ("S1", "S3"), "d5": ("S2", "S4")}
LOOPS = {"d1": (0.5, 1.28), "d3": (1.28, 0.5), "d9": (-0.28, 0.5)}


def _mid(p, q):
    """Milieu du segment pq."""
    return ((p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0)


fig, ax = plt.subplots(figsize=(6.5, 6))
ax.set_xlim(-0.6, 1.6)
ax.set_ylim(-0.4, 1.6)
ax.set_aspect("equal")
ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

for lab, (u, v) in list(STRAIGHT.items()) + list(DIAG.items()):
    x1, y1 = POS[u]
    x2, y2 = POS[v]
    ax.plot([x1, x2], [y1, y2], color=BLUE, linewidth=1.6)
    mx, my = _mid((x1, y1), (x2, y2))
    off = {"d5": (0.05, -0.10), "d6": (-0.12, 0.03)}.get(lab, (0.04, 0.04))
    ax.text(mx + off[0], my + off[1], lab, ha="left", va="bottom", fontsize=10, color=BLUE,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.8})

for lab, (x, y) in LOOPS.items():
    loop = Circle((x, y), 0.16, fill=False, edgecolor=RED, linewidth=1.6)
    ax.add_patch(loop)
    ax.text(x + 0.04, y + 0.16, lab, ha="left", va="bottom", fontsize=10, color=RED)

for node, (x, y) in POS.items():
    ax.plot([x], [y], marker="o", color=BLUE, markersize=9)
    ax.text(x - 0.07, y + 0.07, node, ha="right", va="bottom", fontsize=12, color=BLUE)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
