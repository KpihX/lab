"""Reproduit la figure 1 p.2 de denombrabilite-q : grille et fleches de numerotation.

Schema d'origine (document Word) : petite grille (5 colonnes x 4 lignes)
avec des fleches bleues epaisses qui serpentent de case en case
(balayage de la grille pour numeroter les rationnels) ; une case
hachuree (grise) est sautee ; une fleche sort a droite avec la mention
"... et ainsi de suite jusqu'a l'infini".

Style "stylo" : grille bleue, fleches bleu soutenu, case sautee grise,
fond quadrille bleu.

Sortie : raw/ensembles-cardinaux/denombrabilite-q/assets/grille-fleches.png

Usage :
  uv run scripts/reproduce_denombrabilite_q_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_denombrabilite_q_1.py
>>> # OK -> .../assets/grille-fleches.png (XXXXX o)
>>> # le rendu montre la grille 5x4, la case grise, les fleches bleues
>>> # qui serpentent et la fleche de sortie vers la droite.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/ensembles-cardinaux/denombrabilite-q/assets/grille-fleches.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, ARROW_BLUE, GRAY = "#1a3fb5", "#2f5cb8", "#9a9a9a"
NCOL, NROW = 5, 4

fig, ax = plt.subplots(figsize=(7, 5.2))
ax.set_aspect("equal")
ax.set_xlim(-0.6, NCOL + 2.6)
ax.set_ylim(-0.9, NROW + 0.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)


def cell_center(c, r):
    """Centre de la case (colonne c, ligne r), ligne 0 en haut."""
    return (c + 0.5, NROW - r - 0.5)


# Grille 5x4 ; case sautee (hachuree) en (col 4, ligne 1).
for c in range(NCOL):
    for r in range(NROW):
        x, y = c, NROW - r - 1
        face = GRAY if (c, r) == (4, 1) else "white"
        ax.add_patch(Rectangle((x, y), 1, 1, facecolor=face, edgecolor=BLUE, linewidth=1.4))


def arrow(c1, r1, c2, r2):
    """Fleche epaisse entre centres de cases (raccourcie aux bords)."""
    x1, y1 = cell_center(c1, r1)
    x2, y2 = cell_center(c2, r2)
    dx, dy = x2 - x1, y2 - y1
    ax.add_patch(
        FancyArrow(
            x1 + 0.28 * dx, y1 + 0.28 * dy, 0.44 * dx, 0.44 * dy,
            width=0.16, head_width=0.34, head_length=0.22,
            facecolor=ARROW_BLUE, edgecolor=ARROW_BLUE,
        )
    )


# Serpent de numerotation (schema fidele a l'original) :
# monte a gauche, file a droite en haut, descend a droite,
# revient vers la gauche en sautant la case hachuree, puis ressort.
arrow(0, 3, 0, 2)
arrow(0, 2, 0, 1)
arrow(0, 1, 0, 0)
arrow(0, 0, 1, 0)
arrow(1, 0, 2, 0)
arrow(2, 0, 3, 0)
arrow(3, 0, 4, 0)
arrow(4, 0, 4, 2)
arrow(4, 2, 4, 3)
arrow(3, 2, 3, 1)
arrow(2, 1, 2, 2)
arrow(2, 1, 1, 1)
arrow(2, 3, 1, 3)

# Fleche de sortie vers la droite + mention.
x_out, y_out = cell_center(4, 3)
ax.add_patch(
    FancyArrow(
        x_out + 0.3, y_out, 0.9, 0,
        width=0.16, head_width=0.34, head_length=0.22,
        facecolor=ARROW_BLUE, edgecolor=ARROW_BLUE,
    )
)
ax.text(x_out + 1.5, y_out, "... et ainsi de suite jusqu'à l'infini.",
        color="black", fontsize=11, va="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
