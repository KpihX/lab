"""Reproduit les schemas (a) et (c) p.2 de signaux-corde : elongations triangulaires.

Figures d'origine (imprimees) : (a) y_S1(t) en cm, triangle montant de
(0,0) a (20 ms, 2 cm) puis descendant a (30 ms, 0) ; (c) y_S2(t), pic de
2 cm a 10 ms puis descente a (30 ms, 0).

Style "stylo" : courbes bleues, pic et cotes rouges, fond quadrille bleu.

Sortie : raw/physique/signaux-corde/assets/elongations-s1-s2.png

Usage :
  uv run scripts/reproduce_signaux_corde_2.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_signaux_corde_2.py
>>> # OK -> .../assets/elongations-s1-s2.png (XXXXX o)
>>> # le rendu montre les deux triangles y_S1(t) et y_S2(t).
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/physique/signaux-corde/assets/elongations-s1-s2.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"

fig, axes = plt.subplots(2, 1, figsize=(7, 6), sharex=True)
for ax in axes:
    ax.set_xlim(-1, 34)
    ax.set_ylim(-0.4, 2.8)
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

# (a) y_S1 : pic 2 cm a 20 ms, retour a 0 a 30 ms.
ax = axes[0]
ax.annotate("", xy=(32, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.annotate("", xy=(0, 2.6), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.plot([0, 20, 30], [0, 2, 0], color=BLUE, linewidth=1.8)
ax.plot(20, 2, "o", color=RED, markersize=5)
ax.plot([20, 20], [0, 2], color=RED, linewidth=1.0, linestyle=(0, (4, 3)))
ax.text(20.4, 2.1, "2", color=RED, fontsize=11)
ax.text(10, -0.3, "10", color=BLUE, fontsize=10)
ax.text(20, -0.3, "20", color=BLUE, fontsize=10)
ax.text(30, -0.3, "30", color=BLUE, fontsize=10)
ax.text(33, -0.15, "t (ms)", color=BLUE, fontsize=11)
ax.text(-0.9, 2.3, "yS1 (cm)", color=BLUE, fontsize=11)
ax.text(24, 2.3, "(a)", color=BLUE, fontsize=12)

# (c) y_S2 : pic 2 cm a 10 ms, retour a 0 a 30 ms.
ax = axes[1]
ax.annotate("", xy=(32, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.annotate("", xy=(0, 2.6), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=BLUE, linewidth=1.4))
ax.plot([0, 10, 30], [0, 2, 0], color=BLUE, linewidth=1.8)
ax.plot(10, 2, "o", color=RED, markersize=5)
ax.plot([10, 10], [0, 2], color=RED, linewidth=1.0, linestyle=(0, (4, 3)))
ax.text(10.4, 2.1, "2", color=RED, fontsize=11)
ax.text(10, -0.3, "10", color=BLUE, fontsize=10)
ax.text(20, -0.3, "20", color=BLUE, fontsize=10)
ax.text(30, -0.3, "30", color=BLUE, fontsize=10)
ax.text(33, -0.15, "t (ms)", color=BLUE, fontsize=11)
ax.text(-0.9, 2.3, "yS2 (cm)", color=BLUE, fontsize=11)
ax.text(24, 2.3, "(c)", color=BLUE, fontsize=12)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
