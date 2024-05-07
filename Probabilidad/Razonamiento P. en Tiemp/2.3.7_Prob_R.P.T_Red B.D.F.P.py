"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razon. Probabil. en el Tiempo---> Red Bayes. Dinámica: Filtrado de Partículas

Este script simula un sistema donde se observan estados a través del ruido y luego se filtran utilizando el algoritmo
de Filtrado de Partículas. Los resultados se visualizan en un gráfico donde se muestran los estados verdaderos, 
las observaciones y los estados filtrados."""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de transición de estado
def transition_function(state, noise):
    return state + noise

# Definición de la función de observación
def observation_function(state, noise):
    return state + noise

# Generación de datos simulados
np.random.seed(0)
true_states = np.cumsum(np.random.randn(100))  # Estados verdaderos
observations = true_states + np.random.randn(100)  # Observaciones

# Parámetros del filtro de partículas
num_particles = 1000
initial_state = 0
initial_state_variance = 1
process_noise_variance = 1
observation_noise_variance = 1

# Inicialización de las partículas
particles = np.random.normal(initial_state, np.sqrt(initial_state_variance), num_particles)

# Filtrado de partículas
filtered_states = []
for observation in observations:
    # Predicción del estado
    particles = transition_function(particles, np.random.normal(0, np.sqrt(process_noise_variance), num_particles))
    
    # Pesos de las partículas basados en la observación
    observation_likelihoods = np.exp(-0.5 * ((observation - particles) ** 2) / observation_noise_variance)
    weights = observation_likelihoods / np.sum(observation_likelihoods)
    
    # Re-muestreo de partículas
    indices = np.random.choice(np.arange(num_particles), size=num_particles, replace=True, p=weights)
    particles = particles[indices]
    
    # Estimación del estado filtrado
    filtered_state = np.mean(particles)
    filtered_states.append(filtered_state)

# Visualización de los resultados
plt.figure(figsize=(10, 6))
plt.plot(true_states, label='Estado Verdadero', color='blue')
plt.scatter(np.arange(len(observations)), observations, label='Observaciones', color='green', marker='o')
plt.plot(filtered_states, label='Estado Filtrado', color='red')
plt.title('Filtrado de Partículas')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()
