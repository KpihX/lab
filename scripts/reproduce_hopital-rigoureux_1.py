"""Reproduit le contre-exemple de la p.6 de hopital-rigoureux (limite sequentielle).

Croquis d'origine (stylo bleu sur papier) : axes x (0, 3) et y (1, 2) ;
courbe partant de l'origine, montant vers le point creux (3, 1), saut en
(3, 2) (point plein), puis reprise croissante en dents de scie.
Contexte manuscrit : u_n = 3 -> a = 3, f(x) -> 1 quand x -> a, mais
f(u_n) = f(3) = 2 -> 2 != 1, d'ou l'hypothese u_n != a.

Style "stylo" : courbe bleue, points et titre rouges, fond quadrille bleu.

Sortie : raw/analyse-fonctions/hopital-rigoureux/assets/contre-exemple-limite-sequentielle.png

Usage :
  uv run scripts/reproduce_hopital-rigoureux_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_hopital-rigoureux_1.py
>>> # OK -> .../assets/contre-exemple-limite-sequentielle.png (NNNNN o)
>>> # le rendu montre le saut en x = 3 (creux en 1, plein en 2).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions"
    "/hopital-rigoureux/assets/contre-exemple-limite-sequentielle.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"


def f_left(x):
    """Branche gauche du croquis : monotone de (0,0) vers (3,1)."""
    return 1 - np.exp(-x / 1.5)


xs_l = np.linspace(0, 3, 241)
ys_l = f_left(xs_l)
xs_l = xs_l[ys_l < 1.0]
ys_l = ys_l[ys_l < 1.0]

xs_r = np.linspace(3, 5.2, 160)
ys_r = 2.0 + 0.35 * (xs_r - 3) + 0.12 * np.sin(6 * (xs_r - 3))

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)  # axe des abscisses
ax.axvline(0, color=BLUE, linewidth=1.0)  # axe des ordonnees
ax.plot(xs_l, ys_l, color=BLUE, linewidth=1.6)  # branche gauche
ax.plot(xs_r, ys_r, color=BLUE, linewidth=1.6)  # reprise a droite
ax.plot(3, 1, "o", color=BLUE, markersize=6, markerfacecolor="white",
        markeredgewidth=1.6)  # point creux (3, 1) : limite
ax.plot(3, 2, "o", color=RED, markersize=6)  # point plein (3, 2) : valeur
ax.plot([3], [1], "o", color=RED, markersize=2)  # rappel du saut
ax.set_title("f(x) -> 1 en a = 3 mais f(3) = 2", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
