"""Reproduit le schema p.1 de hint-bornes-denombrable.

Figure d'origine (stylo bleu) : droite graduee de Inf(A)
(point plein) a Sup(A) (point vide), partition de l'intervalle
support I en I1, I2, I3, ... avec marques 1/2, 1/4, 1/8 et
mention d = SupA - InfA.

Sortie : raw/ensembles-cardinaux/hint-bornes-denombrable/assets/hint-bornes-denombrable-1.png

Usage :
  uv run scripts/reproduce_hint-bornes-denombrable_1.py   (depuis ~/KpihX-Labs/Explore/lab/)
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/ensembles-cardinaux"
    "/hint-bornes-denombrable/assets/hint-bornes-denombrable-1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, ax = plt.subplots(figsize=(9, 2.6))
ax.set_xlim(-0.1, 10.6)
ax.set_ylim(-1.1, 1.1)
ax.grid(True, which="major", color="#9db3d8", linewidth=0.8)
ax.grid(True, which="minor", color="#9db3d8", linewidth=0.3, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Droite support avec fleches aux deux bouts.
ax.annotate("", xy=(10.3, 0), xytext=(-0.05, 0),
            arrowprops=dict(arrowstyle="<->", color="black", linewidth=1.2))
# Bornes : Inf(A) point plein, Sup(A) point vide.
ax.scatter([0], [0], color=BLUE, s=70, zorder=3)
ax.scatter([10], [0], facecolor="white", edgecolor=RED, s=70,
           linewidths=1.6, zorder=3)
ax.text(0, -0.55, "Inf(A)", color=BLUE, ha="center", fontsize=11)
ax.text(10, -0.55, "Sup(A)", color=BLUE, ha="center", fontsize=11)

# Marques de partition : 1/2, puis 1/4, puis 1/8.
for x, lab in [(5, "1/2"), (7.5, "1/4"), (8.75, "1/8")]:
    ax.plot([x, x], [-0.12, 0.12], color=RED, linewidth=1.4)
    ax.text(x, 0.30, lab, color=RED, ha="center", fontsize=10)
for x in [9.375, 9.6875]:
    ax.plot([x, x], [-0.08, 0.08], color=RED, linewidth=1.0)

# Accolades des sous-intervalles I1, I2, I3, ...
def brace(x0, x1, y, label):
    ax.annotate("", xy=(x0, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="-[, widthB=2.0, lengthB=0.6",
                                color=BLUE, linewidth=1.2))
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="-[, widthB=2.0, lengthB=0.6",
                                color=BLUE, linewidth=1.2))
    ax.text((x0 + x1) / 2, y - 0.22, label, color=BLUE,
            ha="center", fontsize=11)

brace(0, 5, -0.28, "I1")
brace(5, 7.5, -0.28, "I2")
brace(7.5, 8.75, -0.28, "I3")

ax.text(10.35, 0.45, "d = SupA - InfA", color="black", fontsize=10)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
