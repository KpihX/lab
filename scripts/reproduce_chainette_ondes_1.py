"""Reproduit la figure p.1 de chainette-ondes : la chainette et ses tensions.

Figure d'origine (manuscrite) : courbe de la chainette y = f(x) suspendue
entre deux supports, approche par subdivision en dx ("1ere approche"),
zoom sur un fragment du milieu avec les tensions -T(x), T(x+dx) et le
poids elementaire.

Style "stylo" : courbe et fragments bleus, tensions et cotes rouges,
fond quadrille bleu.

Sortie : raw/physique/chainette-ondes/assets/chainette-tensions.png

Usage :
  uv run scripts/reproduce_chainette_ondes_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_chainette_ondes_1.py
>>> # OK -> .../assets/chainette-tensions.png (XXXXX o)
>>> # le rendu montre la chainette, un fragment dx et les tensions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/chainette-ondes/assets/chainette-tensions.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, axes = plt.subplots(2, 1, figsize=(9, 6))
for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 3.5)
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

x = np.linspace(0.5, 9.5, 400)
a, x0 = 1.1, 5.0
y = a * (np.cosh((x - x0) / a) - 1) * 0.55 + 0.2

# Haut : la chainette entre deux supports.
axes[0].plot(x, y, color=BLUE, linewidth=1.8)
axes[0].plot([0.5, 0.5], [y[0], 3.2], color=BLUE, linewidth=1.2)
axes[0].plot([9.5, 9.5], [y[-1], 3.2], color=BLUE, linewidth=1.2)
axes[0].text(4.4, 0.05, "y = f(x) ?", color=RED, fontsize=12)
axes[0].text(4.0, 3.0, "1ere approche", color=BLUE, fontsize=12)

# Bas : zoom sur le fragment du milieu (dx) et ses tensions.
xm = np.linspace(4.0, 6.0, 100)
ym = a * (np.cosh((xm - x0) / a) - 1) * 0.55 + 0.2
axes[1].plot(xm, ym, color=BLUE, linewidth=2.0)
axes[1].annotate("", xy=(3.6, 0.75), xytext=(4.1, 0.45),
                 arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4))
axes[1].annotate("", xy=(6.4, 0.75), xytext=(5.9, 0.45),
                 arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4))
axes[1].annotate("", xy=(5.0, 0.1), xytext=(5.0, 0.4),
                 arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4))
axes[1].text(3.0, 0.8, "-T(x)", color=RED, fontsize=12)
axes[1].text(6.5, 0.8, "T(x+dx)", color=RED, fontsize=12)
axes[1].text(5.15, 0.05, "dP", color=RED, fontsize=12)
axes[1].annotate("", xy=(6.0, 1.3), xytext=(4.0, 1.3),
                 arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.2))
axes[1].text(4.85, 1.4, "dx", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
