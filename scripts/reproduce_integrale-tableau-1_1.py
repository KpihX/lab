"""Reproduit l'integrale I = integrale dx/(x^2+a^2)^(3/2) (p. integrale-tableau-1).

Fond : pour a > 0 et x > 0, I = 1/(a^2 sqrt(1+a^2 x^-2)) + c, soit
x/(a^2 sqrt(x^2+a^2)) + c. Reproduction (a = 1) : integrande et
primitive sur [-3, 3].

Style "stylo" : courbes bleues, titre rouge, fond quadrille bleu.

Sortie : raw/analyse-integrales/integrale-tableau-1/assets/integrale-3-2.png

Usage :
  uv run scripts/reproduce_integrale-tableau-1_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_integrale-tableau-1_1.py
>>> # OK -> .../assets/integrale-3-2.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/integrale-tableau-1/assets/integrale-3-2.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"
A = 1.0

xs = np.linspace(-3, 3, 1201)
integrande = 1.0 / (xs**2 + A**2) ** 1.5
primitive = xs / (A**2 * np.sqrt(xs**2 + A**2))

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.axvline(0, color=BLUE, linewidth=1.0)
ax.plot(xs, integrande, color=BLUE, linewidth=1.6)
ax.plot(xs, primitive, color=RED, linewidth=1.4)
ax.text(-2.9, 1.05, "1/(x^2+1)^(3/2)", color=BLUE, fontsize=10, va="bottom")
ax.text(1.2, -0.9, "x/sqrt(x^2+1)", color=RED, fontsize=10, va="top")
ax.set_title("I = dx/(x^2+a^2)^(3/2), primitive (a = 1)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
