"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razon. Probabil. en el Tiempo---> Modelos Ocultos de Markov

Este script implementa un modelo oculto de Markov (HMM) y utiliza el algoritmo de Viterbi para encontrar 
la secuencia de estados más probable dados una matriz de transición, una matriz de emisión y una secuencia
de observaciones. Luego, visualiza la secuencia de estados más probable en un gráfico."""

import numpy as np
import matplotlib.pyplot as plt

# Definición del modelo de cadena de Markov oculta (HMM)
class HiddenMarkovModel:
    def __init__(self, transition_matrix, emission_matrix, initial_probabilities):
        self.transition_matrix = transition_matrix
        self.emission_matrix = emission_matrix
        self.initial_probabilities = initial_probabilities
        self.num_states = transition_matrix.shape[0]
        self.num_observations = emission_matrix.shape[1]
    
    # Algoritmo de Viterbi para encontrar la secuencia de estados más probable
    def viterbi(self, observations):
        num_observations = len(observations)
        viterbi_matrix = np.zeros((self.num_states, num_observations))
        backtrack_matrix = np.zeros((self.num_states, num_observations), dtype=int)
        
        # Paso de inicialización
        viterbi_matrix[:, 0] = self.initial_probabilities * self.emission_matrix[:, observations[0]]
        
        # Paso de recursión
        for t in range(1, num_observations):
            for s in range(self.num_states):
                temp_scores = viterbi_matrix[:, t-1] * self.transition_matrix[:, s] * self.emission_matrix[s, observations[t]]
                viterbi_matrix[s, t] = np.max(temp_scores)
                backtrack_matrix[s, t] = np.argmax(temp_scores)
        
        # Paso final
        best_path_prob = np.max(viterbi_matrix[:, -1])
        best_path = [np.argmax(viterbi_matrix[:, -1])]
        for t in range(num_observations-1, 0, -1):
            best_path.append(backtrack_matrix[best_path[-1], t])
        best_path.reverse()
        
        return best_path, best_path_prob

# Definición de los parámetros del modelo HMM
transition_matrix = np.array([[0.7, 0.3],
                              [0.4, 0.6]])

emission_matrix = np.array([[0.2, 0.4, 0.4],
                             [0.5, 0.4, 0.1]])

initial_probabilities = np.array([0.5, 0.5])

# Definición de las observaciones
observations = [0, 1, 2, 0, 2]

# Creación del modelo HMM
hmm = HiddenMarkovModel(transition_matrix, emission_matrix, initial_probabilities)

# Aplicar el algoritmo de Viterbi para encontrar la secuencia de estados más probable
best_path, best_path_prob = hmm.viterbi(observations)

# Visualizar los resultados
print("Secuencia de estados más probable:", best_path)
print("Probabilidad de la secuencia de estados más probable:", best_path_prob)

# Visualizar la secuencia de estados más probable en un gráfico
plt.figure(figsize=(10, 6))
plt.plot(best_path, marker='o')
plt.title('Secuencia de Estados más Probable')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.grid(True)
plt.show()
