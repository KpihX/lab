"""Reproduit le schema "cas d'echec en (i, j), j = 0" p.1 de algorithme-kmp.

Figure d'origine (notes manuscrites) : courte rangee de cases du
texte txt avec echec en position i (case hachuree) ; motif str
court en dessous avec echec en position j = 0 (case hachuree).
Conclusion manuscrite : il faut juste decaler str d'une position
vers la droite, ce qui revient a incrementer i dans le processus.

Sortie : raw/informatique/algorithme-kmp/assets/algorithme-kmp-3.png

Usage :
  uv run scripts/reproduce_algorithme-kmp_3.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/algorithme-kmp/assets/algorithme-kmp-3.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE = "#1a3fb5"

fig, ax = plt.subplots(figsize=(9, 3.4))
ax.set_xlim(-2.2, 10.5)
ax.set_ylim(-2.4, 1.8)
ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)


def row(y, x0, n, edge, hatch_idx=None, labels=None):
    """Dessine une rangee de n cases a partir de x0, ordonnee y."""
    for k in range(n):
        hatch = "///" if hatch_idx is not None and k == hatch_idx else None
        rect = patches.Rectangle((x0 + k, y), 1, 0.8, facecolor="white",
                                 edgecolor=edge, linewidth=1.2, hatch=hatch)
        ax.add_patch(rect)
    if labels:
        for k, lab in labels.items():
            ax.text(x0 + k + 0.5, y + 1.0, lab, ha="center",
                    fontsize=10, color=edge)


# Rangee txt : echec en position i.
row(0.4, 0, 8, "black", hatch_idx=5, labels={5: "i"})
ax.text(-1.4, 0.8, "txt", ha="center", fontsize=11)

# Motif str : echec en position j = 0.
row(-0.9, 3, 3, BLUE, hatch_idx=0, labels={0: "j = 0"})
ax.text(1.6, -0.5, "str", ha="center", fontsize=11, color=BLUE)

# Conclusion : decalage d'une position -> increment de i.
ax.annotate("", xy=(4.5, -1.7), xytext=(3.5, -1.7),
            arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.5))
ax.text(4.0, -2.1, "decaler str d'une position <-> i <- i + 1",
        ha="center", fontsize=10, color=BLUE)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
