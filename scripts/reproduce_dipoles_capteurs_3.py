"""Reproduit la figure p.6b de dipoles-capteurs : U=f(I, theta) de la thermistance.

Graphe d'origine (fond gris) : courbe rouge qui monte vite (partie lineaire
a faibles courants), plafonne vers 9 V, puis redescend doucement (zone a
pente negative par auto-echauffement) ; U en volts en ordonnee (0..10),
I en mA en abscisse (0..100). Reproduction qualitative.

Style "stylo" : courbe rouge, quadrille bleu.

Sortie : raw/physique/dipoles-capteurs/assets/thermistance-u-i.png

Usage :
  uv run scripts/reproduce_dipoles_capteurs_3.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_dipoles_capteurs_3.py
>>> # OK -> .../assets/thermistance-u-i.png (XXXXX o)
>>> # le rendu montre la montee, le plateau puis la pente negative.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/dipoles-capteurs/assets/thermistance-u-i.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

I = np.linspace(0, 100, 300)
U = 10.5 * (1.0 - np.exp(-I / 9.0)) - 0.026 * I

fig, ax = plt.subplots(figsize=(6.5, 5))
ax.set_xlim(0, 105)
ax.set_ylim(0, 10.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.plot(I, U, color=RED, linewidth=1.6)
ax.text(1, 9.7, "U (V)", color=BLUE, fontsize=12)
ax.text(88, 1.6, "I (mA)", color=BLUE, fontsize=12)
ax.text(1, 8.8, "9", color=BLUE, fontsize=9)
ax.text(11, 0.5, "10", color=BLUE, fontsize=9)
ax.text(88, 0.5, "90", color=BLUE, fontsize=9)
ax.text(55, 5.0, "plateau puis\npente negative", color=BLUE, fontsize=10,
        ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
