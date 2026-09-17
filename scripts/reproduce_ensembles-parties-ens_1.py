"""Reproduit le schema ensembles / parties : famille et coefficients.

Manuscrit d'origine (ensembles-parties-ens.jpg) : « Soit ... le
vecteur ... », « Xi ... telle que ... », « est en ... la ... cond...
est 1 », « Soit une famille ... », sommes doubles
« sum_{i in K} d_i x_i », cas « sum d_i x_i = 0 », « Il ... que ...
les ... (Critere ...) ne peuvent ... etre tous ... », « ... tous > 0 »,
« Prenons ... I = ... », « Donc ... sum ... », « Soit ... Xc ... U Xi »,
« D'ou ... », « En raisonnant de facon analogue, ... » [nombreuses
lectures incertaines — doigt sur une zone, ecriture serree].

Ici : diagramme ensembliste — un ensemble X recouvert par une
famille (X1, X2, X3) avec zones positives/negatives evoquant le
signe des coefficients d_i.

Sortie : raw/ensembles-cardinaux/ensembles-parties-ens/assets/ensembles.png

Usage :
  uv run scripts/reproduce_ensembles-parties-ens_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/ensembles-parties-ens/assets/ensembles.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

ax.add_patch(plt.Rectangle((-3, -2.2), 6, 4.4, fill=False, edgecolor=BLUE, linewidth=1.2))  # X
for cx, cy in ((-1.1, 0.3), (1.1, 0.3), (0.0, -0.9)):  # famille X1, X2, X3
    ax.add_patch(Circle((cx, cy), 1.15, fill=False, edgecolor=BLUE, linewidth=1.4))
ax.plot(0, 0.3, "o", color=RED, markersize=6)  # intersection centrale
ax.set_title("X, famille (Xi) : signes des d_i", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
