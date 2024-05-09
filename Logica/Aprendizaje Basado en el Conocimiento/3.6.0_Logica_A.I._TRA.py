"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Aprendizaje Inductivo ---> Tipos de Razonamiento y Aprendizaje"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Generar datos de clasificación
X, y = make_classification(n_samples=100, n_features=2, n_informative=1, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Visualizar los datos
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolors='k')
plt.title('Datos de clasificación generados')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.grid(True)
plt.show()
