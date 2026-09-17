"""Reproduit le schema "cas d'echec en (i,j), j>1" p.1 de algorithme-kmp.

Figure d'origine (notes manuscrites) : portion de txt avec echec
en position i (case hachuree) ; a-ie essai : motif str aligne avec
ses indices 0..K..j (K = longueur du shift candidat) ; (a+1)-ie
essai : motif decale de K (portion Sj recouvrant ti), la comparaison
reprend en position i du texte.

Sortie : raw/informatique/algorithme-kmp/assets/algorithme-kmp-2.png

Usage :
  uv run scripts/reproduce_algorithme-kmp_2.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/algorithme-kmp/assets/algorithme-kmp-2.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(9, 3.4))
ax.set_xlim(-2.2, 13.5)
ax.set_ylim(-2.7, 1.8)
ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)


def row(y, x0, cells, edge):
    """Dessine des cases ; cells = liste de bool (True = hachuree)."""
    for k, h in enumerate(cells):
        rect = patches.Rectangle((x0 + k, y), 1, 0.8, facecolor="white",
                                 edgecolor=edge, linewidth=1.2,
                                 hatch="///" if h else None)
        ax.add_patch(rect)


# Portion de txt, echec en i (case hachuree).
row(0.6, 0, [False] * 3 + [True] + [False] * 7, "black")
ax.text(3.5, 1.7, "i", ha="center", fontsize=11)
ax.text(3.5, 0.35, "j", ha="center", fontsize=10, color=BLUE)

# a-ie essai : motif avec indices 0, K, j.
row(-0.5, 0, [False] * 3 + [True], BLUE)
ax.text(0.5, 0.05, "0", ha="center", fontsize=10, color=BLUE)
ax.text(2.0, 0.05, "K", ha="center", fontsize=10, color=BLUE)
ax.text(3.5, 0.05, "j", ha="center", fontsize=10, color=BLUE)
ax.text(-1.9, -0.1, "a-ie essai", ha="center", fontsize=10, color=BLUE)

# (a+1)-ie essai : motif decale de K, comparaison reprend en i.
row(-1.6, 2, [False] * 4, RED)
ax.text(4.5, -1.15, "j", ha="center", fontsize=10, color=RED)
ax.text(2.5, -1.15, "Sj", ha="center", fontsize=10, color=RED)
ax.text(3.5, -1.15, "K", ha="center", fontsize=10, color=RED)
ax.text(-1.9, -1.2, "(a+1)-ie essai", ha="center", fontsize=10, color=RED)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
