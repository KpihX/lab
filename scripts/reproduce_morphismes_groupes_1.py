"""Reproduit le schéma de démonstration p.2 du manuscrit morphismes-groupes.

Manuscrit d'origine (morphismes-groupes.pdf, p.2, encre bleue) :
"Schéma de démonstration" avec 4 énoncés encerclés : ③ en haut,
① ⟹ ② au milieu (double flèche horizontale), ④ en bas. Flèches
relevées sur le scan : ③ → ① (simple, descend gauche), ② ⟹ ③
(double, monte à gauche), ① ⟹ ② (double, horizontale), ② ⟹ ④
(double, descend à droite), ④ ⟹ ① (double, monte à gauche).
Ici : mêmes 4 noeuds + 5 implications, sens et simple/double
conservés tels que tracés.

Sortie : raw/algebre-arithmetique/morphismes-groupes/assets/triangle-implications.png

Usage :
  uv run scripts/reproduce_morphismes_groupes_1.py  (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/morphismes-groupes/assets/triangle-implications.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLEU = "#1e40af"
BLEU_CLAIR = "#dbe4ff"
ROUGE = "#c81e1e"
QUADRILLE = "#9db3d8"

# Positions : ③ haut, ①/② milieu, ④ bas (comme le croquis).
POS = {"3": (0.0, 2.0), "1": (-1.2, 0.6), "2": (1.2, 0.6), "4": (0.0, -1.2)}
# (départ, arrivée, double?) — relevé fidèle du scan (zoom p.2).
FLECHES = [
    ("3", "1", False),  # ③ → ① : simple
    ("2", "3", True),  # ② ⟹ ③ : double
    ("1", "2", True),  # ① ⟹ ② : double horizontale
    ("2", "4", True),  # ② ⟹ ④ : double
    ("4", "1", True),  # ④ ⟹ ① : double verticale
]

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.2, 2.9)
ax.grid(True, color=QUADRILLE, linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.set_xticks(range(-2, 3))
ax.set_yticks(range(-2, 3))
ax.tick_params(labelbottom=False, labelleft=False, length=0, color=QUADRILLE)
for spine in ax.spines.values():
    spine.set_visible(False)

R = 0.30
for k, (x, y) in POS.items():
    ax.add_patch(Circle((x, y), R, facecolor=BLEU_CLAIR, edgecolor=BLEU, linewidth=2.0, zorder=3))
    ax.text(x, y, k, color=BLEU, fontsize=18, fontweight="bold",
            ha="center", va="center", zorder=4)

for a, b, double in FLECHES:
    x1, y1 = POS[a]
    x2, y2 = POS[b]
    # Raccourcit aux bords des cercles pour ne pas les traverser.
    dx, dy = x2 - x1, y2 - y1
    d = (dx**2 + dy**2) ** 0.5
    ux, uy = dx / d, dy / d
    p1 = (x1 + ux * (R + 0.05), y1 + uy * (R + 0.05))
    p2 = (x2 - ux * (R + 0.10), y2 - uy * (R + 0.10))
    style = "=> " if double else "->"
    # Simple = une flèche ; double (⟹) = deux flèches parallèles, comme tracé.
    offsets = (0.055, -0.055) if double else (0.0,)
    for off in offsets:
        ox, oy = -uy * off, ux * off
        ax.add_patch(FancyArrowPatch(
            (p1[0] + ox, p1[1] + oy), (p2[0] + ox, p2[1] + oy),
            arrowstyle="->", mutation_scale=16,
            color=BLEU, linewidth=2.0 if double else 1.8,
            connectionstyle="arc3,rad=0.06", shrinkA=0, shrinkB=0, zorder=2,
        ))
    _ = style  # (style consigné : simple "->" vs double "=>", comme tracé)

ax.text(0, 2.62, "Schéma de démonstration (p. 2)", color=ROUGE, fontsize=12,
        fontweight="bold", ha="center", va="center")
ax.text(0, -1.95, "① ⟹ ② au milieu, ③ en haut, ④ en bas", color=BLEU, fontsize=10,
        ha="center", va="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
