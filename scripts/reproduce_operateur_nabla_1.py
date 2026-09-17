"""Reproduit la figure p.1 de operateur-nabla : gradient et deplacement M -> M''.

Croquis d'origine (stylo bleu) : point M avec vecteur deplacement dOM
vers M'' (et M' en variante), et vecteur gradient grad phi(M) ; le texte
precise que plus dOM s'eloigne du gradient, plus dphi(M) est faible.

Style "stylo" : vecteurs bleus, gradient et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/physique/operateur-nabla/assets/gradient-deplacement.png

Usage :
  uv run scripts/reproduce_operateur_nabla_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_operateur_nabla_1.py
>>> # OK -> .../assets/gradient-deplacement.png (XXXXX o)
>>> # le rendu montre M, dOM, M'' et le gradient de phi en M.
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/operateur-nabla/assets/gradient-deplacement.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-0.5, 5.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Point M et deplacement vers M''.
ax.plot(1, 1, "o", color=BLUE, markersize=6)
ax.text(0.7, 0.6, "M", color=BLUE, fontsize=13)
ax.annotate("", xy=(4.2, 2.2), xytext=(1, 1),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.6))
ax.text(4.3, 2.2, "M''", color=BLUE, fontsize=13)
ax.text(2.4, 1.1, "dOM", color=BLUE, fontsize=12)

# Variante M' (deplacement proche du gradient).
ax.annotate("", xy=(3.0, 3.4), xytext=(1, 1),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2,
                            linestyle=(0, (4, 3))))
ax.text(3.1, 3.5, "M'", color=BLUE, fontsize=12)

# Gradient en M.
ax.annotate("", xy=(2.6, 3.2), xytext=(1, 1),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=2.0))
ax.text(1.5, 2.6, "grad phi(M)", color=RED, fontsize=12)
ax.text(0.6, 4.3, "phi(M)", color=BLUE, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
