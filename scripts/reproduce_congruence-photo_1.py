"""Reproduit le fond de congruence-photo : solutions de 8x = 8 (mod 12).

Manuscrit : Pp (E1) : 8x + 4 = 0 [12], d = 8 ^ 12 = 4 ; equation (E2)/(E3)
brouillons autour de 2x^2 + 3x - 1 = 0 (mod 8). Pas de schema trace :
reproduction illustrative fidele au sens arithmetique restitue
(x = 1 (3), soit {1, 4, 7, 10} mod 12).
Vue : residus 0..11 (points bleus), solutions en rouge sur ligne 8x-8 = 0 [12].
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/algebre-arithmetique/congruence-photo/assets/congruence-solutions.png
Usage : uv run scripts/reproduce_congruence-photo_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/congruence-photo/assets/congruence-solutions.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

residues = np.arange(0, 12)
solutions = {1, 4, 7, 10}  # 8x = 8 [12] <=> x = 1 [3]
is_sol = np.array([r in solutions for r in residues])

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(-1, 12)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.axhline(0, color="black", linewidth=1.0)
ax.plot(residues[~is_sol], np.zeros((~is_sol).sum()), "o", color="#1a3fb5", markersize=9)
ax.plot(residues[is_sol], np.zeros(is_sol.sum()), "s", color="red", markersize=10)
for r in residues:
    ax.text(r, -0.45, str(r), color="red" if r in solutions else "#1a3fb5",
            fontsize=11, ha="center", fontweight="bold" if r in solutions else "normal")
ax.text(6.0, 0.75, "8x = 8 [12]  <=>  x = 1 [3] = {1, 4, 7, 10} mod 12",
        color="black", fontsize=11, ha="center")
ax.text(6.0, -1.05, "carres rouges : solutions (E1)", color="red", fontsize=10, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
