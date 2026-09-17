"""Reproduit le fond de supplementaire-commun : droites F1, F2 et supplementaire commun G.

Manuscrit : preuve d'existence d'un supplementaire commun (texte seul, sans schema).
Ici illustration : E = R2, F1 = axe Ox, F2 = diagonale, G = droite supplementaire commune.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/algebre-arithmetique/supplementaire-commun/assets/supplementaire-commun.png
Usage : uv run scripts/reproduce_supplementaire-commun_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/supplementaire-commun/assets/supplementaire-commun.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(7, 6))
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

t = np.linspace(-3, 3, 200)
ax.plot(t, np.zeros_like(t), color="#1a3fb5", linewidth=2.2)          # F1 = Ox
ax.plot(t, 0.5 * t, color="#1a3fb5", linewidth=2.2, linestyle="--")   # F2 diagonale
ax.plot(np.zeros_like(t), t, color="red", linewidth=2.2)             # G = Oy commun
ax.text(2.2, 0.15, "F1", color="#1a3fb5", fontsize=12)
ax.text(2.2, 1.25, "F2", color="#1a3fb5", fontsize=12)
ax.text(0.15, 2.4, "G", color="red", fontsize=12)
ax.text(-2.9, -2.6, "E = F1 (+) G = F2 (+) G", color="black", fontsize=10)
ax.plot([0], [0], "o", color="black", markersize=6)
ax.set_xlim(-3.2, 3.2); ax.set_ylim(-3, 3)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
