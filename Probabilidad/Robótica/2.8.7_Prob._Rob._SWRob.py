"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> SW Robótico"""

import numpy as np
import matplotlib.pyplot as plt

# Función para simular el movimiento del robot
def move(x, u):
    # Modelo de movimiento simple: el robot se mueve hacia adelante con ruido añadido
    return x + u + np.random.normal(0, 0.5)

# Función para simular las observaciones del robot
def observe(x):
    # Modelo de observación simple: el robot observa su posición con ruido añadido
    return x + np.random.normal(0, 1)

# Parámetros del filtro de partículas
num_particles = 1000
initial_std = 1.0

# Generar partículas aleatorias como estimaciones iniciales del estado del robot
particles = np.random.normal(0, initial_std, size=(num_particles,))

# Simular el movimiento y las observaciones del robot
true_position = 0  # Posición verdadera del robot
observations = []  # Lista para almacenar las observaciones simuladas
for _ in range(100):
    true_position = move(true_position, 1)  # Movimiento del robot
    observations.append(observe(true_position))  # Observación del robot

# Actualizar las partículas basadas en las observaciones
for obs in observations:
    # Calcular la probabilidad de observar la posición actual dado el estado de cada partícula
    observation_prob = np.exp(-0.5 * ((particles - obs) / 1.0) ** 2)  # Varianza de la observación
    
    # Verificar si hay NaN o probabilidades cero
    if np.isnan(np.sum(observation_prob)) or np.sum(observation_prob) == 0:
        continue
    
    # Reponderar las partículas según la probabilidad de observación
    weights = observation_prob / np.sum(observation_prob)
    
    # Muestrear partículas basadas en los pesos
    particles = np.random.choice(particles, size=num_particles, p=weights)

# Visualizar el resultado
plt.figure(figsize=(10, 6))
plt.hist(particles, bins=30, density=True, alpha=0.5, color='blue', label='Distribución de partículas')
plt.axvline(true_position, color='red', linestyle='--', label='Posición verdadera del robot')
plt.xlabel('Posición')
plt.ylabel('Densidad de probabilidad')
plt.title('Estimación de la posición del robot usando filtro de partículas')
plt.legend()
plt.grid(True)
plt.show()
