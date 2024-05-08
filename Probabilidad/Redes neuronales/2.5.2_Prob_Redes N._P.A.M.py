"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Perceptrón, ADALINE y MADALINE"""

import numpy as np
import matplotlib.pyplot as plt

# Clase para el Perceptrón
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    # Función de activación: función escalón unitario
    def activation_fn(self, x):
        return 1 if x >= 0 else 0

    # Función para predecir la clase
    def predict(self, x):
        z = np.dot(x, self.weights[1:]) + self.weights[0]
        a = self.activation_fn(z)
        return a

    # Función de entrenamiento
    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(y.shape[0]):
                predicted = self.predict(X[i])
                error = y[i] - predicted
                self.weights[1:] += self.learning_rate * error * X[i]
                self.weights[0] += self.learning_rate * error

# Datos de entrada
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])  # Salidas para la operación AND
y_or = np.array([0, 1, 1, 1])   # Salidas para la operación OR
y_xor = np.array([0, 1, 1, 0])  # Salidas para la operación XOR

# Entrenamiento y predicción del Perceptrón para la operación AND
perceptron_and = Perceptron(input_size=2)
perceptron_and.train(X, y_and)
predicted_and = [perceptron_and.predict(x) for x in X]

# Entrenamiento y predicción del Perceptrón para la operación OR
perceptron_or = Perceptron(input_size=2)
perceptron_or.train(X, y_or)
predicted_or = [perceptron_or.predict(x) for x in X]

# Entrenamiento y predicción del Perceptrón para la operación XOR (no linealmente separable)
perceptron_xor = Perceptron(input_size=2)
perceptron_xor.train(X, y_xor)
predicted_xor = [perceptron_xor.predict(x) for x in X]

# Gráficos
plt.figure(figsize=(10, 6))

# Gráfico para la operación AND
plt.subplot(1, 3, 1)
plt.title('Operación AND')
plt.xlabel('X1')
plt.ylabel('X2')
plt.scatter(X[:,0], X[:,1], c=y_and)
plt.plot(X[:,0], -perceptron_and.weights[0]/perceptron_and.weights[1] - (perceptron_and.weights[2]/perceptron_and.weights[1])*X[:,0], 'r')

# Gráfico para la operación OR
plt.subplot(1, 3, 2)
plt.title('Operación OR')
plt.xlabel('X1')
plt.ylabel('X2')
plt.scatter(X[:,0], X[:,1], c=y_or)
plt.plot(X[:,0], -perceptron_or.weights[0]/perceptron_or.weights[1] - (perceptron_or.weights[2]/perceptron_or.weights[1])*X[:,0], 'r')

# Gráfico para la operación XOR
plt.subplot(1, 3, 3)
plt.title('Operación XOR')
plt.xlabel('X1')
plt.ylabel('X2')
plt.scatter(X[:,0], X[:,1], c=y_xor)
plt.plot(X[:,0], -perceptron_xor.weights[0]/perceptron_xor.weights[1] - (perceptron_xor.weights[2]/perceptron_xor.weights[1])*X[:,0], 'r')

plt.tight_layout()
plt.show()
