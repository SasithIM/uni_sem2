from matplotlib import pyplot as plt
import numpy as np

time = np.linspace(-10 * np.pi, 10 * np.pi, 10000)

def sinc(time):
    return np.where(time == 0, 1.0, np.sin(time)/time)

def cof(array):
    return [-1 if int(i)==0 else 1 for i in array]

shifts = np.pi*np.array(range(10))
coefficients = np.array(cof('0011101000'))
combined_wave = np.zeros_like(time)

for shift, cf in zip(shifts, coefficients):
    sine_wave = cf*sinc(time - shift)
    combined_wave += sine_wave
    plt.plot(time, sine_wave, label=f'Shift {shift}', linestyle='--')

# plt.plot(time, combined_wave)
plt.title(f'Sinc Function')
plt.xlabel('Time (radians)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()