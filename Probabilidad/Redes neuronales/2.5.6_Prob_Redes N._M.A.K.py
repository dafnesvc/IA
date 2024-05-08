"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Redes Neuronales ---> Mapas Autoorganizados de Kohonen"""

from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
data = np.random.normal(loc=0, scale=1, size=(1000, 2))

# Normalizar los datos
data = (data - np.min(data)) / (np.max(data) - np.min(data))

# Definir el tamaño del mapa
som = MiniSom(10, 10, 2, sigma=0.5, learning_rate=0.5)

# Inicializar los pesos aleatoriamente
som.random_weights_init(data)

# Entrenar el SOM
som.train_random(data, 1000)

# Obtener los pesos finales
weights = som.get_weights()

# Visualizar el SOM
plt.figure(figsize=(8, 8))
for i in range(weights.shape[0]):
    for j in range(weights.shape[1]):
        plt.scatter(weights[i, j, 0], weights[i, j, 1], color='blue', marker='o', edgecolors='k')
        if i < weights.shape[0] - 1:
            plt.plot([weights[i, j, 0], weights[i + 1, j, 0]], [weights[i, j, 1], weights[i + 1, j, 1]], color='black')
        if j < weights.shape[1] - 1:
            plt.plot([weights[i, j, 0], weights[i, j + 1, 0]], [weights[i, j, 1], weights[i, j + 1, 1]], color='black')

plt.title('Mapa Autoorganizado de Kohonen')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.grid()
plt.show()




