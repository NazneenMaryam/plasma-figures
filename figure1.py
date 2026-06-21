from pathlib import Path
import sys

try:
    import matplotlib.pyplot as plt  # type: ignore[import]
except ImportError as exc:
    print("Error: matplotlib is required to run this script. Install it with `pip install matplotlib`.")
    raise SystemExit(1) from exc

try:
    import numpy as np  # type: ignore[import]
except ImportError as exc:
    print("Error: numpy is required to run this script. Install it with `pip install numpy`.")
    raise SystemExit(1) from exc



time = np.linspace(0, 8, 1000)

-
monochromatic_srs = 1 / (
    1 + np.exp(-2.2 * (time - 3.2))
)

monochromatic_srs = (
    0.68
    * monochromatic_srs
    / np.max(monochromatic_srs)
)

background = 0.035 * (
    1 - np.exp(-0.8 * time)
)

burst_1 = 0.11 * np.exp(
    -((time - 1.8) / 0.18) ** 2
)

burst_2 = 0.20 * np.exp(
    -((time - 2.9) / 0.17) ** 2
)

burst_3 = 0.62 * np.exp(
    -((time - 4.1) / 0.22) ** 2
)

burst_4 = 0.30 * np.exp(
    -((time - 5.4) / 0.25) ** 2
)

burst_5 = 0.21 * np.exp(
    -((time - 6.6) / 0.22) ** 2
)

broadband_srs = (
    background
    + burst_1
    + burst_2
    + burst_3
    + burst_4
    + burst_5
)



fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    time,
    monochromatic_srs,
    linewidth=2.2,
    color="navy",
    label="Monochromatic laser"
)

ax.plot(
    time,
    broadband_srs,
    linewidth=2.0,
    color="darkorange",
    label="Broadband laser"
)

maximum_index = np.argmax(broadband_srs)

maximum_time = time[maximum_index]
maximum_value = broadband_srs[maximum_index]

ax.annotate(
    "Strong intermittent SRS burst",
    xy=(maximum_time, maximum_value),
    xytext=(4.8, 0.78),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=1.2
    ),
    fontsize=10
)



ax.set_xlabel("Time (arbitrary units)")
ax.set_ylabel("Normalized SRS reflectivity")

ax.set_title(
    "Conceptual illustration of intermittent SRS bursts"
)

ax.set_xlim(0, 8)
ax.set_ylim(0, 0.9)

ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()


code_folder = Path(__file__).resolve().parent

output_file = (
    code_folder
    / "figure4_intermittent_srs_bursts.png"
)

fig.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

print("Figure 4 created successfully.")
print(f"Saved at: {output_file}")

plt.show()
