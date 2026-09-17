"""Reproduit la figure p.8 du rapport coniques : construction de l'ellipse aux cercles.

Schema d'origine : cercles Ca (r=a) et Cb (r=b), droite quelconque par O
coupant Ca en Pa et Cb en Pb ; parallele a (D) par Pb et perpendiculaire
a (D) par Pa -> M de (E) ; x = a*cos, y = b*sin.

Sortie : raw/geometrie/coniques-rapport/assets/fig05-ellipse-cercles.png
Usage : uv run scripts/reproduce_coniques_rapport_5.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig05-ellipse-cercles.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

a, b = 5.0, 3.0
theta0 = np.deg2rad(40)
Pa = np.array([a * np.cos(theta0), a * np.sin(theta0)])
Pb = np.array([b * np.cos(theta0), b * np.sin(theta0)])
M = np.array([Pa[0], Pb[1]])

fig, ax = plt.subplots(figsize=(7, 6))
ax.set_aspect("equal")
ax.set_xlim(-6, 6)
ax.set_ylim(-4.5, 5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

th = np.linspace(0, 2 * np.pi, 400)
ax.plot(a * np.cos(th), a * np.sin(th), color="gray", linewidth=1.1)  # (Ca)
ax.plot(b * np.cos(th), b * np.sin(th), color="gray", linewidth=1.1)  # (Cb)
ax.plot(a * np.cos(th), b * np.sin(th), color="black", linewidth=1.6)  # (E)
ax.plot([-6, 6], [0, 0], color="dimgray", linewidth=1.0)
t = np.linspace(-1.5, 1.5, 10)
ax.plot(t * Pb[0], t * Pb[1], color="dimgray", linewidth=1.1)  # rayon OP
ax.plot([M[0], M[0]], [M[1], Pa[1]], color="gray", linewidth=1.0, linestyle="--")
ax.plot([M[0], Pb[0]], [M[1], M[1]], color="gray", linewidth=1.0, linestyle="--")
for pt, name, dx, dy in [(Pa, "Pa", 0.15, 0.1), (Pb, "Pb", 0.15, -0.3),
                         (M, "M", 0.15, 0.1), ((0, 0), "O", 0.1, 0.15)]:
    ax.plot(pt[0], pt[1], "o", color="black", markersize=4)
    ax.text(pt[0] + dx, pt[1] + dy, name, fontsize=11)
ax.text(3.6, 3.6, "(Ca)", fontsize=11)
ax.text(1.4, -2.8, "(Cb)", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
