"""Reproduit le schema y = erf(x).

Image d'origine (erf-schema.jpg) : capture numerique propre —
courbe rouge y = erf(x), sigmoide impaire, paliers y = -1 et
y = +1, grille pointillee, axes x de -5 a 5, y de -2 a 2,
titre rouge « y = erf(x) » en haut a droite.

Ici : erf via scipy.special, asymptotes +-1, meme cadrage.

Sortie : raw/analyse-fonctions/erf-schema/assets/erf.png

Usage :
  uv run scripts/reproduce_erf-schema_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.special import erf

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/erf-schema/assets/erf.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

x = np.linspace(-5, 5, 600)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(1, color=BLUE, linewidth=0.8, linestyle="--")  # palier +1
ax.axhline(-1, color=BLUE, linewidth=0.8, linestyle="--")  # palier -1
ax.axhline(0, color=BLUE, linewidth=1.0)
ax.axvline(0, color=BLUE, linewidth=1.0)
ax.plot(x, erf(x), color=RED, linewidth=1.8)  # y = erf(x)
ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-2.4, 2.4)
ax.set_title("y = erf(x)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
