from pathlib import Path

try:
    import matplotlib  # type: ignore[import]
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore[import]
except ImportError as exc:
    raise SystemExit(
        "Required modules are missing. Install with: pip install matplotlib"
    ) from exc


# --------------------------------------------------
# Electron-density range used in the reviewed study
# --------------------------------------------------
electron_density = [
    0.12,
    0.14,
    0.16,
    0.18,
    0.20
]


# --------------------------------------------------
# Qualitative normalized trends
#
# At lower density:
# kinetic effects and hot-electron production
# become more important.
#
# At higher density:
# broadband suppression of fluid nonlinearities
# becomes more effective.
# --------------------------------------------------
fluid_suppression = [
    0.12,
    0.28,
    0.52,
    0.74,
    0.88
]

kinetic_hot_electron_risk = [
    0.90,
    0.76,
    0.50,
    0.28,
    0.15
]


# --------------------------------------------------
# Create the graph
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    electron_density,
    fluid_suppression,
    marker="o",
    markersize=7,
    linewidth=2.2,
    color="seagreen",
    label="Suppression of fluid nonlinearities"
)

ax.plot(
    electron_density,
    kinetic_hot_electron_risk,
    marker="s",
    markersize=7,
    linewidth=2.2,
    color="darkorange",
    label="Kinetic hot-electron risk"
)


# --------------------------------------------------
# Mark the approximate transition region
# --------------------------------------------------
ax.axvline(
    x=0.16,
    linestyle="--",
    linewidth=1.2,
    color="gray"
)

ax.text(
    0.1605,
    0.95,
    "Approximate transition",
    rotation=90,
    va="top",
    fontsize=9
)


# --------------------------------------------------
# Axis labels and title
# --------------------------------------------------
ax.set_xlabel(r"Electron density, $n_e/n_c$")
ax.set_ylabel("Qualitative normalized level")

ax.set_title(
    "Density-dependent behavior of broadband-driven BSRS"
)

ax.set_xlim(0.115, 0.205)
ax.set_ylim(0, 1.0)

ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()


# --------------------------------------------------
# Save the graph in the same folder as this file
# --------------------------------------------------
code_folder = Path(__file__).resolve().parent

output_file = (
    code_folder
    / "figure5_density_regime_summary.png"
)

fig.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

print("Figure 5 created successfully.")
print(f"Saved at: {output_file}")

plt.show()