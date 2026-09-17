"""Reproduit la figure p.13 de coniques-rapport : hyperbole via le cercle directeur.

Hyperbole (H) : x^2/a^2 - y^2/b^2 = 1, F'(−c,0), F(c,0), cercle directeur
C(F', 2a). M sur la branche droite, P = [F'M) inter C(F',2a),
M = med[FP] inter (F'P) : |MF' − MF| = 2a.
Style gabarits : grille #9db3d8, tick_params sans etiquettes.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

A, B = 4.0, 3.0
C = np.sqrt(A ** 2 + B ** 2)
OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig10-hyperbole-directeur-med.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

F = np.array([C, 0.0])
Fp = np.array([-C, 0.0])
M = np.array([5.6, B * np.sqrt((5.6 / A) ** 2 - 1)])
d = (M - Fp) / np.linalg.norm(M - Fp)
P = Fp + 2 * A * d  # P entre F' et M sur le meme rayon
I = (P + F) / 2  # mil[FP]

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6, alpha=0.7)
ax.tick_params(labelbottom=False, labelleft=False,
               bottom=False, left=False)

x = np.linspace(A, 11, 400)
yh = B * np.sqrt((x / A) ** 2 - 1)
ax.plot(x, yh, color="black", linewidth=1.6, label="(H)")
ax.plot(x, -yh, color="black", linewidth=1.6)
ax.plot(-x, yh, color="black", linewidth=1.0, alpha=0.55)
ax.plot(-x, -yh, color="black", linewidth=1.0, alpha=0.55)
xx = np.linspace(-11, 11, 2)
ax.plot(xx, (B / A) * xx, color="#808080", linewidth=1.0, linestyle="--")
ax.plot(xx, -(B / A) * xx, color="#808080", linewidth=1.0, linestyle="--")

th = np.linspace(0, 2 * np.pi, 600)
ax.plot(Fp[0] + 2 * A * np.cos(th), Fp[1] + 2 * A * np.sin(th),
        color="#808080", linewidth=1.0, label="C(F',2a)")
ax.plot([Fp[0], M[0]], [Fp[1], M[1]], color="#4d4d4d", linewidth=1.2)
ax.plot([P[0], F[0]], [P[1], F[1]], color="#4d4d4d",
        linewidth=1.0, linestyle=(0, (4, 3)))

u = M - I
u = u / np.linalg.norm(u)
t = np.linspace(-4, 5, 2)
ax.plot(I[0] + t * u[0], I[1] + t * u[1], color="black",
        linewidth=1.2, linestyle="--")
ax.text(I[0] + t[-1] * u[0] + 0.15, I[1] + t[-1] * u[1],
        "med[FP]", fontsize=11)

ax.axhline(0, color="black", linewidth=1.0)
for pt, name, dx, dy in ((Fp, "F'", -0.7, -0.6), (F, "F", 0.15, -0.6),
                         (np.zeros(2), "O", 0.1, -0.6),
                         (P, "P", 0.15, 0.15), (M, "M", 0.15, 0.15),
                         (I, "I", 0.15, -0.55)):
    ax.plot(pt[0], pt[1], "ko", markersize=4)
    ax.text(pt[0] + dx, pt[1] + dy, name, fontsize=11)

ax.set_xlim(-11, 11)
ax.set_ylim(-7.5, 7.5)
ax.set_title("Hyperbole : M = med[FP] ∩ (F'P), P ∈ C(F',2a)", fontsize=12)
fig.tight_layout()
fig.savefig(OUT, dpi=110)
print("OK", OUT, "|MF'-MF|=", abs(np.linalg.norm(M - Fp)
                                  - np.linalg.norm(M - F)))
