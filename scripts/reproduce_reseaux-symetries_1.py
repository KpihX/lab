"""Reproduit le fond de reseaux-symetries : losange resistif et chaine de reductions.

Manuscrit : reseau carre -> losange (2R/4R/4R/2R) -> hexagone -> pentagone -> 4R/2.
Ici : losange a 4 noeuds (aretes R) + fleche d'equivalence vers Req.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/reseaux-symetries/assets/reseau-symetries.png
Usage : uv run scripts/reproduce_reseaux-symetries_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/reseaux-symetries/assets/reseau-symetries.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
for ax in (ax1, ax2):
    ax.set_aspect("equal")
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for s in ax.spines.values():
        s.set_visible(False)

# Losange A (gauche) - B (droite), sommets haut/bas
A = np.array([-2.0, 0.0]); B = np.array([2.0, 0.0])
T = np.array([0.0, 1.6]); D = np.array([0.0, -1.6])
for P, Q in [(A, T), (T, B), (B, D), (D, A)]:
    ax1.plot([P[0], Q[0]], [P[1], Q[1]], color="#1a3fb5", linewidth=2.0)
# Bandes internes equivalentes 2R/4R/4R/2R
for y, lab in [(0.8, "2R"), (0.27, "4R"), (-0.27, "4R"), (-0.8, "2R")]:
    xl = -2.0 * (1 - abs(y) / 1.6)
    ax1.plot([-xl, xl], [y, y], color="red", linewidth=1.4)
    ax1.text(0.1, y + 0.08, lab, color="red", fontsize=10)
ax1.plot([A[0]], [A[1]], "o", color="black", markersize=7)
ax1.plot([B[0]], [B[1]], "o", color="black", markersize=7)
ax1.text(-2.3, 0.15, "A", fontsize=13); ax1.text(2.05, 0.15, "B", fontsize=13)
ax1.set_xlim(-3, 3); ax1.set_ylim(-2.2, 2.2)
ax1.set_title("Reseau (R par cote)", fontsize=11)

# Reductions en cascade -> Req
ax2.text(0.5, 4.3, "carre = losange = hexagone", color="#1a3fb5", fontsize=11, ha="center")
ax2.annotate("", xy=(0.5, 3.4), xytext=(0.5, 4.0),
             arrowprops=dict(arrowstyle="->", color="black", lw=1.6))
ax2.text(0.5, 3.0, "pentagone = 4R / 2", color="red", fontsize=12, ha="center")
ax2.plot([0.5], [2.2], "o", color="black", markersize=8)
ax2.text(0.5, 1.9, "Req = 2R", fontsize=12, ha="center")
ax2.set_xlim(0, 1); ax2.set_ylim(1.2, 4.8)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
