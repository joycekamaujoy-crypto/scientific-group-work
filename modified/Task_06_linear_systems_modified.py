"""MODIFIED VERSION of Task E: increase observed CPU total."""
import numpy as np
A = np.array([[4., 2.], [8., 12.]])
b = np.array([24., 72.])  # CHANGED INPUT: CPU total was 20, now 24
solution = np.linalg.solve(A, b)
print("MODIFIED CPU total:", b[0])
print(f"Type A server units: {solution[0]:.2f}")
print(f"Type B server units: {solution[1]:.2f}")
print("Verification:", A @ solution)
