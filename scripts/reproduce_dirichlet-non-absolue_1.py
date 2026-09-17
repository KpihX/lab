"""Reproduit le schema Dirichlet non-absolu : |sin t|/t vs sin t/t.

Manuscrit d'origine (dirichlet-non-absolue.jpg) : « Nature de
I = integrale de 1 a +inf de |sin t|/t dt », I diverge (comparaison
par encadrement sur chaque intervalle [k*pi, (k+1)*pi]), « d'apres
le critere de Cauchy, I diverge ».

Ici : f(t) = |sin t|/t (bleu) et son integrale cumulee croissante
de type log (rouge) sur [1, 40], qui illustre la divergence.

Sortie : raw/analyse-suites-series/dirichlet-non-absolue/assets/dirichlet.png

Usage :
  uv run scripts/reproduce_dirichlet-non-absolue_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/tableau-noir"
    "/dirichlet-non-absolue/assets/dirichlet.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

t = np.linspace(1, 40, 2000)
f = np.abs(np.sin(t)) / t
F = np.cumsum(f) * (t[1] - t[0])  # integrale cumulee (diverge ~ log)

fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
for spine in ax.spines.values():
    spine.set_visible(False)

ax.axhline(0, color=BLUE, linewidth=1.0)
ax.plot(t, f, color=BLUE, linewidth=1.2)  # |sin t| / t
ax.plot(t, F, color=RED, linewidth=1.6)  # integrale cumulee divergente
ax.set_title("I = int |sin t|/t diverge (Cauchy)", color=RED, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
