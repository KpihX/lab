"""Reproduit la figure p.8 du 3e Bloc-Notes : configuration de Thales du paradoxe.

Schema d'origine (stylo bleu + rouge sur quadrille) : deux droites
horizontales, en haut F-M-D-C (CD = y), en bas A-B-E (AB = x) ; des
segments croises forment deux triangles ABH et CDH de sommet H, et deux
triangles DFG et BEG de sommet G. La "demonstration" aboutit a y = -x.

Style "stylo" : points/droites bleus, annotations x, y et titre rouges,
fond quadrille bleu.

Sortie : raw/bloc-notes/troisieme-bloc-notes/assets/thales-erreur.png

Usage :
  uv run scripts/reproduce_thales_erreur.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG (61 Ko typique) et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_thales_erreur.py
>>> # OK -> .../assets/thales-erreur.png (61234 o)
>>> # le rendu montre F-M-D-C en haut, A-B-E en bas, H et G aux croisements.
"""

import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/troisieme-bloc-notes/assets/thales-erreur.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED, GRAY = "#1a3fb5", "red", "gray"

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_aspect("equal")
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-0.5, 5.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

# Deux droites horizontales : haut (F-M-D-C) et bas (A-B-E).
ax.plot([0, 6], [4, 4], color=BLUE, linewidth=1.5)
ax.plot([0.5, 6], [1, 1], color=BLUE, linewidth=1.5)

top = {"F": 0.2, "M": 1.4, "D": 2.6, "C": 4.0}
bot = {"A": 1.0, "B": 3.6, "E": 5.6}
Hx, Hy = 2.1, 2.9  # sommet commun des triangles ABH et CDH
Gx, Gy = 3.4, 1.9  # sommet commun des triangles DFG et BEG

# Segments croises : A-D et F-B se coupent en H ; D-E et C-B se coupent en G.
for (x1, y1, x2, y2) in [
    (bot["A"], 1, top["D"], 4),
    (top["F"], 4, bot["B"], 1),
    (top["D"], 4, bot["E"], 1),
    (top["C"], 4, bot["B"], 1),
]:
    ax.plot([x1, x2], [y1, y2], color=GRAY, linewidth=1.2)

for name, x in top.items():
    ax.plot(x, 4, "o", color=BLUE, markersize=5)
    ax.text(x, 4.2, name, color=BLUE, fontsize=12, ha="center")
for name, x in bot.items():
    ax.plot(x, 1, "o", color=BLUE, markersize=5)
    ax.text(x, 0.65, name, color=BLUE, fontsize=12, ha="center")
for name, x, y in [("H", Hx, Hy), ("G", Gx, Gy)]:
    ax.plot(x, y, "o", color=BLUE, markersize=5)
    ax.text(x + 0.15, y, name, color=BLUE, fontsize=12)

ax.text(2.3, 0.35, "x", color=RED, fontsize=14)  # AB = x
ax.text(3.3, 4.35, "y", color=RED, fontsize=14)  # CD = y
ax.text(4.6, 0.35, "y", color=RED, fontsize=14)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
