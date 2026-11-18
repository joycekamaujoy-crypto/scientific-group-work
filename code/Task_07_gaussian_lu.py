"""
TASK F: Gaussian Elimination and LU Decomposition
Real-world case: solving repeated measurement systems with the same coefficient matrix.
"""
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# INPUT: coefficient matrix A is reused for several measurement vectors b.
A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])
measurement_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]

# Factorize A once; reuse the LU factors for each new right-hand side.
lu, piv = lu_factor(A)

for number, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    print(f"Measurement set {number}")
    print("Solution:", np.round(x, 6))
    print("Residual norm:", np.linalg.norm(residual))
    print()

# Compare with a direct solve for the first measurement set.
print("Direct solution:", np.linalg.solve(A, measurement_sets[0]))
