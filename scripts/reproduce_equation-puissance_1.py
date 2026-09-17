"""Reproduit le schema de l'equation en puissance.

Manuscrit d'origine (equation-puissance.jpg) : resolution par
disjonction de cas [B1], [B2] ... : « 4x + 5 + 9 = ... »,
« (B1) <=> ... 5 + 9 + ... », « => 5x + 9 ... 2 ... »,
« - Pour c = 0 », « (B1) <=> 1 = S ... », « => ... »,
« Pour ... », « |B1| <=> 49 + ... + 1 = ... », « ... 03 ... A1 »,
« Nous avons (B1) => ... 0 = 2 ... + 1 ... », « ... 5 ... 9 ... »,
« ... |9|, |9| ... », « ... 6 ... 2 ... + 1 », « ... q = ... K x + ... »,
« ... S ... = S ... », « ... 5 ... S ... + 2 ... », « ... 5x ... S ... »,
« => ... 5x ... S ... [100] », « ... * ... S ... = 2S ... (par ... ) »,
« ... N1 = 0 ... N2 O ... », « ... (B1) ... N1 ... 0,1 ... »
[tres nombreuses lectures incertaines].

Ici : arbre des cas [B1]/[B2] et courbes representatives des deux
membres (droite 5x + 9 et parabole) dont les intersections
donnent les solutions discutees par cas.

Sortie : raw/algebre-arithmetique/equation-puissance/assets/equation-puissance.png

Usage :
  uv run scripts/reproduce_equation-puissance_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/equation-puissance/assets/equation-puissance.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

x = np.linspace(-4, 3, 400)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.axvline(0, color=BLUE, linewidth=1.0)
ax.plot(x, 5 * x + 9, color=BLUE, linewidth=1.6)  # membre de gauche (B1)
ax.plot(x, x**2 + 1, color=RED, linewidth=1.6)  # membre de droite (B2)
ax.set_title("Cas [B1] / [B2] : intersections = solutions", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
