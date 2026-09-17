"""Reproduit la figure p.1 de chemin-evitant-q2 : carre unite et chemin [O,B]U[B,A].

Schema d'origine (stylo bleu sur papier) : le carre D = [0,1]x[0,1]
avec O = (0,0) en bas a gauche et A = (1,1) en haut a droite ;
la diagonale (Delta) = [O,A] ; le point B = (1/sqrt(2), 1-1/sqrt(2))
a l'interieur, sous la diagonale ; les segments [O,B] et [B,A]
forment le chemin continu evitant Q^2.

Style "stylo" : carre et segments bleus, annotations O, A, B
rouges, fond quadrille bleu. La droite d'essai (Delta) n'est pas
reproduite (pente a non fixee) ; aucune diagonale sur le source
(corrige 2026-09-07 apres relecture p.1 a r=150).

Sortie : raw/ensembles-cardinaux/chemin-evitant-q2/assets/chemin-ob-ba.png

Usage :
  uv run scripts/reproduce_chemin_evitant_q2_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_chemin_evitant_q2_1.py
>>> # OK -> .../assets/chemin-ob-ba.png (XXXXX o)
>>> # le rendu montre le carre, O en bas a gauche, A en haut a droite,
>>> # B sous la diagonale, et le chemin brise [O,B]U[B,A] en bleu.
"""

import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/ensembles-cardinaux/chemin-evitant-q2/assets/chemin-ob-ba.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

Bx, By = 1 / 2**0.5, 1 - 1 / 2**0.5  # B = (1/sqrt(2), 1-1/sqrt(2))

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-0.12, 1.18)
ax.set_ylim(-0.15, 1.18)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Carre D = [0,1]x[0,1].
for (x1, y1, x2, y2) in [(0, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 1), (0, 1, 0, 0)]:
    ax.plot([x1, x2], [y1, y2], color=BLUE, linewidth=1.5)

# Chemin [O,B] U [B,A] en bleu.
ax.plot([0, Bx], [0, By], color=BLUE, linewidth=1.8)
ax.plot([Bx, 1], [By, 1], color=BLUE, linewidth=1.8)

# Points et etiquettes.
for name, x, y, dx, dy in [("O", 0, 0, -0.07, -0.07), ("A", 1, 1, 0.03, 0.02), ("B", Bx, By, 0.03, 0.02)]:
    ax.plot(x, y, "o", color=BLUE, markersize=5)
    ax.text(x + dx, y + dy, name, color=RED, fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
