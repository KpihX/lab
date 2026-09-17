"""Reproduit la figure p.1 de premiers-essais-01 : grille de mots croises.

Schema d'origine (imprime) : grille rectangulaire cases noires / cases
blanches, 10 mots numerotes (definitions 1 a 10 de l'exercice 1).

Reproduction schematique simplifiee : contours des emplacements des
10 mots (horizontaux / verticaux), numeros en rouge. Ne vise pas la
conformite case a case avec la grille imprimee.

Sortie : raw/bloc-notes/premiers-essais-01/assets/mots-croises.png

Usage :
  uv run scripts/reproduce_premiers_essais_01_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/premiers-essais-01/assets/mots-croises.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "blue", "red"
NCOLS, NROWS = 20, 12

# (col, lig, longueur, direction) des 10 mots — positions approchees.
WORDS = [
    (9, 0, 7, "v", "1"),
    (7, 1, 8, "v", "2"),
    (2, 2, 9, "h", "3"),
    (5, 2, 9, "v", "4"),
    (6, 3, 6, "v", "5"),
    (7, 5, 10, "h", "6"),
    (14, 6, 6, "v", "7"),
    (9, 7, 7, "h", "8"),
    (12, 7, 4, "v", "9"),
    (6, 7, 5, "h", "10"),
]

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, NCOLS)
ax.set_ylim(0, NROWS)
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# fond noir de la grille
ax.add_patch(Rectangle((0, 0), NCOLS, NROWS, facecolor="black", zorder=1))

for col, lig, lon, sens, num in WORDS:
    for i in range(lon):
        c = col + i if sens == "h" else col
        r = lig if sens == "h" else lig + i
        y = NROWS - 1 - r  # ligne 0 en haut
        ax.add_patch(Rectangle((c, y), 1, 1, facecolor="white", edgecolor=BLUE, lw=1.2, zorder=2))
    y0 = NROWS - 1 - lig
    ax.text(col + 0.05, y0 + 0.55, num, color=RED, fontsize=9, zorder=3)  # numero rouge

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
