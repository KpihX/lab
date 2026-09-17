"""Reproduit la figure p.3 du 3e Bloc-Notes : hexagone regulier inscrit.

Style "stylo" : hexagone rouge, cercle circonscrit gris, fond quadrille,
centre O, rayon r, apotheme h, angle alpha, cote a.
Sortie : raw/bloc-notes/troisieme-bloc-notes/assets/hexagone-cercle.png
Usage : uv run scripts/reproduce_hexagone_cercle.py  (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/troisieme-bloc-notes/assets/hexagone-cercle.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

r = 1.0
angles = np.linspace(0, 2 * np.pi, 7) + np.pi / 6
hx, hy = r * np.cos(angles), r * np.sin(angles)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.3, 1.5)
ax.set_ylim(-1.3, 1.3)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
ax.set_axisbelow(True)

theta = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(theta), np.sin(theta), color="gray", linewidth=1.5)  # cercle crayon
ax.plot(hx, hy, color="red", linewidth=2.0)  # hexagone stylo rouge
ax.plot([0, hx[0]], [0, hy[0]], color="red", linewidth=1.5)  # rayon r
ax.plot([0, (hx[0] + hx[1]) / 2], [0, (hy[0] + hy[1]) / 2], color="red", linewidth=1.2)  # apotheme h

ax.plot(0, 0, "o", color="red")
ax.text(0.03, -0.1, "O", color="red", fontsize=13)
ax.text(hx[0] / 2 + 0.05, hy[0] / 2, "r", color="red", fontsize=13)
ax.text(0.28, 0.28, "h", color="red", fontsize=13)
ax.text(0.12, 0.05, "α", color="red", fontsize=13)
ax.text((hx[0] + hx[1]) / 2, (hy[0] + hy[1]) / 2 + 0.08, "a", color="red", fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
