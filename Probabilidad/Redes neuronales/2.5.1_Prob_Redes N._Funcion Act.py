"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Funciones de Activación"""
import numpy as np
import matplotlib.pyplot as plt

# Función de activación: Sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función de activación: ReLU (Rectified Linear Unit)
def relu(x):
    return np.maximum(0, x)

# Función de activación: Tangente Hiperbólica
def tanh(x):
    return np.tanh(x)

# Definir el rango de valores para x
x = np.linspace(-5, 5, 100)

# Calcular las salidas de las funciones de activación para el rango de valores de x
sigmoid_output = sigmoid(x)
relu_output = relu(x)
tanh_output = tanh(x)

# Graficar las funciones de activación
plt.figure(figsize=(10, 6))

plt.plot(x, sigmoid_output, label='Sigmoide', color='blue')
plt.plot(x, relu_output, label='ReLU', color='red')
plt.plot(x, tanh_output, label='Tangente Hiperbólica', color='green')

plt.title('Funciones de Activación')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
