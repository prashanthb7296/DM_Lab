# Program 7: Divisive Hierarchical Clustering

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

data = np.array([
    [1, 1], [1.5, 1.5],
    [5, 5], [5.5, 5],
    [9, 1], [9.5, 1.5]
])

required_clusters = 3

def squared_error(indices):
    points = data[indices]
    centre = points.mean(axis=0)
    return np.sum((points - centre) ** 2)

clusters = [np.arange(len(data))]

while len(clusters) < required_clusters:
    split_position = max(
        (
            i for i, indices in enumerate(clusters)
            if len(indices) > 1
        ),
        key=lambda i: squared_error(clusters[i])
    )

    indices = clusters.pop(split_position)

    splitter = KMeans(
        n_clusters=2,
        random_state=42,
        n_init=10
    )

    sub_labels = splitter.fit_predict(data[indices])

    clusters.append(indices[sub_labels == 0])
    clusters.append(indices[sub_labels == 1])

# Order the final clusters from left to right
clusters.sort(key=lambda indices: data[indices, 0].mean())

labels = np.empty(len(data), dtype=int)

for cluster_no, indices in enumerate(clusters, start=1):
    labels[indices] = cluster_no

for i, (point, label) in enumerate(zip(data, labels), start=1):
    print(f"P{i} {point.tolist()} -> Cluster {label}")

for cluster_no in range(1, required_clusters + 1):
    points = data[labels == cluster_no]

    plt.scatter(
        points[:, 0],
        points[:, 1],
        label=f"Cluster {cluster_no}"
    )

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Divisive Hierarchical Clustering")
plt.legend()
plt.show()