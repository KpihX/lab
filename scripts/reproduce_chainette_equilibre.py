"""Reproduit la figure p.136 (bas) de quatrieme-bloc-notes : morceau de corde.

Figure d'origine (manuscrite) : morceau incline de corde entre M(x,y) et
M(x+dx), tensions T(x) (bas) et T(x+dx) (haut), poids P(x), projection
horizontale dx, angle alpha avec l'horizontale.

Style "stylo" : morceau bleu, vecteurs et cotes rouges, fond quadrille.

Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/chainette-equilibre.png

Usage :
  uv run scripts/reproduce_chainette_equilibre.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/chainette-equilibre.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(8, 5.5))
ax.set_xlim(-1.5, 7)
ax.set_ylim(-2.5, 4.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

M = np.array([0.5, 0.0])
N = np.array([4.5, 2.5])
ax.plot([M[0], N[0]], [M[1], N[1]], color=BLUE, linewidth=2.0)
ax.plot(M[0], M[1], "o", color=BLUE, markersize=6)
ax.plot(N[0], N[1], "o", color=BLUE, markersize=6)

# Tangente : T(x+dx) vers le haut-droit en N, T(x) vers le bas-gauche en M.
u = (N - M) / np.linalg.norm(N - M)
ax.annotate("", xy=tuple(N + 1.8 * u), xytext=tuple(N),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.5))
ax.annotate("", xy=tuple(M - 1.8 * u), xytext=tuple(M),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.5))
# Poids P(x) vertical vers le bas au milieu.
Mid = (M + N) / 2
ax.annotate("", xy=(Mid[0], Mid[1] - 1.4), xytext=tuple(Mid),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.5))

ax.text(N[0] + 1.9 * u[0] + 0.1, N[1] + 1.9 * u[1], "T(x+dx)", color=RED, fontsize=13)
ax.text(M[0] - 1.9 * u[0] - 1.3, M[1] - 1.9 * u[1] - 0.2, "T(x)", color=RED, fontsize=13)
ax.text(Mid[0] + 0.2, Mid[1] - 1.5, "P(x)", color=RED, fontsize=13)
ax.text(M[0] - 0.5, M[1] + 0.25, "M(x,y)", color=RED, fontsize=11)

# Angle alpha avec l'horizontale en M.
ang = np.degrees(np.arctan2(u[1], u[0]))
ax.plot([M[0], M[0] + 1.6], [M[1], M[1]], color=BLUE, linewidth=1.0,
        linestyle=(0, (4, 3)))
ax.add_patch(Arc(M, 1.1, 1.1, theta1=0, theta2=ang, color=RED, linewidth=1.3))
ax.text(M[0] + 0.75, M[1] + 0.3, "\u03b1", color=RED, fontsize=14)

# Projection dx en bas.
ax.annotate("", xy=(N[0], -1.8), xytext=(M[0], -1.8),
            arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.2))
ax.plot([M[0], M[0]], [M[1], -1.8], color=BLUE, linewidth=1.0,
        linestyle=(0, (4, 3)))
ax.plot([N[0], N[0]], [N[1], -1.8], color=BLUE, linewidth=1.0,
        linestyle=(0, (4, 3)))
ax.text((M[0] + N[0]) / 2 - 0.2, -1.5, "dx", color=RED, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
