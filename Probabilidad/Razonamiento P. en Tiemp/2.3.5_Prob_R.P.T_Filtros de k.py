"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razon. Probabil. en el Tiempo---> Filtros de Kalman
Este script implementa un filtro de Kalman para estimar una serie de datos observados utilizando un modelo lineal de 
espacio de estados. Luego, visualiza los datos verdaderos, los datos observados y los datos predichos por el filtro 
de Kalman en un gráfico."""

import numpy as np
import matplotlib.pyplot as plt

# Definición de las matrices de transición y de observación
transition_matrix = np.array([[1, 1],
                               [0, 1]])
observation_matrix = np.array([[1, 0]])

# Definición de las matrices de covarianza del proceso y de observación
process_covariance = 0.1
observation_covariance = 1.0

# Definición del filtro de Kalman
def kalman_filter(observed_data):
    # Inicialización de las matrices de estado y covarianza
    initial_state = np.array([0, 0])
    initial_covariance = np.eye(2)
    predicted_states = [initial_state]
    
    current_state = initial_state
    current_covariance = initial_covariance
    
    # Aplicación del filtro de Kalman
    for observation in observed_data:
        # Predicción del siguiente estado
        predicted_state = np.dot(transition_matrix, current_state)
        predicted_covariance = np.dot(transition_matrix, np.dot(current_covariance, transition_matrix.T)) + process_covariance
        
        # Actualización del estado basado en la observación
        innovation = observation - np.dot(observation_matrix, predicted_state)
        innovation_covariance = observation_covariance + np.dot(observation_matrix, np.dot(predicted_covariance, observation_matrix.T))
        
        kalman_gain = np.dot(predicted_covariance, np.dot(observation_matrix.T, np.linalg.inv(innovation_covariance)))
        current_state = predicted_state + np.dot(kalman_gain, innovation)
        current_covariance = predicted_covariance - np.dot(kalman_gain, np.dot(observation_matrix, predicted_covariance))
        
        # Guardar el estado predicho
        predicted_states.append(current_state)
    
    return np.array(predicted_states)

# Generación de datos simulados
np.random.seed(0)
true_data = np.cumsum(np.random.randn(100, 2), axis=0)
observed_data = true_data[:, 0] + np.random.randn(100)  # Observación de la primera dimensión

# Aplicación del filtro de Kalman
predicted_states = kalman_filter(observed_data)

# Visualización de los resultados
plt.figure(figsize=(10, 6))
plt.plot(true_data[:, 0], label='Verdadero')
plt.plot(observed_data, label='Observado', marker='o', linestyle='None')
plt.plot(predicted_states[:, 0], label='Predicho')
plt.title('Filtro de Kalman')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

