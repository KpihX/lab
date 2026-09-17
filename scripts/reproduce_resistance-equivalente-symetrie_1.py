"""Reproduit le fond de resistance-equivalente-symetrie : circuit (C) + 4 x 2R en parallele.

Manuscrit : octaedre A-A1..A4-B, plans de symetrie -> VAi egaux -> 4 resistances
2R en parallele entre A et B, Req = 1/(4/2R) = R/2.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/resistance-equivalente-symetrie/assets/circuit-equivalent.png
Usage : uv run scripts/reproduce_resistance-equivalente-symetrie_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/resistance-equivalente-symetrie/assets/circuit-equivalent.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
for ax in (ax1, ax2):
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for s in ax.spines.values():
        s.set_visible(False)

# (C) : octaedre projete : A haut, B bas, carre median A1..A4
A = np.array([0.0, 2.0]); B = np.array([0.0, -2.0])
M = [np.array([-1.4, 0.0]), np.array([0.0, 0.9]),
     np.array([1.4, 0.0]), np.array([0.0, -0.9])]
names = ["A1", "A2", "A3", "A4"]
for i, P in enumerate(M):
    Q = M[(i + 1) % 4]
    ax1.plot([P[0], Q[0]], [P[1], Q[1]], color="#1a3fb5", linewidth=1.8)
    ax1.plot([A[0], P[0]], [A[1], P[1]], color="#1a3fb5", linewidth=1.4)
    ax1.plot([B[0], P[0]], [B[1], P[1]], color="#1a3fb5", linewidth=1.4)
    ax1.text(P[0] * 1.15, P[1] + 0.12, names[i], fontsize=10)
ax1.plot([A[0]], [A[1]], "o", color="black", markersize=7)
ax1.plot([B[0]], [B[1]], "o", color="black", markersize=7)
ax1.text(0.15, 2.05, "A", fontsize=13); ax1.text(0.15, -2.0, "B", fontsize=13)
ax1.text(-1.9, -2.3, "(C) : aretes R", fontsize=10)
ax1.set_xlim(-2.4, 2.4); ax1.set_ylim(-2.7, 2.7)
ax1.set_aspect("equal")
ax1.set_title("Circuit (C)", fontsize=11)

# Equivalent : 4 blocs 2R en parallele
ax2.plot([0, 6], [4.5, 4.5], color="black", linewidth=2.0)  # rail A
ax2.plot([0, 6], [0.5, 0.5], color="black", linewidth=2.0)  # rail B
for i, x in enumerate([0.8, 2.3, 3.8, 5.3]):
    ax2.plot([x, x], [4.5, 3.4], color="black", linewidth=1.4)
    rect = plt.Rectangle((x - 0.35, 2.1), 0.7, 1.3, facecolor="white",
                         edgecolor="#1a3fb5", linewidth=2.0)
    ax2.add_patch(rect)
    ax2.text(x, 2.75, "2R", fontsize=10, ha="center", color="#1a3fb5")
    ax2.plot([x, x], [2.1, 0.5], color="black", linewidth=1.4)
ax2.text(-0.25, 4.5, "A", fontsize=13); ax2.text(-0.25, 0.5, "B", fontsize=13)
ax2.text(3.0, -0.15, "Req = R/2", fontsize=12, ha="center", color="red")
ax2.set_xlim(-0.6, 6.4); ax2.set_ylim(-0.5, 5.2)
ax2.set_title("4 x 2R en parallele", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
