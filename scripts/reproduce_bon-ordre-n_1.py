"""Reproduit le fond de bon-ordre-n : toute partie non vide de N admet un plus petit element.

Illustration : droite N, partie A (points bleus), son min m = a_1 <= n.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/ensembles-cardinaux/bon-ordre-n/assets/bon-ordre.png
Usage : uv run scripts/reproduce_bon-ordre-n_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/ensembles-cardinaux/bon-ordre-n/assets/bon-ordre.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

A = [3, 5, 6, 9, 12]
fig, ax = plt.subplots(figsize=(9, 2.8))
ax.set_xlim(-1, 14)
ax.set_ylim(-1.2, 1.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.plot([-0.5, 13.5], [0, 0], color="black", linewidth=1.4)
for k in range(0, 14):
    ax.plot([k, k], [-0.12, 0.12], color="black", linewidth=1.0)
    ax.text(k, -0.55, str(k), fontsize=9, ha="center", color="black")
for a in A:
    ax.plot(a, 0, "o", color="#1a3fb5", markersize=10)
ax.plot(A[0], 0, "o", color="red", markersize=12, fillstyle="none", markeredgewidth=2)
ax.text(A[0], 0.55, "min A = m", color="red", fontsize=11, ha="center")
ax.text(8, 1.0, "A = {a1, a2, ...} ⊂ N", color="#1a3fb5", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
