"""Reproduit la figure p.10 du 3e Bloc-Notes : demi-cercles emboites (paradoxe pi = 2).

Schema d'origine (crayon gris + rouge sur quadrille) : un grand
demi-cercle de diametre [O, I] (O marque, "1" rouge au milieu), a
l'interieur 2 moyens demi-cercles, puis 3 petits, puis 4 minuscules.
A chaque etape la longueur totale vaut pi ; a l'infini les arcs se
confondent avec le diametre, d'ou "2 = pi".

Style "stylo" : arcs gris (crayon), diametre et labels bleus, "1" et O rouges,
fond quadrille bleu.

Sortie : raw/bloc-notes/troisieme-bloc-notes/assets/demicercles-pi2.png

Usage :
  uv run scripts/reproduce_demicercles_pi2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_demicercles_pi2.py
>>> # OK -> .../assets/demicercles-pi2.png (48312 o)
>>> # le rendu montre 1 grand + 2 moyens + 3 petits + 4 minuscules arcs sur [O, I].
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/troisieme-bloc-notes/assets/demicercles-pi2.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, GRAY = "#1a3fb5", "red", "gray"

fig, ax = plt.subplots(figsize=(7, 4))
ax.set_aspect("equal")
ax.set_xlim(-0.3, 4.3)
ax.set_ylim(-0.4, 2.3)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.plot([0, 4], [0, 0], color=BLUE, linewidth=1.5)  # diametre [O, I]
theta = np.linspace(0, np.pi, 200)
for n in (1, 2, 3, 4):  # 1 grand, 2 moyens, 3 petits, 4 minuscules
    r = 2.0 / n
    for k in range(n):
        cx = r + 2 * k * r
        ax.plot(cx + r * np.cos(theta), r * np.sin(theta), color=GRAY, linewidth=1.2)

ax.plot(0, 0, "o", color=RED)
ax.text(-0.12, -0.25, "O", color=RED, fontsize=13)
ax.text(2.0, -0.25, "1", color=RED, fontsize=13)  # "1" rouge au milieu
ax.text(4.0, -0.25, "I", color=BLUE, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
