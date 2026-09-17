"""Reproduit le schema haut p.120 du 4e Bloc-Notes : Jacobien polaire.

Element d'aire dA' (encadre rouge) : petit "rectangle" courbe de cotes
dr (radial) et rd(theta) (orthoradial), entre les rayons r et r+dr.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/jacobien-polaire.png
Usage : uv run scripts/reproduce_jacobien_polaire.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/jacobien-polaire.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

r, dr = 2.0, 0.55
t1, t2 = 28.0, 42.0
tm = (t1 + t2) / 2

fig, ax = plt.subplots(figsize=(6, 5))
ax.set_aspect("equal")
ax.set_xlim(-0.5, 3.6)
ax.set_ylim(-0.5, 3.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

# element d'aire dA' : secteur annulaire
wedge = Wedge((0, 0), r + dr, t1, t2, width=dr, facecolor="none",
              edgecolor="dimgray", linewidth=1.2)
ax.add_patch(wedge)
# rayons et arcs de construction (crayon)
for t in (t1, t2):
    rad = np.deg2rad(t)
    ax.plot([0, (r + dr + 0.7) * np.cos(rad)], [0, (r + dr + 0.7) * np.sin(rad)],
            color="dimgray", linewidth=0.9)
tt = np.deg2rad(np.linspace(t1, t2, 60))
ax.plot((r + dr + 0.35) * np.cos(tt), (r + dr + 0.35) * np.sin(tt),
        color="dimgray", linewidth=0.8, linestyle=(0, (3, 3)))

ax.text(0.02, -0.18, "O", fontsize=11, color="dimgray")

# annotations : dA' encadre rouge, dr radial, rd(theta) orthoradial
rm = r + dr / 2
radm = np.deg2rad(tm)
ax.text(rm * np.cos(radm) - 0.15, rm * np.sin(radm) - 0.05, "dA'",
        fontsize=13, color="red",
        bbox=dict(boxstyle="square,pad=0.25", edgecolor="red",
                  facecolor="white", linewidth=1.2))
rad1 = np.deg2rad(t1)
ax.text((r + dr / 2) * np.cos(rad1) + 0.08, (r + dr / 2) * np.sin(rad1) - 0.3,
        "dr", fontsize=12, color="red")
ax.text((r + 0.1) * np.cos(radm) - 0.35, (r + 0.1) * np.sin(radm) + 0.28,
        "rdθ", fontsize=12, color="red")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
