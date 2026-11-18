"""MODIFIED VERSION of Task D: rotate by 90 degrees instead of 45."""
import numpy as np
points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
angle_degrees = 90  # CHANGED PARAMETER: was 45
angle = np.deg2rad(angle_degrees)
rotation = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
scale = np.array([[2., 0.], [0., 1.5]])
transform = rotation @ scale
print(f"MODIFIED ROTATION ANGLE: {angle_degrees} degrees")
print("Transformed points:\n", np.round(points @ transform.T, 4))
