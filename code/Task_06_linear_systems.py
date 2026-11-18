"""
TASK E: Solution of Systems of Linear Equations
Real-world case: estimating the number of two server types from resource totals.
"""
import numpy as np

# Unknowns: x = Type A servers; y = Type B servers.
# Type A: 4 CPU units and 8 GB RAM. Type B: 2 CPU units and 12 GB RAM.
# Known totals: 20 CPU units and 72 GB RAM.
A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])
b = np.array([20.0, 72.0])

# Solve Ax=b. Do not use an explicit inverse for this task.
solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A server units: {solution[0]:.0f}")
print(f"Type B server units: {solution[1]:.0f}")
print("Check A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
