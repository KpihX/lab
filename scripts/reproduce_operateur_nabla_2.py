"""Reproduit la figure p.1 de operateur-nabla : isothermes et gradient thermique.

Croquis d'origine (stylo bleu) : point M entoure d'isothermes cotees
(environ 274 K, 277 K, 294 K) avec le vecteur gradient de T en M pointant
vers les temperatures croissantes.

Style "stylo" : isothermes bleues, gradient et cotes rouges,
fond quadrille bleu.

Sortie : raw/physique/operateur-nabla/assets/isothermes-gradient.png

Usage :
  uv run scripts/reproduce_operateur_nabla_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_operateur_nabla_2.py
>>> # OK -> .../assets/isothermes-gradient.png (XXXXX o)
>>> # le rendu montre M, trois isothermes et le gradient de T.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/operateur-nabla/assets/isothermes-gradient.png"
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

# Trois isothermes concentriques autour de M.
for w, h, temp in [(4.6, 3.8, "274 K"), (3.4, 2.8, "277 K"), (2.2, 1.8, "294 K")]:
    ax.add_patch(Ellipse((2.5, 2.5), w, h, fill=False, edgecolor=BLUE,
                         linewidth=1.4))
    ax.text(2.5 + w / 2 + 0.1, 2.5, temp, color=RED, fontsize=11)

# Point M et gradient vers les temperatures croissantes.
ax.plot(2.5, 2.5, "o", color=BLUE, markersize=6)
ax.text(2.2, 2.1, "M", color=BLUE, fontsize=13)
ax.annotate("", xy=(4.6, 4.4), xytext=(2.5, 2.5),
            arrowprops=dict(arrowstyle="->", color=RED, linewidth=2.0))
ax.text(3.9, 4.5, "grad T(M)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
