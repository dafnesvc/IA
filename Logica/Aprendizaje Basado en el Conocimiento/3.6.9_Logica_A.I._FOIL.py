"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Aprendizaje Inductivo ---> Programación Lógica Inductiva: FOIL"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generar datos de ejemplo para clasificación
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar un clasificador de regresión logística
log_reg_clf = LogisticRegression()
log_reg_clf.fit(X_train, y_train)

# Predecir las etiquetas de clase para el conjunto de prueba
y_pred = log_reg_clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

# Visualizar los datos y las regiones de decisión del clasificador
plt.figure(figsize=(8, 6))
plt.title('Programación Lógica Inductiva: FOIL')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Crear una malla de puntos para visualizar la región de decisión
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
Z = log_reg_clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)

plt.colorbar(label='Clase')
plt.tight_layout()
plt.show()

print(f'Precisión del clasificador de regresión logística: {accuracy:.2f}')
