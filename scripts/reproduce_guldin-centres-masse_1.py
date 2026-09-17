"""Reproduit la figure p.1 de guldin-centres-masse : courbe (Cf) et surface de revolution.

Schema d'origine (cahier quadrille, stylo bleu + surlignage) : repere (O, i, j, k)
en bas a gauche, axe (Ox), courbe (Cf) au-dessus de l'axe entre les abscisses
a et b, doublee en pointilles (moitie symetrique suggeree), cotes verticaux
l2/l3 en a et b, aire A1 sous la courbe.

Style "stylo" : courbe bleue, symetrique en pointilles rouges, axes noirs,
fond quadrille bleu.

Sortie : raw/geometrie/guldin-centres-masse/assets/courbe-surface-revolution.png

Usage :
  uv run scripts/reproduce_guldin-centres-masse_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_guldin-centres-masse_1.py
>>> # OK -> .../assets/courbe-surface-revolution.png (XXXXX o)
>>> # le rendu montre l'axe (Ox), la courbe (Cf) entre a et b,
>>> # sa symetrique en pointilles et l'aire A1 hachuree.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/guldin-centres-masse/assets/courbe-surface-revolution.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, INK = "#1a3fb5", "#d31f1f", "black"

fig, ax = plt.subplots(figsize=(7, 4.6))
ax.set_xlim(-0.6, 5.4)
ax.set_ylim(-2.2, 2.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Axe (Ox) et origine O.
ax.annotate("", xy=(5.2, 0), xytext=(-0.5, 0),
            arrowprops=dict(arrowstyle="->", color=INK, linewidth=1.4))
ax.text(5.25, 0.08, "(Ox)", color=INK, fontsize=11)
ax.text(-0.35, -0.3, "O", color=INK, fontsize=12)

# Petits vecteurs i, j du repere en bas a gauche.
ax.annotate("", xy=(-0.1, -0.9), xytext=(-0.4, -1.5),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2))
ax.text(-0.05, -1.0, "i", color=BLUE, fontsize=11)
ax.annotate("", xy=(0.35, -1.2), xytext=(-0.4, -1.5),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2))
ax.text(0.42, -1.25, "k", color=BLUE, fontsize=11)

# Courbe (Cf) entre a=1 et b=4, strictement au-dessus de (Ox).
xs = np.linspace(1.0, 4.0, 200)
f = 1.1 + 0.35 * np.sin(1.6 * (xs - 1.0)) + 0.12 * (xs - 1.0)
ax.plot(xs, f, color=BLUE, linewidth=2.0)
ax.text(3.1, 1.95, "(Cf)", color=BLUE, fontsize=13)

# Moitie symetrique suggeree (pointilles) : l'autre moitie de la surface.
ax.plot(xs, -f, color=RED, linewidth=1.4, linestyle=(0, (4, 3)))
ax.plot([1.0, 1.0], [-f[0], f[0]], color=BLUE, linewidth=1.4)
ax.plot([4.0, 4.0], [-f[-1], f[-1]], color=BLUE, linewidth=1.4)

# Cotes verticaux l2 (en a) et l3 (en b), abscisses a et b.
ax.plot([1.0, 1.0], [0, f[0]], color=BLUE, linewidth=1.2, linestyle="--")
ax.plot([4.0, 4.0], [0, f[-1]], color=BLUE, linewidth=1.2, linestyle="--")
ax.text(0.92, -0.35, "a", color=INK, fontsize=12)
ax.text(3.95, -0.35, "b", color=INK, fontsize=12)
ax.text(0.55, 0.75, "l2", color=BLUE, fontsize=11)
ax.text(4.15, 0.85, "l3", color=BLUE, fontsize=11)

# Aire A1 sous la courbe (hachures).
ax.fill_between(xs, 0, f, color=BLUE, alpha=0.10)
ax.text(2.3, 0.55, "A1", color=BLUE, fontsize=12)
ax.text(2.3, -1.35, "A4", color=RED, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
