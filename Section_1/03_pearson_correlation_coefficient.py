# Program 3: Calculate Pearson Correlation Coefficient

import numpy as np

study_hours = np.array([2, 3, 4, 5, 6, 7])
marks = np.array([40, 50, 60, 70, 80, 90])

correlation_matrix = np.corrcoef(study_hours, marks)
pearson_r = correlation_matrix[0, 1]

print(f"Pearson correlation coefficient = {pearson_r:.2f}")