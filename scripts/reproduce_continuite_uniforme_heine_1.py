"""Reproduit la figure p.1 de continuite-uniforme-heine : fonction palier.

Schema d'origine (stylo bleu sur papier) : petit repere avec les
graduations -1, 0, 1 en abscisse et 1 en ordonnee ; palier y = 0
a gauche de 0 (cercle ouvert en 0), palier y = 1 a droite de 0,
discontinuite en 0 (saut de 1 > epsilon = 0,5).

Style "stylo" : paliers et axes bleus, annotations et points
ouverts/fermes rouges, fond quadrille bleu.

Sortie : raw/analyse-fonctions/continuite-uniforme-heine/assets/palier-0-1.png

Usage :
  uv run scripts/reproduce_continuite_uniforme_heine_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_continuite_uniforme_heine_1.py
>>> # OK -> .../assets/palier-0-1.png (XXXXX o)
>>> # le rendu montre deux paliers (0 a gauche, 1 a droite) avec
>>> # un cercle ouvert en (0,0) et un point plein en (0,1).
"""

import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions/continuite-uniforme-heine/assets/palier-0-1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-0.4, 1.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Axes du repere.
ax.axhline(0, color=BLUE, linewidth=1.2)
ax.axvline(0, color=BLUE, linewidth=1.2)

# Paliers : y = 0 sur ]-1, 0[, y = 1 sur ]0, 1].
ax.plot([-1, 0], [0, 0], color=BLUE, linewidth=1.8)
ax.plot([0, 1], [1, 1], color=BLUE, linewidth=1.8)

# Discontinuite en 0 : cercle ouvert en (0,0), point plein en (0,1).
ax.plot(0, 0, "o", color=BLUE, markersize=8, markerfacecolor="white", markeredgewidth=1.8)
ax.plot(0, 1, "o", color=BLUE, markersize=6)

# Graduations annotees en rouge.
for x, dx in [(-1, -0.08), (0, 0.03), (1, 0.02)]:
    ax.text(x + dx, -0.14, f"{x}", color=RED, fontsize=12)
ax.text(0.05, 1.02, "1", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
