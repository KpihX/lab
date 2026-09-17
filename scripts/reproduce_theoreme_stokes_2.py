"""Reproduit le petit schema d'orientation p.2 de theoreme-stokes.

Croquis d'origine (stylo, bas-droite p.2) : petit contour ferme
(cercle/carre) fleche illustrant le sens d'orientation du contour (C).

Style "stylo" : contour bleu, fleches de sens rouges, fond quadrille bleu.

Sortie : raw/physique/theoreme-stokes/assets/orientation-contour-stokes.png

Usage :
  uv run scripts/reproduce_theoreme_stokes_2.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/theoreme-stokes/assets/orientation-contour-stokes.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)
ax.set_aspect("equal")
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Petit contour ferme (cercle) = contour (C) vu de pres.
t = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.cos(t), np.sin(t), color=BLUE, linewidth=2.0)

# Fleches de sens (orientation directe).
for ang in (45, 135, 225, 315):
    a = np.deg2rad(ang)
    x, y = np.cos(a), np.sin(a)
    tx, ty = -np.sin(a), np.cos(a)  # tangente directe
    ax.annotate(
        "",
        xy=(x + 0.28 * tx, y + 0.28 * ty),
        xytext=(x - 0.28 * tx, y - 0.28 * ty),
        arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.8),
    )

ax.text(1.15, -0.15, "(C)", color=BLUE, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
