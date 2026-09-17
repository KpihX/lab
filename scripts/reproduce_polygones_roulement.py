"""Reproduit la figure p.152 de quatrieme-bloc-notes : roulement polygonal.

Figure d'origine (manuscrite) : petit disque (D) sur grand disque (D'),
assimiles a des polygones reguliers inscrits de cote commun dl -> 0,
angles elementaires dtheta (petit) et dtheta' (grand) autour du point
de contact.

Style "stylo" : cercles et cordes bleus, angles et cotes rouges, fond
quadrille bleu.

Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/polygones-roulement.png

Usage :
  uv run scripts/reproduce_polygones_roulement.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/polygones-roulement.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(7, 8))
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-2.8, 4.6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_aspect("equal")

Rp, R = 2.0, 0.9
Op = np.array([0.0, 0.0])
T = np.array([0.0, Rp])
O = np.array([0.0, Rp + R])

ax.add_patch(Circle(Op, Rp, fill=False, color=BLUE, linewidth=1.8))
ax.add_patch(Circle(O, R, fill=False, color=BLUE, linewidth=1.8))
ax.plot(T[0], T[1], "o", color=RED, markersize=6)
ax.plot(Op[0], Op[1], "o", color=BLUE, markersize=5)
ax.plot(O[0], O[1], "o", color=BLUE, markersize=5)

# Cotes elementaires dl : deux rayons + corde de chaque cote du contact.
dtheta_p = np.radians(28.0)
dtheta = np.radians(62.0)
for sgn, ang0, rad, c in ((-1, 90.0, Rp, Op), (1, 90.0, Rp, Op)):
    a = np.radians(ang0 + sgn * np.degrees(dtheta_p) / 2)
    Pt = c + rad * np.array([np.cos(a), np.sin(a)])
    ax.plot([c[0], Pt[0]], [c[1], Pt[1]], color=BLUE, linewidth=1.1,
            linestyle=(0, (4, 3)))
a_lo = np.radians(90 - np.degrees(dtheta_p) / 2)
a_hi = np.radians(90 + np.degrees(dtheta_p) / 2)
P1 = Op + Rp * np.array([np.cos(a_lo), np.sin(a_lo)])
P2 = Op + Rp * np.array([np.cos(a_hi), np.sin(a_hi)])
ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color=BLUE, linewidth=2.0)

for sgn in (-1, 1):
    a = np.radians(270 + sgn * np.degrees(dtheta) / 2)
    Pt = O + R * np.array([np.cos(a), np.sin(a)])
    ax.plot([O[0], Pt[0]], [O[1], Pt[1]], color=BLUE, linewidth=1.1,
            linestyle=(0, (4, 3)))
a_lo2 = np.radians(270 - np.degrees(dtheta) / 2)
a_hi2 = np.radians(270 + np.degrees(dtheta) / 2)
Q1 = O + R * np.array([np.cos(a_lo2), np.sin(a_lo2)])
Q2 = O + R * np.array([np.cos(a_hi2), np.sin(a_hi2)])
ax.plot([Q1[0], Q2[0]], [Q1[1], Q2[1]], color=BLUE, linewidth=2.0)

ax.add_patch(Arc(Op, 0.9, 0.9, theta1=90 - np.degrees(dtheta_p) / 2,
                 theta2=90 + np.degrees(dtheta_p) / 2, color=RED, linewidth=1.3))
ax.add_patch(Arc(O, 0.7, 0.7, theta1=270 - np.degrees(dtheta) / 2,
                 theta2=270 + np.degrees(dtheta) / 2, color=RED, linewidth=1.3))

ax.text(0.7, 2.1, "dl", color=RED, fontsize=13)
ax.text(-0.95, 1.85, "dl", color=RED, fontsize=13)
ax.text(0.55, 0.55, "d\u03b8'", color=RED, fontsize=14)
ax.text(0.55, 2.75, "d\u03b8", color=RED, fontsize=14)
ax.text(Op[0] + 0.15, Op[1] - 0.5, "O'", color=RED, fontsize=13)
ax.text(O[0] + 0.15, O[1] + 0.15, "O", color=RED, fontsize=13)
ax.text(-1.5, -0.5, "(D')", color=RED, fontsize=14)
ax.text(1.15, 3.3, "(D)", color=RED, fontsize=14)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
