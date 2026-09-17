"""Reproduit l'equation de fonctions (E) : f(f(x)f(y)) + f(x+y) = f(xy) (p. equation-fonctions).

Figure d'origine : page de calculs manuscrits, pas de schema geometrique.
Reproduction = illustration du fond : les trois solutions annoncees
x |-> 1-x (bleu), x |-> -1+x (rouge), x |-> 0 (gris) sur [-3, 3].

Style "stylo" : courbes bleu/rouge, titre rouge, fond quadrille bleu.

Sortie : raw/analyse-fonctions/equation-fonctions/assets/equation-fonctions.png

Usage :
  uv run scripts/reproduce_equation-fonctions_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_equation-fonctions_1.py
>>> # OK -> .../assets/equation-fonctions.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/equation-fonctions/assets/equation-fonctions.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

xs = np.linspace(-3, 3, 1201)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.axvline(0, color=BLUE, linewidth=1.0)
ax.plot(xs, 1 - xs, color=BLUE, linewidth=1.6)
ax.plot(xs, -1 + xs, color=RED, linewidth=1.6)
ax.plot(xs, np.zeros_like(xs), color="grey", linewidth=1.2, linestyle="--")
ax.text(1.6, -0.4, "1-x", color=BLUE, fontsize=11)
ax.text(1.6, 0.4, "-1+x", color=RED, fontsize=11)
ax.text(1.6, 0.12, "0", color="grey", fontsize=11)
ax.set_title("(E): f(f(x)f(y))+f(x+y)=f(xy) — solutions", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
