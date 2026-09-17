"""Reproduit le schema de cycloide-schema : arches de cycloide (roulement sans glissement).

Original : capture d'arcs gris reguliers sur fond quadrille, axe x gradue (0,10,20,30).
Vue : cycloide x = t - sin t, y = 1 - cos t, 5 arches.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/geometrie/cycloide-schema/assets/cycloide.png
Usage : uv run scripts/reproduce_cycloide-schema_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/cycloide-schema/assets/cycloide.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

r = 1.0
t = np.linspace(0, 5 * 2 * np.pi, 2000)
x = r * (t - np.sin(t))
y = r * (1 - np.cos(t))
fig, ax = plt.subplots(figsize=(9, 3.5))
ax.set_xlim(-0.5, 5 * 2 * np.pi + 0.5)
ax.set_ylim(-0.5, 2.8)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.plot([0, 5 * 2 * np.pi], [0, 0], color="black", linewidth=1.4)
ax.plot(x, y, color="#4a4a4a", linewidth=3.0)
for k in range(6):
    ax.plot(k * 2 * np.pi, 0, "o", color="#4a4a4a", markersize=5)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
