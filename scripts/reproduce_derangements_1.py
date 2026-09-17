"""Reproduit le schema des derangements : D_n / n! -> 1/e.

Manuscrit d'origine (derangements.jpg) : nombre de permutations sans
point fixe, formule D_n = n! * sum_{k=0}^n (-1)^k / k!, preuve par
crible (A_i = {permutations fixant i}), approximation D_n ~ n!/e
et « E(n!/e + 0,5) ».

Ici : courbe des sommes partielles S_n = sum_{k=0}^n (-1)^k/k!
convergeant vers 1/e (droite rouge), echelle n = 0..10.

Sortie : raw/probas/derangements/assets/derangements.png

Usage :
  uv run scripts/reproduce_derangements_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import math

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/derangements/assets/derangements.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

ns = np.arange(0, 11)
Ss = np.array([sum(((-1) ** k) / math.factorial(k) for k in range(n + 1)) for n in ns])

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(1 / math.e, color=RED, linewidth=1.2)  # limite 1/e
ax.plot(ns, Ss, "o-", color=BLUE, linewidth=1.6)  # sommes partielles S_n
ax.set_title("D_n / n! -> 1/e", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
