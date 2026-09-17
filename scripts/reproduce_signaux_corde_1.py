"""Reproduit la figure p.1 de signaux-corde : perturbation a deux dates.

Figure d'origine (imprimee) : corde horizontale photographiee a
t = 0,10 s (bosse a gauche) et a t = 0,20 s (bosse decalee a droite) ;
l'ecart entre les deux positions est cote 1,0 m (pointilles verticaux).

Style "stylo" : corde et bosses bleues, cotes rouges,
fond quadrille bleu.

Sortie : raw/physique/signaux-corde/assets/corde-deux-dates.png

Usage :
  uv run scripts/reproduce_signaux_corde_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_signaux_corde_1.py
>>> # OK -> .../assets/corde-deux-dates.png (XXXXX o)
>>> # le rendu montre la corde aux deux dates et la cote 1,0 m.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/signaux-corde/assets/corde-deux-dates.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, axes = plt.subplots(2, 1, figsize=(9, 4.5), sharex=True)
for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.6, 1.6)
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

x = np.linspace(0, 10, 600)


def bump(xc, w=0.7, h=0.8):
    """Bosse gaussienne centree en xc."""
    return h * np.exp(-((x - xc) / w) ** 2)


# t = 0,10 s : bosse a gauche.
axes[0].plot(x, bump(2.0), color=BLUE, linewidth=1.8)
axes[0].text(0.15, 0.9, "t = 0,10 s", color=BLUE, fontsize=12)
axes[0].plot([2.0, 2.0], [-0.6, 1.6], color=RED, linewidth=1.0,
             linestyle=(0, (4, 3)))

# t = 0,20 s : bosse decalee a droite.
axes[1].plot(x, bump(7.0), color=BLUE, linewidth=1.8)
axes[1].text(0.15, 0.9, "t = 0,20 s", color=BLUE, fontsize=12)
axes[1].plot([7.0, 7.0], [-0.6, 1.6], color=RED, linewidth=1.0,
             linestyle=(0, (4, 3)))
axes[1].plot([2.0, 2.0], [-0.6, 1.6], color=RED, linewidth=1.0,
             linestyle=(0, (4, 3)))

# Cote 1,0 m entre les deux positions.
axes[1].annotate("", xy=(7.0, 1.3), xytext=(2.0, 1.3),
                 arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.4))
axes[1].text(4.5, 1.35, "1,0 m", color=RED, fontsize=12, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
