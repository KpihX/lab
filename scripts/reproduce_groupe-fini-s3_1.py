"""Reproduit la table de multiplication de S3.

Manuscrit d'origine (groupe-fini-s3.jpg) : en haut, les 6
elements S3 = {f0 = (1 2 3 / 1 2 3), f1 = (1 2 3 / 1 3 2) = f1^-1,
f2 = (1 2 3 / 2 1 3) [lecture incertaine] = f2^-1,
f3 = (1 2 3 / 2 3 1), f4 = (1 2 3 / 3 2 1) = f4^-1,
f5 = (1 2 3 / 3 1 2)} [indices et images partiellement incertains],
puis la table de Cayley 6x6 manuscrite ; a droite : « Nota : Tout
groupe fini admet un ... et n ... / y^n = e mais n'est pas ...
... monogene : ... » [lecture incertaine]. En bas, enonce imprime :
« 63. Donner la table de multiplication de S3. 64. Soient (G,T),
(G',_) deux groupes, f : G -> G' un morphisme de groupes. —
Montrer que pour tout sous groupe H de G, f(H) est un sous groupe
de G'. ... Montrer que pour tout sous groupe H' de G', f^-1(H')
est un sous ... » [coupe].

Ici : table de Cayley de S3 calculee (permutations de {1,2,3}),
lignes/colonnes f0..f5, cases colorees par ordre du produit.

Sortie : raw/algebre-arithmetique/groupe-fini-s3/assets/s3.png

Usage :
  uv run scripts/reproduce_groupe-fini-s3_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import itertools

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/groupe-fini-s3/assets/s3.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

perms = list(itertools.permutations((1, 2, 3)))  # f0..f5
index = {p: i for i, p in enumerate(perms)}


def compose(p, q):
    """p o q : appliquer q puis p (notations du manuscrit)."""
    return tuple(p[q[i] - 1] for i in range(3))


table = np.array([[index[compose(p, q)] for q in perms] for p in perms])

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.imshow(table, cmap="Blues", vmin=0, vmax=5)  # table de Cayley
for i in range(6):
    for j in range(6):
        ax.text(j, i, f"f{table[i, j]}", ha="center", va="center", fontsize=8, color=RED)
ax.set_title("S3 : table de multiplication (f0..f5)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
