"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razon. Probabil. en el Tiempo---> Algoritmo Hacia Delante-Atrás
Este script implementa el algoritmo Hacia Delante-Atrás para calcular la distribución de probabilidad 
marginal de los estados ocultos en un modelo de cadena de Markov oculta (HMM). Luego, visualiza la probabilidad
de cada estado oculto a lo largo del tiempo."""

import numpy as np
import matplotlib.pyplot as plt

# Definición del modelo de cadena de Markov oculta (HMM)
# Matriz de transición de estado
transition_matrix = np.array([[0.7, 0.3],
                              [0.4, 0.6]])

# Probabilidades iniciales de los estados ocultos
initial_probabilities = np.array([0.5, 0.5])

# Matriz de emisión (probabilidad de observación dado el estado oculto)
emission_matrix = np.array([[0.2, 0.4, 0.4],
                             [0.5, 0.4, 0.1]])

# Lista de observaciones
observations = [0, 1, 2, 0, 2]

# Algoritmo Hacia Delante
def forward_algorithm(observations, transition_matrix, emission_matrix, initial_probabilities):
    num_states = transition_matrix.shape[0]
    num_observations = len(observations)
    
    # Inicializar la matriz de avance
    forward_matrix = np.zeros((num_states, num_observations))
    
    # Paso de inicialización
    forward_matrix[:, 0] = initial_probabilities * emission_matrix[:, observations[0]]
    
    # Paso de recursión
    for t in range(1, num_observations):
        for j in range(num_states):
            forward_matrix[j, t] = np.sum(forward_matrix[:, t-1] * transition_matrix[:, j]) * emission_matrix[j, observations[t]]
    
    return forward_matrix

# Algoritmo Hacia Atrás
def backward_algorithm(observations, transition_matrix, emission_matrix):
    num_states = transition_matrix.shape[0]
    num_observations = len(observations)
    
    # Inicializar la matriz de retroceso
    backward_matrix = np.zeros((num_states, num_observations))
    
    # Paso de terminación
    backward_matrix[:, -1] = 1
    
    # Paso de recursión
    for t in range(num_observations-2, -1, -1):
        for i in range(num_states):
            backward_matrix[i, t] = np.sum(transition_matrix[i, :] * emission_matrix[:, observations[t+1]] * backward_matrix[:, t+1])
    
    return backward_matrix

# Calcular la distribución de probabilidad marginal utilizando Hacia Delante-Atrás
def forward_backward_algorithm(observations, transition_matrix, emission_matrix, initial_probabilities):
    forward_matrix = forward_algorithm(observations, transition_matrix, emission_matrix, initial_probabilities)
    backward_matrix = backward_algorithm(observations, transition_matrix, emission_matrix)
    
    num_states = transition_matrix.shape[0]
    num_observations = len(observations)
    
    # Calcular la probabilidad marginal para cada estado en cada paso de tiempo
    marginal_probabilities = np.zeros((num_states, num_observations))
    for t in range(num_observations):
        marginal_probabilities[:, t] = forward_matrix[:, t] * backward_matrix[:, t] / np.sum(forward_matrix[:, t] * backward_matrix[:, t])
    
    return marginal_probabilities

# Calcular la distribución de probabilidad marginal
marginal_probabilities = forward_backward_algorithm(observations, transition_matrix, emission_matrix, initial_probabilities)

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.plot(marginal_probabilities[0], label='Estado Oculto 1')
plt.plot(marginal_probabilities[1], label='Estado Oculto 2')
plt.title('Distribución de Probabilidad Marginal de los Estados Ocultos')
plt.xlabel('Tiempo')
plt.ylabel('Probabilidad')
plt.legend()
plt.grid(True)
plt.show()

