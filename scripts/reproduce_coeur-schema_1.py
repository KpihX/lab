"""Reproduit le schema de coeur-schema : coeur GeoGebra f + g.

Original : f(x) = sqrt(1-(|x|-1)^2) (haut, bleu), g(x) = -3*sqrt(1-sqrt(|x|/2)) (bas, rouge).
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/geometrie/coeur-schema/assets/coeur.png
Usage : uv run scripts/reproduce_coeur-schema_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coeur-schema/assets/coeur.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(6.5, 6.5))
ax.set_xlim(-2.6, 2.6)
ax.set_ylim(-3.4, 2.2)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_aspect("equal")

ax.plot([-2.6, 2.6], [0, 0], color="black", linewidth=1.2)
ax.plot([0, 0], [-3.4, 2.2], color="black", linewidth=1.2)
x1 = np.linspace(-2, 2, 1200)
f = np.sqrt(np.clip(1 - (np.abs(x1) - 1) ** 2, 0, None))
ax.plot(x1, f, color="#2b6cb0", linewidth=2.2)
x2 = np.linspace(-2, 2, 1200)
g = -3 * np.sqrt(np.clip(1 - np.sqrt(np.abs(x2) / 2), 0, None))
ax.plot(x2, g, color="#c0392b", linewidth=2.2)
ax.text(-2.15, 0.15, "-2", fontsize=10)
ax.text(1.95, 0.15, "2", fontsize=10)
ax.text(0.1, 0.25, "0", fontsize=10)
ax.text(0.12, -2.0, "-2", fontsize=10)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
