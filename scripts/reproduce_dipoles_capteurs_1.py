"""Reproduit la figure p.5 de dipoles-capteurs : caracteristique U=f(I) du rheostat.

Graphe d'origine (papier millimetre) : droite rouge passant par l'origine,
U(V) en ordonnee (1..9), I(A) en abscisse (0,1..0,9) ; mesures pour R = 10 ohm
(I = 0,1 A -> U = 1 V ... I = 0,4 A -> U = 4 V), soit U = R.I.

Style "stylo" : courbe rouge, quadrille bleu.

Sortie : raw/physique/dipoles-capteurs/assets/caracteristique-rheostat.png

Usage :
  uv run scripts/reproduce_dipoles_capteurs_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_dipoles_capteurs_1.py
>>> # OK -> .../assets/caracteristique-rheostat.png (XXXXX o)
>>> # le rendu montre la droite U = 10.I passant par l'origine.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/dipoles-capteurs/assets/caracteristique-rheostat.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

R = 10.0
I = np.linspace(0, 0.95, 100)
U = R * I

fig, ax = plt.subplots(figsize=(6.5, 5))
ax.set_xlim(0, 1.0)
ax.set_ylim(0, 10)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.plot(I, U, color=RED, linewidth=1.6)
ax.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4], "o", color=BLUE, markersize=4)
ax.text(0.02, 9.3, "U(V)", color=RED, fontsize=12)
ax.text(0.9, 1.3, "I(A)", color=RED, fontsize=12)
ax.text(0.03, 8.2, "9", color=BLUE, fontsize=9)
ax.text(0.03, 1.0, "1", color=BLUE, fontsize=9)
ax.text(0.1, 0.4, "0,1", color=BLUE, fontsize=9)
ax.text(0.82, 0.4, "0,9", color=BLUE, fontsize=9)
ax.text(0.55, 7.5, "U = R.I (R = 10 ohm)", color=BLUE, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
