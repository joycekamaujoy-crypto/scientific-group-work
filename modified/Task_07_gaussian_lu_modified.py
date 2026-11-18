"""MODIFIED VERSION of Task F: change one measurement vector."""
import numpy as np
from scipy.linalg import lu_factor, lu_solve
A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
b = np.array([18., 10., 10.])  # CHANGED INPUT: first entry was 15
lu, piv = lu_factor(A)
x = lu_solve((lu, piv), b)
print("MODIFIED measurement vector:", b)
print("Solution:", np.round(x, 6))
print("Residual norm:", np.linalg.norm(b - A @ x))
