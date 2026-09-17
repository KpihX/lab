"""Reproduit la figure de cone-cylindriques (prise 1, ex-cone-coordonnees-1) : cone d'axe Oz, rayon R, hauteur H, surface (S).

Manuscrit : aire laterale du cone, schema du cone avec base hachuree, point M, OH.
Vue : triangle/cote + ellipse de base, axe vertical, cotes R et H.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/geometrie/cone-cylindriques/assets/cone.png
Usage : uv run scripts/reproduce_cone-cylindriques_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/cone-cylindriques/assets/cone.png"
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
ax.plot([-R, S[0]], [C[1], S[1]], color="#1a3fb5", linewidth=1.6)
ax.plot([R, S[0]], [C[1], S[1]], color="#1a3fb5", linewidth=1.6)
ax.plot([S[0], C[0]], [S[1], C[1]], color="red", linewidth=1.6, linestyle="--")
ax.plot([C[0], R], [C[1], C[1]], color="red", linewidth=1.6)
ax.plot(S[0], S[1], "o", color="black", markersize=5)
ax.plot(C[0], C[1], "o", color="black", markersize=5)
ax.text(0.15, -1.4, "H", color="red", fontsize=12)
ax.text(1.0, -3.3, "R", color="red", fontsize=12)
ax.text(0.12, 0.1, "S", fontsize=12)
ax.text(-2.6, -1.2, "(S)", color="#1a3fb5", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
