"""Reproduit la figure de champ-bobine : spire circulaire, point M(x,y,z), centre et rayon.

Manuscrit : champ B(M) cree par une bobine (spire), schema ellipse + axe.
Vue : spire en ellipse, centre O, rayon R, point M sur l'axe, vecteurs OM/MM'.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/champ-bobine/assets/spire.png
Usage : uv run scripts/reproduce_champ-bobine_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/champ-bobine/assets/spire.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(7.5, 5.5))
ax.set_xlim(-4, 4.5)
ax.set_ylim(-3.5, 4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_aspect("equal")

th = np.linspace(0, 2 * np.pi, 400)
ax.plot(2.5 * np.cos(th), 1.0 * np.sin(th), color="#1a3fb5", linewidth=1.8)
ax.plot([-3.4, 3.4], [0, 0], color="black", linewidth=1.0)
ax.plot([0, 0], [-2.6, 3.4], color="black", linewidth=1.0)
O = np.array([0.0, 0.0])
M = np.array([0.0, 2.6])
P = np.array([2.5, 0.0])
ax.plot(O[0], O[1], "o", color="black", markersize=6)
ax.plot(M[0], M[1], "o", color="red", markersize=6)
ax.plot([O[0], P[0]], [O[1], P[1]], color="red", linewidth=1.6)
ax.plot([O[0], M[0]], [O[1], M[1]], color="red", linewidth=1.6, linestyle="--")
ax.plot([M[0], P[0]], [M[1], P[1]], color="#1a3fb5", linewidth=1.4)
ax.text(0.12, -0.3, "O", fontsize=12)
ax.text(0.15, 2.7, "M", color="red", fontsize=12)
ax.text(1.2, -0.35, "R", color="red", fontsize=12)
ax.text(2.6, 0.15, "P", color="#1a3fb5", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
