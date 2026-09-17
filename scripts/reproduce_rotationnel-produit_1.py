"""Reproduit le fond de rotationnel-produit : champ g module par f et son rotationnel.

Manuscrit : preuve de rot(f.g) = f.rot(g) + grad(f) ^ g (calcul seul, sans schema).
Ici illustration fidele du propos : g(x,y) = (-y, x), f(x,y) = 1 + x/4.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/rotationnel-produit/assets/champ-rotationnel.png
Usage : uv run scripts/reproduce_rotationnel-produit_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/rotationnel-produit/assets/champ-rotationnel.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(7, 6))
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

x = np.arange(-3, 3.5, 1.0); y = np.arange(-3, 3.5, 1.0)
X, Y = np.meshgrid(x, y)
f = 1 + X / 4.0
U, V = -Y * f, X * f
ax.quiver(X, Y, U, V, color="#1a3fb5", scale=28, width=0.006)
# Vecteur rotationnel (sortant) au centre : grad(f) ^ g + f.rot(g)
ax.plot([0], [0], "o", color="red", markersize=9)
ax.text(0.25, 0.25, "rot(fg) // Oz", color="red", fontsize=11)
ax.text(-3.4, 3.6, "g(x,y) = (-y, x), f = 1+x/4", color="black", fontsize=10)
ax.set_xlim(-4, 4); ax.set_ylim(-4, 4.2)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
