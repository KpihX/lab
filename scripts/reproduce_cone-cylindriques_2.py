"""Reproduit la figure de cone-cylindriques (prise 2, ex-cone-cylindriques-2) : cone en coordonnees cylindriques, element dS.

Manuscrit : dS vectoriel, dS = (2R/H ...) h dh dtheta ; schema du cone + couronne.
Vue : cone + anneau de base (r, dr, dtheta) evoquant l'integration cylindrique.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/geometrie/cone-cylindriques/assets/cone-cyl.png
Usage : uv run scripts/reproduce_cone-cylindriques_2.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/cone-cylindriques/assets/cone-cyl.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(6.5, 6))
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-4.5, 1.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_aspect("equal")

S = np.array([0.0, 0.0])
C = np.array([0.0, -3.0])
R = 2.0
th = np.linspace(0, 2 * np.pi, 300)
ax.plot(R * np.cos(th), C[1] + 0.45 * np.sin(th), color="#1a3fb5", linewidth=1.6)
th2 = np.linspace(0.3, 1.1, 60)
ax.plot(1.2 * np.cos(th2), C[1] + 0.45 * np.sin(th2), color="red", linewidth=3.0)
ax.plot([-R, S[0]], [C[1], S[1]], color="#1a3fb5", linewidth=1.6)
ax.plot([R, S[0]], [C[1], S[1]], color="#1a3fb5", linewidth=1.6)
ax.plot([S[0], C[0]], [S[1], C[1]], color="red", linewidth=1.4, linestyle="--")
ax.annotate("", xy=(1.35, -2.9), xytext=(0.1, -2.9),
            arrowprops=dict(arrowstyle="<->", color="red", linewidth=1.4))
ax.text(0.6, -2.6, "r dθ", color="red", fontsize=11)
ax.text(0.15, -1.4, "h", color="red", fontsize=12)
ax.text(-2.8, -0.6, "dS", color="#1a3fb5", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
