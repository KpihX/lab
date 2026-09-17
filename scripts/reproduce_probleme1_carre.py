"""Reproduit la figure p.50 du 4e Bloc-Notes : probleme 1 (carre).

Carre ABCD, diagonale AC, droites secantes (D1) horizontale par B et (D2)
oblique par A, angle pi/4 en A entre AB et AC. AC/AB = sqrt(2),
C = S(B) avec S = similitude(A, sqrt(2), pi/4).
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/probleme1-carre.png
Usage : uv run scripts/reproduce_probleme1_carre.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/probleme1-carre.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

A = np.array([0.0, 0.0])
B = np.array([2.0, 0.0])
C = np.array([2.0, 2.0])
D = np.array([0.0, 2.0])

fig, ax = plt.subplots(figsize=(6.5, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.6, 3.6)
ax.set_ylim(-1.2, 3.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

ax.annotate("", xy=(3.4, 0), xytext=(-1.4, 0),
            arrowprops=dict(arrowstyle="-", color="dimgray", linewidth=1.2))
ax.text(2.75, 0.12, "(Δ1)", fontsize=12, color="dimgray")
u = np.array([1.0, 0.45])
ax.plot([A[0] - 1.3 * u[0], A[0] + 3.2 * u[0]],
        [A[1] - 1.3 * u[1], A[1] + 3.2 * u[1]],
        color="dimgray", linewidth=1.2)
ax.text(2.75, 1.55, "(Δ2)", fontsize=12, color="dimgray")

sqx = [A[0], B[0], C[0], D[0], A[0]]
sqy = [A[1], B[1], C[1], D[1], A[1]]
ax.plot(sqx, sqy, color="black", linewidth=1.5)
ax.plot([A[0], C[0]], [A[1], C[1]], color="red", linewidth=1.3)

arc = np.linspace(0, np.pi / 4, 50)
ax.plot(A[0] + 0.7 * np.cos(arc), A[1] + 0.7 * np.sin(arc),
        color="red", linewidth=1.3)
ax.text(0.62, 0.28, "π/4", color="red", fontsize=12)

for P, lab, dx, dy in [(A, "A", -0.2, -0.25), (B, "B", 0.05, -0.25),
                       (C, "C", 0.06, 0.05), (D, "D", -0.22, 0.05)]:
    ax.plot(P[0], P[1], "o", color="black", markersize=4)
    ax.text(P[0] + dx, P[1] + dy, lab, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
