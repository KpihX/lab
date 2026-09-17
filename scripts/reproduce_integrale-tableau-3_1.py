"""Reproduit I_n = integrale_0^1 (1-t^2)^n dt (p. integrale-tableau-3).

Fond : recurrence I_{n+1} = 2(n+1)/(2n+3) I_n, d'ou
I_n = (2^n n!)^2/(2n+1)! = somme_{k=0}^n (-1)^k C_n^k/(2k+1).
Reproduction : courbes (1-t^2)^n pour n = 0..3 et aire I_1 hachuree.

Style "stylo" : courbes bleues, aire rouge clair, fond quadrille bleu.

Sortie : raw/analyse-integrales/integrale-tableau-3/assets/in-wallis.png

Usage :
  uv run scripts/reproduce_integrale-tableau-3_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # $ uv run scripts/reproduce_integrale-tableau-3_1.py
>>> # OK -> .../assets/in-wallis.png (NNNNN o)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/integrale-tableau-3/assets/in-wallis.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

ts = np.linspace(0, 1, 801)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.axvline(0, color=BLUE, linewidth=1.0)
for n in range(4):
    ax.plot(ts, (1 - ts**2) ** n, color=BLUE, linewidth=1.4)
    ax.text(1.01, float((1 - 1.0**2) ** n) + 0.03 + 0.06 * (3 - n),
            f"n={n}", color=BLUE, fontsize=10, va="center", clip_on=False)
ax.fill_between(ts, (1 - ts**2) ** 1, color=RED, alpha=0.25)
ax.set_title("I_n = integrale_0^1 (1-t^2)^n dt", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
