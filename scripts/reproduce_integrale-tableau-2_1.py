"""Reproduit l'integrale de Frullani I = integrale_0^1 (x^b-x^a)/ln x dx (p. integrale-tableau-2).

Fond : par f(t) = integrale_0^1 (e^{bt ln x}-e^{at ln x})/ln x dx,
f'(t) integree donne f(1) = ln|(b+1)/(a+1)|. Reproduction (a = 0.3,
b = 0.7) : integrande sur ]0, 1[ et aire = ln((b+1)/(a+1)).

Style "stylo" : courbe bleue, aire rouge clair, fond quadrille bleu.

Sortie : raw/analyse-integrales/integrale-tableau-2/assets/frullani.png

Usage :
  uv run scripts/reproduce_integrale-tableau-2_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_integrale-tableau-2_1.py
>>> # OK -> .../assets/frullani.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/integrale-tableau-2/assets/frullani.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"
A, B = 0.3, 0.7

xs = np.linspace(0.001, 0.999, 1201)
ys = (xs**B - xs**A) / np.log(xs)

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
ax.text(0.55, 0.28, "aire = ln((b+1)/(a+1))", color=RED, fontsize=11)
ax.set_title("(x^b-x^a)/ln x, a=0.3, b=0.7", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
