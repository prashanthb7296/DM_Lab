# Program 4: Calculate Euclidean Distance

import numpy as np

customer_a = np.array([25, 45000])
customer_b = np.array([30, 52000])

difference = customer_a - customer_b
euclidean_distance = np.sqrt(np.sum(difference ** 2))

print("Difference vector:", difference)
print(f"Euclidean distance = {euclidean_distance:.4f}")