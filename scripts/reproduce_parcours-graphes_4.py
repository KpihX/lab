"""Reproduit les etapes intermediaires G' et G'1 p.7 de parcours-graphes.

Figure d'origine (notes manuscrites, p.7) :
- G' = G sans C (C = d2, droit haut S1-S2) : reste d1 (boucle haut),
  d6/d5 (diagonales), d4 (droit droite), d3 (boucle droite),
  d7 (bas), d8 (droit gauche), d9 (boucle gauche).
- G'1 = G' sans B1 (B1 = d1 -> d3 -> d7 -> d9) : reste le triangle
  d6 (S1-S3), d4 (S2-S3), d5 (S2-S4), d8 (S4-S1). Le carre hachure
  a gauche sur le manuscrit (B1 retire/rature) n'est pas un graphe.

Sortie : raw/informatique/parcours-graphes/assets/parcours-graphes-4.png

Usage :
  uv run scripts/reproduce_parcours-graphes_4.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/parcours-graphes/assets/parcours-graphes-4.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

POS = {
    "S1": (0.0, 1.0),
    "S2": (1.0, 1.0),
    "S3": (1.0, 0.0),
    "S4": (0.0, 0.0),
}
# G' : tout sauf d2.
GPRIME_STRAIGHT = {
    "d4": ("S2", "S3"),
    "d7": ("S4", "S3"),
    "d8": ("S4", "S1"),
}
GPRIME_DIAG = {"d6": ("S1", "S3"), "d5": ("S2", "S4")}
GPRIME_LOOPS = {"d1": (0.5, 1.28), "d3": (1.28, 0.5), "d9": (-0.28, 0.5)}
# G'1 : residu apres B1 = d1 -> d3 -> d7 -> d9.
G1_STRAIGHT = {"d4": ("S2", "S3"), "d8": ("S4", "S1")}
G1_DIAG = {"d6": ("S1", "S3"), "d5": ("S2", "S4")}


def _mid(p, q):
    return ((p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0)


def _draw(ax, straight, diag, loops):
    for lab, (u, v) in list(straight.items()) + list(diag.items()):
        x1, y1 = POS[u]
        x2, y2 = POS[v]
        ax.plot([x1, x2], [y1, y2], color=BLUE, linewidth=1.6)
        mx, my = _mid((x1, y1), (x2, y2))
        off = {"d5": (0.05, -0.10), "d6": (-0.12, 0.03)}.get(lab, (0.04, 0.04))
        ax.text(mx + off[0], my + off[1], lab, ha="left", va="bottom",
                fontsize=10, color=BLUE,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.8})
    for lab, (x, y) in loops.items():
        ax.add_patch(Circle((x, y), 0.16, fill=False, edgecolor=RED, linewidth=1.6))
        ax.text(x + 0.04, y + 0.16, lab, ha="left", va="bottom", fontsize=10, color=RED)
    for node, (x, y) in POS.items():
        ax.plot([x], [y], marker="o", color=BLUE, markersize=9)
        ax.text(x - 0.07, y + 0.07, node, ha="right", va="bottom", fontsize=12, color=BLUE)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
for ax in (ax1, ax2):
    ax.set_xlim(-0.6, 1.6)
    ax.set_ylim(-0.4, 1.6)
    ax.set_aspect("equal")
    ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
    ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

ax1.set_title("G' = G sans C (C = d2 retire)", fontsize=11)
_draw(ax1, GPRIME_STRAIGHT, GPRIME_DIAG, GPRIME_LOOPS)

ax2.set_title("G'1 = G' sans B1 (reste d6, d4, d5, d8)", fontsize=11)
_draw(ax2, G1_STRAIGHT, G1_DIAG, {})

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
