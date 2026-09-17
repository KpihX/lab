"""Reproduit la figure p.3 de suite-croissante (lot analyse-suites-series).

Figure d'origine (capture GeoGebra) : nuage de points bleus en escalier
(U_n : 1 une fois, 2 deux fois, 3 trois fois, ...), courbe verte de
l'equivalent (1 + sqrt(8n-7)) / 2 superposee ; axes ~0-98 / ~0-44,
quadrillage fin.

Style "stylo" : points bleus, courbe rouge (convention du lot : la courbe
verte d'origine est rendue rouge), fond quadrille bleu.

Sortie : raw/analyse-suites-series/suite-croissante/assets/suite-croissante.png

Usage :
  uv run scripts/reproduce_suite_croissante_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-suites-series"
    "/suite-croissante/assets/suite-croissante.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

# Escalier : m repete m fois (n = 1..98 comme sur la capture).
ns, vals = [], []
n = 1
m = 1
while n <= 98:
    for _ in range(m):
        if n > 98:
            break
        ns.append(n)
        vals.append(m)
        n += 1
    m += 1
ns = np.array(ns)
vals = np.array(vals)

# Equivalent (1 + sqrt(8n-7)) / 2.
x = np.linspace(1, 98, 400)
equiv = (1 + np.sqrt(8 * x - 7)) / 2

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 100)
ax.set_ylim(0, 44)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xlabel("n")
ax.set_ylabel("U_n")

ax.scatter(ns, vals, color=BLUE, s=18, zorder=3)
ax.plot(x, equiv, color=RED, linewidth=1.5)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
