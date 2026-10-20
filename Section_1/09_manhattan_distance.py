# Program 9: Calculate Manhattan Distance

import numpy as np

point_a = np.array([2, 4, 6])
point_b = np.array([5, 1, 2])

absolute_differences = np.abs(point_a - point_b)
manhattan_distance = np.sum(absolute_differences)

print("Absolute differences:", absolute_differences.tolist())
print("Manhattan distance:", manhattan_distance)