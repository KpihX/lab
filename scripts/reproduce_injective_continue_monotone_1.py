"""Reproduit les trois croquis "en toit" de la preuve injective-continue => monotone.

Schemas d'origine (stylo bleu sur papier) : a chaque contradiction par le
theoreme des valeurs intermediaires, l'auteur dessine un "toit" : une valeur
y au sommet, reliee par deux segments a ses deux antecedents x1 et x2 sur
l'axe, avec les valeurs f(a), f(b), f(c), f(d) annotees autour.
  - p.1 : y = (f(b)+f(c))/2 au sommet, x1 dans ]c;d[, x2 dans ]b;c[ ;
    f(a) a gauche, f(b), f(c), f(d) autour.
  - p.2 : variante avec f(c), f(b) au sommet, f(a) et f(d) en bas.
  - p.3 : variante avec f(c) au sommet, f(a) a gauche, f(b) a droite.

Style "stylo" : traits/points bleus, valeur y et titre rouges,
fond quadrille bleu.

Sortie : raw/analyse-fonctions/injective-continue-monotone/assets/croquis-tvi.png

Usage :
  uv run scripts/reproduce_injective_continue_monotone_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_injective_continue_monotone_1.py
>>> # OK -> .../assets/croquis-tvi.png (NNNNN o)
>>> # le rendu montre 3 panneaux "toit" : y relie a x1 et x2 a chaque fois.
"""

import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions"
    "/injective-continue-monotone/assets/croquis-tvi.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
fig.suptitle("Croquis TVI : y et ses deux antecedents x1, x2", color=RED, fontsize=12)

panels = [
    dict(
        title="p.1 : y=(f(b)+f(c))/2",
        top=(0.5, 0.85, "y"),
        feet=[(0.25, "x1"), (0.75, "x2")],
        notes=[(0.05, 0.35, "f(a)"), (0.22, 0.62, "f(b)"), (0.78, 0.62, "f(c)"), (0.95, 0.35, "f(d)")],
    ),
    dict(
        title="p.2 : cas a<c",
        top=(0.5, 0.85, "f(c)"),
        feet=[(0.25, "x1"), (0.75, "x2")],
        notes=[(0.05, 0.2, "f(a)"), (0.9, 0.62, "f(b)"), (0.9, 0.2, "f(d)")],
    ),
    dict(
        title="p.3 : triplet (a,c,b)",
        top=(0.5, 0.85, "f(c)"),
        feet=[(0.3, "x1"), (0.7, "x2")],
        notes=[(0.05, 0.25, "f(a)"), (0.95, 0.25, "f(b)")],
    ),
]


def draw_panel(ax, spec):
    """Dessine un panneau "toit" : sommet y relie aux deux antecedents."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title(spec["title"], color=BLUE, fontsize=10)
    tx, ty, tlabel = spec["top"]
    ax.plot(tx, ty, "o", color=RED, markersize=5)
    ax.text(tx, ty + 0.06, tlabel, color=RED, fontsize=11, ha="center")
    for fx, flabel in spec["feet"]:
        ax.plot([tx, fx], [ty, 0.1], color=BLUE, linewidth=1.2)  # segment y -> xi
        ax.plot(fx, 0.1, "o", color=BLUE, markersize=5)
        ax.text(fx, 0.02, flabel, color=BLUE, fontsize=11, ha="center")
    ax.plot([0.02, 0.98], [0.1, 0.1], color=BLUE, linewidth=1.0)  # axe des antecedents
    for nx, ny, nlabel in spec["notes"]:
        ax.text(nx, ny, nlabel, color=BLUE, fontsize=9, ha="center")


for ax, spec in zip(axes, panels):
    draw_panel(ax, spec)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
