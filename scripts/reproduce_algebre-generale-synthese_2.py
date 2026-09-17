"""Reproduit le diagramme de Venn p.8 du manuscrit algebre-generale-synthese.

Manuscrit d'origine (cahier quadrille, encre bleue ; page tournee a 90 degres
sur le scan) : 3 cercles etiquetes A, B, C avec lentilles hachurees,
verification booleenne (A u C) d(B n C) = ... = (A dB) n C.

Ici : memes 3 disques qu'en p.7 (A en haut, B bas-gauche, C bas-droite) ;
les zones hachurees sont celles de (A n C) d(B n C) = (A dB) n C,
i.e. dans C, appartenir a exactement un de A, B.

Sortie : raw/algebre-arithmetique/algebre-generale-synthese/assets/venn-diff-sym-p8.png

Usage :
  uv run scripts/reproduce_algebre-generale-synthese_2.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique"
    "/algebre-generale-synthese/assets/venn-diff-sym-p8.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLEU = "#1e40af"
ROUGE = "#c81e1e"
QUADRILLE = "#9db3d8"

CIRCLES = {"A": (0.0, 0.55), "B": (-0.5, -0.35), "C": (0.5, -0.35)}
R = 0.75

xs = np.linspace(-1.7, 1.7, 600)
ys = np.linspace(-1.3, 1.75, 600)
X, Y = np.meshgrid(xs, ys)
inside = {k: (X - cx) ** 2 + (Y - cy) ** 2 <= R**2 for k, (cx, cy) in CIRCLES.items()}
target = inside["C"] & (inside["A"] ^ inside["B"])  # (A n C) d(B n C)
outside = ~(inside["A"] | inside["B"] | inside["C"])
Z = np.where(outside, np.nan, np.where(target, 1.0, 0.0))

fig, ax = plt.subplots(figsize=(6, 6))
ax.grid(True, color=QUADRILLE, linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.contourf(X, Y, Z, levels=[0.5, 1.5], colors=["#ffd6d6"],
            hatches=["///"], edgecolors=ROUGE)
for k, (cx, cy) in CIRCLES.items():
    ax.add_patch(plt.Circle((cx, cy), R, fill=False, edgecolor=BLEU, linewidth=2.0))
if True:  # etiquettes hors des disques : A au-dessus, B a gauche, C a droite
    ax.text(CIRCLES["A"][0], CIRCLES["A"][1] + R + 0.12, "A", color=BLEU,
            fontsize=16, fontweight="bold", ha="center", va="center")
    ax.text(CIRCLES["B"][0] - R - 0.18, CIRCLES["B"][1], "B", color=BLEU,
            fontsize=16, fontweight="bold", ha="center", va="center")
    ax.text(CIRCLES["C"][0] + R + 0.18, CIRCLES["C"][1], "C", color=BLEU,
            fontsize=16, fontweight="bold", ha="center", va="center")
ax.set_aspect("equal")
ax.set_xlim(-1.7, 1.7)
ax.set_ylim(-1.3, 1.75)
ax.set_xticks(np.arange(-1.6, 1.61, 0.2))
ax.set_yticks(np.arange(-1.2, 1.76, 0.2))
ax.tick_params(labelbottom=False, labelleft=False, length=0, color=QUADRILLE)
ax.set_title("(A n C) d(B n C) = (A dB) n C : zones hachurees", color=ROUGE, fontsize=11, pad=8)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
