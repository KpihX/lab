"""Reproduit la figure p.49 du 4e Bloc-Notes : acceleration en rotation.

Cercle de rayon r, axe horizontal M, point G repere par l'angle theta,
vitesse v tangente, vitesse angulaire omega (arc fleche), rayons et axes.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/acceleration-rotation.png
Usage : uv run scripts/reproduce_acceleration_rotation.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/acceleration-rotation.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

r = 1.0
th = np.deg2rad(60)
G = np.array([r * np.cos(th), r * np.sin(th)])
T = np.array([-np.sin(th), np.cos(th)])  # tangente directe

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.5, 1.7)
ax.set_ylim(-1.4, 1.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

t = np.linspace(0, 2 * np.pi, 400)
ax.plot(r * np.cos(t), r * np.sin(t), color="gray", linewidth=1.5)
ax.annotate("", xy=(1.6, 0), xytext=(-1.4, 0),
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.2))
ax.annotate("", xy=(0, 1.4), xytext=(0, -1.3),
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.0))
ax.plot([0, G[0]], [0, G[1]], color="red", linewidth=1.6)  # rayon OG
ax.plot(G[0], G[1], "o", color="red", markersize=5)
ax.annotate("", xy=tuple(G + 0.7 * T), xytext=tuple(G + 0.1 * T),
            arrowprops=dict(arrowstyle="->", color="red", linewidth=1.6))

arc = np.linspace(0, th, 60)
ax.plot(0.35 * np.cos(arc), 0.35 * np.sin(arc), color="red", linewidth=1.4)
w = np.linspace(np.deg2rad(100), np.deg2rad(160), 40)
ax.plot(0.55 * np.cos(w), 0.55 * np.sin(w), color="darkblue", linewidth=1.2)
ax.annotate("", xy=tuple(0.55 * np.array([np.cos(w[-1]), np.sin(w[-1])])),
            xytext=tuple(0.55 * np.array([np.cos(w[-2]), np.sin(w[-2])])),
            arrowprops=dict(arrowstyle="->", color="darkblue"))

ax.text(1.55, -0.14, "M", fontsize=13)
ax.text(-0.14, 0.06, "O", fontsize=12)
ax.text(G[0] + 0.08, G[1] + 0.05, "G", color="red", fontsize=12)
ax.text(0.38, 0.14, "θ", color="red", fontsize=13)
ax.text(float(G[0] + 0.75 * T[0]) + 0.03, float(G[1] + 0.75 * T[1]),
        "v", color="red", fontsize=13)
ax.text(-0.62, 0.62, "ω", color="darkblue", fontsize=13)
ax.text(G[0] / 2 - 0.12, G[1] / 2, "r", color="red", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
