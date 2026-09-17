"""Reproduit le fond de parabole-naturelle : jet d'eau parabolique bassine -> seau.
Photo : aucune ecriture, jet balistique entre deux recipients.
Vue : trajectoire y = x - 0.55 x^2, bassine (gauche) et seau (droite) schematises.
Sortie : raw/physique/parabole-naturelle/assets/jet-parabolique.png
Usage : uv run scripts/reproduce_parabole-naturelle_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/parabole-naturelle/assets/jet-parabolique.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

x = np.linspace(0, 1.85, 200)
y = 1.6 * x - 0.85 * x ** 2 + 0.55

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(-0.3, 2.3)
ax.set_ylim(0, 2.2)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.plot(x, y, color="#1a3fb5", linewidth=2.0)
ax.add_patch(patches.Rectangle((-0.25, 0), 0.6, 0.55, facecolor="#7fb3e8", edgecolor="#1a3fb5", linewidth=1.5))
ax.add_patch(patches.Rectangle((1.7, 0), 0.35, 0.4, facecolor="#bfe0f5", edgecolor="#1a3fb5", linewidth=1.5))
ax.text(0.05, 0.2, "bassine", color="#0d2470", fontsize=10)
ax.text(1.72, 0.12, "seau", color="#0d2470", fontsize=10)
ax.text(0.9, 1.85, "jet parabolique  y ~ x - x^2", color="#1a3fb5", fontsize=11, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
