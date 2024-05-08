"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> Localización: Monte-Carlo
Este script simula el movimiento y la observación de un robot en un entorno 2D y utiliza el algoritmo
Monte Carlo para estimar la distribución de probabilidad de la posición del robot. La distribución de
probabilidad resultante se visualiza utilizando un mapa de calor, donde los valores más altos indican una
mayor probabilidad de que el robot esté en esa posición."""

import numpy as np
import matplotlib.pyplot as plt

# Función para generar una distribución de probabilidad inicial uniforme
def initialize_belief(grid_size):
    return np.ones((grid_size, grid_size)) / (grid_size * grid_size)

# Función para simular un paso del robot y actualizar la creencia
def move_and_update_belief(belief, move_direction, true_position, grid_size, move_noise):
    # Crear una matriz de transición de movimiento
    move_transition = np.zeros_like(belief)
    if move_direction == 'up':
        move_transition[:-1, :] = belief[1:, :]
    elif move_direction == 'down':
        move_transition[1:, :] = belief[:-1, :]
    elif move_direction == 'left':
        move_transition[:, :-1] = belief[:, 1:]
    elif move_direction == 'right':
        move_transition[:, 1:] = belief[:, :-1]
    
    # Aplicar ruido al movimiento
    move_transition = np.roll(move_transition, move_noise, axis=(0, 1))
    
    # Normalizar la creencia después del movimiento
    updated_belief = move_transition / np.sum(move_transition)
    
    return updated_belief

# Función para simular una observación y actualizar la creencia
def sense_and_update_belief(belief, true_position, observation, sensor_accuracy):
    # Calcular la probabilidad de observar el estado actual dado la observación
    observation_prob = np.zeros_like(belief)
    observation_prob[true_position] = 1.0 if observation else 0.0
    
    # Aplicar la precisión del sensor
    observation_prob = observation_prob * sensor_accuracy + (1 - observation_prob) * (1 - sensor_accuracy)
    
    # Actualizar la creencia basada en la observación
    updated_belief = belief * observation_prob
    updated_belief /= np.sum(updated_belief)
    
    return updated_belief

# Parámetros de la simulación
grid_size = 10
true_position = (5, 5)
initial_belief = initialize_belief(grid_size)
move_directions = ['up', 'down', 'left', 'right']
sensor_accuracy = 0.8
move_noise = 1

# Simulación de pasos del robot
num_steps = 5
for step in range(num_steps):
    # Simular movimiento
    move_direction = np.random.choice(move_directions)
    belief = move_and_update_belief(initial_belief, move_direction, true_position, grid_size, move_noise)
    
    # Simular observación
    observation = np.random.rand() < sensor_accuracy
    belief = sense_and_update_belief(belief, true_position, observation, sensor_accuracy)
    
    # Actualizar creencia inicial para el próximo paso
    initial_belief = belief

# Graficar la creencia final
plt.imshow(belief, cmap='Blues', origin='lower')
plt.title('Distribución de Probabilidad de la Posición del Robot')
plt.xlabel('Columna')
plt.ylabel('Fila')
plt.colorbar(label='Probabilidad')
plt.xticks(np.arange(grid_size))
plt.yticks(np.arange(grid_size))
plt.scatter(true_position[1], true_position[0], color='red', label='Posición Verdadera', zorder=10)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
