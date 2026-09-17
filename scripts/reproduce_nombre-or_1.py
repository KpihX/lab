"""Reproduit le fond de nombre-or : Phi^n = F_n Phi + F_{n-1}, croissance Fibonacci.
Manuscrit : Phi^2=Phi+1, Phi^n=F_n Phi+F_{n-1}, formules F_{n+1}, K_n, Phi^-n.
Vue : barres log(Phi^n) lineaires + points F_n, rectangle d'or evoque.
Sortie : raw/analyse-suites-series/nombre-or/assets/phi-fibonacci.png
Usage : uv run scripts/reproduce_nombre-or_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/analyse-suites-series/nombre-or/assets/phi-fibonacci.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

phi = (1 + np.sqrt(5)) / 2
n = np.arange(0, 10)
Phi_n = phi ** n
F = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], dtype=float)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(0.8, 120)
ax.set_yscale("log")
ax.grid(True, color="#9db3d8", linewidth=0.6, which="both")
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.plot(n, Phi_n, "o-", color="#1a3fb5", markersize=6, label="Phi^n")
ax.plot(n, F, "s--", color="red", markersize=5, label="F_n (Fibonacci)")
ax.text(6.5, 60, "Phi^n = Fn.Phi + Fn-1", color="#1a3fb5", fontsize=11)
ax.text(0.2, 2.2, "Phi^2 = Phi + 1", color="red", fontsize=11)
ax.legend(frameon=True, fontsize=9)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
