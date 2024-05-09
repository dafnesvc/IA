"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Aprendizaje Inductivo ---> Conjuntos de Hipótesis: Boosting"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Generar datos de ejemplo para clasificación
X, y = make_classification(n_samples=100, n_features=2, n_informative=1, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Crear el clasificador base (usaremos árboles de decisión)
base_classifier = DecisionTreeClassifier(max_depth=1)

# Crear el clasificador AdaBoost
adaboost_clf = AdaBoostClassifier(base_estimator=base_classifier, n_estimators=50, learning_rate=1)

# Entrenar el clasificador AdaBoost
adaboost_clf.fit(X, y)

# Visualizar la frontera de decisión obtenida por el clasificador AdaBoost
plt.figure(figsize=(10, 6))

# Crear una malla de puntos para la visualización
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# Predecir la clase para cada punto en la malla
Z = adaboost_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Visualizar los datos de entrenamiento
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')

plt.title('Frontera de Decisión con AdaBoost')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()
