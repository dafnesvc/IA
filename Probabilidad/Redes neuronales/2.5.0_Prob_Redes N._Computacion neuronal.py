"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Computación Neuronal
En este ejemplo, se crea un modelo de computación neuronal simple con dos entradas (features) 
y una sola neurona en la capa de salida. Los pesos y el sesgo se inicializan con valores aleatorios y luego
se calcula la salida del modelo aplicando la función de activación sigmoide. Finalmente, se visualiza la salida 
del modelo en un gráfico de dispersión bidimensional, donde el color representa la salida de la neurona."""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función de activación (en este caso, la función sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Definir los datos de entrada
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Definir los pesos y el sesgo (valores iniciales aleatorios)
np.random.seed(0)
weights = np.random.randn(2)
bias = np.random.randn(1)

# Calcular la salida del modelo
output = sigmoid(np.dot(X, weights) + bias)

# Graficar los resultados
plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], c=output, cmap='viridis', s=100)
plt.title('Computación Neuronal')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Output')
plt.show()
