"""Reproduit la figure p.4 de coniques-rapport : diametres de la parabole.

Parabole (P) : y^2 = 2 p x (p = 2), axe focal (Delta) : y = 0.
Deux cordes paralleles MN et M'N' (pente 1), milieux I et I' alignes
sur le diametre (delta') : y = 2 (cf. manuscrit : y_I = a.p/b = cte).
Style gabarits : grille #9db3d8, tick_params sans etiquettes.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

P = 2.0
OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig08-parabole-diametres.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6, alpha=0.7)
ax.tick_params(labelbottom=False, labelleft=False,
               bottom=False, left=False)

# Parabole y^2 = 2 p x
y = np.linspace(-6, 7, 600)
x = y ** 2 / (2 * P)
ax.plot(x, y, color="black", linewidth=1.6, label="(P)")

# Axe focal (Delta) : y = 0
ax.axhline(0, color="black", linewidth=1.0)
ax.text(9.6, 0.25, "(Δ)", fontsize=11)

# Deux cordes paralleles de pente m = 1 : y = x + k (k = ±0.5, sécantes)
for k, names in ((0.5, ("M", "N")), (-0.5, ("M'", "N'"))):
    col = "#4d4d4d"
    disc = P ** 2 + 2 * P * k  # > 0 : y = P ± sqrt(disc)
    y1 = P - np.sqrt(disc)
    y2 = P + np.sqrt(disc)
    x1, x2 = y1 ** 2 / (2 * P), y2 ** 2 / (2 * P)
    ax.plot([x1, x2], [y1, y2], color=col, linewidth=1.2)
    yield_pts = ((x1, y1), (x2, y2))
    for (xp, yp), name, dx, dy in zip(
        yield_pts, names,
        (-0.55, 0.3) if k == 0.5 else (0.3, 0.3),
        (-0.4, -0.5) if k == 0.5 else (0.35, -0.55),
    ):
        ax.plot(xp, yp, "ko", markersize=4)
        ax.text(xp + dx, yp + dy, name, fontsize=11)
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
    ax.plot(xm, ym, "ko", markersize=5)
    ax.text(xm - 0.55, ym + 0.3,
            "I" if k == 0.5 else "I'", fontsize=11, fontweight="bold")

# Diametre (delta') : y = P / m = 2
ax.axhline(P / 1.0, color="#808080", linewidth=1.2, linestyle="--")
ax.text(9.6, 2.25, "(δ') : y = 2", fontsize=11, color="#333333")

ax.set_xlim(-1, 11)
ax.set_ylim(-5.5, 7.5)
ax.set_title("Parabole y² = 2px — cordes // et diamètre (δ')", fontsize=12)
fig.tight_layout()
fig.savefig(OUT, dpi=110)
print("OK", OUT)
