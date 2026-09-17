"""Reproduit le fond de cauchy-schwarz-droite-disque (ax+by=1 => 1/(x^2+y^2) <= a^2+b^2).

Fond : Cauchy-Schwarz, ex. a=2, b=1. Droite 2x+y=1 a distance
1/sqrt(5) de l'origine ; tout point (x,y) de la droite verifie
x^2+y^2 >= 1/5, soit 1/(x^2+y^2) <= 5. Reproduction : droite bleue,
cercle minimal rouge de rayon 1/sqrt(5).
Style "stylo" : droite bleue, cercle rouge, fond quadrille bleu.

Sortie : raw/analyse-fonctions/cauchy-schwarz-droite-disque/assets/cauchy-droite-cercle.png

Usage :
  uv run scripts/reproduce_cauchy-schwarz-droite-disque_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/photos-dessins"
    "/cauchy-schwarz-droite-disque/assets/cauchy-droite-cercle.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

a, b = 2.0, 1.0
r = 1.0 / np.sqrt(a**2 + b**2)

xs = np.linspace(-1.2, 1.2, 400)
ys = (1 - a * xs) / b

th = np.linspace(0, 2 * np.pi, 400)
cx, cy = r * np.cos(th), r * np.sin(th)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_aspect("equal")
ax.plot(xs, ys, color=BLUE, linewidth=1.6)
ax.plot(cx, cy, color=RED, linewidth=1.6)
ax.plot([0], [0], "o", color=RED, markersize=4)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_title("2x+y=1 : x2+y2 >= 1/5 (Cauchy-Schwarz)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
