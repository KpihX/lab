"""Reproduit la figure p.2 de Normes en dimension infinie : pic triangulaire.

Schema d'origine (stylo bleu sur papier) : graphe de f_n^2 sur [0, b],
nul sauf sur [a, a+1/n] ou il forme un triangle de hauteur n en a,
s'annulant en a+1/n ; axe des abscisses avec les marques 0, a,
a+1/n, b ; fleche et etiquette "f_n^2" vers le segment descendant,
etiquette "n" pres du sommet.

Style "stylo" : traits et annotations bleus, fond quadrille bleu.

Sortie : raw/analyse-fonctions/normes-dim-infinie/assets/pic-triangulaire.png

Usage :
  uv run scripts/reproduce_normes_dim_infinie_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_normes_dim_infinie_1.py
>>> # OK -> .../assets/pic-triangulaire.png (NNNNN o)
>>> # le rendu montre le pic triangulaire de hauteur n en a, zero en a+1/n.
"""

import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions"
    "/normes-dim-infinie/assets/pic-triangulaire.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

# Positions generiques (a=1, 1/n=0.25, b=3, hauteur n=2).
a, peak, zero, b = 1.0, 2.0, 1.25, 3.0

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(-0.3, 3.4)
ax.set_ylim(-0.5, 2.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Axe des abscisses et ordonnees.
ax.plot([-0.3, 3.4], [0, 0], color=BLUE, linewidth=1.0)
ax.plot([0, 0], [-0.5, 2.6], color=BLUE, linewidth=1.0)

# Montant vertical en a, segment descendant, palier nul jusqu'a b.
ax.plot([a, a], [0, peak], color=BLUE, linewidth=1.5)
ax.plot([a, zero], [peak, 0], color=BLUE, linewidth=1.5)
ax.plot([zero, b], [0, 0], color=BLUE, linewidth=2.5)
# Prolongement nul avant a (comme sur le croquis).
ax.plot([0, a], [0, 0], color=BLUE, linewidth=1.0)

# Marques d'abscisses.
for x in (a, zero, b):
    ax.plot([x, x], [-0.08, 0.08], color=BLUE, linewidth=1.2)
ax.text(0.02, -0.28, "0", color=BLUE, fontsize=12, ha="left")
ax.text(a, -0.28, "a", color=BLUE, fontsize=12, ha="center")
ax.text(zero, -0.28, "a+1/n", color=BLUE, fontsize=12, ha="center")
ax.text(b, -0.28, "b", color=BLUE, fontsize=12, ha="center")

# Annotations : hauteur n et etiquette f_n^2 avec fleche.
ax.text(a - 0.28, peak - 0.25, "n", color=BLUE, fontsize=13, ha="center")
ax.plot(a, peak, "o", color=BLUE, markersize=4)
ax.annotate(
    "$f_n^2$",
    xy=((a + zero) / 2, peak / 2),
    xytext=((a + zero) / 2 + 0.35, peak / 2 + 0.55),
    color=RED,
    fontsize=13,
    ha="center",
    arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.2),
)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
