"""Reproduit la figure p.14 du 4e Bloc-Notes : lentille mince convergente.

Axe optique horizontal, lentille (double fleche verticale) en O, objet AB
en A (F entre A et O), image A'B' renversee, rayons B->O->B' et
B->(parallele)->F'->B'. Thales : AB/A'B' = OA/OA'.
Sortie : raw/bloc-notes/quatrieme-bloc-notes/assets/lentille-conjugaison.png
Usage : uv run scripts/reproduce_lentille_conjugaison.py (depuis Explore/lab/)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/bloc-notes/quatrieme-bloc-notes/assets/lentille-conjugaison.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

A, F, O, Fp, Ap = -3.0, -1.5, 0.0, 1.5, 3.5
hB, hBp = 1.2, -1.4  # hauteurs objet / image (renversee)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.set_aspect("equal")
ax.set_xlim(-4.2, 4.6)
ax.set_ylim(-2.2, 2.0)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
ax.set_axisbelow(True)

ax.axhline(0, color="gray", linewidth=1.0)  # axe optique
# lentille mince : trait vertical + pointes de fleche
ax.plot([O, O], [-1.7, 1.7], color="black", linewidth=1.5)
ax.annotate("", xy=(O, 1.9), xytext=(O, 1.6),
            arrowprops=dict(arrowstyle="->", color="black"))
ax.annotate("", xy=(O, -1.9), xytext=(O, -1.6),
            arrowprops=dict(arrowstyle="->", color="black"))

# objet AB et image A'B'
ax.plot([A, A], [0, hB], color="red", linewidth=2.0)
ax.annotate("", xy=(A, hB + 0.15), xytext=(A, 0),
            arrowprops=dict(arrowstyle="->", color="red"))
ax.plot([Ap, Ap], [0, hBp], color="red", linewidth=2.0)
ax.annotate("", xy=(Ap, hBp - 0.15), xytext=(Ap, 0),
            arrowprops=dict(arrowstyle="->", color="red"))

# rayon passant par O : B -> O -> B'
ax.plot([A, Ap], [hB, hBp], color="dimgray", linewidth=1.2)
# rayon parallele a l'axe puis par F' : B -> lentille -> F' -> B'
ax.plot([A, O], [hB, hB], color="dimgray", linewidth=1.2)
ax.plot([O, Ap], [hB, hBp], color="dimgray", linewidth=1.2)

for x, lab in [(A, "A"), (F, "F"), (O, "O"), (Fp, "F'"), (Ap, "A'")]:
    ax.plot(x, 0, "o", color="black", markersize=3)
    ax.text(x - 0.08, -0.28, lab, fontsize=12)
ax.text(A - 0.35, hB + 0.1, "B", color="red", fontsize=12)
ax.text(Ap + 0.05, hBp - 0.1, "B'", color="red", fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
