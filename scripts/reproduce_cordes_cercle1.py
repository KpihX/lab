"""Reproduit la figure p.20 du 4e Bloc-Notes : cordes du cercle 1.

Cercle, diametre horizontal BD (B a gauche, D a droite), point A en haut
relie a D, segment vertical AC coupant BD en E avec angle droit marque,
points F, M, y annotes.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/cordes-cercle1.png
Usage : uv run scripts/reproduce_cordes_cercle1.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/cordes-cercle1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

xc, yc = -0.35, 0.15  # AC decale a gauche du centre (comme au manuscrit)
R = 1.0
Ax = xc
Ay_top = yc + np.sqrt(R**2 - xc**2)
Ay_bot = yc - np.sqrt(R**2 - xc**2)
A = np.array([Ax, Ay_top])
C = np.array([Ax, Ay_bot])
B = np.array([xc - R, yc])
D = np.array([xc + R, yc])
E = np.array([Ax, yc])

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.7, 1.4)
ax.set_ylim(-1.4, 1.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

theta = np.linspace(0, 2 * np.pi, 400)
ax.plot(xc + R * np.cos(theta), yc + R * np.sin(theta),
        color="gray", linewidth=1.5)  # cercle crayon
ax.plot([B[0], D[0]], [B[1], D[1]], color="black", linewidth=1.2)  # diametre BD
ax.plot([A[0], C[0]], [A[1], C[1]], color="black", linewidth=1.2)  # corde AC
ax.plot([A[0], D[0]], [A[1], D[1]], color="black", linewidth=1.2)  # corde AD
ax.plot([B[0], C[0]], [B[1], C[1]], color="dimgray", linewidth=1.0)  # BC
# verticale du centre (repere y du manuscrit)
ax.plot([0.25, 0.25], [yc - R - 0.3, yc + R + 0.2],
        color="dimgray", linewidth=0.8)

s = 0.09  # marque d'angle droit en E
ax.plot([E[0], E[0] + s], [E[1], E[1]], color="black", linewidth=1.2)
ax.plot([E[0] + s, E[0] + s], [E[1], E[1] + s], color="black", linewidth=1.2)
ax.plot([E[0], E[0] + s], [E[1] + s, E[1] + s], color="black", linewidth=1.2)

ax.text(A[0] + 0.05, A[1] + 0.08, "A", fontsize=13)
ax.text(C[0] + 0.05, C[1] - 0.18, "C", fontsize=13)
ax.text(B[0] - 0.2, B[1] + 0.05, "B", fontsize=13)
ax.text(D[0] + 0.05, D[1] + 0.02, "D", fontsize=13)
ax.text(E[0] - 0.22, E[1] - 0.22, "E", fontsize=12)
ax.text(E[0] + 0.05, E[1] + 0.28, "F", fontsize=12)
ax.text(B[0] + 0.18, E[1] - 0.24, "M", fontsize=12)
ax.text(0.28, E[1] - 0.26, "y", fontsize=12)
ax.text(0.3, 0.45, "O", fontsize=12, color="dimgray")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
