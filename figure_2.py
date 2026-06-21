from pathlib import Path
import sys

try:
    import matplotlib.pyplot as plt  
except ImportError:
    print("matplotlib is required to generate the figure. Install it with 'pip install matplotlib'.")
    sys.exit(1)

case_names = [
    "Monochromatic\nplane wave",
    "Low-coherence\nplane wave",
    "Monochromatic\nwith CPP",
    "Low-coherence\nwith CPP"
]

sbs_reflectivity = [
    27.36,
    8.78,
    49.45,
    10.34
]

bar_colors = [
    "steelblue",
    "orange",
    "seagreen",
    "crimson"
]

fig, ax = plt.subplots(figsize=(9, 5.5))

bars = ax.bar(
    case_names,
    sbs_reflectivity,
    width=0.45,          # reduced bar width
    color=bar_colors     # different color for each bar
)


for bar, value in zip(bars, sbs_reflectivity):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 1,
        f"{value:.2f}%",
        ha="center",
        va="bottom",
        fontsize=10
    )

ax.set_xlabel("Laser condition")
ax.set_ylabel("Overall SBS reflectivity (%)")
ax.set_title(
    "Comparison of SBS reflectivity for monochromatic "
    "and low-coherence lasers"
)

ax.set_ylim(0, 60)
ax.grid(axis="y", alpha=0.3)

fig.tight_layout()

code_folder = Path(__file__).resolve().parent

output_file = (
    code_folder
    / "figure3_sbs_reflectivity_comparison.png"
)

fig.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

print("Figure 3 created successfully.")
print(f"Saved at: {output_file}")

plt.show()
