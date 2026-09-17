"""Reproduit la figure p.25 du 4e Bloc-Notes : quadrilatere convexe inscrit.

Quadrilatere M3-M2-M1-M0 inscrit dans un cercle de centre O, diagonales
M3-M1 et M2-M0 tracees, rayons O-M1, O-M2, O-M0.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/quadrilatere-convexe.png
Usage : uv run scripts/reproduce_quadrilatere_convexe.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/quadrilatere-convexe.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)


def pt(deg, r=1.0):
    a = np.deg2rad(deg)
    return np.array([r * np.cos(a), r * np.sin(a)])


O = np.zeros(2)
M1 = pt(0)
M0 = pt(-90)
M3 = pt(140)
M2 = pt(75)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.3)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

theta = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(theta), np.sin(theta), color="gray", linewidth=1.5)
quad = [M3, M2, M1, M0, M3]
qx, qy = [p[0] for p in quad], [p[1] for p in quad]
ax.plot(qx, qy, color="black", linewidth=1.4)  # cotes
ax.plot([M3[0], M1[0]], [M3[1], M1[1]],
        color="dimgray", linewidth=1.0)  # diagonale 1
ax.plot([M2[0], M0[0]], [M2[1], M0[1]],
        color="dimgray", linewidth=1.0)  # diagonale 2
for P in (M1, M2, M0):
    ax.plot([O[0], P[0]], [O[1], P[1]], color="dimgray", linewidth=0.9)

ax.plot(O[0], O[1], "o", color="black", markersize=4)
ax.text(M3[0] - 0.25, M3[1] + 0.05, "M3", fontsize=12)
ax.text(M2[0] - 0.05, M2[1] + 0.08, "M2", fontsize=12)
ax.text(M1[0] + 0.05, M1[1] + 0.02, "M1", fontsize=12)
ax.text(M0[0] - 0.05, M0[1] - 0.2, "M0", fontsize=12)
ax.text(O[0] - 0.16, O[1] - 0.14, "O", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
