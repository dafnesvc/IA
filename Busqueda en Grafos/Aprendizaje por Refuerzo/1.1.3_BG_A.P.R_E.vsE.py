""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Aprendizaje Por Refuerzo---> Exploración vs. Explotación
Este código simula la exploración vs. explotación utilizando el método epsilon-greedy. 
En cada iteración, el agente elige aleatoriamente si explora una acción nueva o explota una acción
conocida. Se registran las recompensas obtenidas en cada iteración y se grafican para observar cómo
varían a lo largo del tiempo."""

import numpy as np
import matplotlib.pyplot as plt

# Función para simular una recompensa aleatoria
def get_reward():
    return np.random.normal(0, 1)

# Algoritmo de Exploración vs. Explotación (epsilon-greedy)
def explore_exploit(epsilon, num_iterations):
    rewards = []  # Lista para almacenar las recompensas obtenidas en cada iteración
    q_value = 0  # Valor inicial de la acción
    
    for i in range(num_iterations):
        if np.random.rand() < epsilon:  # Acción aleatoria (exploración)
            reward = get_reward()
        else:  # Acción basada en el valor Q actual (explotación)
            reward = get_reward() + q_value
        
        # Actualizar el valor Q promedio
        q_value = (q_value * i + reward) / (i + 1)
        
        # Almacenar la recompensa obtenida en esta iteración
        rewards.append(reward)
    
    return rewards

# Definir los parámetros
epsilon = 0.1  # Factor de exploración
num_iterations = 1000  # Número de iteraciones

# Ejecutar el algoritmo de exploración vs. explotación
rewards = explore_exploit(epsilon, num_iterations)

# Graficar las recompensas obtenidas en cada iteración
plt.plot(np.arange(num_iterations), rewards)
plt.xlabel('Iteración')
plt.ylabel('Recompensa')
plt.title('Exploración vs. Explotación (epsilon-greedy)')
plt.show()
