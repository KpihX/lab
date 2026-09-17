"""Reproduit la figure p.27 du 4e Bloc-Notes : cordes du cercle 2.

Cercle de centre O, diametre vertical M1-M0, corde M3-M2, segment O-bas
(beta), angles alpha, alpha', alpha'' pres du sommet et theta a droite.
M' et M'' = intersections pres du centre. alpha != 0 (marge).
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/cordes-cercle2.png
Usage : uv run scripts/reproduce_cordes_cercle2.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/cordes-cercle2.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)


def pt(deg, r=1.0):
    a = np.deg2rad(deg)
    return np.array([r * np.cos(a), r * np.sin(a)])


O = np.zeros(2)
M1 = pt(90)
M0 = pt(-90)
M3 = pt(160)
M2 = pt(10)
Q = pt(-115)  # pied du segment issu de O (angle beta)

fig, ax = plt.subplots(figsize=(6, 6.4))
ax.set_aspect("equal")
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

theta = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(theta), np.sin(theta), color="gray", linewidth=1.5)
ax.plot([M1[0], M0[0]], [M1[1], M0[1]], color="black", linewidth=1.2)
ax.plot([M3[0], M2[0]], [M3[1], M2[1]], color="black", linewidth=1.2)
ax.plot([O[0], Q[0]], [O[1], Q[1]], color="black", linewidth=1.1)
ax.plot([M3[0], M0[0]], [M3[1], M0[1]],
        color="dimgray", linewidth=0.9, linestyle=(0, (4, 4)))

ax.plot(O[0], O[1], "o", color="black", markersize=4)
ax.text(M1[0] + 0.06, M1[1] + 0.05, "M1", fontsize=12)
ax.text(M0[0] + 0.06, M0[1] - 0.16, "M0", fontsize=12)
ax.text(M3[0] - 0.28, M3[1] + 0.03, "M3", fontsize=12)
ax.text(M2[0] + 0.05, M2[1] + 0.0, "M2", fontsize=12)
ax.text(O[0] - 0.2, O[1] + 0.02, "O", fontsize=12)
ax.text(0.12, 0.55, "α", fontsize=13)
ax.text(-0.28, 0.42, "α'", fontsize=12)
ax.text(0.18, 0.18, "α''", fontsize=12)
ax.text(0.42, 0.3, "θ", fontsize=12)
ax.text(0.12, 0.08, "M'", fontsize=11)
ax.text(0.22, -0.12, "M''", fontsize=11)
ax.text(Q[0] - 0.2, Q[1] + 0.12, "β", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
