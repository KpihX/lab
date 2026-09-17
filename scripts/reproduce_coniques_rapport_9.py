"""Reproduit la figure p.9 de coniques-rapport : ellipse via le cercle directeur.

Ellipse (E) : x^2/a^2 + y^2/b^2 = 1, F'(-c,0), F(c,0), cercle directeur
C(F', 2a). P sur le cercle, M = med[PF] inter (F'P) : MF + MF' = 2a,
et med[PF] est la tangente a (E) en M.
Style gabarits : grille #9db3d8, tick_params sans etiquettes.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

A, B = 5.0, 3.0
C = np.sqrt(A ** 2 - B ** 2)
THETA = np.deg2rad(60.0)
OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/coniques-rapport/assets/fig09-ellipse-directeur-med.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

F = np.array([C, 0.0])
Fp = np.array([-C, 0.0])
P = Fp + 2 * A * np.array([np.cos(THETA), np.sin(THETA)])

# M sur la demi-droite [F'P) tel que MF + MF' = 2a (resolution numerique de s)
d = (P - Fp) / (2 * A)
f = lambda s: (s + np.linalg.norm(Fp + s * d - F)) - 2 * A
s = 2 * A / 2
for _ in range(200):
    s -= (f(s)) / (1 + np.dot(Fp + s * d - F, d)
                   / max(np.linalg.norm(Fp + s * d - F), 1e-12))
M = Fp + s * d
I = (P + F) / 2  # mil[PF], sur la mediatrice = tangente en M

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6, alpha=0.7)
ax.tick_params(labelbottom=False, labelleft=False,
               bottom=False, left=False)

th = np.linspace(0, 2 * np.pi, 600)
ax.plot(A * np.cos(th), B * np.sin(th), color="black",
        linewidth=1.6, label="(E)")
ax.plot(Fp[0] + 2 * A * np.cos(th), Fp[1] + 2 * A * np.sin(th),
        color="#808080", linewidth=1.0, label="C(F',2a)")
ax.plot([Fp[0], P[0]], [Fp[1], P[1]], color="#4d4d4d", linewidth=1.2)
ax.plot([P[0], F[0]], [P[1], F[1]], color="#4d4d4d",
        linewidth=1.0, linestyle=(0, (4, 3)))

# med[PF] (tangente en M) : droite passant par I et M, prolongee
u = M - I
u = u / np.linalg.norm(u)
t = np.linspace(-4, 6, 2)
ax.plot(I[0] + t * u[0], I[1] + t * u[1], color="black",
        linewidth=1.2, linestyle="--")
ax.text(I[0] + t[0] * u[0] - 1.9, I[1] + t[0] * u[1] - 0.15,
        "med[PF]", fontsize=11)

ax.axhline(0, color="black", linewidth=1.0)
for pt, name, dx, dy in ((Fp, "F'", -0.7, -0.55), (F, "F", 0.15, -0.55),
                         (np.zeros(2), "O", 0.1, -0.55),
                         (P, "P", 0.15, 0.15), (M, "M", 0.15, 0.15),
                         (I, "I", 0.15, -0.5)):
    ax.plot(pt[0], pt[1], "ko", markersize=4)
    ax.text(pt[0] + dx, pt[1] + dy, name, fontsize=11)

ax.set_xlim(-11, 8)
ax.set_ylim(-7, 10.5)
ax.set_title("Ellipse : M = med[PF] ∩ (F'P), P ∈ C(F',2a)", fontsize=12)
fig.tight_layout()
fig.savefig(OUT, dpi=110)
print("OK", OUT, "M:", M, "MF+MF'=", np.linalg.norm(M - F)
      + np.linalg.norm(M - Fp))
