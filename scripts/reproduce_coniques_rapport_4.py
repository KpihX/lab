"""Reproduit la figure p.7 du rapport coniques : ellipse foyer-directrice sur l'axe.

Schema d'origine : axe focal (Delta) horizontal, directrice (D) verticale en K,
foyer F, sommets A et A', centre O = mil[AA'], x^2/a^2 + y^2/b^2 = 1, e = c/a.

Sortie : raw/geometrie/coniques-rapport/assets/fig04-ellipse-foyer.png
Usage : uv run scripts/reproduce_coniques_rapport_4.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig04-ellipse-foyer.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

a, b = 5.0, 3.0
c = np.sqrt(a**2 - b**2)
e = c / a
Kx = a / e

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_aspect("equal")
ax.set_xlim(-7, 8)
ax.set_ylim(-4, 4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

th = np.linspace(0, 2 * np.pi, 400)
ax.plot(a * np.cos(th), b * np.sin(th), color="black", linewidth=1.6)  # (E)
ax.plot([-7, 8], [0, 0], color="dimgray", linewidth=1.0)  # axe focal
ax.plot([Kx, Kx], [-3.8, 3.8], color="dimgray", linewidth=1.2)  # (D)
for px, name in [(-a, "A'"), (a, "A"), (c, "F"), (-c, "F'"), (0, "O"), (Kx, "K")]:
    ax.plot(px, 0, "o", color="black", markersize=4)
    ax.text(px + 0.1, 0.2, name, fontsize=11)
ax.text(Kx + 0.2, 3.2, "(D)", fontsize=12)
ax.text(-6.5, 0.3, "(Δ)", fontsize=12)
ax.text(-2.5, 3.0, "(E) : x²/a² + y²/b² = 1", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
