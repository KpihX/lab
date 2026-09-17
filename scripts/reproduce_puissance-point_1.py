"""Reproduit le fond de puissance-point : cercle, point M, MA.MB = MO^2 - R^2.
Manuscrit : cercle C, secante par M coupant en A et B, puissance f(M).
Vue : cercle, point M exterieur, secante M-A-B, tangente, formule.
Sortie : raw/geometrie/puissance-point/assets/puissance-point.png
Usage : uv run scripts/reproduce_puissance-point_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/puissance-point/assets/puissance-point.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

th = np.linspace(0, 2 * np.pi, 400)
fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(-1.5, 4.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.plot(np.cos(th), np.sin(th), color="#1a3fb5", linewidth=1.8)
M = np.array([3.2, 0.6])
ax.plot(M[0], M[1], "o", color="red", markersize=8)
ax.text(M[0] + 0.1, M[1] + 0.1, "M", color="red", fontsize=12)
ax.plot(0, 0, "o", color="black", markersize=5)
ax.text(0.08, 0.12, "O", fontsize=11)
d = M / np.linalg.norm(M)
T = d * 1.0 + np.array([-d[1], d[0]]) * np.sqrt(np.linalg.norm(M) ** 2 - 1) * 0 + np.array([0.28, 0.96])
T = np.array([0.28, 0.96])
ax.plot([M[0], T[0]], [M[1], T[1]], color="red", linewidth=1.5)
ax.plot([M[0], -1.0], [M[1], -0.28], color="#1a3fb5", linewidth=1.5)
ax.plot(-0.94, -0.34, "o", color="#1a3fb5", markersize=6)
ax.plot(0.94, 0.34, "o", color="#1a3fb5", markersize=6)
ax.text(-1.05, -0.6, "A", color="#1a3fb5", fontsize=11)
ax.text(1.0, 0.5, "B", color="#1a3fb5", fontsize=11)
ax.text(1.2, -1.8, "P(M) = MA.MB = MO^2 - R^2", color="red", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
