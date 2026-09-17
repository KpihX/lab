"""Reproduit la figure de caracteristiques-plan (prise 1, ex-caracteristiques-plan-1) : plan (P) et vecteur normal n.

Manuscrit : Soit (P): ax+by+cz+d=0, n=(a,b,c) vecteur normal ; point H projete.
Vue 3D schematique : plan en quadrillage, normale rouge, point H.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/geometrie/caracteristiques-plan/assets/plan-normal.png
Usage : uv run scripts/reproduce_caracteristiques-plan_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/caracteristiques-plan/assets/plan-normal.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(7.5, 5.5))
ax.set_xlim(-5, 5)
ax.set_ylim(-4, 6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_aspect("equal")

# Plan vu en coupe oblique : parallelogramme.
P = np.array([[-4, -2.5], [4, -1.5], [2.5, 2.5], [-4.5, 1.5], [-4, -2.5]])
ax.plot(P[:, 0], P[:, 1], color="#1a3fb5", linewidth=1.8)
for t in np.linspace(0, 1, 7):
    a = P[0] * (1 - t) + P[3] * t
    b = P[1] * (1 - t) + P[2] * t
    ax.plot([a[0], b[0]], [a[1], b[1]], color="#1a3fb5", linewidth=0.7, alpha=0.6)
H = np.array([0.0, -0.5])
N = np.array([0.6, 3.6])
ax.plot(H[0], H[1], "o", color="red", markersize=7)
ax.annotate("", xy=N, xytext=H, arrowprops=dict(arrowstyle="->", color="red", linewidth=2.0))
ax.text(H[0] - 0.9, H[1] - 0.3, "H", color="red", fontsize=13)
ax.text(N[0] + 0.15, N[1] + 0.1, "n=(a,b,c)", color="red", fontsize=12)
ax.text(-3.4, -2.0, "(P): ax+by+cz+d=0", color="#1a3fb5", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
