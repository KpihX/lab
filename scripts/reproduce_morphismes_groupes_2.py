"""Reproduit le triangle p/χ p.3 du manuscrit morphismes-groupes.

Manuscrit d'origine (morphismes-groupes.pdf, p.3 bas, encre bleue) :
φ = χ ∘ p avec φ : (G1,×) → (φ(G1) ⊂ G2,∘) en haut (flèche
horizontale), p : (G1,×) ↘ (G1/Ker φ, ×bar) en diagonale
descendante, χ : (G1/Ker φ, ×bar) ↗ (φ(G1) ⊂ G2,∘) en diagonale
montante. Ici : mêmes 3 noeuds + 3 flèches étiquetées φ, p, χ.

Sortie : raw/algebre-arithmetique/morphismes-groupes/assets/triangle-p-chi.png

Usage :
  uv run scripts/reproduce_morphismes_groupes_2.py  (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/morphismes-groupes/assets/triangle-p-chi.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLEU = "#1e40af"
ROUGE = "#c81e1e"
QUADRILLE = "#9db3d8"

# Noeuds tels que disposés sur le manuscrit : φ en haut, p ↘, χ ↗.
A = (-2.0, 1.2)  # (G1, x)
B = (2.0, 1.2)  # (phi(G1) ⊂ G2, o)
C = (0.0, -1.2)  # (G1/Ker phi, xbar)
LABELS = {
    A: r"$(G_1,\times)$",
    B: r"$(\varphi(G_1)\subset G_2,\circ)$",
    C: r"$(G_1/\mathrm{Ker}\,\varphi,\bar{\times})$",
}

fig, ax = plt.subplots(figsize=(7, 5.2))
ax.set_xlim(-3.6, 3.6)
ax.set_ylim(-2.4, 2.5)
ax.grid(True, color=QUADRILLE, linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.set_xticks(range(-3, 4))
ax.set_yticks(range(-2, 3))
ax.tick_params(labelbottom=False, labelleft=False, length=0, color=QUADRILLE)
for spine in ax.spines.values():
    spine.set_visible(False)

for (x, y), lab in LABELS.items():
    ax.text(x, y, lab, color=BLEU, fontsize=13, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
                      edgecolor=BLEU, linewidth=1.6), zorder=3)

def fleche(p1, p2, etiquette, decal):
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="->", mutation_scale=16, color=BLEU, linewidth=2.0,
        connectionstyle="arc3,rad=0.0", shrinkA=12, shrinkB=12, zorder=2))
    mx, my = (p1[0] + p2[0]) / 2 + decal[0], (p1[1] + p2[1]) / 2 + decal[1]
    ax.text(mx, my, etiquette, color=BLEU, fontsize=16, fontweight="bold",
            ha="center", va="center",
            bbox=dict(boxstyle="circle,pad=0.25", facecolor="white",
                      edgecolor="none"), zorder=4)

fleche(A, B, "φ", (0, 0.35))  # φ horizontale en haut
fleche(A, C, "p", (-0.35, 0.0))  # p diagonale descendante
fleche(C, B, "χ", (0.35, 0.0))  # χ diagonale montante

ax.text(0, 2.05, "Décomposition canonique : φ = χ ∘ p (p. 3)", color=ROUGE,
        fontsize=12, fontweight="bold", ha="center", va="center")
ax.text(0, -2.05, "p surjective, χ bijective", color=ROUGE, fontsize=10,
        ha="center", va="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
