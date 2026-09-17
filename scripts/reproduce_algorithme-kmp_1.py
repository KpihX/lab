"""Reproduit le schema "Contexte" p.1 de algorithme-kmp.

Figure d'origine (notes manuscrites) : ligne de cases du texte
txt (indices 0..m-n..m-1), avec m = long(txt), n = long(str) ;
1er essai : motif str aligne en 0..n-1 -> echec ;
2e essai : motif decale d'une position -> echec (le motif
glisse jusqu'en fin de texte).

Sortie : raw/informatique/algorithme-kmp/assets/algorithme-kmp-1.png

Usage :
  uv run scripts/reproduce_algorithme-kmp_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/algorithme-kmp/assets/algorithme-kmp-1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

M, N = 14, 4  # txt de longueur m, motif str de longueur n.

fig, ax = plt.subplots(figsize=(9, 3.2))
ax.set_xlim(-1.5, M + 0.5)
ax.set_ylim(-2.6, 1.6)
ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)


def row(y, x0, n, edge, hatch_last=False, labels=None):
    """Dessine une rangee de n cases a partir de x0, ordonnee y."""
    for k in range(n):
        fc = "white"
        ec = edge
        hatch = None
        if hatch_last and k == n - 1:
            hatch = "///"
        rect = patches.Rectangle((x0 + k, y), 1, 0.8, facecolor=fc,
                                 edgecolor=ec, linewidth=1.2, hatch=hatch)
        ax.add_patch(rect)
    if labels:
        for k, lab in labels.items():
            ax.text(x0 + k + 0.5, y + 1.0, lab, ha="center",
                    fontsize=9, color=edge)


# Ligne du texte.
row(0.4, 0, M, "black", labels={0: "0", M - N: "m-n", M - 1: "m-1"})
ax.text(-1.2, 0.8, "txt", ha="center", fontsize=11)
ax.text(M + 0.2, 0.8, "m = long(txt)", ha="left", fontsize=10)
ax.text(M + 0.2, 0.3, "n = long(str)", ha="left", fontsize=10)

# 1er essai : motif en position 0.
row(-0.7, 0, N, BLUE, hatch_last=True,
    labels={0: "0", N - 1: "n-1"})
ax.text(-1.2, -0.3, "1er essai", ha="center", fontsize=10, color=BLUE)
ax.text(N + 0.3, -0.3, "-> echec", ha="left", fontsize=10)

# 2e essai : motif decale d'une position.
row(-1.8, 1, N, RED, hatch_last=True)
ax.text(-1.2, -1.4, "2e essai", ha="center", fontsize=10, color=RED)
ax.text(N + 1.3, -1.4, "-> echec", ha="left", fontsize=10)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
