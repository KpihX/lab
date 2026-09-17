"""Reproduit le schema type p.1 de couplage-masse-ressort : chaine verticale O - k1 - m1 - k2 - m2.

Planche d'origine (imprimee p.1, reprise stylo pp.2-7) : point fixe O en haut,
axe vertical descendant, ressort k1, masse m1 (rectangle, repere O1, fleche y1),
ressort k2, masse m2 (rectangle, repere O2, fleche y2).
Reproduction synthetique en un seul axe.

Style "stylo" : ressorts et masses bleus, axes et etiquettes rouges,
fond quadrille bleu.

Sortie : raw/physique/couplage-masse-ressort/assets/couplage-masse-ressort_fig1.png

Usage :
  uv run scripts/reproduce_couplage-masse-ressort_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_couplage-masse-ressort_1.py
>>> # OK -> .../assets/couplage-masse-ressort_fig1.png (XXXXX o)
>>> # le rendu montre la chaine O, k1, m1 (O1/y1), k2, m2 (O2/y2).
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/couplage-masse-ressort/assets/couplage-masse-ressort_fig1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(4.5, 7))
ax.set_aspect("equal")
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)


def spring(ax, x, y_top, y_bot, width=1.6, n=8):
    """Dessine un ressort vertical en zigzag entre y_top et y_bot."""
    xs, ys = [x], [y_top]
    span = y_top - y_bot
    for i in range(1, 2 * n):
        xs.append(x + width / 2 * (1 if i % 2 else -1))
        ys.append(y_top - span * i / (2 * n))
    xs.append(x)
    ys.append(y_bot)
    ax.plot(xs, ys, color=BLUE, linewidth=1.6)


def mass(ax, x, y, w=2.4, h=1.0, label=""):
    """Dessine une masse rectangulaire centree en x, base en y."""
    ax.add_patch(
        Rectangle((x - w / 2, y), w, h, fill=False, edgecolor=BLUE, linewidth=1.8)
    )
    ax.text(x, y + h / 2, label, color=BLUE, fontsize=12, ha="center", va="center")


def axis_y(ax, x, y_top, y_bot, label=""):
    """Dessine un axe vertical descendant rouge avec son etiquette."""
    ax.annotate(
        "",
        xy=(x, y_bot),
        xytext=(x, y_top),
        arrowprops=dict(arrowstyle="->", color=RED, linewidth=1.4),
    )
    ax.text(x + 0.35, (y_top + y_bot) / 2, label, color=RED, fontsize=12, va="center")


# Support fixe O.
ax.plot([3.2, 6.8], [19.2, 19.2], color=BLUE, linewidth=2.2)
for i in range(4):
    ax.plot([3.6 + i * 0.8, 3.6 + i * 0.8], [19.2, 19.6], color=BLUE, linewidth=1.2)
ax.text(5.0, 18.6, "O", color=RED, fontsize=13, ha="right", va="center")

# Chaine : k1, m1, k2, m2.
spring(ax, 5.0, 19.2, 15.2)
ax.text(3.4, 17.2, "k1", color=BLUE, fontsize=12, ha="center")
mass(ax, 5.0, 14.2, label="m1")
ax.text(3.4, 14.7, "m1", color=BLUE, fontsize=12, ha="center")
spring(ax, 5.0, 14.2, 10.2)
ax.text(3.4, 12.2, "k2", color=BLUE, fontsize=12, ha="center")
mass(ax, 5.0, 9.2, label="m2")
ax.text(3.4, 9.7, "m2", color=BLUE, fontsize=12, ha="center")

# Axes y1 (origine O1) et y2 (origine O2) : deux fleches distinctes.
ax.text(5.0, 15.6, "O1", color=RED, fontsize=11, ha="left", va="center")
axis_y(ax, 6.8, 15.6, 12.0, "y1")
ax.text(5.0, 10.6, "O2", color=RED, fontsize=11, ha="left", va="center")
axis_y(ax, 6.8, 10.6, 6.5, "y2")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
