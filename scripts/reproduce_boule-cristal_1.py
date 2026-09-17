"""Reproduit le fond de boule-cristal (schema masse-ressort, p. boule-cristal).

Fond : support fixe (2 traits horizontaux), ressort (zigzag vertical,
~6 ondulations), boule (disque plein gris). Labels d'origine : "ressort"
(face au zigzag), "boule" (face au disque). Aucune formule sur l'original.
Style : traces noires/grises, labels gris, fond quadrille bleu.

Sortie : raw/dessins-photos/boule-cristal/assets/boule-cristal-schema.png

Usage :
  uv run scripts/reproduce_boule-cristal_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/photos-dessins"
    "/boule-cristal/assets/boule-cristal-schema.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(3.2, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

# Support fixe : 2 traits horizontaux paralleles (plafond)
ax.plot([2, 8], [9.4, 9.4], color="black", linewidth=1.6)
ax.plot([2, 8], [9.1, 9.1], color="black", linewidth=1.6)

# Ressort : zigzag vertical ~6 ondulations entre support et boule
n = 6
y_top, y_bot = 9.1, 3.4
ys = np.linspace(y_top, y_bot, 2 * n + 1)
xs = np.full_like(ys, 5.0)
xs[1:-1:2] = 4.2
xs[2:-1:2] = 5.8
ax.plot([5.0, 5.0], [9.4, y_top], color="black", linewidth=1.2)
ax.plot(xs, ys, color="black", linewidth=1.2)

# Boule : disque plein gris attache a l'extremite basse
boule = plt.Circle((5.0, 2.2), 1.1, color="grey", alpha=0.7, ec="black", lw=1.2)
ax.add_patch(boule)
ax.plot([5.0, 5.0], [y_bot, 3.3], color="black", linewidth=1.2)

# Labels d'origine (a droite)
ax.text(6.6, 6.2, "ressort", color="dimgrey", fontsize=10, va="center")
ax.text(6.6, 2.2, "boule", color="dimgrey", fontsize=10, va="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
