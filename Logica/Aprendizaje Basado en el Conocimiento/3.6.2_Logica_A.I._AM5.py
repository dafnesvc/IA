"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Aprendizaje Inductivo ---> Árboles de Regresión: M5"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor

# Generar datos de ejemplo para regresión
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# Crear el clasificador de árbol de regresión
tree_reg = DecisionTreeRegressor(max_depth=3)
tree_reg.fit(X, y)

# Predecir valores para nuevos datos
X_new = np.linspace(min(X), max(X), 100).reshape(-1, 1)
y_pred = tree_reg.predict(X_new)

# Visualizar los datos y la regresión obtenida por el árbol
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Datos de entrenamiento')
plt.plot(X_new, y_pred, color='red', label='Predicción del árbol de regresión')
plt.title('Árbol de Regresión con el algoritmo M5')
plt.xlabel('Característica')
plt.ylabel('Etiqueta')
plt.legend()
plt.grid(True)
plt.show()

