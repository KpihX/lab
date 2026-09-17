"""Reproduit la figure p.51 du 4e Bloc-Notes : probleme 2 (cercles tangents).

Deux droites secantes (D1), (D2) en Om, trois cercles de centres O1, O'',
O' tangents aux deux droites (centres sur la bissectrice), point A sur le
cercle median, A'/A'' = intersections de (Om A) avec le petit cercle.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/probleme2-cercle.png
Usage : uv run scripts/reproduce_probleme2_cercle.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/probleme2-cercle.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

slope = 0.25
half = np.arctan(slope)
s = np.sin(half)
O1x, O2x, O3x = 3.0, 5.4, 8.0
O1 = np.array([O1x, 0.0])
Opp = np.array([O2x, 0.0])
Op = np.array([O3x, 0.0])
r1, r2, r3 = O1x * s, O2x * s, O3x * s

A = Opp + r2 * np.array([np.cos(2.2), np.sin(2.2)])
d = A / np.linalg.norm(A)  # direction Om -> A
# intersections de la droite Om + t*d avec le cercle (O1, r1)
oc = O1
b = float(np.dot(oc, d))
disc = b**2 - (float(np.dot(oc, oc)) - r1**2)
t1, t2 = b - np.sqrt(disc), b + np.sqrt(disc)
Apr, As = t1 * d, t2 * d

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_aspect("equal")
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-2.8, 2.8)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

X = np.linspace(-0.5, 10.5, 100)
ax.plot(X, slope * X, color="dimgray", linewidth=1.2)
ax.plot(X, -slope * X, color="dimgray", linewidth=1.2)
ax.text(8.6, 8.6 * slope + 0.15, "(Δ1)", fontsize=12, color="dimgray")
ax.text(8.6, -8.6 * slope - 0.3, "(Δ2)", fontsize=12, color="dimgray")

for O, r in [(O1, r1), (Opp, r2), (Op, r3)]:
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(O[0] + r * np.cos(t), O[1] + r * np.sin(t),
            color="gray", linewidth=1.4)
    ax.plot(O[0], O[1], "o", color="black", markersize=3)

tA = np.linspace(0, 1, 50)
ax.plot(tA * 10.2 * d[0], tA * 10.2 * d[1],
        color="black", linewidth=1.0, linestyle=(0, (4, 3)))

ax.plot(A[0], A[1], "o", color="red", markersize=5)
ax.plot(Apr[0], Apr[1], "o", color="black", markersize=3)
ax.plot(As[0], As[1], "o", color="black", markersize=3)
ax.text(0.05, 0.18, "Ω", fontsize=12)
ax.text(O1[0] - 0.1, O1[1] + 0.25, "O1", fontsize=11)
ax.text(Opp[0] - 0.1, Opp[1] + 0.3, "O''", fontsize=11)
ax.text(Op[0] - 0.05, Op[1] + 0.35, "O'", fontsize=11)
ax.text(A[0] + 0.12, A[1] + 0.05, "A", color="red", fontsize=12)
ax.text(Apr[0] - 0.25, Apr[1] - 0.25, "A'", fontsize=11)
ax.text(As[0] + 0.08, As[1] + 0.05, "A''", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
