"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Aprendizaje Probabilístico ---> Máquinas de Vectores Soporte (Núcleo)"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Cargar el conjunto de datos de iris
iris = datasets.load_iris()
X = iris.data[:, :2]  # Usamos solo las dos primeras características para la visualización
y = iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un clasificador SVM con núcleo (kernel) gaussiano (RBF)
clf = SVC(kernel='rbf', C=1, gamma='scale')

# Entrenar el clasificador SVM
clf.fit(X_train, y_train)

# Función para visualizar el límite de decisión y los vectores de soporte
def plot_decision_boundary(X, y, clf):
    plt.figure(figsize=(10, 6))

    # Graficar los puntos de datos
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, s=30, edgecolors='k')

    # Crear una malla para graficar el límite de decisión
    h = .02  # Tamaño del paso en la malla
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Graficar el resultado en color
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.5)

    # Graficar los vectores de soporte
    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k')

    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.title('SVM con núcleo RBF')

    plt.show()

# Visualizar el límite de decisión y los vectores de soporte
plot_decision_boundary(X_train, y_train, clf)
