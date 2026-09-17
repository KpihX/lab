"""Reproduit la figure de l'equation vectorielle (cerf-volant).

Manuscrit d'origine (equation-vectorielle.jpg) : equation (Ex) en
x avec produit vectoriel, « Si B ^ x ... (B1, B) ... »,
« une base de ... », « Alors ... », « (6x) => ... Reciproquement,
A verifie ... », « (6x) ... », « x = ... 1/(...) ... »,
« A = ... determinant 3x3 ... », « + (A + ... ) != 0 »,
« D'ou l'existence et l'unicite de x », « Donne ... d : ... 1/... »,
« b = ... », « Ainsi ... A ... », « Sinon (6x) => ... »,
« ... (6x) ... », « (Bx) => ... », « => ... » [lectures incertaines].
En haut a droite : figure quadrilatere type cerf-volant / losange.

Ici : quadrilatere (cerf-volant) + base de vecteurs (A, B) et le
vecteur solution x construit comme combinaison.

Sortie : raw/algebre-arithmetique/equation-vectorielle/assets/equation-vectorielle.png

Usage :
  uv run scripts/reproduce_equation-vectorielle_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/equation-vectorielle/assets/equation-vectorielle.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

P = np.array([[0.2, 2.6], [1.8, 1.6], [0.6, 0.1], [-0.6, 1.5], [0.2, 2.6]])  # cerf-volant
A = np.array([1.6, 0.5])
B = np.array([0.4, 1.4])

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

ax.plot(P[:, 0], P[:, 1], color=BLUE, linewidth=1.4)  # quadrilatere
O = np.zeros(2)
ax.arrow(O[0], O[1], A[0], A[1], color=BLUE, width=0.02, head_width=0.09)
ax.arrow(O[0], O[1], B[0], B[1], color=BLUE, width=0.02, head_width=0.09)
ax.arrow(O[0], O[1], (A + B)[0] / 2, (A + B)[1] / 2, color=RED, width=0.03, head_width=0.11)  # x solution
ax.set_title("(Ex) : existence et unicite de x", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
