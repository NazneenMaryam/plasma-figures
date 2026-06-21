from pathlib import Path

try:
    import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]
except ImportError as exc:
    raise ImportError(
        "matplotlib is required to run this script. "
        "Install it with `pip install matplotlib`."
    ) from exc

try:
    import numpy as np  # type: ignore[reportMissingModuleSource]
except ImportError as exc:
    raise ImportError(
        "numpy is required to run this script. "
        "Install it with `pip install numpy`."
    ) from exc

# Make the random phases reproducible
np.random.seed(10)

# Time axis
time = np.linspace(0, 10, 5000)

# Broadband laser parameters
number_of_components = 40
central_frequency = 2 * np.pi * 20
relative_bandwidth = 0.08

total_bandwidth = relative_bandwidth * central_frequency

# Frequency components around the central frequency
frequencies = central_frequency + np.linspace(
    -total_bandwidth / 2,
    total_bandwidth / 2,
    number_of_components
)

# Random phase for each frequency component
phases = np.random.uniform(
    0,
    2 * np.pi,
    number_of_components
)

# Calculate the total electric field
electric_field = np.zeros_like(time)

for frequency, phase in zip(frequencies, phases):
    electric_field += (
        np.cos(frequency * time + phase)
        / np.sqrt(number_of_components)
    )

# Laser intensity is proportional to the square of the electric field
broadband_intensity = electric_field**2

# Normalize the average broadband intensity to 1
broadband_intensity /= np.mean(broadband_intensity)

# Constant narrowband reference intensity
narrowband_intensity = np.ones_like(time)

# Create the graph
fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    time,
    broadband_intensity,
    linewidth=1.2,
    label="Broadband laser"
)
ax.plot( time, narrowband_intensity, linewidth=2, label="Narrowband laser" )

ax.set_xlabel("Time (Seconds)")
ax.set_ylabel("Normalized laser intensity")
ax.set_title("Temporal intensity modulation of a broadband laser")

ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()

# Save the image in the same folder as this Python file
code_folder = Path(__file__).resolve().parent
output_file = code_folder / "figure5_broadband_pulses.png"

fig.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

print("Figure 5 created successfully.")
print(f"Saved at: {output_file}")

plt.show()
