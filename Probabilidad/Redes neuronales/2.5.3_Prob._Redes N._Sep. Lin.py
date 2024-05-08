"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Separabilidad Lineal"""
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(0)
num_samples = 100
x1 = np.random.normal(loc=0, scale=1, size=(num_samples, 2))
x2 = np.random.normal(loc=3, scale=1, size=(num_samples, 2))

# Visualizar los datos
plt.figure(figsize=(8, 6))
plt.scatter(x1[:, 0], x1[:, 1], color='blue', label='Clase 1')
plt.scatter(x2[:, 0], x2[:, 1], color='red', label='Clase 2')
plt.title('Separabilidad Lineal de Datos')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

