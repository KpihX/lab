"""Reproduit la famille (f_k : x |-> cos(x^k)) etudiee p. independance-cos.

Figure d'origine (stylo bleu sur papier Seyes) : pas de schema, preuve
d'independance lineaire par l'absurde. Reproduction = illustration du
fond : traces de cos(x^k) pour k = 0, 1, 2, 3 sur [0, 2], oscillations
de plus en plus rapides — intuition visuelle de la liberte de la famille.

Style "stylo" : courbes bleues, titre rouge, fond quadrille bleu.

Sortie : raw/analyse-fonctions/independance-cos/assets/famille-cos.png

Usage :
  uv run scripts/reproduce_independance-cos_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_independance-cos_1.py
>>> # OK -> .../assets/famille-cos.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/independance-cos/assets/famille-cos.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

xs = np.linspace(0, 2, 1201)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

for k in range(4):
    ax.plot(xs, np.cos(xs**k), color=BLUE, linewidth=1.4)
    ax.text(2.01, float(np.cos(2.0**k)), f"k={k}", color=RED, fontsize=10,
            va="center", clip_on=False)

ax.set_title("f_k(x) = cos(x^k), k = 0..3 (famille libre)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
