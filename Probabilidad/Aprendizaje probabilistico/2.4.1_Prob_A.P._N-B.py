"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Aprendizaje Probabilístico ---> Naïve-Bayes"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

# Generamos datos de ejemplo
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Dividimos los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos y entrenamos el clasificador Naïve-Bayes
clf = GaussianNB()
clf.fit(X_train, y_train)

# Realizamos predicciones sobre el conjunto de prueba
y_pred = clf.predict(X_test)

# Calculamos la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Visualizamos la matriz de confusión
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Matriz de Confusión')
plt.colorbar()
plt.xlabel('Predicciones')
plt.ylabel('Valores Verdaderos')
plt.show()
