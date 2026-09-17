"""Reproduit la figure 2 p.2 de denombrabilite-q : tableau de numerotation.

Schema d'origine (document Word) : tableau 11 colonnes x 7 lignes.
Ligne d'en-tete de "..." verticaux ; 5 lignes de numeros d'ordre
(les cases hachurees/grises = couples non premiers entre eux ou axes,
sautees par la numerotation) ; colonne d'axe en gras (5, 4, 3, 2, 1) ;
ligne d'etiquettes p en gras (-4, -3, -2, -1, vide, 0, 1, 2, 3).

Valeurs relevees mot a mot sur le scan :
  ligne q=5 : ..., 18, 19, 20, 21, 5, grise, 22, 23, 24, ...
  ligne q=4 : ..., grise, 13, grise, 12, 4, grise, 11, grise, 25, ...
  ligne q=3 : ..., 17, grise, 4, 5, 3, grise, 6, 10, grise, ...
  ligne q=2 : ..., grise, 14, grise, 1, 2, grise, 7, grise, 26, ...
  ligne q=1 : ..., 16, 15, 3, 2, 1, 0, 8, 9, 27, ...
  etiquettes : ..., -4, -3, -2, -1, (vide), 0, 1, 2, 3, ...

Style "stylo" : bordures bleues, cases sautees grises, axe en bleu gras,
fond quadrille bleu.

Sortie : raw/ensembles-cardinaux/denombrabilite-q/assets/tableau-numerotation.png

Usage :
  uv run scripts/reproduce_denombrabilite_q_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_denombrabilite_q_2.py
>>> # OK -> .../assets/tableau-numerotation.png (XXXXX o)
>>> # le rendu montre le tableau 11x7 avec cases grises et colonne d'axe.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/ensembles-cardinaux/denombrabilite-q/assets/tableau-numerotation.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, GRAY, AXIS = "#1a3fb5", "#9a9a9a", "#0f2f9e"
G = "G"  # case hachuree (grise)

ROWS = [
    ["⋮", "⋮", "⋮", "⋮", "⋮", "⋮", "⋮", "⋮", "⋮", "⋮", "⋱"],
    ["…", "18", "19", "20", "21", "5", G, "22", "23", "24", "…"],
    ["…", G, "13", G, "12", "4", G, "11", G, "25", "…"],
    ["…", "17", G, "4", "5", "3", G, "6", "10", G, "…"],
    ["…", G, "14", G, "1", "2", G, "7", G, "26", "…"],
    ["…", "16", "15", "3", "2", "1", "0", "8", "9", "27", "…"],
    ["…", "-4", "-3", "-2", "-1", "", "0", "1", "2", "3", "…"],
]
AXIS_COL = 5  # colonne d'axe (5, 4, 3, 2, 1)
BOLD_ROWS = {6}  # ligne d'etiquettes en gras

NCOL, NROW = len(ROWS[0]), len(ROWS)

fig, ax = plt.subplots(figsize=(11, 5.2))
ax.set_aspect("equal")
ax.set_xlim(-0.6, NCOL + 0.6)
ax.set_ylim(-0.6, NROW + 0.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

for r, row in enumerate(ROWS):
    for c, val in enumerate(row):
        x, y = c, NROW - r - 1
        is_gray = val == G
        ax.add_patch(
            Rectangle((x, y), 1, 1,
                      facecolor=GRAY if is_gray else "white",
                      edgecolor=BLUE, linewidth=1.2)
        )
        if not is_gray and val != "":
            bold = (c == AXIS_COL and 1 <= r <= 5) or r in BOLD_ROWS
            ax.text(x + 0.5, y + 0.5, val, ha="center", va="center",
                    fontsize=11, fontweight="bold" if bold else "normal",
                    color=AXIS if bold else "black")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
