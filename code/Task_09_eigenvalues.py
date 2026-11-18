"""
TASK H: Eigenvalues and Eigenvectors
Real-world case: estimating the structural importance of nodes in a network.
"""
import numpy as np

# Adjacency matrix for an undirected network; node order is A, B, C, D.
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

# Each eigenvector is stored as a column in eigenvectors.
eigenvalues, eigenvectors = np.linalg.eig(A)

# Select the eigenvector associated with the largest real eigenvalue.
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Normalize scores so that they add to 1.
centrality = dominant_vector / dominant_vector.sum()
nodes = ["A", "B", "C", "D"]

print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify A v = lambda v.
v = np.real(eigenvectors[:, index])
print("Verification error:", np.linalg.norm(A @ v - dominant_value * v))
