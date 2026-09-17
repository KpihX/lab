"""Reproduit l'integrale du nombre d'or (p. integrale-or-tableau).

Fond : I = integrale de 1/(1+x^phi)^phi dx, phi = (1+sqrt(5))/2, avec
en particulier integrale de 0 a +infini = 1. Reproduction : courbe de
l'integrande sur [0, 3] et aire sous la courbe (= 1) hachuree.

Style "stylo" : courbe bleue, aire rouge clair, fond quadrille bleu.

Sortie : raw/analyse-integrales/integrale-or-tableau/assets/integrande-or.png

Usage :
  uv run scripts/reproduce_integrale-or-tableau_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_integrale-or-tableau_1.py
>>> # OK -> .../assets/integrande-or.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/integrale-or-tableau/assets/integrande-or.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"
PHI = (1 + np.sqrt(5)) / 2  # nombre d'or

xs = np.linspace(0, 3, 801)
ys = 1.0 / (1.0 + xs**PHI) ** PHI

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.axvline(0, color=BLUE, linewidth=1.0)
ax.fill_between(xs, ys, color=RED, alpha=0.25)
ax.plot(xs, ys, color=BLUE, linewidth=1.6)
ax.text(0.15, 0.75, "aire 0..inf = 1", color=RED, fontsize=11)
ax.set_title("1/(1+x^phi)^phi, phi = (1+sqrt(5))/2", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
