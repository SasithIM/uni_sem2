import numpy as np
import matplotlib.pyplot as plt

# Define the time axis (x-values)
t = np.linspace(0, 10 * np.pi, 1000)  # From 0 to 2π with 1000 points

# Define the number of sine waves to add
num_waves = 500  # Sum sine waves up to 5 Hz (1 Hz, 2 Hz, 3 Hz, 4 Hz, 5 Hz)

# Initialize the combined wave
combined_wave = np.zeros_like(t)

# Loop through each integer multiple and add the sine wave
for i in range(1, num_waves + 1, 2):
    frequency = i  # Frequency in Hz (1 Hz, 2 Hz, etc.)
    amplitude = 1.0 / i  # Amplitude decreases with frequency (optional)
    sine_wave = amplitude * np.sin(frequency * t) #* pow(-1, i)  # Add the sine wave
    combined_wave += sine_wave

    # Plot each individual sine wave (optional)
    plt.plot(t, sine_wave, label=f'{frequency} Hz, Amplitude {amplitude:.2f}', linestyle='--')

# Plot the combined sine wave
plt.plot(t, combined_wave, label='Combined Wave', linewidth=2)

# Add labels, title, and legend
plt.title(f'Sum of Sine Waves (1 Hz to {num_waves} Hz)')
plt.xlabel('Time (radians)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
# Show the plot
plt.show()