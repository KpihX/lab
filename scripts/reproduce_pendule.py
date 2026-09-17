"""Reproduit la figure p.107 (haut) du 4e Bloc-Notes : pendule pesant.

Pivot O, verticale en pointilles vers G0 (equilibre), fil OG a l'angle
theta de la verticale, tension T (de G vers O), poids P (vertical vers
le bas en G), arc de trajectoire. Schema au crayon, pale a l'origine.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/pendule.png
Usage : uv run scripts/reproduce_pendule.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/pendule.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

L = 1.0
th = np.deg2rad(28)  # angle a la verticale (cf. scan p.107)
O = np.array([0.0, 1.0])
G = O + L * np.array([np.sin(th), -np.cos(th)])
G0 = O + np.array([0.0, -L])

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.2, 1.4)
ax.set_ylim(-0.6, 1.4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

# verticale d'equilibre (pointilles) + fil OG (crayon)
ax.plot([O[0], G0[0]], [O[1], G0[1]], color="dimgray", linewidth=0.9,
        linestyle=(0, (4, 4)))
ax.plot([O[0], G[0]], [O[1], G[1]], color="gray", linewidth=1.5)
# arc de trajectoire possible autour de G0
sw = np.linspace(np.deg2rad(-35), np.deg2rad(35), 60)
ax.plot(O[0] + L * np.sin(sw), O[1] - L * np.cos(sw),
        color="gray", linewidth=0.9, linestyle=(0, (4, 4)))

ax.plot(O[0], O[1], "o", color="black", markersize=5)
ax.plot(G[0], G[1], "o", color="black", markersize=6)
ax.plot(G0[0], G0[1], "o", color="dimgray", markersize=4)

# tension T : de G vers O
uT = (O - G) / np.linalg.norm(O - G)
ax.annotate("", xy=tuple(G + 0.55 * uT), xytext=tuple(G + 0.08 * uT),
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.4))
# poids P : vertical vers le bas depuis G
ax.annotate("", xy=tuple(G + np.array([0.0, -0.6])), xytext=tuple(G + np.array([0.0, -0.08])),
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.4))

# angle theta au pivot (entre verticale et fil)
arc = np.linspace(-np.pi / 2, -np.pi / 2 + th, 40)
px, py = O[0] + 0.3 * np.cos(arc), O[1] + 0.3 * np.sin(arc)
ax.plot(px, py, color="black", linewidth=1.1)

ax.text(O[0] - 0.16, O[1] + 0.06, "O", fontsize=12)
ax.text(G[0] + 0.07, G[1] - 0.03, "G", fontsize=12)
ax.text(G0[0] - 0.20, G0[1] - 0.05, "G0", fontsize=11, color="dimgray")
ax.text(0.10, 0.62, "θ", fontsize=13)
ax.text(float(G[0] + 0.58 * uT[0]) + 0.02, float(G[1] + 0.58 * uT[1]),
        "T", fontsize=13)
ax.text(G[0] + 0.07, float(G[1] - 0.62), "P", fontsize=13)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
