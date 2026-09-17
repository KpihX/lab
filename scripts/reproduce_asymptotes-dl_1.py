"""Reproduit le fond d'asymptotes-dl : courbe (C) et asymptote (C') au voisinage de +inf.

Manuscrit : etude de f(x)-g(x) -> 0, position de (C) par rapport a (C').
Ici illustration fidele du propos : f(x) = x + 1/x et asymptote g(x) = x.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/analyse-fonctions/asymptotes-dl/assets/courbe-asymptote.png
Usage : uv run scripts/reproduce_asymptotes-dl_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions/asymptotes-dl/assets/courbe-asymptote.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0.3, 8)
ax.set_ylim(-1.5, 9)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

x = np.linspace(0.35, 8, 600)
f = x + 1 / x
g = x
ax.plot(x, f, color="#1a3fb5", linewidth=2.0, label="C : y=f(x)")
ax.plot(x, g, color="red", linewidth=1.6, linestyle="--", label="C' : asymptote")
ax.fill_between(x, g, f, color="#1a3fb5", alpha=0.12)
ax.text(6.5, 7.6, "(C') : y=x", color="red", fontsize=12)
ax.text(2.2, 4.6, "(C) : y=f(x)", color="#1a3fb5", fontsize=12)
ax.text(1.0, 2.6, "f(x)-g(x) -> 0", color="black", fontsize=11)
ax.legend(frameon=True, fontsize=9, loc="lower right")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
