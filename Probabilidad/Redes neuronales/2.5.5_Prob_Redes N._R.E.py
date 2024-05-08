"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Retropropagación del Error"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Definir la derivada de la función de activación sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada y salida
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Inicializar los pesos de forma aleatoria
np.random.seed(0)
input_neurons = 2
hidden_neurons = 5
output_neurons = 1
hidden_weights = np.random.uniform(size=(input_neurons, hidden_neurons))
output_weights = np.random.uniform(size=(hidden_neurons, output_neurons))

# Hiperparámetro
learning_rate = 0.1
epochs = 10000

# Entrenamiento con retropropagación del error
loss_history = []

for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(X, hidden_weights)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, output_weights)
    predicted_output = sigmoid(output_layer_input)

    # Cálculo de la pérdida
    loss = np.mean(np.square(y - predicted_output))
    loss_history.append(loss)

    # Backpropagation
    output_error = y - predicted_output
    output_delta = output_error * sigmoid_derivative(predicted_output)
    hidden_error = output_delta.dot(output_weights.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

    # Actualización de pesos
    output_weights += hidden_layer_output.T.dot(output_delta) * learning_rate
    hidden_weights += X.T.dot(hidden_delta) * learning_rate

# Visualización de la pérdida durante el entrenamiento
plt.plot(loss_history)
plt.title('Pérdida durante el entrenamiento')
plt.xlabel('Época')
plt.ylabel('Pérdida')
plt.show()

