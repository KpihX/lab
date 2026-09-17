"""Reproduit le fond de preambule-manuscrit : dessin d'enfant, deux personnages rayes.
Manuscrit : aucun texte sauf une ligne crayon en bas ; deux bonhommes colores.
Vue : deux silhouettes schematiques avec bandes colorees evoquant le dessin.
Sortie : raw/divers/preambule-manuscrit/assets/deux-personnages.png
Usage : uv run scripts/reproduce_preambule-manuscrit_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/divers/preambule-manuscrit/assets/deux-personnages.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

colors = ["#333333", "#e85454", "#6fce6f", "#e8d44f", "#e89b4f", "#6fa8dc"]
for px in (2.2, 6.8):
    ax.add_patch(patches.Circle((px, 4.6), 0.7, fill=False, edgecolor="black", linewidth=1.5))
    for i, c in enumerate(colors):
        ax.add_patch(patches.Rectangle((px - 0.8, 3.4 - i * 0.35), 1.6, 0.35, facecolor=c, alpha=0.7, edgecolor="none"))
    ax.plot([px - 0.8, px - 0.8], [0.6, 1.0], color="black", linewidth=1.5)
    ax.plot([px + 0.8, px + 0.8], [0.6, 1.0], color="black", linewidth=1.5)
ax.plot([3.0, 5.2], [3.2, 3.8], color="black", linewidth=1.5)
ax.text(5, 0.15, "dessin d'enfant : deux personnages (reproduction schematique)", fontsize=10, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
