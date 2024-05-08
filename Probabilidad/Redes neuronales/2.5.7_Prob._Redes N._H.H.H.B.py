"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Hamming, Hopfield, Hebb, Boltzmann
Este ejemplo entrena un perceptrón utilizando el algoritmo de Hebb para la compuerta lógica OR.
Los puntos en el gráfico muestran las diferentes combinaciones de entrada, y están coloreados de
acuerdo con la predicción del perceptrón (0 o 1)."""

import numpy as np
import matplotlib.pyplot as plt

# Función de activación (escalonada)
def step_function(x):
    return 1 if x >= 0 else 0

# Función de entrenamiento del perceptrón utilizando el algoritmo de Hebb
def train_perceptron(X, y):
    num_features = X.shape[1]
    weights = np.zeros(num_features)
    
    for i in range(X.shape[0]):
        for j in range(num_features):
            weights[j] += X[i][j] * y[i]
    
    return weights

# Función para hacer predicciones con el perceptrón entrenado
def predict_perceptron(X, weights):
    return step_function(np.dot(X, weights))

# Datos de entrenamiento (OR gate)
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 1])

# Entrenar el perceptrón
weights = train_perceptron(X_train, y_train)

# Hacer predicciones
predictions = np.array([predict_perceptron(x, weights) for x in X_train])

# Visualizar resultados
plt.scatter(X_train[:,0], X_train[:,1], c=predictions, cmap='bwr')
plt.xlabel('Input 1')
plt.ylabel('Input 2')
plt.title('Perceptrón (Algoritmo de Hebb) - OR Gate')
plt.show()
