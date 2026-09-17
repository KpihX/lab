"""Reproduit l = lim_{x->0} |sin x|^{cos x}/x = 1 (p. limite-tableau-2).

Fond : |sin x|/x x |sin x|^{cos x - 1} = 1 x e^{(cos x-1)/x x
x/|sin x| x |sin x| ln|sin x|} -> e^{0x1x0} = 1, car |sin x| -> 0 et
lim_{y->0} y ln y = 0. Reproduction : courbe des deux cotes de 0 et
droite limite y = 1.

Style "stylo" : courbe bleue, limite rouge, fond quadrille bleu.

Sortie : raw/analyse-fonctions/limite-tableau-2/assets/limite-sincos.png

Usage :
  uv run scripts/reproduce_limite-tableau-2_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_limite-tableau-2_1.py
>>> # OK -> .../assets/limite-sincos.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/limite-tableau-2/assets/limite-sincos.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

xg = np.linspace(-1, -0.01, 600)
xd = np.linspace(0.01, 1, 600)


def f(x):
    """|sin x|^{cos x} / x."""
    return np.abs(np.sin(x)) ** np.cos(x) / x


fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.axvline(0, color=BLUE, linewidth=1.0)
ax.axhline(1, color=RED, linewidth=1.2, linestyle="--")
ax.plot(xg, f(xg), color=BLUE, linewidth=1.6)
ax.plot(xd, f(xd), color=BLUE, linewidth=1.6)
ax.set_title("l = lim |sin x|^cos x / x = 1", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
