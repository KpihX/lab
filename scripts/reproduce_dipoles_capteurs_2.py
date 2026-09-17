"""Reproduit la figure p.6a de dipoles-capteurs : R=f(theta) de la thermistance CTN.

Graphe d'origine (fond gris) : courbe rouge decroissante, R en ohms en
ordonnee (100..900), theta en degres C en abscisse (10..90) ; allure de la
loi R(T) = R(T0).exp[B.(1/T - 1/T0)]. Reproduction qualitative.

Style "stylo" : courbe rouge, quadrille bleu.

Sortie : raw/physique/dipoles-capteurs/assets/thermistance-r-theta.png

Usage :
  uv run scripts/reproduce_dipoles_capteurs_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_dipoles_capteurs_2.py
>>> # OK -> .../assets/thermistance-r-theta.png (XXXXX o)
>>> # le rendu montre R qui chute quand theta augmente (CTN).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/dipoles-capteurs/assets/thermistance-r-theta.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

theta = np.linspace(10, 90, 200)
R = 1400.0 * np.exp(-theta / 24.0)

fig, ax = plt.subplots(figsize=(6.5, 5))
ax.set_xlim(5, 95)
ax.set_ylim(0, 950)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.plot(theta, R, color=RED, linewidth=1.6)
ax.text(12, 880, "R (ohm)", color=BLUE, fontsize=12)
ax.text(62, 320, "theta (degC)", color=BLUE, fontsize=12)
ax.text(6, 895, "900", color=BLUE, fontsize=9)
ax.text(6, 95, "100", color=BLUE, fontsize=9)
ax.text(11, 40, "10", color=BLUE, fontsize=9)
ax.text(86, 40, "90", color=BLUE, fontsize=9)
ax.text(55, 500, "CTN", color=BLUE, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
