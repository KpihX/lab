"""Reproduit la figure p.3 de chainette-ondes : corde et onde mecanique.

Figure d'origine (manuscrite) : corde tendue entre deux masses, egartee
de sa position de repos par une perturbation (bosse sinusoidale) ;
droite "du repos" sous la corde ; zoom sur un fragment du milieu avec
les tensions et le poids elementaire dP(x).

Style "stylo" : corde et onde bleues, repos et annotations rouges,
fond quadrille bleu.

Sortie : raw/physique/chainette-ondes/assets/corde-onde.png

Usage :
  uv run scripts/reproduce_chainette_ondes_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_chainette_ondes_2.py
>>> # OK -> .../assets/corde-onde.png (XXXXX o)
>>> # le rendu montre la corde perturbee, la droite de repos et le zoom.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/chainette-ondes/assets/corde-onde.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, axes = plt.subplots(2, 1, figsize=(9, 6))
for ax in axes:
    ax.set_xlim(0, 10)
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
axes[0].set_ylim(-1.5, 2.5)
axes[1].set_ylim(-0.5, 2.5)

x = np.linspace(0.5, 9.5, 500)

# Haut : corde perturbee entre deux masses + droite de repos.
axes[0].plot(x, 0.9 * np.sin(2 * np.pi * (x - 0.5) / 3.0)
             * np.exp(-((x - 3.0) / 4.0) ** 2) + 1.0,
             color=BLUE, linewidth=1.8)
axes[0].plot([0.5, 0.5], [-1.0, 2.2], color=BLUE, linewidth=2.2)
axes[0].plot([9.5, 9.5], [-1.0, 2.2], color=BLUE, linewidth=2.2)
axes[0].plot([0.3, 0.7], [-1.0, -1.0], color=BLUE, linewidth=2.2)
axes[0].plot([9.3, 9.7], [-1.0, -1.0], color=BLUE, linewidth=2.2)
axes[0].plot([0.5, 9.5], [-0.5, -0.5], color=RED, linewidth=1.2,
             linestyle=(0, (4, 3)))
axes[0].text(4.3, -1.2, "du repos", color=RED, fontsize=12)

# Bas : zoom sur le fragment du milieu.
xm = np.linspace(4.0, 6.0, 200)
ym = 0.9 * np.sin(2 * np.pi * (xm - 0.5) / 3.0) + 1.0
axes[1].plot(xm, ym, color=BLUE, linewidth=2.0)
axes[1].annotate("", xy=(3.7, 1.9), xytext=(4.15, 1.55),
                 arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4))
axes[1].annotate("", xy=(6.3, 1.9), xytext=(5.85, 1.55),
                 arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4))
axes[1].annotate("", xy=(5.0, 0.6), xytext=(5.0, 1.1),
                 arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4))
axes[1].text(3.0, 2.0, "T(x)", color=RED, fontsize=12)
axes[1].text(6.4, 2.0, "T(x+dx)", color=RED, fontsize=12)
axes[1].text(5.15, 0.5, "dP(x)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
