from pathlib import Path

try:
    from matplotlib import pyplot as plt  # type: ignore[import]
except ImportError as exc:
    raise ImportError(
        "Required package matplotlib not found. Install matplotlib to run this script."
    ) from exc

import math

# Speed of light in vacuum (m/s)
speed_of_light = 299792458.0

# Laser wavelength: 351 nm
laser_wavelength = 351e-9

# Calculate the laser period in femtoseconds
laser_period_fs = (
    laser_wavelength / speed_of_light
) * 1e15

# Relative laser bandwidth values in percent
bandwidth_percent = [0.5, 0.6, 1.0, 1.5, 2.5, 5.0, 10.0]

# Convert percentage values into fractional values
relative_bandwidth = [b / 100.0 for b in bandwidth_percent]

# Coherence time:
# tau_c = 2*pi / Delta_omega
#
# Since:
# Delta_omega = relative_bandwidth * omega_0
#
# and:
# omega_0 = 2*pi / T_0
#
# therefore:
# tau_c = T_0 / relative_bandwidth
coherence_time_fs = [laser_period_fs / rb for rb in relative_bandwidth]

# Create the graph
fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    bandwidth_percent,
    coherence_time_fs,
    marker="o",
    linewidth=2,
    label="Coherence time"
)

# Add the calculated value above each point
for bandwidth, coherence_time in zip(
    bandwidth_percent,
    coherence_time_fs
):
    ax.text(
        bandwidth,
        coherence_time + 5,
        f"{coherence_time:.0f}",
        ha="center",
        fontsize=9
    )

ax.set_xlabel("Relative laser bandwidth (%)")
ax.set_ylabel("Coherence time (fs)")
ax.set_title(
    "Coherence time as a function of laser bandwidth"
)

ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()

# Save the image in the same folder as this Python file
code_folder = Path(__file__).resolve().parent

output_file = (
    code_folder
    / "figure2_coherence_time_vs_bandwidth.png"
)

fig.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

print("Figure 2 created successfully.")
print(f"Saved at: {output_file}")

plt.show()