"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Aprendizaje Probabilístico ---> Aprendizaje Bayesiano"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import plot_confusion_matrix

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el clasificador de Bayes ingenuo gaussiano
clf = GaussianNB()
clf.fit(X_train, y_train)

# Predecir las etiquetas para los datos de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = np.mean(y_pred == y_test)
print("Precisión del clasificador de Bayes ingenuo gaussiano:", accuracy)

# Visualizar la matriz de confusión
plot_confusion_matrix(clf, X_test, y_test, cmap=plt.cm.Blues, display_labels=iris.target_names)
plt.title('Matriz de Confusión')
plt.show()
