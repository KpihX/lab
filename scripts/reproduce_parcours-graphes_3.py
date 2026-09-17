"""Reproduit les 4 mini-schemas "parite du degre : entree/sortie" p.2 de parcours-graphes.

Figure d'origine (notes manuscrites) : pour un sommet A d'un
graphe connexe G, selon que deg(A) est pair ou impair et selon
que le parcours commence ou non par A, on doit finir (ou non)
par A. Quatre cas illustres par des fleches "debut/fin" et une
boucle de retour sur A.

Sortie : raw/informatique/parcours-graphes/assets/parcours-graphes-3.png

Usage :
  uv run scripts/reproduce_parcours-graphes_3.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/informatique"
    "/parcours-graphes/assets/parcours-graphes-3.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

CASES = [
    # (titre, fleche debut (xy, xytext), fleche fin (xy, xytext)).
    ("deg pair : on commence par A\n-> on finit par A",
     ((-0.45, 0.15), (-2.0, 0.15), "debut"), ((-0.45, -0.35), (-2.0, -0.35), "fin")),
    ("deg pair : on ne commence pas par A\n-> on ne finit pas par A",
     ((-0.45, 0.15), (-2.0, 0.15), "passage"), ((2.0, -0.15), (0.45, -0.15), "passage")),
    ("deg impair : on commence par A\n-> on ne finit pas par A",
     ((2.0, 0.15), (0.45, 0.15), "debut"), ((2.0, -0.15), (0.45, -0.15), "fin")),
    ("deg impair : on ne commence pas par A\n-> on finit par A",
     ((-0.45, 0.15), (-2.0, 0.15), "debut"), ((-0.45, -0.35), (-2.0, -0.35), "fin")),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
for ax, (title, deb, fin) in zip(axes.flat, CASES):
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-1.8, 1.8)
    ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
    ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title(title, fontsize=10)

    # Sommet A.
    circ = patches.Circle((0, 0), 0.45, facecolor="white",
                          edgecolor=BLUE, linewidth=1.6)
    ax.add_patch(circ)
    ax.text(0, 0, "A", ha="center", va="center", fontsize=12, color=BLUE)

    # Fleche "debut" (bleue) et fleche "fin" (rouge), sens selon le cas.
    (dx, dy), (tx, ty), dlab = deb
    ax.annotate("", xy=(dx, dy), xytext=(tx, ty),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.4))
    ax.text(tx, ty + 0.3, dlab, ha="center", fontsize=9, color=BLUE)
    (dx, dy), (tx, ty), flab = fin
    ax.annotate("", xy=(dx, dy), xytext=(tx, ty),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.4))
    ax.text(tx, ty - 0.3, flab, ha="center", fontsize=9, color=RED)

    # Boucle de retour sur A.
    loop = patches.Arc((0, 0), 1.8, 1.8, theta1=50, theta2=310,
                       edgecolor="black", linewidth=1.1)
    ax.add_patch(loop)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
