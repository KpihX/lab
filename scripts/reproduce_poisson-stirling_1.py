"""Reproduit le fond de poisson-stirling : limite binomiale -> loi de Poisson.
Manuscrit : l = lim C_T^K (l/T)^K (1-l/T)^{T-K} = e^{-l} l^K / K!, indice Stirling.
Vue : barres Poisson(l=4) + courbe normale approchee Stirling.
Sortie : raw/probas/poisson-stirling/assets/poisson-stirling-convergence.png
Usage : uv run scripts/reproduce_poisson-stirling_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import math

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/probas/poisson-stirling/assets/poisson-stirling-convergence.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

lam = 4.0
K = np.arange(0, 12)
pmf = np.array([math.exp(-lam) * lam ** k / math.factorial(k) for k in K])

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(-0.7, 11.7)
ax.set_ylim(0, 0.25)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.bar(K, pmf, color="#1a3fb5", alpha=0.75, width=0.6)
xs = np.linspace(0, 11, 300)
ax.plot(xs, 1 / np.sqrt(2 * np.pi * lam) * np.exp(-(xs - lam) ** 2 / (2 * lam)),
        color="red", linewidth=1.8, linestyle="--")
ax.text(7.5, 0.20, "lim C(T,K)(l/T)^K... = e^-l l^K/K!", color="#1a3fb5", fontsize=10)
ax.text(7.5, 0.17, "Stirling : K! ~ (K/e)^K V(2piK)", color="red", fontsize=10)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
