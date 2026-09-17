"""Reproduit la figure p.11/14 du rapport coniques : hyperbole et asymptotes.

Schema d'origine : (H) x^2/a^2 - y^2/b^2 = 1, foyers F/F', directrice (D): x=a/e,
asymptotes (D'): y = +/- b/a*x, c = sqrt(a^2+b^2), e = c/a.

Sortie : raw/geometrie/coniques-rapport/assets/fig06-hyperbole-asymptotes.png
Usage : uv run scripts/reproduce_coniques_rapport_6.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig06-hyperbole-asymptotes.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

a, b = 3.0, 2.0
c = np.sqrt(a**2 + b**2)

fig, ax = plt.subplots(figsize=(7, 6))
ax.set_aspect("equal")
ax.set_xlim(-7, 7)
ax.set_ylim(-5, 5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

y = np.linspace(-5, 5, 600)
for s in (-1, 1):  # deux branches
    x = s * a * np.sqrt(1 + (y / b) ** 2)
    ax.plot(x, y, color="black", linewidth=1.6)
xs = np.linspace(-7, 7, 50)
for s in (-1, 1):
    ax.plot(xs, s * b / a * xs, color="gray", linewidth=1.1, linestyle="--")
ax.plot([-7, 7], [0, 0], color="dimgray", linewidth=1.0)
for px, name in [(c, "F"), (-c, "F'"), (a, "A"), (-a, "A'"), (0, "O")]:
    ax.plot(px, 0, "o", color="black", markersize=4)
    ax.text(px + 0.1, 0.25, name, fontsize=11)
ax.text(4.5, 3.6, "y = b/a·x", fontsize=10, color="dimgray")
ax.text(4.5, -3.6, "y = −b/a·x", fontsize=10, color="dimgray")
ax.text(-5.5, 3.5, "(H)", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
