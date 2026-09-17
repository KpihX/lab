"""Reproduit la figure p.23 (cas 2) du 4e Bloc-Notes : angles inscrits.

Cercle de centre O, sommet M2 sur le cercle, rayons vers M1, M' et M0 ;
angles alpha', alpha'' en M2, theta/theta'/theta'' au centre. Cas 1 (diametre
M2-M0, theta = 2 alpha) rappele en pointilles fins.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/angles-inscrits.png
Usage : uv run scripts/reproduce_angles_inscrits.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/angles-inscrits.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)


def pt(deg, r=1.0):
    a = np.deg2rad(deg)
    return np.array([r * np.cos(a), r * np.sin(a)])


O = np.zeros(2)
M2 = pt(180)
M1 = pt(55)
Mp = pt(8)
M0 = pt(-50)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.3, 1.3)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

theta = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(theta), np.sin(theta), color="gray", linewidth=1.5)
for P in (M2, M1, Mp, M0):
    ax.plot([M2[0], P[0]], [M2[1], P[1]], color="black", linewidth=1.1)
for P in (M1, Mp, M0):
    ax.plot([O[0], P[0]], [O[1], P[1]], color="dimgray", linewidth=1.0)
# rappel cas 1 : diametre M2-M0 en pointilles
ax.plot([M2[0], -M2[0]], [M2[1], -M2[1]],
        color="dimgray", linewidth=0.8, linestyle=(0, (4, 4)))

ax.plot(O[0], O[1], "o", color="black", markersize=4)
ax.text(M2[0] - 0.22, M2[1] - 0.02, "M2", fontsize=12)
ax.text(M1[0] + 0.05, M1[1] + 0.05, "M1", fontsize=12)
ax.text(Mp[0] + 0.06, Mp[1] - 0.02, "M'", fontsize=12)
ax.text(M0[0] + 0.05, M0[1] - 0.15, "M0", fontsize=12)
ax.text(O[0] - 0.16, O[1] - 0.14, "O", fontsize=12)
ax.text(M2[0] + 0.28, M2[1] + 0.05, "α', α''", fontsize=12)
ax.text(0.25, 0.28, "θ', θ''", fontsize=12)
ax.text(0.35, -0.12, "θ", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
