"""Reproduit la figure p.5 du rapport coniques : miroir parabolique convergent.

Schema d'origine : faisceau de rayons incidents paralleles a l'axe focal,
reflechis vers le foyer F (ou x_F = p/2) ; symetrie du cas y_M > 0 / y_M < 0.

Sortie : raw/geometrie/coniques-rapport/assets/fig03-miroir-convergent.png
Usage : uv run scripts/reproduce_coniques_rapport_3.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig03-miroir-convergent.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

p = 2.0
F = np.array([p / 2, 0.0])

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_aspect("equal")
ax.set_xlim(-1, 6)
ax.set_ylim(-4, 4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

y = np.linspace(-3.5, 3.5, 400)
ax.plot(y**2 / (2 * p), y, color="black", linewidth=1.6)  # (P)
ax.plot([-1, 6], [0, 0], color="dimgray", linewidth=1.0)
ax.plot(F[0], F[1], "o", color="black", markersize=5)
ax.text(F[0] + 0.1, F[1] + 0.15, "F", fontsize=12)
for ym in (2.6, 1.4, -1.4, -2.6):  # rayons incidents puis reflechis vers F
    xm = ym**2 / (2 * p)
    ax.annotate("", xy=(xm, ym), xytext=(6, ym),
                arrowprops=dict(arrowstyle="->", color="dimgray", lw=1.1))
    ax.plot([xm, F[0]], [ym, F[1]], color="black", linewidth=1.1)
ax.text(4.5, 3.1, "(D) incidents", fontsize=11)
ax.text(2.2, -3.2, "convergent vers F", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
