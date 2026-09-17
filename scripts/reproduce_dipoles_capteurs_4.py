"""Reproduit la figure p.7 de dipoles-capteurs : U=f(I) de la photoresistance.

Capture Regressi d'origine : trois droites passant par l'origine, une par
eclairement E (U en V en ordonnee, I en mA en abscisse) :
  E = 29 lux : U = 22,7 x I  (R = 22,7 kohm)
  E = 114 lux : U = 5,85 x I (R = 5,85 kohm)
  E = 236 lux : U = 2,62 x I (R = 2,62 kohm)
Couleurs d'origine (bleu, vert, rouge) conservees pour distinguer les 3 E.

Style "stylo" : quadrille bleu #9db3d8.

Sortie : raw/physique/dipoles-capteurs/assets/photoresistance-u-i.png

Usage :
  uv run scripts/reproduce_dipoles_capteurs_4.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_dipoles_capteurs_4.py
>>> # OK -> .../assets/photoresistance-u-i.png (XXXXX o)
>>> # le rendu montre les 3 droites, d'autant plus pentues que E est faible.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/dipoles-capteurs/assets/photoresistance-u-i.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, GREEN = "#1a3fb5", "red", "#2a8a2a"

I = np.linspace(0, 2, 100)

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(0, 2.05)
ax.set_ylim(0, 6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.plot(I, 22.7 * I, color=BLUE, linewidth=1.6)
ax.plot(I, 5.85 * I, color=GREEN, linewidth=1.6)
ax.plot(I, 2.62 * I, color=RED, linewidth=1.6)
ax.text(0.22, 5.3, "E=29 lux : U = 22,7 x I", color=BLUE, fontsize=9)
ax.text(0.75, 4.7, "E=114 lux : U = 5,85 x I", color=GREEN, fontsize=9)
ax.text(1.35, 4.1, "E=236 lux : U = 2,62 x I", color=RED, fontsize=9)
ax.text(0.03, 5.6, "U (V)", color=BLUE, fontsize=12)
ax.text(1.9, 0.25, "I (mA)", color=BLUE, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
