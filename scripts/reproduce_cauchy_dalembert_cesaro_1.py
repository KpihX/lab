"""Reproduit le schema p.1 de cauchy-dalembert-cesaro (lot B0).

Schema d'origine (stylo bleu sur papier) : deux cercles concentriques
traces en haut a gauche ; une fleche annote le (grand) cercle
"critere de d'Alembert", une autre le (petit) cercle
"critere de Cauchy".

Style "stylo" : cercles et fleches bleus, annotations rouges,
fond quadrille bleu.

Sortie : raw/analyse-suites-series/cauchy-dalembert-cesaro/assets/criteres-cercles.png

Usage :
  uv run scripts/reproduce_cauchy_dalembert_cesaro_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_cauchy_dalembert_cesaro_1.py
>>> # OK -> .../assets/criteres-cercles.png (NNNNN o)
>>> # le rendu montre les deux cercles concentriques et leurs etiquettes.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-suites-series"
    "/cauchy-dalembert-cesaro/assets/criteres-cercles.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(6, 5))
ax.set_aspect("equal")
ax.set_xlim(-3.5, 5.5)
ax.set_ylim(-3.0, 3.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Deux cercles concentriques (stylo bleu).
theta = np.linspace(0, 2 * np.pi, 200)
ax.plot(2.2 * np.cos(theta), 2.2 * np.sin(theta), color=BLUE, linewidth=1.5)
ax.plot(1.1 * np.cos(theta), 1.1 * np.sin(theta), color=BLUE, linewidth=1.5)

# Fleches d'annotation.
ax.annotate("", xy=(1.55, 1.55), xytext=(3.2, 2.4),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2))
ax.text(3.3, 2.4, "critère de d'Alembert", color=RED, fontsize=11)
ax.annotate("", xy=(0.78, 0.78), xytext=(3.2, 1.2),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.2))
ax.text(3.3, 1.2, "critère de Cauchy", color=RED, fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
