"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Aprendizaje Inductivo ---> Árboles de Decisión: ID3"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data[:, 2:]  # Longitud y ancho del pétalo
y = iris.target

# Crear el clasificador de árbol de decisión
tree_clf = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_clf.fit(X, y)

# Visualizar el árbol de decisión
plt.figure(figsize=(10, 8))
plot_tree(tree_clf, filled=True, feature_names=iris.feature_names[2:], class_names=iris.target_names)
plt.title("Árbol de decisión generado por el algoritmo ID3")
plt.show()
