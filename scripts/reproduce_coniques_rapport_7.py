"""Reproduit la figure p.15/17 du rapport coniques : rotation des axes (angle alpha).

Schema d'origine : repere (O, ex, ey) et repere tourne (O, i, j) avec
Mes(ex->, i->) = alpha ; j = -sin a*ex + cos a*ey, i = cos a*ex + sin a*ey ;
but : faire disparaitre le terme en xy (cf. tan 2a, c...+...).

Sortie : raw/geometrie/coniques-rapport/assets/fig07-rotation-axes.png
Usage : uv run scripts/reproduce_coniques_rapport_7.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig07-rotation-axes.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

alpha = np.deg2rad(30)
ex, ey = np.array([1.0, 0.0]), np.array([0.0, 1.0])
vi = np.cos(alpha) * ex + np.sin(alpha) * ey
vj = -np.sin(alpha) * ex + np.cos(alpha) * ey

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.5, 4)
ax.set_ylim(-1.5, 4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

O = np.zeros(2)
for v, name, col in [(ex, "ex", "dimgray"), (ey, "ey", "dimgray"),
                     (vi, "i", "black"), (vj, "j", "black")]:
    ax.annotate("", xy=O + 3 * v, xytext=O,
                arrowprops=dict(arrowstyle="->", color=col, lw=1.3))
    ax.text(*(O + 3.15 * v), name, fontsize=12, color=col)
ax.plot(O[0], O[1], "o", color="black", markersize=4)
ax.text(0.1, -0.3, "O", fontsize=12)
th = np.linspace(0, alpha, 60)
ax.plot(0.8 * np.cos(th), 0.8 * np.sin(th), color="black", linewidth=1.2)
ax.text(0.9, 0.3, "α", fontsize=13)
# ellipse temoin (Sigma) pour motiver le changement de repere
t = np.linspace(0, 2 * np.pi, 300)
ax.plot(2.2 + 1.6 * np.cos(t) * np.cos(0.5) - 0.8 * np.sin(t) * np.sin(0.5),
        1.6 + 1.6 * np.cos(t) * np.sin(0.5) + 0.8 * np.sin(t) * np.cos(0.5),
        color="gray", linewidth=1.2)
ax.text(3.0, 3.0, "(Σ)", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
