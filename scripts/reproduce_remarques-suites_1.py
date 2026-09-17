"""Reproduit le fond de remarques-suites : Un=1/n et Vn=(-1)^n/n -> 0, quotient non convergent.
Manuscrit : lim Up/Vp = 0 n'entraine pas convergence de Up/Vp ; contre-exemples.
Vue : deux suites convergeant vers 0, quotient oscillant mis en evidence.
Sortie : raw/analyse-suites-series/remarques-suites/assets/quotient-u-v.png
Usage : uv run scripts/reproduce_remarques-suites_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/analyse-suites-series/remarques-suites/assets/quotient-u-v.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

n = np.arange(1, 30)
U = 1 / n
V = (-1) ** n / n

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(0, 30)
ax.set_ylim(-0.6, 1.1)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.axhline(0, color="black", linewidth=1.0)
ax.plot(n, U, "o-", color="#1a3fb5", markersize=4, label="Un = 1/n -> 0")
ax.plot(n, V, "s--", color="red", markersize=4, label="Vn = (-1)^n/n -> 0")
ax.text(15, 0.6, "Up/Vp = (-1)^n : diverge (contre-exemple)", color="red", fontsize=10)
ax.legend(frameon=True, fontsize=9)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
