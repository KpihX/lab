"""Reproduit la figure de caracteristiques-plan (prise 2, ex-caracteristiques-plan-2) : deux vecteurs directeurs u, v du plan (P).

Manuscrit : u et v directeurs de (P), n = u wedge v normal ; cas c=0 (n horizontal).
Schema : plan en coupe, u et v dans le plan, n perpendiculaire.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/geometrie/caracteristiques-plan/assets/plan-directeurs.png
Usage : uv run scripts/reproduce_caracteristiques-plan_2.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/caracteristiques-plan/assets/plan-directeurs.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(7.5, 5.5))
ax.set_xlim(-5, 5)
ax.set_ylim(-4, 6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_aspect("equal")

P = np.array([[-4, -2.5], [4, -1.5], [2.5, 2.5], [-4.5, 1.5], [-4, -2.5]])
ax.plot(P[:, 0], P[:, 1], color="#1a3fb5", linewidth=1.8)
O = np.array([-0.5, -0.5])
U = O + np.array([2.6, 0.5])
V = O + np.array([0.4, 2.2])
N = O + np.array([-0.5, 3.4])
for t in np.linspace(0, 1, 7):
    a = P[0] * (1 - t) + P[3] * t
    b = P[1] * (1 - t) + P[2] * t
    ax.plot([a[0], b[0]], [a[1], b[1]], color="#1a3fb5", linewidth=0.7, alpha=0.6)
ax.annotate("", xy=U, xytext=O, arrowprops=dict(arrowstyle="->", color="#1a3fb5", linewidth=2.0))
ax.annotate("", xy=V, xytext=O, arrowprops=dict(arrowstyle="->", color="#1a3fb5", linewidth=2.0))
ax.annotate("", xy=N, xytext=O, arrowprops=dict(arrowstyle="->", color="red", linewidth=2.0))
ax.text(U[0] + 0.1, U[1] + 0.1, "u", color="#1a3fb5", fontsize=13)
ax.text(V[0] + 0.1, V[1] + 0.1, "v", color="#1a3fb5", fontsize=13)
ax.text(N[0] + 0.15, N[1] + 0.1, "n = u ∧ v", color="red", fontsize=12)
ax.text(-3.4, -2.0, "(P)", color="#1a3fb5", fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
