"""Reproduit lim_{M->0} [(somme_{k=1}^n k^M)/n]^{1/M} = racine n-ieme de n! (p. limite-tableau-1).

Fond (11/06/2021) : passage a l'exponentielle, taux d'accroissement du
log et de l'exponentielle, car M ln k -> 0 et (1/n)somme(k^M-1) -> 0.
Reproduction (n = 5) : la fonction de M des deux cotes de 0 tend vers
la droite racine 5-ieme de 120.

Style "stylo" : courbe bleue, limite rouge, fond quadrille bleu.

Sortie : raw/analyse-fonctions/limite-tableau-1/assets/moyenne-puissance.png

Usage :
  uv run scripts/reproduce_limite-tableau-1_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_limite-tableau-1_1.py
>>> # OK -> .../assets/moyenne-puissance.png (NNNNN o)
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/limite-tableau-1/assets/moyenne-puissance.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"
N = 5
LIM = math.factorial(N) ** (1.0 / N)  # racine n-ieme de n!


def Mp(M):
    """Moyenne de puissance [(somme k^M)/n]^{1/M}."""
    return ((np.arange(1, N + 1) ** M).mean()) ** (1.0 / M)


mg = np.linspace(-2, -0.05, 400)
md = np.linspace(0.05, 2, 400)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(LIM, color=RED, linewidth=1.4, linestyle="--")
ax.plot(mg, [Mp(m) for m in mg], color=BLUE, linewidth=1.6)
ax.plot(md, [Mp(m) for m in md], color=BLUE, linewidth=1.6)
ax.text(1.1, LIM + 0.05, "racine 5e de 120", color=RED, fontsize=10, va="bottom")
ax.set_title("M -> [(somme k^M)/5]^(1/M) -> 5e racine de 120", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
