"""Reproduit le schema factorielle-expression : croissance de n!

Manuscrit d'origine (factorielle-expression.jpg, a l'envers) :
« Montrer que pour ... m-1 ... », « n! = ... », sommes de
coefficients binomiaux « sum ... = 1 », « f(n) = ... »,
« Pour tout n ... », « d_x n! ... », « f(n) ... »,
« ( ... 3 ... ) » [tres nombreuses lectures incertaines —
page photographiee a l'envers, encre bleue sur quadrille].

Ici : batons de n! (echelle log) pour n = 0..7 + rappel de la
formule n! = 1 x 2 x ... x n.

Sortie : raw/algebre-arithmetique/factorielle-expression/assets/factorielle.png

Usage :
  uv run scripts/reproduce_factorielle-expression_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
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
    "/factorielle-expression/assets/factorielle.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

ns = np.arange(0, 8)
facts = np.array([math.factorial(n) for n in ns], dtype=float)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.bar(ns, np.log10(facts + 1), color=BLUE, alpha=0.7)  # log10(n!+1)
ax.plot(ns, np.log10(facts + 1), "o-", color=RED, linewidth=1.6)
ax.set_title("n! : croissance (echelle log)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
