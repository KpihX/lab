"""Reproduit l'enigme des sabliers (7 min + 11 min -> 15 min).

Manuscrit d'origine (enigme-sabliers.jpg) : « Sol : cuisson de
15 min oeuf avec [sabliers] 11 min et 7 min », chronologie
t = 0 (on lance les deux, on met l'oeuf a cuire), t = 7
(« on met de cote », on retourne le 7 min), t = 11 min,
t = 22 min (« on retourne », « bonne degustation »),
duree totale 22 - 7 = 15 min. A droite : deux schemas de
circuits (pont de diodes, resistance, source) [motif incertain].

Ici : frise chronologique des deux sabliers (bandes 11 min en
bleu, 7 min en rouge) avec jalons t = 0, 7, 11, 18, 22 et la
fenetre de cuisson de 15 min.

Sortie : raw/divers/enigme-sabliers/assets/sabliers.png

Usage :
  uv run scripts/reproduce_enigme-sabliers_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/enigme-sabliers/assets/sabliers.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# bandes : sablier 11 min (lance en 0, puis retourne en 11) et 7 min
ax.broken_barh([(0, 11), (11, 11)], (2.2, 0.7), facecolor=BLUE, alpha=0.7)  # 11 min
ax.broken_barh([(0, 7), (7, 7), (14, 7)], (1.2, 0.7), facecolor=RED, alpha=0.7)  # 7 min
ax.broken_barh([(7, 15)], (0.2, 0.7), facecolor="none", edgecolor=RED, linewidth=1.6)  # cuisson 15 min
for t in (0, 7, 11, 14, 18, 21, 22):
    ax.axvline(t, color=BLUE, linewidth=0.8, linestyle="--")
ax.set_xlim(-1, 24)
ax.set_ylim(0, 3.2)
ax.set_title("7 min + 11 min -> 15 min (22 - 7)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
