"""Reproduit le schema p.123 du 4e Bloc-Notes : triangle ABC, sous-aires.

Triangle ABC au crayon (A en haut, B en bas a gauche, C a droite),
point interieur P relie aux sommets + marquage des sous-aires
A1 (haut), A2 (gauche), A3 (bas), A4 (droite) en bleu et des
longueurs m, y, x', t, z, b', d, c.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/triangle-sous-aires.png
Usage : uv run scripts/reproduce_triangle_sous_aires.py (depuis Explore/lab/)
"""

import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/triangle-sous-aires.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

A = (2.0, 3.6)
B = (0.0, 0.0)
C = (4.4, 0.3)
P = (2.05, 1.35)  # point interieur

fig, ax = plt.subplots(figsize=(6, 5.2))
ax.set_aspect("equal")
ax.set_xlim(-0.7, 5.1)
ax.set_ylim(-0.6, 4.2)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

# triangle ABC (crayon gris)
for X, Y in ((A, B), (B, C), (C, A)):
    ax.plot([X[0], Y[0]], [X[1], Y[1]], color="dimgray", linewidth=1.2)
# ceviennes depuis P (crayon)
for S in (A, B, C):
    ax.plot([P[0], S[0]], [P[1], S[1]], color="dimgray", linewidth=0.9)
ax.plot([P[0]], [P[1]], marker="o", markersize=3, color="dimgray")

# sommets
ax.text(A[0] - 0.05, A[1] + 0.15, "A", fontsize=13)
ax.text(B[0] - 0.28, B[1] - 0.05, "B", fontsize=13)
ax.text(C[0] + 0.08, C[1] - 0.05, "C", fontsize=13)

# sous-aires A1..A4 (bleu comme au manuscrit)
ax.text(2.0, 2.75, "A₁", fontsize=12, color="blue")
ax.text(1.05, 1.15, "A₂", fontsize=12, color="blue")
ax.text(1.95, 0.55, "A₃", fontsize=12, color="blue")
ax.text(2.85, 1.2, "A₄", fontsize=12, color="blue")

# longueurs annotees (bleu, positions du manuscrit)
ax.text(1.35, 2.05, "m", fontsize=11, color="blue")
ax.text(2.25, 2.0, "y", fontsize=11, color="blue")
ax.text(0.75, 1.45, "x'", fontsize=11, color="blue")
ax.text(1.55, 1.05, "t", fontsize=11, color="blue")
ax.text(2.45, 0.75, "z", fontsize=11, color="blue")
ax.text(3.35, 1.35, "b'", fontsize=11, color="blue")
ax.text(2.0, -0.25, "d", fontsize=11, color="blue")
ax.text(0.55, 2.6, "c", fontsize=11, color="blue")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
