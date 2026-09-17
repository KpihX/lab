"""Reproduit le fond de jacobien-changement-variable-ordre2 (changement de variable, jacobien).

Fond : dS2 = ||dr/da ^ dr/db|| da db = |J| da db. Ex. affine
x = a+0.5b, y = 0.25a+1.5b : le rectangle [0,1]x[0,1] devient un
parallelogramme engendre par dr/da=(1,0.25), dr/db=(0.5,1.5),
aire = |det J| = 1.375. Reproduction : rectangle + image.
Style "stylo" : rectangle bleu, parallelogramme rouge, vecteurs.

Sortie : raw/analyse-fonctions/jacobien-changement-variable-ordre2/assets/jacobien-parallelogramme.png

Usage :
  uv run scripts/reproduce_jacobien-changement-variable-ordre2_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/photos-dessins"
    "/jacobien-changement-variable-ordre2/assets/jacobien-parallelogramme.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

# (a,b) -> (x,y), coins du carre unite
corners_ab = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
X = corners_ab[:, 0] + 0.5 * corners_ab[:, 1]
Y = 0.25 * corners_ab[:, 0] + 1.5 * corners_ab[:, 1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 4.2))
for ax in (ax1, ax2):
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_aspect("equal")

ax1.plot(corners_ab[:, 0], corners_ab[:, 1], color=BLUE, linewidth=1.6)
ax1.arrow(0, 0, 1, 0, color=BLUE, width=0.02, head_width=0.08, length_includes_head=True)
ax1.arrow(0, 0, 0, 1, color=BLUE, width=0.02, head_width=0.08, length_includes_head=True)
ax1.set_xlim(-0.3, 1.6)
ax1.set_ylim(-0.3, 2.0)
ax1.set_title("plan (a,b) : da db", color=BLUE, fontsize=11)

ax2.plot(X, Y, color=RED, linewidth=1.6)
ax2.arrow(0, 0, 1, 0.25, color=RED, width=0.02, head_width=0.08, length_includes_head=True)
ax2.arrow(0, 0, 0.5, 1.5, color=RED, width=0.02, head_width=0.08, length_includes_head=True)
ax2.set_xlim(-0.3, 2.0)
ax2.set_ylim(-0.3, 2.0)
ax2.set_title("|J| da db : aire du //logramme", color=RED, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
