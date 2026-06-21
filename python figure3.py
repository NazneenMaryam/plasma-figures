from pathlib import Path

try:
    from matplotlib import pyplot as plt 
except ImportError as exc:
    raise ImportError(
        "Required package matplotlib not found. Install matplotlib to run this script."
    ) from exc

import math


speed_of_light = 299792458.0


laser_wavelength = 351e-9


laser_period_fs = (
    laser_wavelength / speed_of_light
) * 1e15


bandwidth_percent = [0.5, 0.6, 1.0, 1.5, 2.5, 5.0, 10.0]


relative_bandwidth = [b / 100.0 for b in bandwidth_percent]


coherence_time_fs = [laser_period_fs / rb for rb in relative_bandwidth]


fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    bandwidth_percent,
    coherence_time_fs,
    marker="o",
    linewidth=2,
    label="Coherence time"
)


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
