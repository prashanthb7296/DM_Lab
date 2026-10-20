# Program 5: Customer Segmentation Using K-Means Clustering

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

age = [22, 25, 28, 40, 42, 45]
spending_score = [20, 25, 30, 70, 75, 80]

data = np.column_stack((age, spending_score))

model = KMeans(n_clusters=2, random_state=42, n_init=10)
raw_labels = model.fit_predict(data)

# Rename clusters according to increasing centroid age
order = np.argsort(model.cluster_centers_[:, 0])
label_map = {old: new + 1 for new, old in enumerate(order)}
segments = np.array([label_map[label] for label in raw_labels])
centres = model.cluster_centers_[order]

for i, (customer, segment) in enumerate(zip(data, segments), 1):
    print(f"Customer {i}: {customer.tolist()} -> Segment {segment}")

print("Centroids:", np.round(centres, 2).tolist())

for segment in [1, 2]:
    points = data[segments == segment]
    plt.scatter(
        points[:, 0],
        points[:, 1],
        label=f"Segment {segment}"
    )

plt.scatter(
    centres[:, 0],
    centres[:, 1],
    marker="X",
    s=180,
    color="black",
    label="Centroids"
)

plt.xlabel("Customer Age")
plt.ylabel("Spending Score")
plt.title("K-Means Customer Segmentation")
plt.legend()
plt.show()