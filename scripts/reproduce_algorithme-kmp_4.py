"""Reproduit le schema "lps / meilleur candidat C_i" p.2 de algorithme-kmp.

Figure d'origine (notes manuscrites) : rangee de cases du motif
str avec fleche lps[i-1] et accolade C_i = str[i - l_{i-1} - 1 : i[
pointant l'indice i ; legende : le meilleur candidat pour l_i.
Rq manuscrite : lps[x] = l_x.

Sortie : raw/informatique/algorithme-kmp/assets/algorithme-kmp-4.png

Usage :
  uv run scripts/reproduce_algorithme-kmp_4.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/algorithme-kmp/assets/algorithme-kmp-4.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, GREEN = "#1a3fb5", "#0a7a2e"

N = 10  # cases du motif str.
L = 4   # l_{i-1} = lps[i-1], exemple.

fig, ax = plt.subplots(figsize=(10, 3.8))
ax.set_xlim(-1.5, N + 1.5)
ax.set_ylim(-2.2, 2.4)
ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Rangee str.
for k in range(N):
    rect = patches.Rectangle((k, 0), 1, 0.8, facecolor="white",
                             edgecolor="black", linewidth=1.2)
    ax.add_patch(rect)
ax.text(-1.0, 0.4, "str", ha="center", fontsize=11)

# Fleche lps[i-1] au-dessus du debut (longueur l_{i-1}).
ax.annotate("", xy=(L, 1.7), xytext=(0, 1.7),
            arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.4))
ax.text(L / 2, 1.9, "lps[i-1] = l(i-1)", ha="center",
        fontsize=10, color=BLUE)

# Accolade C_i : str[i - l_{i-1} - 1 : i[ (ici i = N, candidat bleu).
i = N
c0 = i - L - 1
ax.annotate("", xy=(c0, -0.5), xytext=(i, -0.5),
            arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.4))
ax.text((c0 + i) / 2, -1.1, "C(i) = str[i-l(i-1)-1 : i[",
        ha="center", fontsize=10, color=GREEN)
ax.text(i - 0.5, 1.1, "i", ha="center", fontsize=11, color=GREEN)

ax.text(N / 2, -1.8, "meilleur candidat pour l(i)",
        ha="center", fontsize=10)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
