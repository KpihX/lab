"""Reproduit la convergence de S_n = somme_{k=0}^n (2k+1)^4/(7k^2+1)^3 (p. serie-convergence).

Fond : 0 <= U_k <= 81/343 x 1/k^2 (k >= 1), d'ou S_n croissante majorée
par 162/343 + 1, donc convergente. Reproduction : sommes partielles
S_n et majorant horizontal.

Style "stylo" : courbe bleue, majorant rouge, fond quadrille bleu.

Sortie : raw/analyse-suites-series/serie-convergence/assets/sommes-partielles.png

Usage :
  uv run scripts/reproduce_serie-convergence_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_serie-convergence_1.py
>>> # OK -> .../assets/sommes-partielles.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/serie-convergence/assets/sommes-partielles.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

ks = np.arange(0, 51)
uk = (2 * ks + 1) ** 4 / (7 * ks**2 + 1) ** 3
sn = np.cumsum(uk)
majorant = 162 / 343 + 1

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(majorant, color=RED, linewidth=1.4, linestyle="--")
ax.plot(ks, sn, "o-", color=BLUE, linewidth=1.4, markersize=4)
ax.text(30, majorant + 0.02, "162/343 + 1", color=RED, fontsize=10, va="bottom")
ax.set_title("S_n croissante majoree -> converge", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
