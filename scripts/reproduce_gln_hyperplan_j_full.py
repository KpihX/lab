"""Reproduit le schéma J (cas rg(A) = n) p.2 du manuscrit gln-hyperplan.

Matrice dessinee : permutation cyclique (trace nulle, rang plein) ::

    J = [[0, I_{n-1}],
         [1, 0 ... 0]]

soit J[i, i+1] = 1 et J[n, 1] = 1, 0 ailleurs. Illustration avec n = 5.
Le scan montre exactement cette forme (1re ligne "0 1 0 ... 0",
derniere ligne "1 0 ... 0", blocs "0 / I_{n-1} / 1 / 0...0").

Style "stylo" : quadrille #9db3d8, cases "1" en bleu, "0" en gris,
crochets bleu stylo, separation de blocs en rouge.
Sortie : raw/algebre-arithmetique/gln-hyperplan/assets/j-rang-plein.png
Usage : uv run scripts/reproduce_gln_hyperplan_j_full.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/gln-hyperplan/assets/j-rang-plein.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLEU = "#1e40af"
ROUGE = "#c81e1e"
GRIS = "#6b7280"
QUADRILLE = "#9db3d8"

n = 5
ones = [(i, i + 1) for i in range(n - 1)] + [(n - 1, 0)]

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.6, n + 1.3)
ax.set_ylim(-1.4, n + 1.0)
ax.invert_yaxis()
ax.grid(True, color=QUADRILLE, linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.tick_params(labelbottom=False, labelleft=False, length=0, color=QUADRILLE)

for i in range(n):
    for j in range(n):
        if (i, j) in ones:
            ax.add_patch(Rectangle((j, i), 1, 1, facecolor="#dbe4ff",
                                   edgecolor=BLEU, linewidth=1.6))
            ax.text(j + 0.5, i + 0.5, "1", color=BLEU, fontsize=16,
                    fontweight="bold", ha="center", va="center")
        else:
            ax.text(j + 0.5, i + 0.5, "0", color=GRIS, fontsize=11,
                    ha="center", va="center")

# Crochets bleu stylo autour de la matrice (bords x=0 et x=n).
ax.plot([-0.2, -0.4, -0.4, -0.2], [0, 0, n, n], color=BLEU, linewidth=2.0)
ax.plot([n + 0.2, n + 0.4, n + 0.4, n + 0.2], [0, 0, n, n],
        color=BLEU, linewidth=2.0)

# Separation des blocs [0 | I_{n-1}] / [1 | 0...0] : traits rouges.
ax.plot([0, n], [n - 1, n - 1], color=ROUGE, linewidth=1.2,
        linestyle="--")
ax.plot([1, 1], [0, n - 1], color=ROUGE, linewidth=1.2,
        linestyle="--")

ax.text(-0.9, n / 2, "J =", color=BLEU, fontsize=18, fontweight="bold",
        ha="right", va="center")
ax.text(0.5, -0.45, "0", color=BLEU, fontsize=13, ha="center", va="center")
ax.text((1 + n) / 2, -0.45, "I(n-1)", color=ROUGE, fontsize=13,
        fontweight="bold", ha="center", va="center")
ax.text(n, n + 0.55, "tr J = 0,  rg J = n", color=ROUGE, fontsize=11,
        ha="right", va="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
