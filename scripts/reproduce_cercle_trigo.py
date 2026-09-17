"""Reproduit la figure p.27 du 3e Bloc-Notes : cercle trigonometrique (lim sin/cos).

Schema d'origine (crayon gris + rouge sur quadrille) : cercle de centre O,
point I (1, 0), M image de alpha sur le cercle, P projete de M sur OI,
Q projete sur OJ, T sur la tangente issue de I ; cos alpha = OP,
sin alpha = OQ, tan alpha = IT.

Style "stylo" : cercle/axes gris (crayon), points et labels rouges,
fond quadrille bleu.

Sortie : raw/bloc-notes/troisieme-bloc-notes/assets/cercle-trigo.png

Usage :
  uv run scripts/reproduce_cercle_trigo.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_cercle_trigo.py
>>> # OK -> .../assets/cercle-trigo.png (52410 o)
>>> # le rendu montre O, I, M, P, Q, T, l'angle alpha et les 3 relations en rouge.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/troisieme-bloc-notes/assets/cercle-trigo.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

RED, GRAY = "red", "gray"
alpha = np.deg2rad(50)
M = np.array([np.cos(alpha), np.sin(alpha)])
P = np.array([M[0], 0.0])
Q = np.array([0.0, M[1]])
T = np.array([1.0, np.tan(alpha)])

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-1.4, 1.8)
ax.set_ylim(-1.3, 1.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

theta = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(theta), np.sin(theta), color=GRAY, linewidth=1.5)  # cercle crayon
ax.plot([-1.3, 1.6], [0, 0], color=GRAY, linewidth=1.0)  # axe OI
ax.plot([0, 0], [-1.2, 1.5], color=GRAY, linewidth=1.0)  # axe OJ
ax.plot([1, 1], [0, 1.5], color=GRAY, linewidth=1.2)  # tangente en I
ax.plot([0, T[0]], [0, T[1]], color=GRAY, linewidth=1.2)  # rayon OMT
ax.plot([0, M[0]], [0, M[1]], color=RED, linewidth=1.5)  # OM
ax.plot([M[0], P[0]], [M[1], P[1]], color=RED, linewidth=1.2)  # MP
ax.plot([M[0], Q[0]], [M[1], Q[1]], color=RED, linewidth=1.2)  # MQ
ax.plot([M[0], T[0]], [M[1], T[1]], color=RED, linewidth=1.2)  # MT

for name, pt, dx, dy in [
    ("O", (0, 0), -0.12, -0.15),
    ("I", (1, 0), 0.05, -0.18),
    ("J", (0, 1), 0.06, 0.03),
    ("M", M, 0.05, 0.05),
    ("P", P, 0.0, -0.2),
    ("Q", Q, -0.22, 0.0),
    ("T", T, 0.06, 0.02),
]:
    ax.plot(pt[0], pt[1], "o", color=RED, markersize=4)
    ax.text(pt[0] + dx, pt[1] + dy, name, color=RED, fontsize=12)
ax.text(0.18, 0.08, "α", color=RED, fontsize=13)
ax.text(1.15, -0.9, "cos α = OP", color=RED, fontsize=11)
ax.text(1.15, -1.05, "sin α = OQ", color=RED, fontsize=11)
ax.text(1.15, -1.2, "tan α = IT", color=RED, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
