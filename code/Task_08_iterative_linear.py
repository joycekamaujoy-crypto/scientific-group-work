"""
TASK G: Iterative Methods for Linear Systems
Real-world case: steady-state temperatures at five interior points in a wall.
"""
import numpy as np
import matplotlib.pyplot as plt

# A diagonally dominant coefficient matrix encourages convergence.
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])
# Boundary influence: left = 100°C; right = 20°C.
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    """Jacobi updates all unknowns using values from the previous iteration."""
    diagonal = np.diag(A)
    remainder = A - np.diagflat(diagonal)
    x = np.zeros_like(b, dtype=float)
    errors = []

    for _ in range(max_iter):
        new_x = (b - remainder @ x) / diagonal
        error = np.linalg.norm(new_x - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return new_x, errors
        x = new_x
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    """Gauss-Seidel immediately reuses updated values within an iteration."""
    x = np.zeros_like(b, dtype=float)
    errors = []

    for _ in range(max_iter):
        old_x = x.copy()
        for i in range(len(b)):
            left = A[i, :i] @ x[:i]
            right = A[i, i + 1:] @ old_x[i + 1:]
            x[i] = (b[i] - left - right) / A[i, i]
        error = np.linalg.norm(x - old_x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi temperatures:", np.round(x_j, 6))
print("Gauss-Seidel temperatures:", np.round(x_gs, 6))
print("Direct solution:", np.round(x_exact, 6))
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
