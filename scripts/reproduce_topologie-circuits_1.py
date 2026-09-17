"""Reproduit le fond de topologie-circuits : graphe (n, b, m) avec b = (n-1) + m.

Manuscrit : recurrence sur b (init b=2 : deux noeuds, deux branches en croix).
Ici : graphe n=2, b=3, m=2 + rappel du cas b=2.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/topologie-circuits/assets/topologie-circuit.png
Usage : uv run scripts/reproduce_topologie-circuits_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/topologie-circuits/assets/topologie-circuit.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
for ax in (ax1, ax2):
    ax.set_aspect("equal")
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for s in ax.spines.values():
        s.set_visible(False)

# Cas b=2 du manuscrit : deux noeuds, deux branches (droite + croix)
ax1.plot([0, 0], [-1.5, 1.5], color="#1a3fb5", linewidth=2.2)
ax1.plot([-0.5, 0.5], [-1.5, 1.5], color="#1a3fb5", linewidth=2.2)
ax1.plot([0.5, -0.5], [-1.5, 1.5], color="#1a3fb5", linewidth=2.2)
for yy in (1.5, -1.5):
    ax1.plot([0], [yy], "o", color="black", markersize=8)
ax1.text(0.15, 1.0, "R", color="red", fontsize=11)
ax1.text(0.55, -0.6, "R", color="red", fontsize=11)
ax1.text(0.0, -2.0, "b=2 : n=1, m=2", fontsize=10, ha="center")
ax1.set_xlim(-2, 2); ax1.set_ylim(-2.4, 2.4)
ax1.set_title("Initialisation P(2)", fontsize=11)

# Graphe general : n=3 noeuds, b=4 branches, m=2 mailles -> 4 = (3-1)+2
P = [np.array([-1.5, -1.0]), np.array([1.5, -1.0]), np.array([0.0, 1.5])]
edges = [(0, 1), (1, 2), (2, 0), (0, 1)]
off = [0.0, 0.0, 0.0, 0.45]
for (i, j), dy in zip(edges, off):
    A, B = P[i], P[j]
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2 + dy
    ax2.plot([A[0], mx, B[0]], [A[1], my, B[1]], color="#1a3fb5", linewidth=2.0)
for k, A in enumerate(P):
    ax2.plot([A[0]], [A[1]], "o", color="black", markersize=9)
    ax2.text(A[0] + 0.15, A[1] + 0.15, f"N{k + 1}", fontsize=11)
ax2.text(0.0, -1.9, "b=4, n=3, m=2 : 4=(3-1)+2", fontsize=10, ha="center")
ax2.set_xlim(-2.4, 2.4); ax2.set_ylim(-2.4, 2.4)
ax2.set_title("Heredite : b = (n-1) + m", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
