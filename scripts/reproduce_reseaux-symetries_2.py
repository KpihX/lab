"""Eclate reseaux-symetries en 5 panneaux, un par maillon de la chaine de reduction.

Manuscrit (1 page) : reseau carre en losange (R par cote, A -> B) = losange a
bandes 2R/4R/4R/2R (symetrie AD, antisymetrie CD) = hexagone (6 x R + 2 x 4R)
= pentagone (4R/4R + 2R/2R) = 4R/2 = 2R. Valeurs recopiees au mieux (lisibilite
~60 %, voir md : plusieurs [lecture incertaine]).
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/reseaux-symetries/assets/reseau-symetries-5-panneaux.png
Usage : uv run scripts/reproduce_reseaux-symetries_2.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/reseaux-symetries/assets/reseau-symetries-5-panneaux.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, axs = plt.subplots(1, 5, figsize=(20, 4.6))
for ax in axs:
    ax.set_aspect("equal")
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for s in ax.spines.values():
        s.set_visible(False)

# P1 : grille carree en losange, R par cote, A (gauche) -> B (droite)
ax = axs[0]
c = [np.array([-1.6, 0.0]), np.array([0.0, 1.4]), np.array([1.6, 0.0]), np.array([0.0, -1.4])]
for P, Q in [(c[0], c[1]), (c[1], c[2]), (c[2], c[3]), (c[3], c[0]),
              (c[0], c[2]), (c[1], c[3])]:
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color="#1a3fb5", linewidth=1.8)
for P in c:
    ax.plot([P[0]], [P[1]], "o", color="black", markersize=6)
ax.text(-2.0, 0.1, "A", fontsize=13)
ax.text(1.7, 0.1, "B", fontsize=13)
ax.text(0.0, -1.85, "R / cote", color="#1a3fb5", fontsize=10, ha="center")
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.1, 2.1)
ax.set_title("(1) carre = losange", fontsize=11)

# P2 : losange a bandes horizontales 2R / 4R / 4R / 2R
ax = axs[1]
A = np.array([-1.8, 0.0])
B = np.array([1.8, 0.0])
T = np.array([0.0, 1.5])
D = np.array([0.0, -1.5])
for P, Q in [(A, T), (T, B), (B, D), (D, A)]:
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color="#1a3fb5", linewidth=2.0)
for y, lab in [(0.75, "2R"), (0.25, "4R"), (-0.25, "4R"), (-0.75, "2R")]:
    xl = 1.8 * (1 - abs(y) / 1.5)
    ax.plot([-xl, xl], [y, y], color="red", linewidth=1.4)
    ax.text(0.08, y + 0.09, lab, color="red", fontsize=10)
ax.plot([A[0]], [A[1]], "o", color="black", markersize=7)
ax.plot([B[0]], [B[1]], "o", color="black", markersize=7)
ax.text(-2.1, 0.1, "A", fontsize=13)
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.1, 2.1)
ax.set_title("(2) bandes 2R/4R", fontsize=11)

# P3 : hexagone, contour 6 x R, 2 barres internes 4R
ax = axs[2]
ang = np.pi / 2 + np.arange(6) * np.pi / 3
hx = 1.5 * np.cos(ang)
hy = 1.7 * np.sin(ang)
ax.plot(np.append(hx, hx[0]), np.append(hy, hy[0]), color="#1a3fb5", linewidth=2.0)
for xx in (-0.75, 0.75):
    ax.plot([xx, xx], [-1.35, 1.35], color="red", linewidth=1.4)
    ax.text(xx + 0.06, 0.0, "4R", color="red", fontsize=10)
for x, y in zip(hx, hy):
    ax.plot([x], [y], "o", color="black", markersize=5)
ax.text(0.0, -2.0, "6 cotes R", color="#1a3fb5", fontsize=10, ha="center")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.3, 2.3)
ax.set_title("(3) hexagone", fontsize=11)

# P4 : pentagone, 4R/4R dedans, 2R/2R
ax = axs[3]
ang = np.pi / 2 + np.arange(5) * 2 * np.pi / 5
px = 1.5 * np.cos(ang)
py = 1.5 * np.sin(ang)
ax.plot(np.append(px, px[0]), np.append(py, py[0]), color="#1a3fb5", linewidth=2.0)
ax.plot([-0.7, 0.7], [0.5, 0.5], color="red", linewidth=1.4)
ax.plot([-0.7, 0.7], [-0.5, -0.5], color="red", linewidth=1.4)
ax.text(0.78, 0.5, "4R", color="red", fontsize=10)
ax.text(0.78, -0.5, "4R", color="red", fontsize=10)
ax.text(-1.9, 1.1, "2R", color="red", fontsize=10)
ax.text(-1.9, -1.1, "2R", color="red", fontsize=10)
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.1, 2.1)
ax.set_title("(4) pentagone", fontsize=11)

# P5 : calcul de marge -> Req = 4R/2 = 2R
ax = axs[4]
ax.text(0.5, 3.6, "1/2R + 2/4R", fontsize=12, ha="center")
ax.text(0.5, 2.9, "12R/7 + R", fontsize=12, ha="center")
ax.text(0.5, 2.2, "6R/7 + R", fontsize=12, ha="center")
ax.text(0.5, 1.3, "Req = 4R/2 = 2R", fontsize=13, ha="center", color="red")
ax.set_xlim(0, 1)
ax.set_ylim(0.5, 4.2)
ax.set_title("(5) equivalente", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
