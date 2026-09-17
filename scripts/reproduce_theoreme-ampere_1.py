"""OBSOLETE — ne plus executer : remplace par reproduce_theoreme-ampere_2.py
(3 panneaux : Cas 1 + Cas 2 haricot + forme locale). Ce script _1.py ne dessine
que 2 panneaux et ecraserait assets/ampere-contours.png en regressant la figure.
Conserve pour historique uniquement.

Reproduit le fond de theoreme-ampere : fil I, cercles de B et contour (Gamma).

Manuscrit : Cas 1 (contour enlace -> C = mu0.I), Cas 2 (compensation 2 a 2 -> C = 0),
forme locale mu0.j = rot(B).
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/theoreme-ampere/assets/ampere-contours.png
Usage : uv run scripts/reproduce_theoreme-ampere_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/theoreme-ampere/assets/ampere-contours.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
for ax in (ax1, ax2):
    ax.set_aspect("equal")
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for s in ax.spines.values():
        s.set_visible(False)

# Cas 1 : fil en O, B orthoradial, contour (Gamma) enlace
th = np.linspace(0, 2 * np.pi, 300)
for r in (0.8, 1.4, 2.0):
    ax1.plot(r * np.cos(th), r * np.sin(th), color="#1a3fb5", linewidth=1.1, alpha=0.7)
ax1.plot([0], [0], "o", color="red", markersize=10)
ax1.text(0.12, 0.12, "I", color="red", fontsize=13)
tg = np.linspace(0, 2 * np.pi, 200)
ax1.plot(1.7 * np.cos(tg), 1.7 * np.sin(tg), color="black", linewidth=2.0)
ax1.annotate("", xy=(-1.7, 0.15), xytext=(-1.55, 0.7),
             arrowprops=dict(arrowstyle="->", color="black", lw=1.6))
ax1.text(1.75, 0.1, "(G)", fontsize=12)
ax1.text(-2.6, 2.6, "C = mu0.I", color="black", fontsize=11)
ax1.set_xlim(-3, 3); ax1.set_ylim(-3, 3)
ax1.set_title("Cas 1 : courant enlace", fontsize=11)

# Forme locale : surface (S) traverse par j, bordee par (Gamma)
sx = np.array([-1.5, 1.5, 1.5, -1.5, -1.5]); sy = np.array([-1.2, -1.2, 1.2, 1.2, -1.2])
ax2.fill(sx, sy, color="#1a3fb5", alpha=0.12)
ax2.plot(sx, sy, color="black", linewidth=2.0)
for xx in np.linspace(-1.1, 1.1, 6):
    ax2.annotate("", xy=(xx, -0.4), xytext=(xx, -1.6),
                 arrowprops=dict(arrowstyle="->", color="red", lw=1.4))
ax2.text(0.15, 1.35, "(S), j", color="red", fontsize=11)
ax2.text(1.6, 0.0, "(G)", fontsize=12)
ax2.text(-2.6, -2.5, "mu0.j = rot(B)", color="black", fontsize=11)
ax2.set_xlim(-3, 3); ax2.set_ylim(-3, 3)
ax2.set_title("Forme locale", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
