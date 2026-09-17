"""Reproduit I = integrale ln(x+1)/(x^2+1) dx via le dilogarithme (p. integrale-tableau-4).

Fond : decomposition en elements simples complexes 1/((x-i)(x+i)) =
a/(x-i) + b/(x+i), changements affines ramenant a Li_2(z) =
-integrale_0^z ln(1-t)/t dt ; resultat en Li_2 et logarithmes complexes.
Reproduction (partie reelle) : integrande ln(x+1)/(x^2+1) sur [0, 3].

Style "stylo" : courbe bleue, aire rouge clair, fond quadrille bleu.

Sortie : raw/analyse-integrales/integrale-tableau-4/assets/dilog-integrande.png

Usage :
  uv run scripts/reproduce_integrale-tableau-4_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_integrale-tableau-4_1.py
>>> # OK -> .../assets/dilog-integrande.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/integrale-tableau-4/assets/dilog-integrande.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

xs = np.linspace(0, 3, 801)
ys = np.log(xs + 1) / (xs**2 + 1)

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
ax.set_title("ln(x+1)/(x^2+1) -> primitive en Li_2", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
