"""Reproduit la figure p.2 de premiers-essais-01 : carte mere (Figure 1).

Schema d'origine (imprime) : photo-schema d'une carte mere bleue avec
7 emplacements numerotes (1 : socket processeur, 2 : slots PCI,
3 : slots memoire, 4 : chipset, 5 : ventilateur, 6 : port,
7 : connecteur d'alimentation) + Tableau 1 (liste a-j des composants).

Reproduction schematique simplifiee : carte en bleu, emplacements en
rectangles, numeros en rouge. Le Tableau 1 est transcrit dans le .md.

Sortie : raw/bloc-notes/premiers-essais-01/assets/carte-mere.png

Usage :
  uv run scripts/reproduce_premiers_essais_01_2.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/premiers-essais-01/assets/carte-mere.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "blue", "red"

# (x, y, largeur, hauteur, numero) en coordonnees schematiques.
SLOTS = [
    (6.2, 4.5, 1.6, 1.6, "1"),  # socket processeur
    (0.5, 4.5, 2.2, 2.0, "2"),  # slots PCI
    (3.2, 1.2, 4.6, 0.8, "3"),  # slots memoire
    (1.0, 1.5, 0.8, 0.8, "4"),  # chipset
    (4.0, 4.0, 1.2, 1.2, "5"),  # ventilateur
    (1.8, 1.0, 0.5, 1.3, "6"),  # port
    (5.5, 5.5, 1.0, 0.7, "7"),  # connecteur alimentation
]

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 9)
ax.set_ylim(0, 7.5)
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.add_patch(Rectangle((0.2, 0.5), 8.4, 6.5, facecolor="lightsteelblue",
                       edgecolor=BLUE, lw=2))  # carte mere bleue
for x, y, w, h, num in SLOTS:
    ax.add_patch(Rectangle((x, y), w, h, facecolor="white", edgecolor=BLUE, lw=1.5))
    cx, cy = x + w / 2, y + h / 2
    ax.add_patch(Circle((cx, cy), 0.35, facecolor="white", edgecolor=RED, lw=1.5))
    ax.text(cx, cy - 0.12, num, color=RED, fontsize=12, ha="center")  # numero rouge

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
