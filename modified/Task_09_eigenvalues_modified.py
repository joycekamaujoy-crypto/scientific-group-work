"""MODIFIED VERSION of Task H: add a link between nodes A and D."""
import numpy as np
A = np.array([[0.,1.,1.,1.],  # CHANGED: A-D connection added
              [1.,0.,1.,1.],
              [1.,1.,0.,1.],
              [1.,1.,1.,0.]])
values, vectors = np.linalg.eig(A)
i = np.argmax(np.real(values))
scores = np.abs(np.real(vectors[:, i]))
scores /= scores.sum()
print("MODIFIED NETWORK: added an A-D connection.")
for node, score in zip(["A","B","C","D"], scores):
    print(f"{node}: {score:.4f}")
