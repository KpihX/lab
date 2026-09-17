"""Reproduit le fond de convergence-monotone : suite croissante majoree -> borne sup S.

Manuscrit : (Un) croissante => U(N) admet une borne sup S, mtq lim Un = S.
Vue : termes Un (points bleus) croissant vers S (ligne rouge), bande epsilon.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/analyse-suites-series/convergence-monotone/assets/suite-sup.png
Usage : uv run scripts/reproduce_convergence-monotone_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/analyse-suites-series/convergence-monotone/assets/suite-sup.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

S = 5.0
n = np.arange(0, 14)
U = S - 4.0 * np.exp(-0.35 * n)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(-1, 14)
ax.set_ylim(0, 6)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.axhline(S, color="red", linewidth=1.8, linestyle="--")
ax.axhspan(S - 0.5, S, color="red", alpha=0.10)
ax.plot(n, U, "o", color="#1a3fb5", markersize=6)
ax.plot(n, U, color="#1a3fb5", linewidth=1.2)
ax.text(12.2, S + 0.1, "S = sup", color="red", fontsize=11)
ax.text(1.0, 1.6, "Un ↗,  S-ε < Un ≤ S", color="#1a3fb5", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
