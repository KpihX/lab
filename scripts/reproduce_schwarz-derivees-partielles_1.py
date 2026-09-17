"""Reproduit le fond de schwarz-derivees-partielles : nappe f et tangentes partielles.

Manuscrit : preuve de d2f/dxidxj = d2f/dxjdxi par taux d'accroissement (sans schema).
Ici illustration : f(x,y) = x^2.y + y^3, tangentes partielles en (1, 0.5).
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/analyse-fonctions/schwarz-derivees-partielles/assets/schwarz-derivees.png
Usage : uv run scripts/reproduce_schwarz-derivees-partielles_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions/schwarz-derivees-partielles/assets/schwarz-derivees.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection="3d")
x = np.linspace(-1.5, 1.5, 60); y = np.linspace(-1.5, 1.5, 60)
X, Y = np.meshgrid(x, y)
F = X ** 2 * Y + Y ** 3
ax.plot_surface(X, Y, F, color="#1a3fb5", alpha=0.55, edgecolor="#9db3d8", linewidth=0.25)
# Point (1, 0.5) et tangentes partielles d2f/dxdx/dydy
x0, y0 = 1.0, 0.5
f0 = x0 ** 2 * y0 + y0 ** 3
tx = np.linspace(0.2, 1.8, 20)
ax.plot(tx, np.full_like(tx, y0), (tx ** 2 * y0 + y0 ** 3), color="red", linewidth=2.5)
ty = np.linspace(-0.3, 1.3, 20)
ax.plot(np.full_like(ty, x0), ty, (x0 ** 2 * ty + ty ** 3), color="green", linewidth=2.5)
ax.scatter([x0], [y0], [f0], color="black", s=40)
ax.text(x0, y0, f0 + 0.6, "d2f/dxdy = d2f/dydx", fontsize=10)
ax.tick_params(labelbottom=False, labelleft=False, length=0)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
