"""Reproduit le fond de integrale-trigo-demi-disque-pi (integrale trigo, encre rouge).

Fond : J = int_{-2}^{2} x^3 cos(x/2) sqrt(4-x^2) dx (=0, impaire)
+ int_{-2}^{2} 1/2 sqrt(4-x^2) dx ; x=2 sin t donne J = pi
(aire d'un demi-disque de rayon 2, divisee par 2).
Reproduction : courbe y = 1/2 sqrt(4-x^2) et aire = pi.
Style "stylo" : courbe bleue, aire rouge hachuree, grille bleue.

Sortie : raw/analyse-integrales/integrale-trigo-demi-disque-pi/assets/integrale-demi-disque.png

Usage :
  uv run scripts/reproduce_integrale-trigo-demi-disque-pi_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/photos-dessins"
    "/integrale-trigo-demi-disque-pi/assets/integrale-demi-disque.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

xs = np.linspace(-2, 2, 400)
ys = 0.5 * np.sqrt(4 - xs**2)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.fill_between(xs, ys, color=RED, alpha=0.25)
ax.plot(xs, ys, color=BLUE, linewidth=1.6)
ax.plot([-2, 2], [0, 0], color=RED, linewidth=1.2)
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-0.2, 1.4)
ax.set_title("1/2 sqrt(4-x2) : aire = pi (demi-disque / 2)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
