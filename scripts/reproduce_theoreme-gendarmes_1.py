"""Reproduit le fond de theoreme-gendarmes : Un <= Vn <= Wn prises en etau vers a=0.

Manuscrit : (Un) bornee x Vn -> 0, puis encadrement Un <= Vn <= Wn -> lim Vn = a.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/analyse-fonctions/theoreme-gendarmes/assets/gendarmes-suites.png
Usage : uv run scripts/reproduce_theoreme-gendarmes_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions/theoreme-gendarmes/assets/gendarmes-suites.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 5))
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

n = np.arange(1, 31)
U = -1.0 / n
W = 1.0 / n
V = np.sin(n) / n
ax.plot(n, U, color="#1a3fb5", linewidth=2.0, marker="o", markersize=3, label="Un")
ax.plot(n, W, color="#1a3fb5", linewidth=2.0, marker="o", markersize=3, label="Wn")
ax.plot(n, V, color="red", linewidth=2.0, marker="o", markersize=3, label="Vn")
ax.plot(n, np.zeros_like(n), color="black", linewidth=1.0, linestyle="--")
ax.text(24, 0.12, "a = 0", fontsize=12)
ax.text(2, 0.62, "Un <= Vn <= Wn", fontsize=11)
ax.legend(frameon=True, fontsize=9, loc="upper right")
ax.set_xlim(0.5, 31); ax.set_ylim(-1.1, 1.1)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
