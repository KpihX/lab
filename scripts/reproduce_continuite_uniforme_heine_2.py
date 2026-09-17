"""Reproduit la figure p.2 de continuite-uniforme-heine : sin(exp(x)).

Schema d'origine (stylo bleu sur papier) : courbe oscillante
d'amplitude constante dont la frequence augmente vers la droite
(sin(e^x) sur x >= 0 environ), axes x horizontal et y vertical
avec origine O.

Style "stylo" : courbe et axes bleus, origine O rouge,
fond quadrille bleu.

Sortie : raw/analyse-fonctions/continuite-uniforme-heine/assets/sin-exp-oscillations.png

Usage :
  uv run scripts/reproduce_continuite_uniforme_heine_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_continuite_uniforme_heine_2.py
>>> # OK -> .../assets/sin-exp-oscillations.png (XXXXX o)
>>> # le rendu montre des oscillations qui se resserrent vers la droite.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions/continuite-uniforme-heine/assets/sin-exp-oscillations.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

xs = np.linspace(-0.5, 2.6, 4000)
ys = np.sin(np.exp(xs))

fig, ax = plt.subplots(figsize=(7, 3.5))
ax.set_xlim(-0.6, 2.7)
ax.set_ylim(-1.4, 1.4)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Axes et courbe.
ax.axhline(0, color=BLUE, linewidth=1.2)
ax.plot(xs, ys, color=BLUE, linewidth=1.2)

# Origine O et fleches d'axes en rouge/bleu.
ax.text(-0.12, -0.22, "O", color=RED, fontsize=13)
ax.annotate("", xy=(2.7, 0), xytext=(2.45, 0),
            arrowprops=dict(color=BLUE, arrowstyle="->", linewidth=1.2))
ax.text(2.6, 0.12, "x", color=BLUE, fontsize=13)
ax.annotate("", xy=(0, 1.4), xytext=(0, 1.15),
            arrowprops=dict(color=BLUE, arrowstyle="->", linewidth=1.2))
ax.text(0.06, 1.22, "y", color=BLUE, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
