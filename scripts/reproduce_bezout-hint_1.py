"""Reproduit le fond de bezout-hint : ideal <M1..Mn> = mZ sur la droite des entiers.

Manuscrit : hint du theoreme de Bezout generalise (sous-groupes de Z).
Illustration : droite graduee, multiples de m (= mZ) en bleu, generateurs Mi en rouge.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/algebre-arithmetique/bezout-hint/assets/ideal-mz.png
Usage : uv run scripts/reproduce_bezout-hint_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/bezout-hint/assets/ideal-mz.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

m = 4
Mi = [6, 10, 14]
fig, ax = plt.subplots(figsize=(9, 2.6))
ax.set_xlim(-8.5, 16.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.plot([-8, 16], [0, 0], color="black", linewidth=1.4)
for k in range(-8, 17):
    ax.plot([k, k], [-0.12, 0.12], color="black", linewidth=1.0)
for k in range(-8, 17, m):
    ax.plot(k, 0, "o", color="#1a3fb5", markersize=9)
for v in Mi:
    ax.plot(v, 0, "s", color="red", markersize=8)
    ax.text(v, 0.45, f"M={v}", color="red", fontsize=10, ha="center")
ax.text(0, -0.75, "<M1..Mn> = mZ,  m = 4", color="#1a3fb5", fontsize=12, ha="center")
ax.text(12.5, 0.45, "mZ (ronds bleus)", color="#1a3fb5", fontsize=10)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
