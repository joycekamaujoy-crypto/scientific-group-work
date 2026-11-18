"""
TASK A: NumPy Arrays and Numerical Computation
Real-world case: daily weather-station temperature readings.
"""
import numpy as np

# INPUT: 24 hourly temperatures in degrees Celsius.
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# OPERATIONS: descriptive statistics and vectorized unit conversion.
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)
temperatures_f = 1.8 * temperatures_c + 32

# OUTPUT: summary statistics and a sample of converted readings.
print(f"Daily mean: {mean_temp:.2f} °C")
print(f"Minimum: {min_temp:.2f} °C")
print(f"Maximum: {max_temp:.2f} °C")
print("First six Fahrenheit readings:", np.round(temperatures_f[:6], 2))
