"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Aprendizaje Probabilístico --->k-NN, k-Medias y Clustering"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

# Generar datos de muestra
X, y = make_classification(n_samples=300, n_features=2, n_classes=3, n_clusters_per_class=1, n_informative=2, n_redundant=0, n_repeated=0, random_state=42)

# Algoritmo k-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Algoritmo k-NN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Plot de los datos de muestra
plt.figure(figsize=(12, 5))

# Subplot para k-Means
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', marker='o', edgecolor='k', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', c='red', s=200, label='Centroides')
plt.title('k-Means')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

# Subplot para k-NN
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k', s=50)
plt.title('k-NN')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Plot de los resultados
plt.tight_layout()
plt.show()



