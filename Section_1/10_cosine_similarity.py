# Program 10: Calculate Cosine Similarity Between Two Vectors

import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([2, 3, 4])

dot_product = np.dot(vector_a, vector_b)
magnitude_a = np.linalg.norm(vector_a)
magnitude_b = np.linalg.norm(vector_b)

cosine_similarity = dot_product / (magnitude_a * magnitude_b)

print("Dot product:", dot_product)
print(f"Cosine similarity: {cosine_similarity:.4f}")