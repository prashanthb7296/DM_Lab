# Program 6: Agglomerative Hierarchical Clustering

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

data = np.array([
    [1, 1], [1.5, 1.5],
    [5, 5], [5.5, 5],
    [9, 1], [9.5, 1.5]
])

model = AgglomerativeClustering(n_clusters=3, linkage="ward")
raw_labels = model.fit_predict(data)

# Rename clusters from left to right for readable output
groups = [
    np.where(raw_labels == label)[0]
    for label in np.unique(raw_labels)
]
groups.sort(key=lambda indices: data[indices, 0].mean())

labels = np.empty(len(data), dtype=int)

for new_label, indices in enumerate(groups, start=1):
    labels[indices] = new_label

for i, (point, label) in enumerate(zip(data, labels), start=1):
    print(f"P{i} {point.tolist()} -> Cluster {label}")

linkage_matrix = linkage(data, method="ward")
dendrogram(
    linkage_matrix,
    labels=[f"P{i}" for i in range(1, 7)]
)

plt.xlabel("Data Objects")
plt.ylabel("Ward Distance")
plt.title("Agglomerative Hierarchical Clustering")
plt.show()