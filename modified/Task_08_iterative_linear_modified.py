"""MODIFIED VERSION of Task G: change the right boundary influence."""
import numpy as np
A = np.array([[2.,-1.,0.,0.,0.],[-1.,2.,-1.,0.,0.],
              [0.,-1.,2.,-1.,0.],[0.,0.,-1.,2.,-1.],
              [0.,0.,0.,-1.,2.]])
b = np.array([100., 0., 0., 0., 40.])  # CHANGED: right boundary influence 20 -> 40
x = np.zeros_like(b)
tol = 1e-8
for iteration in range(500):
    old = x.copy()
    for i in range(len(b)):
        x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
    if np.linalg.norm(x - old, ord=np.inf) < tol:
        break
print("MODIFIED right boundary influence: 40")
print("Gauss-Seidel temperatures:", np.round(x, 6))
print("Iterations:", iteration + 1)
