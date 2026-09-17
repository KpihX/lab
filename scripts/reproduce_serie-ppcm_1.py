"""Reproduit le fond de serie-ppcm : Un = 1/ppcm(1..n) dominee par 1/n(n-1).

Manuscrit : n(n-1) | ppcm(1..n) donc Un <= 1/n(n-1), convergence par comparaison.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/algebre-arithmetique/serie-ppcm/assets/serie-ppcm.png
Usage : uv run scripts/reproduce_serie-ppcm_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from math import gcd

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/serie-ppcm/assets/serie-ppcm.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

def lcm(a, b):
    return a // gcd(a, b) * b

ns = np.arange(2, 9)
L = 1
pp = []
for n in ns:
    L = lcm(int(L), int(n))
    pp.append(L)
pp = np.array(pp, dtype=float)
Un = 1.0 / pp
maj = 1.0 / (ns * (ns - 1))

fig, ax = plt.subplots(figsize=(8, 5))
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

w = 0.35
ax.bar(ns - w / 2, Un, width=w, color="#1a3fb5", label="Un = 1/ppcm(1..n)")
ax.bar(ns + w / 2, maj, width=w, color="red", alpha=0.75, label="1/n(n-1)")
ax.set_yscale("log")
ax.text(7.6, maj[-1] * 1.4, "Un <= 1/n(n-1)", color="black", fontsize=10, ha="right")
ax.legend(frameon=True, fontsize=9, loc="upper right")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
