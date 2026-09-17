"""Reproduit la figure p.136 (haut) de quatrieme-bloc-notes : chainette et sol.

Figure d'origine (manuscrite) : repere orthonorme (O, i, j) au point le
plus bas O de la corde, courbe (C) en U (cosh), deux montants verticaux
de hauteur H, sol horizontal hachure en bas.

Style "stylo" : courbe, montants et sol bleus, annotations rouges, fond
quadrille bleu.

Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/chainette-sol.png

Usage :
  uv run scripts/reproduce_chainette_sol.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/chainette-sol.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_xlim(-5, 5)
ax.set_ylim(-2.5, 5.2)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

a, D = 0.5, 6.0
x = np.linspace(-D / 2, D / 2, 400)
y = 1.0 / a * (np.cosh(a * x) - 1.0)
Htop = float(y.max()) + 1.6
sol = -1.5

ax.plot(x, y, color=BLUE, linewidth=1.8)
# Montants verticaux.
for xe in (-D / 2, D / 2):
    ye = 1.0 / a * (np.cosh(a * xe) - 1.0)
    ax.plot([xe, xe], [ye, Htop], color=BLUE, linewidth=1.4)
    ax.plot(xe, ye, "o", color=BLUE, markersize=5)
# Sol hachure.
ax.plot([-5, 5], [sol, sol], color=BLUE, linewidth=1.6)
for xh in np.arange(-4.8, 5.0, 0.4):
    ax.plot([xh, xh - 0.25], [sol, sol - 0.3], color=BLUE, linewidth=1.0)

# Repere (O, i, j) au point le plus bas.
ax.annotate("", xy=(1.2, 0.0), xytext=(0.0, 0.0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.annotate("", xy=(0.0, 1.2), xytext=(0.0, 0.0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.plot(0.0, 0.0, "o", color=BLUE, markersize=5)
ax.text(0.1, -0.55, "O", color=RED, fontsize=13)
ax.text(1.3, -0.15, "i", color=RED, fontsize=13)
ax.text(0.15, 1.15, "j", color=RED, fontsize=13)

# Cote H sur le montant droit + labels.
ax.annotate("", xy=(D / 2, Htop), xytext=(D / 2, sol),
            arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.2))
ax.text(D / 2 + 0.25, (Htop + sol) / 2, "H", color=RED, fontsize=14)
ax.text(-2.2, 1.9, "(C)", color=RED, fontsize=14)
ax.text(3.6, sol + 0.15, "sol", color=RED, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
