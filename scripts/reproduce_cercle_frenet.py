"""Reproduit la figure p.106 du 4e Bloc-Notes : mouvement circulaire (base de Frenet).

Cercle de centre O, point M sur le cercle, rayon OM, vecteur vitesse V
tangent, vecteur acceleration a (vers l'interieur), base (t, n) en M
(t tangente, n normale vers le centre), angle theta au centre.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/cercle-frenet.png
Usage : uv run scripts/reproduce_cercle_frenet.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/cercle-frenet.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

r = 1.0
phi = np.deg2rad(35)  # position de M (cf. scan p.106 : haut-droite)
M = np.array([r * np.cos(phi), r * np.sin(phi)])
O = np.zeros(2)
T = np.array([-np.sin(phi), np.cos(phi)])  # tangente directe
N = -np.array([np.cos(phi), np.sin(phi)])  # normale vers le centre

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.5, 1.7)
ax.set_ylim(-1.4, 1.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

t = np.linspace(0, 2 * np.pi, 400)
ax.plot(r * np.cos(t), r * np.sin(t), color="gray", linewidth=1.5)
# rayon OM (repere vertical court + rayon, comme au crayon)
ax.plot([O[0], M[0]], [O[1], M[1]], color="black", linewidth=1.1)
ax.plot([O[0], O[0]], [O[1], O[1] + 0.35], color="dimgray", linewidth=0.9,
        linestyle=(0, (4, 4)))
ax.plot(O[0], O[1], "o", color="black", markersize=4)
ax.plot(M[0], M[1], "o", color="black", markersize=5)

# vitesse V tangente (longue fleche)
ax.annotate("", xy=tuple(M + 0.85 * T), xytext=tuple(M + 0.08 * T),
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.4))
# acceleration a (vers la gauche/interieur)
A = np.array([-0.85, 0.25])
ax.annotate("", xy=tuple(M + A), xytext=tuple(M),
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.4))
# vecteur tangent unitaire t (petite fleche)
ax.annotate("", xy=tuple(M + 0.45 * T), xytext=tuple(M + 0.12 * T),
            arrowprops=dict(arrowstyle="->", color="dimgray", linewidth=1.1))
# vecteur normal unitaire n (vers le centre)
ax.annotate("", xy=tuple(M + 0.45 * N), xytext=tuple(M + 0.12 * N),
            arrowprops=dict(arrowstyle="->", color="dimgray", linewidth=1.1))

# angle theta au centre (entre la verticale et OM)
arc = np.linspace(np.pi / 2 - 0.15, phi, 40) if phi < np.pi / 2 else \
    np.linspace(phi, np.pi / 2 + 0.15, 40)
arc = np.linspace(phi, np.pi / 2, 40)
ax.plot(0.3 * np.cos(arc), 0.3 * np.sin(arc), color="black", linewidth=1.1)

ax.text(O[0] - 0.16, O[1] - 0.16, "O", fontsize=12)
ax.text(M[0] + 0.07, M[1] + 0.03, "M", fontsize=12)
ax.text(float(M[0] + 0.88 * T[0]) + 0.02, float(M[1] + 0.88 * T[1]) + 0.02,
        "V", fontsize=13)
ax.text(float(M[0] + A[0]) - 0.14, float(M[1] + A[1]) + 0.03,
        "a", fontsize=13)
ax.text(float(M[0] + 0.48 * T[0]) - 0.03, float(M[1] + 0.48 * T[1]) + 0.04,
        "t", fontsize=12)
ax.text(float(M[0] + 0.48 * N[0]) + 0.03, float(M[1] + 0.48 * N[1]) - 0.05,
        "n", fontsize=12)
ax.text(0.18, 0.42, "θ", fontsize=13)
ax.text(M[0] / 2 + 0.05, M[1] / 2 - 0.18, "an", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
