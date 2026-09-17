"""Reproduit I = integrale_0^{pi/2} ln cos x ln sin x / tan x dx = zeta(3)/8 (p. integrale-zeta3).

Fond : t = sin x, developpement -ln(1-t^2)/2 = somme t^{2k}/(2k),
integration par parties terme a terme -> 1/8 somme 1/k^3 = zeta(3)/8.
Reproduction : integrande sur ]0, pi/2[ et aire hachuree (= zeta(3)/8).

Style "stylo" : courbe bleue, aire rouge clair, fond quadrille bleu.

Sortie : raw/analyse-integrales/integrale-zeta3/assets/integrande-zeta3.png

Usage :
  uv run scripts/reproduce_integrale-zeta3_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_integrale-zeta3_1.py
>>> # OK -> .../assets/integrande-zeta3.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/integrale-zeta3/assets/integrande-zeta3.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

xs = np.linspace(0.02, np.pi / 2 - 0.02, 1201)
ys = np.log(np.cos(xs)) * np.log(np.sin(xs)) / np.tan(xs)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.fill_between(xs, ys, color=RED, alpha=0.25)
ax.plot(xs, ys, color=BLUE, linewidth=1.6)
ax.text(0.9, 0.35, "aire = zeta(3)/8", color=RED, fontsize=11)
ax.set_title("ln cos x ln sin x / tan x sur [0, pi/2]", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
