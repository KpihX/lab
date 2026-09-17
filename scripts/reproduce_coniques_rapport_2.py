"""Reproduit la figure p.3 du rapport coniques : parabole foyer-directrice (cas e=1).

Schema d'origine : axe horizontal (Delta), directrice (D) verticale en K,
foyer F, origine O milieu de [KO], parabole y^2 = 2px, F(p/2, 0), (D): x+p/2=0.

Sortie : raw/geometrie/coniques-rapport/assets/fig02-parabole-foyer.png
Usage : uv run scripts/reproduce_coniques_rapport_2.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig02-parabole-foyer.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

p = 2.0
F = (p / 2, 0.0)
K = (-p / 2, 0.0)

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_aspect("equal")
ax.set_xlim(-3, 5)
ax.set_ylim(-4, 4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

y = np.linspace(-3.5, 3.5, 400)
x = y**2 / (2 * p)
ax.plot(x, y, color="black", linewidth=1.6)  # (P)
ax.plot([K[0], K[0]], [-3.8, 3.8], color="dimgray", linewidth=1.2)  # (D)
ax.plot([-3, 5], [0, 0], color="dimgray", linewidth=1.0)  # (Delta)
for pt, name, dx, dy in [(F, "F", 0.1, 0.15), (K, "K", -0.3, 0.15), ((0, 0), "O", 0.05, 0.15)]:
    ax.plot(pt[0], pt[1], "o", color="black", markersize=4)
    ax.text(pt[0] + dx, pt[1] + dy, name, fontsize=12)
ax.text(K[0] - 0.6, 3.4, "(D)", fontsize=12)
ax.text(4.3, 0.2, "(Δ)", fontsize=12)
ax.text(2.6, 2.6, "(P) : y² = 2px", fontsize=11)
# un point M et sa projection H sur (D) : MF = MH
M = (2.0, np.sqrt(2 * p * 2.0))
H = (K[0], M[1])
ax.plot(M[0], M[1], "o", color="black", markersize=4)
ax.text(M[0] + 0.1, M[1] + 0.1, "M", fontsize=12)
ax.plot([M[0], H[0]], [M[1], H[1]], color="gray", linewidth=1.0, linestyle="--")
ax.plot([M[0], F[0]], [M[1], F[1]], color="gray", linewidth=1.0, linestyle="--")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
