"""Reproduit le fond de conjecture-jeukwa : somme 1..10^n = concatenation de 10^n/2 avec lui-meme.

Manuscrit : S = 10^n(10^n+1)/2, ex. 1..100 -> 5050.
Vue : deux blocs de chiffres accoles (bloc A | bloc A), cas n=2 : "50"|"50".
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/algebre-arithmetique/conjecture-jeukwa/assets/concatenation.png
Usage : uv run scripts/reproduce_conjecture-jeukwa_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/conjecture-jeukwa/assets/concatenation.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.add_patch(patches.Rectangle((1, 1), 3.5, 1.6, facecolor="#dbeafe", edgecolor="#1a3fb5", linewidth=2))
ax.add_patch(patches.Rectangle((4.5, 1), 3.5, 1.6, facecolor="#fee2e2", edgecolor="red", linewidth=2))
ax.text(2.75, 1.8, "50", ha="center", fontsize=20, color="#1a3fb5")
ax.text(6.25, 1.8, "50", ha="center", fontsize=20, color="red")
ax.text(5, 3.0, "Σ(1..100) = 5050 = «50» concat «50»", ha="center", fontsize=12)
ax.text(5, 0.5, "10ⁿ/2 concat 10ⁿ/2", ha="center", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
