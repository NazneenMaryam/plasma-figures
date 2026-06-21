from pathlib import Path

try:
    import matplotlib.pyplot as plt  # type: ignore[import]  # pylint: disable=import-error
except ImportError as err:
    raise ImportError(
        "matplotlib is required to run this script. Install it with "
        "'pip install matplotlib'."
    ) from err

# Maximum SRS/driving-pulse field ratios reported by Guo et al.
case_names = [
    "Narrowband\nLG pulse",
    "Broadband\nLG pulse",
    "Narrowband\nlight spring",
    "Broadband light spring\nwith random phases"
]

srs_field_ratio = [
    0.36,
    0.20,
    0.15,
    0.05
]

# Different color for each bar
bar_colors = [
    "steelblue",
    "darkorange",
    "seagreen",
    "crimson"
]


# Create the graph
fig, ax = plt.subplots(figsize=(9, 5.5))

bars = ax.bar(
    case_names,
    srs_field_ratio,
    width=0.30,
    color=bar_colors
)


# Write the value above each bar
for bar, value in zip(bars, srs_field_ratio):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.012,
        f"{value:.2f}",
        ha="center",
        va="bottom",
        fontsize=10
    )


# Axis labels and title
ax.set_xlabel("Laser condition")
ax.set_ylabel(
    "Maximum SRS / driving-pulse field ratio"
)

ax.set_title(
    "Suppression of SRS by temporal and angular incoherence"
)

ax.set_ylim(0, 0.42)
ax.grid(axis="y", alpha=0.3)

fig.tight_layout()


# Save the image in the same folder as this Python file
code_folder = Path(__file__).resolve().parent

output_file = (
    code_folder
    / "figure6_angular_incoherence_srs.png"
)

fig.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

print("Figure 6 created successfully.")
print(f"Saved at: {output_file}")

plt.show()