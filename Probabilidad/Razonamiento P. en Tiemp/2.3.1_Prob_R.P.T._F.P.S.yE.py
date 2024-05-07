"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razon. Probabil. en el Tiempo---> Filtrado, Predicción, Suavizado y Explicación
Este script simula el filtrado y la predicción de una serie temporal de posición utilizando el filtro de Kalman.
Genera datos de observación sintéticos basados en una función sinusoidal y los filtra utilizando el filtro de Kalman. 
Luego visualiza la posición verdadera, las observaciones, el estado filtrado y el estado predicho en un gráfico."""


import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo y proceso de medición
dt = 0.1  # Paso de tiempo
A = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0]])  # Matriz de medición
Q = np.array([[0.1, 0], [0, 0.01]])  # Covarianza del proceso de estado
R = np.array([[0.5]])  # Covarianza del proceso de medición

# Estado inicial
x0 = np.array([[0], [0]])  # Posición y velocidad inicial
P0 = np.eye(2)  # Covarianza inicial

# Generar datos de observación sintéticos
num_steps = 100
true_position = np.sin(np.linspace(0, 2 * np.pi, num_steps))  # Posición verdadera
observations = true_position + np.random.normal(0, np.sqrt(R[0, 0]), num_steps)  # Observaciones con ruido

# Filtro de Kalman
x_hat = x0
P_hat = P0
filtered_states = []
predicted_states = []

for z in observations:
    # Predicción
    x_hat_minus = np.dot(A, x_hat)
    P_minus = np.dot(np.dot(A, P_hat), A.T) + Q

    # Actualización (corrección)
    y = z - np.dot(H, x_hat_minus)
    S = np.dot(np.dot(H, P_minus), H.T) + R
    K = np.dot(np.dot(P_minus, H.T), np.linalg.inv(S))
    x_hat = x_hat_minus + np.dot(K, y)
    P_hat = P_minus - np.dot(np.dot(K, H), P_minus)

    # Almacenar estados filtrados y predichos
    filtered_states.append(x_hat[0, 0])
    predicted_states.append(x_hat_minus[0, 0])

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.plot(range(num_steps), true_position, label='Posición Verdadera', color='green')
plt.scatter(range(num_steps), observations, label='Observaciones', color='blue', marker='x')
plt.plot(range(num_steps), filtered_states, label='Estado Filtrado', color='red')
plt.plot(range(num_steps), predicted_states, label='Estado Predicho', color='orange', linestyle='--')
plt.title('Filtrado y Predicción con Filtro de Kalman')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.legend()
plt.grid(True)
plt.show()
