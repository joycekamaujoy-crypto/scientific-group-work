"""MODIFIED VERSION of Task C: use a more accurate square-root approximation."""
import numpy as np
true_value = np.sqrt(2)
approx_value = 1.414213  # CHANGED INPUT: closer to sqrt(2) than 1.414
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print("MODIFIED APPROXIMATION:", approx_value)
print(f"Absolute error: {absolute_error:.10f}")
print(f"Relative error: {relative_error:.8%}")
print("Smaller approximation error means a more accurate estimate.")
