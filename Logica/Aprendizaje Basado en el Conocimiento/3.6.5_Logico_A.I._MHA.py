"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Aprendizaje Inductivo ---> Mejor Hipótesis Actual"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Generar datos de ejemplo para clasificación
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Inicializar y entrenar el clasificador de hipótesis actual (Naive Bayes)
hypothesis_clf = GaussianNB()
hypothesis_clf.fit(X, y)

# Predecir las etiquetas de clase para los datos de entrenamiento
y_pred = hypothesis_clf.predict(X)

# Calcular la precisión del clasificador de hipótesis actual
accuracy = accuracy_score(y, y_pred)

# Visualizar los datos y las regiones de decisión
plt.figure(figsize=(8, 6))
plt.title('Mejor Hipótesis Actual')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Crear una malla de puntos para visualizar la región de decisión
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
Z = hypothesis_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)

plt.colorbar(label='Clase')
plt.tight_layout()
plt.show()

print(f'Precisión del clasificador de hipótesis actual: {accuracy:.2f}')
