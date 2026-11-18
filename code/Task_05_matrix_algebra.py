"""
TASK D: Matrix Algebra and Matrix Operations
Real-world case: rotate and scale 2-D points in a graphics application.
"""
import numpy as np

# INPUT: four square corners, represented as row-wise [x, y] coordinates.
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

angle_degrees = 45
angle = np.deg2rad(angle_degrees)

# Rotation and non-uniform scaling matrices.
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combine transformations. Row-wise points multiply by the transpose.
transformation = rotation @ scale
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Combined transformation matrix:\n", transformation)
print("Transformed points:\n", np.round(transformed_points, 4))
print("Determinant:", np.linalg.det(transformation))
