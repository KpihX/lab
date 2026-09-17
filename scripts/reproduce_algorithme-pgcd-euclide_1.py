"""Reproduit le fond de algorithme-pgcd-euclide (algo PGCD Euclide, p. algorithme-pgcd-euclide).

Fond : restes successifs d'Euclide pour (a,b)=(1071,462) :
1071 = 2x462+147, 462 = 3x147+21, 147 = 7x21+0 -> PGCD=21,
dernier reste non nul. Reproduction : barres des restes -> 0.
Style "stylo" : barres bleues, PGCD rouge, fond quadrille bleu.

Sortie : raw/algebre-arithmetique/algorithme-pgcd-euclide/assets/euclide-restes.png

Usage :
  uv run scripts/reproduce_algorithme-pgcd-euclide_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/photos-dessins"
    "/algorithme-pgcd-euclide/assets/euclide-restes.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

restes = [1071, 462, 147, 21, 0]
labels = ["a", "b", "r1", "r2=PGCD", "0"]

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

xs = np.arange(len(restes))
ax.bar(xs, restes, color=BLUE, edgecolor=BLUE)
ax.axhline(21, color=RED, linewidth=1.4, linestyle="--")
ax.text(3.1, 21 + 30, "PGCD = 21", color=RED, fontsize=10, va="bottom")
ax.set_title("Euclide : restes -> 0, PGCD = dernier reste non nul", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
