"""MODIFIED VERSION of Task A: warmer daily readings."""
import numpy as np
temperatures_c = np.array([
    20.5, 20.0, 19.8, 19.5, 19.9, 21.0,
    23.5, 25.8, 27.6, 29.1, 30.3, 31.0,
    31.4, 31.1, 30.5, 29.6, 28.2, 26.8,
    25.4, 24.1, 23.0, 22.2, 21.6, 21.0
])
print("MODIFIED INPUT: readings increased by 2°C.")
print(f"New mean: {np.mean(temperatures_c):.2f} °C")
print(f"New minimum: {np.min(temperatures_c):.2f} °C")
print(f"New maximum: {np.max(temperatures_c):.2f} °C")
print("First six Fahrenheit readings:", np.round(1.8 * temperatures_c[:6] + 32, 2))
