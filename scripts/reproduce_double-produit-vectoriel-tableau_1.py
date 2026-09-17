"""Reproduit le schema du double produit vectoriel.

Manuscrit d'origine (double-produit-vectoriel-tableau.jpg) :
demonstration de a ^ (b ^ c) par developpement du determinant
3x3 dans la base (i, j, k) : coordonnees (a1,a2,a3), (b1,b2,b3),
(c1,c2,c3), regroupement en « d1 = a2c2 + a3c3 » et
« b1 - a2b2 - a3b3 » [lectures incertaines], conclusion encadree
« a ^ (b ^ c) = (a.c)b - (a.b)c ».

Ici : vecteurs a, b, c dans le plan + illustration du resultat
(a.c)b - (a.b)c comme combinaison lineaire (parallélogramme).

Sortie : raw/algebre-arithmetique/double-produit-vectoriel-tableau/assets/double-produit.png

Usage :
  uv run scripts/reproduce_double-produit-vectoriel-tableau_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/double-produit-vectoriel-tableau/assets/double-produit.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

a = np.array([2.0, 0.6])
b = np.array([0.7, 1.6])
c = np.array([1.8, 1.4])
res = np.dot(a, c) * b - np.dot(a, b) * c  # (a.c)b - (a.b)c

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

O = np.zeros(2)
for vec, col, w in ((a, BLUE, 1.4), (b, BLUE, 1.4), (c, BLUE, 1.0)):
    ax.arrow(O[0], O[1], vec[0], vec[1], color=col, width=0.02, head_width=0.1, linewidth=w)
ax.arrow(O[0], O[1], res[0], res[1], color=RED, width=0.03, head_width=0.12)  # resultat
ax.plot([b[0], b[0] + c[0]], [b[1], b[1] + c[1]], color=BLUE, linewidth=0.8, linestyle="--")
ax.plot([c[0], b[0] + c[0]], [c[1], b[1] + c[1]], color=BLUE, linewidth=0.8, linestyle="--")
ax.set_title("a ^ (b ^ c) = (a.c)b - (a.b)c", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
