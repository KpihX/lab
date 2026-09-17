"""Reproduit la courbe (Cg) de f(x) = 1 - 2x*sqrt(1-x^2) sur [-1, 1].

Croquis d'origine (stylo bleu sur papier, p.2 de accroissements-finis) :
courbe partant de (-1, 1), maximum (2) en x = -1/sqrt(2), traversee de
l'axe des ordonnees en (0, 1), minimum (0) en x = 1/sqrt(2), remontee
en (1, 1). Tableau de variations : f' + 0 - 0 +.

Style "stylo" : courbe bleue, points et titre rouges, fond quadrille bleu.

Sortie : raw/analyse-fonctions/accroissements-finis/assets/courbe-cg.png

Usage :
  uv run scripts/reproduce_accroissements-finis_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_accroissements-finis_1.py
>>> # OK -> .../assets/courbe-cg.png (NNNNN o)
>>> # le rendu montre la courbe en cloche asymetrique avec max 2 et min 0.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions"
    "/accroissements-finis/assets/courbe-cg.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"


def f(x):
    """La fonction etudiee : f(x) = 1 - 2x*sqrt(1-x^2)."""
    return 1 - 2 * x * np.sqrt(1 - x**2)


xs = np.linspace(-1, 1, 801)
ys = f(xs)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)  # axe des abscisses
ax.axvline(0, color=BLUE, linewidth=1.0)  # axe des ordonnees
ax.plot(xs, ys, color=BLUE, linewidth=1.6)  # (Cg)

pts = [(-1.0, 1.0), (-1 / np.sqrt(2), 2.0), (1 / np.sqrt(2), 0.0), (1.0, 1.0)]
for px, py in pts:
    ax.plot(px, py, "o", color=RED, markersize=5)
ax.set_title("(Cg) : f(x) = 1 - 2x*sqrt(1-x^2)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
