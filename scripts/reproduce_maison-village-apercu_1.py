"""Reproduit l'apercu 3D de la maison de village (p. maison-village-apercu).

Figure d'origine : rendu 3D (640x480) d'une maison blanche a deux
niveaux — rez-de-chaussee ouvert en terrasse couverte (tables, chaises,
balustrades), etage avec baies et oculus, toiture-terrasse.
Reproduction = elevation schematique 2D fidele : socle, corps principal,
terrasse couverte avec balustrades, tables, etage avec fenetres et
oculus.

Style "stylo" : traits bleus, titre rouge, fond quadrille bleu.

Sortie : raw/divers/maison-village-apercu/assets/maison-elevation.png

Usage :
  uv run scripts/reproduce_maison-village-apercu_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_maison-village-apercu_1.py
>>> # OK -> .../assets/maison-elevation.png (NNNNN o)
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/maison-village-apercu/assets/maison-elevation.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 9)

# Socle / terrain
ax.add_patch(Rectangle((-1, -1), 12, 1, facecolor="none", edgecolor=BLUE, linewidth=1.6))
# Corps principal (rez-de-chaussee)
ax.add_patch(Rectangle((0, 0), 10, 3.5, facecolor="none", edgecolor=BLUE, linewidth=1.6))
# Terrasse couverte centrale (ouverture)
ax.add_patch(Rectangle((3, 0), 4, 2.6, facecolor="none", edgecolor=BLUE, linewidth=1.2))
# Balustrades gauche / droite de la terrasse
for x0 in (0.5, 7.5):
    for i in range(5):
        ax.plot([x0 + i * 0.4, x0 + i * 0.4], [0.2, 1.0], color=BLUE, linewidth=1.0)
    ax.plot([x0 - 0.1, x0 + 1.7], [1.0, 1.0], color=BLUE, linewidth=1.2)
# Tables de la terrasse (vues de face : plateaux + pieds)
for x0 in (3.6, 5.6):
    ax.add_patch(Rectangle((x0, 0.9), 1.0, 0.12, facecolor="none", edgecolor=BLUE, linewidth=1.2))
    ax.plot([x0 + 0.1, x0 + 0.1], [0, 0.9], color=BLUE, linewidth=1.0)
    ax.plot([x0 + 0.9, x0 + 0.9], [0, 0.9], color=BLUE, linewidth=1.0)
# Etage
ax.add_patch(Rectangle((1, 3.5), 8, 2.6, facecolor="none", edgecolor=BLUE, linewidth=1.6))
# Baies de l'etage
for x0 in (2.0, 4.2, 6.4):
    ax.add_patch(Rectangle((x0, 4.0), 1.2, 1.6, facecolor="none", edgecolor=BLUE, linewidth=1.2))
# Attique + oculus + petite baie (toiture-terrasse)
ax.add_patch(Rectangle((3, 6.1), 4, 1.6, facecolor="none", edgecolor=BLUE, linewidth=1.6))
ax.add_patch(Circle((4.0, 7.0), 0.3, facecolor="none", edgecolor=BLUE, linewidth=1.2))
ax.add_patch(Rectangle((5.8, 6.6), 0.6, 0.8, facecolor="none", edgecolor=BLUE, linewidth=1.2))
# Escaliers lateraux (triangles)
ax.add_patch(Polygon([[0, 0], [0, 3.5], [1, 3.5]], closed=True, facecolor="none",
                      edgecolor=BLUE, linewidth=1.2))
ax.set_title("Maison de village — elevation (apercu)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
