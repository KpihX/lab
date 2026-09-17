"""Reproduit le repere cylindrique du manuscrit surface-2 (differentielle-surface, prise 2, ex-differentielle-surface-2).

Manuscrit d'origine (differentielle-surface-prise2.jpg) : meme « Etude
differentielle d'une surface » que surface-1 (quasi-jumeau),
avec l'accent sur les coordonnees cylindriques : point M(r,theta,z),
r = x^2 + y^2 [lecture incertaine], base (e_r, e_theta, e_z),
puis element de surface dS et aire A = integrale sur S de dS.

Ici : cercle de rayon r dans le plan z = cste, vecteurs e_r et
e_theta en M, axe (O,z) et rappel de la cote z.

Sortie : raw/geometrie/differentielle-surface/assets/surface-2.png

Usage :
  uv run scripts/reproduce_differentielle-surface_2.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/differentielle-surface/assets/surface-2.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

theta = np.linspace(0, 2 * np.pi, 200)
r = 1.5
th0 = 0.9
M = np.array([r * np.cos(th0), r * np.sin(th0)])
er = np.array([np.cos(th0), np.sin(th0)]) * 0.9
et = np.array([-np.sin(th0), np.cos(th0)]) * 0.9

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

ax.plot(r * np.cos(theta), r * np.sin(theta), color=BLUE, linewidth=1.6)  # cercle r = cste
ax.plot([0, 0], [-2, 2], color=BLUE, linewidth=1.0)  # axe (O,z) projete
ax.plot(0, 0, "o", color=RED, markersize=5)  # origine O
ax.plot(M[0], M[1], "o", color=RED, markersize=5)  # point M
ax.plot([0, M[0]], [0, M[1]], color=BLUE, linewidth=1.0, linestyle="--")  # rayon OM
ax.arrow(M[0], M[1], er[0], er[1], color=BLUE, width=0.02, head_width=0.09)  # e_r
ax.arrow(M[0], M[1], et[0], et[1], color=BLUE, width=0.02, head_width=0.09)  # e_theta
ax.set_title("M(r,theta,z) : (e_r, e_theta, e_z)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
