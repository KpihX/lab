"""Reproduit la figure p.53 du 4e Bloc-Notes : theoreme de Ptolemee.

Quadrilatere convexe direct ABCD, diagonales AC et BD, point E = S(A)
sur la diagonale BD (S = similitude envoyant D sur C). BDA et BEC
semblables.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/ptolemee.png
Usage : uv run scripts/reproduce_ptolemee.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/ptolemee.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

A = np.array([0.0, 3.0])
B = np.array([0.0, 0.0])
C = np.array([2.6, 0.4])
D = np.array([3.2, 2.2])
E = B + 0.45 * (D - B)  # E sur la diagonale BD

fig, ax = plt.subplots(figsize=(6.5, 6))
ax.set_aspect("equal")
ax.set_xlim(-0.8, 4.0)
ax.set_ylim(-0.8, 3.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

qx = [A[0], B[0], C[0], D[0], A[0]]
qy = [A[1], B[1], C[1], D[1], A[1]]
ax.plot(qx, qy, color="black", linewidth=1.5)
ax.plot([A[0], C[0]], [A[1], C[1]], color="dimgray", linewidth=1.1)
ax.plot([B[0], D[0]], [B[1], D[1]], color="dimgray", linewidth=1.1)
ax.plot(E[0], E[1], "o", color="red", markersize=6)

for P, lab, dx, dy in [(A, "A", -0.25, 0.05), (B, "B", -0.25, -0.2),
                       (C, "C", 0.08, -0.05), (D, "D", 0.08, 0.05)]:
    ax.plot(P[0], P[1], "o", color="black", markersize=4)
    ax.text(P[0] + dx, P[1] + dy, lab, fontsize=13)
ax.text(E[0] - 0.28, E[1] + 0.08, "E", color="red", fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
