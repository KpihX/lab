"""Reproduit l'inegalite n! > sqrt(n^n) (p. inegalites-factorielles).

Figure d'origine : pas de schema, preuve par appariement des facteurs
(n-k)(k+1). Reproduction = illustration du fond : log10(n!) vs
log10(sqrt(n^n)) = (n/2)log10(n) pour n = 1..8, la courbe factorielle
domine des n = 3.

Style "stylo" : courbes bleues, titre rouge, fond quadrille bleu.

Sortie : raw/analyse-suites-series/inegalites-factorielles/assets/fact-vs-racine.png

Usage :
  uv run scripts/reproduce_inegalites-factorielles_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_inegalites-factorielles_1.py
>>> # OK -> .../assets/fact-vs-racine.png (NNNNN o)
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/inegalites-factorielles/assets/fact-vs-racine.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

ns = np.arange(1, 9)
log_fact = np.array([math.log10(math.factorial(int(n))) for n in ns])
log_rac = (ns / 2.0) * np.log10(ns)
log_rac[0] = 0.0  # 1*log10(1) = 0

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.plot(ns, log_fact, "o-", color=BLUE, linewidth=1.6, markersize=5)
ax.plot(ns, log_rac, "s-", color=RED, linewidth=1.4, markersize=5)
ax.text(8.1, float(log_fact[-1]), "log(n!)", color=BLUE, fontsize=10, va="center", clip_on=False)
ax.text(8.1, float(log_rac[-1]), "log(sqrt(n^n))", color=RED, fontsize=10, va="center", clip_on=False)
ax.set_title("n! > sqrt(n^n) des n = 3 (echelle log10)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
