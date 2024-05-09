"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Aprendizaje Inductivo ---> Listas de Decisión: K-DL y K-DT"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score

# Generar datos de ejemplo para clasificación
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Inicializar y entrenar el clasificador K-DL
kdl_clf = QuadraticDiscriminantAnalysis()
kdl_clf.fit(X, y)

# Inicializar y entrenar el clasificador K-DT
kdt_clf = DecisionTreeClassifier(max_depth=3)
kdt_clf.fit(X, y)

# Predecir las etiquetas de clase para los datos de entrenamiento
y_pred_kdl = kdl_clf.predict(X)
y_pred_kdt = kdt_clf.predict(X)

# Calcular la precisión de los clasificadores
accuracy_kdl = accuracy_score(y, y_pred_kdl)
accuracy_kdt = accuracy_score(y, y_pred_kdt)

# Visualizar los datos y las regiones de decisión
plt.figure(figsize=(12, 6))

# Plotear la primera región de decisión (K-DL)
plt.subplot(1, 2, 1)
plt.title('K-DL (Quadratic Discriminant Analysis)')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Crear una malla de puntos para visualizar la región de decisión
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
Z = kdl_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)

# Plotear la segunda región de decisión (K-DT)
plt.subplot(1, 2, 2)
plt.title('K-DT (Decision Tree)')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Crear una malla de puntos para visualizar la región de decisión
Z = kdt_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)

plt.tight_layout()
plt.show()

print(f'Precisión de K-DL: {accuracy_kdl:.2f}')
print(f'Precisión de K-DT: {accuracy_kdt:.2f}')
