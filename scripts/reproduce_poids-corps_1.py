"""Reproduit le fond de poids-corps : poids P = M g applique en G, centre de masse.
Manuscrit : dP = dm g, torseur, M_G, G_z centre de masse des solides.
Vue : corps rectangulaire, point G, fleche poids vers le bas, axe z.
Sortie : raw/physique/poids-corps/assets/poids-centre-masse.png
Usage : uv run scripts/reproduce_poids-corps_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/poids-corps/assets/poids-centre-masse.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 2)
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.add_patch(patches.Rectangle((-1, -1), 2, 2, facecolor="#cfe0f7", edgecolor="#1a3fb5", linewidth=1.8))
ax.plot(0, 0, "o", color="red", markersize=9)
ax.text(0.12, 0.12, "G (centre de masse)", color="red", fontsize=11)
ax.annotate("", xy=(0, -2.2), xytext=(0, -0.1),
            arrowprops=dict(arrowstyle="->", color="red", linewidth=2.2))
ax.text(0.15, -1.4, "P = M g", color="red", fontsize=12)
ax.text(-1.6, 1.3, "dP = dm g", color="#1a3fb5", fontsize=11)
ax.text(-1.6, 0.9, "solide (V)", color="#1a3fb5", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
