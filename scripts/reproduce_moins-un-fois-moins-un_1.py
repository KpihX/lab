"""Reproduit le fond de moins-un-fois-moins-un : (-1)x(-1)=1, inverses pour +.
Manuscrit : (-1)x(-1)+(-1)=0 et (-1)+1=0 donc (-1)x(-1)=1 par unicite de l'inverse.
Vue : droite graduee -1, 0, 1, fleches oppose/inverse, point produit.
Sortie : raw/algebre-arithmetique/moins-un-fois-moins-un/assets/anneau-moins-un.png
Usage : uv run scripts/reproduce_moins-un-fois-moins-un_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/algebre-arithmetique/moins-un-fois-moins-un/assets/anneau-moins-un.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 3.2))
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1, 1)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.axhline(0, color="black", linewidth=1.2)
for x, lab, col in [(-1, "-1", "#1a3fb5"), (0, "0", "black"), (1, "1", "#1a3fb5"), (1, "(-1)x(-1)=1", "red")]:
    ax.plot(x, 0, "o", color=col, markersize=9)
ax.text(-1, 0.25, "-1", color="#1a3fb5", fontsize=12, ha="center")
ax.text(0, 0.25, "0 neutre +", color="black", fontsize=11, ha="center")
ax.text(1, 0.25, "1", color="red", fontsize=12, ha="center")
ax.text(1, -0.45, "(-1)x(-1) = 1", color="red", fontsize=11, ha="center")
ax.annotate("", xy=(-0.9, -0.2), xytext=(0.9, -0.2),
            arrowprops=dict(arrowstyle="<->", color="#1a3fb5", linewidth=1.4))
ax.text(0, -0.35, "+ inverses", color="#1a3fb5", fontsize=10, ha="center")

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
