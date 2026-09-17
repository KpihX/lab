"""Reproduit les schemas types p.1 de associations-resistances : reductions serie/parallele.

Planche d'origine (stylo bleu) : une quinzaine de vignettes de circuits
entre bornes A et B (resistances R0..R5 en rectangles), reduites pas a pas
en Req serie ou parallele (annotations "serie", "parallele", "Req").
Reproduction synthetique des trois motifs recurrents : serie, parallele,
mixte (R1 en serie avec R2//R3).

Style "stylo" : fils et rectangles bleus, Req et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/physique/associations-resistances/assets/reductions-serie-parallele.png

Usage :
  uv run scripts/reproduce_associations_resistances_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_associations_resistances_1.py
>>> # OK -> .../assets/reductions-serie-parallele.png (XXXXX o)
>>> # le rendu montre les trois motifs serie, parallele et mixte entre A et B.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/associations-resistances/assets/reductions-serie-parallele.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)


def resistor(ax, x, y, w, h, label):
    """Dessine une resistance rectangle avec son etiquette."""
    ax.add_patch(Rectangle((x, y), w, h, fill=False, edgecolor=BLUE, linewidth=1.6))
    ax.text(x + w / 2, y + h / 2, label, color=BLUE, fontsize=10,
            ha="center", va="center")


def bornes(ax, label_a="A", label_b="B"):
    """Bornes A (gauche) et B (droite) reliees par des fils."""
    ax.text(0.3, 3, label_a, color=BLUE, fontsize=12)
    ax.text(9.3, 3, label_b, color=BLUE, fontsize=12)


# (a) Serie : R1 - R2 sur un fil unique.
ax = axes[0]
bornes(ax)
ax.plot([1, 3], [3, 3], color=BLUE, linewidth=1.5)
resistor(ax, 3, 2.4, 1.6, 1.2, "R1")
ax.plot([4.6, 5.4], [3, 3], color=BLUE, linewidth=1.5)
resistor(ax, 5.4, 2.4, 1.6, 1.2, "R2")
ax.plot([7, 9], [3, 3], color=BLUE, linewidth=1.5)
ax.text(5, 0.7, "serie", color=RED, fontsize=11, ha="center")

# (b) Parallele : R1 // R2 entre deux noeuds.
ax = axes[1]
bornes(ax)
ax.plot([1, 3], [3, 3], color=BLUE, linewidth=1.5)
ax.plot([7, 9], [3, 3], color=BLUE, linewidth=1.5)
ax.plot([3, 3], [1.5, 4.5], color=BLUE, linewidth=1.5)
ax.plot([7, 7], [1.5, 4.5], color=BLUE, linewidth=1.5)
resistor(ax, 4.2, 3.9, 1.6, 1.2, "R1")
ax.plot([3, 4.2], [4.5, 4.5], color=BLUE, linewidth=1.5)
ax.plot([5.8, 7], [4.5, 4.5], color=BLUE, linewidth=1.5)
resistor(ax, 4.2, 0.9, 1.6, 1.2, "R2")
ax.plot([3, 4.2], [1.5, 1.5], color=BLUE, linewidth=1.5)
ax.plot([5.8, 7], [1.5, 1.5], color=BLUE, linewidth=1.5)
ax.text(5, 0.2, "parallele", color=RED, fontsize=11, ha="center")

# (c) Mixte : R1 en serie avec (R2 // R3).
ax = axes[2]
bornes(ax)
ax.plot([1, 2.2], [3, 3], color=BLUE, linewidth=1.5)
resistor(ax, 2.2, 2.4, 1.4, 1.2, "R1")
ax.plot([3.6, 4.4], [3, 3], color=BLUE, linewidth=1.5)
ax.plot([7.6, 9], [3, 3], color=BLUE, linewidth=1.5)
ax.plot([4.4, 4.4], [1.5, 4.5], color=BLUE, linewidth=1.5)
ax.plot([7.6, 7.6], [1.5, 4.5], color=BLUE, linewidth=1.5)
resistor(ax, 5.3, 3.9, 1.4, 1.2, "R2")
ax.plot([4.4, 5.3], [4.5, 4.5], color=BLUE, linewidth=1.5)
ax.plot([6.7, 7.6], [4.5, 4.5], color=BLUE, linewidth=1.5)
resistor(ax, 5.3, 0.9, 1.4, 1.2, "R3")
ax.plot([4.4, 5.3], [1.5, 1.5], color=BLUE, linewidth=1.5)
ax.plot([6.7, 7.6], [1.5, 1.5], color=BLUE, linewidth=1.5)
ax.text(5, 0.2, "mixte", color=RED, fontsize=11, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
