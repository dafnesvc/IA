"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razonamiento Probabilístico--->Monte Carlo para Cadenas de Markov"""


import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición de la cadena de Markov
transition_matrix = np.array([[0.7, 0.3],
                              [0.4, 0.6]])

# Definir el estado inicial de la cadena de Markov
initial_state = np.array([0.5, 0.5])

# Número de pasos de la simulación
num_steps = 1000

# Inicializar la lista para almacenar los estados
states = [initial_state]

# Realizar el muestreo de la cadena de Markov utilizando Monte Carlo
for _ in range(num_steps):
    # Obtener el estado actual
    current_state = states[-1]
    # Calcular la próxima transición utilizando la matriz de transición
    next_state = np.random.choice([0, 1], p=current_state.dot(transition_matrix))
    # Agregar el próximo estado a la lista de estados
    states.append(transition_matrix[next_state])

# Convertir la lista de estados en un array para facilitar la manipulación
states = np.array(states)

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.plot(states[:, 0], label='Estado 0')
plt.plot(states[:, 1], label='Estado 1')
plt.title('Simulación de una Cadena de Markov con Monte Carlo')
plt.xlabel('Número de Pasos')
plt.ylabel('Probabilidad de Estar en el Estado')
plt.legend()
plt.grid(True)
plt.show()
