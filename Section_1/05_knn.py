# Program 5: Classify a Customer Using K-Nearest Neighbours (KNN)

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

income = np.array([[20], [25], [35], [45], [55], [65]])

customer_class = np.array(
    ["Low", "Low", "Medium", "Medium", "High", "High"]
)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(income, customer_class)

new_customer = np.array([[48]])
prediction = knn.predict(new_customer)

distances, indices = knn.kneighbors(new_customer)

print("New customer income:", new_customer[0, 0])
print("Nearest classes:", customer_class[indices[0]].tolist())
print("Distances:", distances[0].tolist())
print("Predicted class:", prediction[0])