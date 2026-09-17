"""Reproduit l'element de surface (differentielle-surface, prise 1, ex-differentielle-surface-1) : nappe parametree et vecteur normal.

Manuscrit d'origine (differentielle-surface-prise1.jpg) : « Etude
differentielle d'une surface », repere orthonorme, OM(u,v),
vecteurs tangents d(OM)/du et d(OM)/dv, vecteur normal n,
parallelogramme elementaire dS, vecteur surface dSvec = n*dS,
aire A = integrale double sur S de dS.

Ici : portion de nappe z = 0.15*(x^2 + y^2) avec en un point M les
deux vecteurs tangents (bleu) et la normale (rouge), + cadre du
parallelogramme elementaire.

Sortie : raw/geometrie/differentielle-surface/assets/surface-1.png

Usage :
  uv run scripts/reproduce_differentielle-surface_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/differentielle-surface/assets/surface-1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

u = np.linspace(-1.5, 1.5, 25)
v = np.linspace(-1.5, 1.5, 25)
U, V = np.meshgrid(u, v)
Z = 0.15 * (U**2 + V**2)

fig = plt.figure(figsize=(6.4, 4.6))
ax = fig.add_subplot(111, projection="3d")
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees

ax.plot_surface(U, V, Z, color=BLUE, alpha=0.25, edgecolor="#9db3d8", linewidth=0.3)

# point M(0.6, 0.4) et vecteurs tangents d(OM)/du, d(OM)/dv + normale
M = np.array([0.6, 0.4, 0.15 * (0.6**2 + 0.4**2)])
Tu = np.array([0.7, 0.0, 0.15 * 2 * 0.6 * 0.7])
Tv = np.array([0.0, 0.7, 0.15 * 2 * 0.4 * 0.7])
N = np.cross(Tu, Tv)
N = N / np.linalg.norm(N) * 0.8
for vec, col in ((Tu, BLUE), (Tv, BLUE), (N, RED)):
    ax.quiver(M[0], M[1], M[2], vec[0], vec[1], vec[2], color=col, linewidth=1.6)
ax.set_title("dSvec = n dS, A = integrale de dS", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
