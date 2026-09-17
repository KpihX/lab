"""Reproduit la figure p.7 de dipoles-capteurs : R=f(E) de la photoresistance.

Graphe d'origine : courbe decroissante, R en kohm en ordonnee (0..9),
E en lux en abscisse (0..800) ; la resistance chute quand l'eclairement
augmente. Reproduction qualitative (courbe bleue).

Style "stylo" : courbe bleue, quadrille bleu #9db3d8.

Sortie : raw/physique/dipoles-capteurs/assets/photoresistance-r-e.png

Usage :
  uv run scripts/reproduce_dipoles_capteurs_5.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_dipoles_capteurs_5.py
>>> # OK -> .../assets/photoresistance-r-e.png (XXXXX o)
>>> # le rendu montre R qui chute quand E augmente.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/dipoles-capteurs/assets/photoresistance-r-e.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

E = np.linspace(0, 850, 300)
R = 6.0 * np.exp(-E / 90.0) + 3.0 * np.exp(-E / 500.0)

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(0, 870)
ax.set_ylim(0, 9.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.plot(E, R, color=BLUE, linewidth=1.4)
ax.text(10, 8.9, "R (kohm)", color=BLUE, fontsize=12)
ax.text(770, 1.3, "E (lux)", color=BLUE, fontsize=12)
ax.text(10, 8.0, "9", color=BLUE, fontsize=9)
ax.text(95, 0.4, "100", color=BLUE, fontsize=9)
ax.text(795, 0.4, "800", color=BLUE, fontsize=9)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
