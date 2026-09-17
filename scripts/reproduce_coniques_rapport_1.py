"""Reproduit la figure p.1 du rapport coniques : cone double (C) coupe par un plan (Pi).

Schema d'origine (stylo bleu + crayon) : cone double d'axe vertical,
sommet O, plan (Pi) oblique de normale n, point courant M(x,y,z),
indication |z| = a*sqrt(x^2+y^2).

Sortie : raw/geometrie/coniques-rapport/assets/fig01-cone-plan.png
Usage : uv run scripts/reproduce_coniques_rapport_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig01-cone-plan.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(6, 7))
ax.set_aspect("equal")
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

th = np.linspace(0, 2 * np.pi, 200)
for zc, rx in [(4.0, 1.6), (-4.0, 1.6)]:  # bases du cone double
    ax.plot(rx * np.cos(th), zc + 0.35 * np.sin(th), color="gray", linewidth=1.2)
# generatrices (crayon gris)
for sx in (-1, 1):
    ax.plot([0, sx * 1.6], [0, 4.0], color="gray", linewidth=1.2)
    ax.plot([0, sx * 1.6], [0, -4.0], color="gray", linewidth=1.2)
# axe vertical Omega
ax.plot([0, 0], [-4.6, 4.6], color="dimgray", linewidth=1.0)
ax.annotate("", xy=(0.9, 3.4), xytext=(0, 3.4),
            arrowprops=dict(arrowstyle="->", color="black", lw=1.2))
ax.text(1.0, 3.5, "n", fontsize=12)
ax.text(0.15, 3.0, "Ω", fontsize=12)
# plan (Pi) oblique passant pres du sommet
xs = np.linspace(-2.6, 2.6, 50)
ax.plot(xs, 0.45 * xs + 0.4, color="black", linewidth=1.4)
ax.text(2.0, 1.7, "(Π)", fontsize=12)
ax.text(-2.4, 3.2, "(C)", fontsize=12)
ax.text(0.1, -0.35, "O", fontsize=12)
ax.plot(0, 0, "o", color="black", markersize=4)
ax.text(-1.9, 0.2, "|z|", fontsize=11, color="dimgray")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
