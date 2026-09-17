"""Reproduit le fond de recurrence-justification : bon ordre de N, minimum m0 de A.
Manuscrit : A subset N, minimum m0, p-1 et p, absurde, hypotheses -> P(n) vraie.
Vue : droite N, ensemble A (points bleus), minimum m0, predecesseur p-1 hors A.
Sortie : raw/algebre-arithmetique/recurrence-justification/assets/bon-ordre-minimum.png
Usage : uv run scripts/reproduce_recurrence-justification_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/recurrence-justification/assets/bon-ordre-minimum.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 3.2))
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-1, 1.2)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.axhline(0, color="black", linewidth=1.2)
A = [3, 4, 5, 7, 8]
for k in range(10):
    ax.plot(k, 0, "o", color="#1a3fb5" if k in A else "gray",
            markersize=9 if k in A else 6, alpha=1.0 if k in A else 0.4)
ax.plot(3, 0, "o", color="red", markersize=12, markerfacecolor="none", markeredgewidth=2)
ax.text(3, 0.35, "m0 = min A", color="red", fontsize=11, ha="center")
ax.text(2, -0.45, "p-1 hors A", color="gray", fontsize=10, ha="center")
ax.text(6, 0.35, "A : P(n) vraie", color="#1a3fb5", fontsize=11, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
