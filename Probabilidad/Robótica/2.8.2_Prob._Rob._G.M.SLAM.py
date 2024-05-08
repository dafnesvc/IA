"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> Generación de Mapas: SLAM
Este código utiliza el filtro de partículas para estimar la posición de un robot en un mapa, 
dadas las observaciones de algunos landmarks. Luego, visualiza las partículas, los landmarks y la
 posición estimada del robot en un gráfico."""

import numpy as np
import matplotlib.pyplot as plt

# Función para generar partículas aleatorias
def generate_particles(num_particles, map_size):
    particles = np.random.rand(num_particles, 2) * map_size
    return particles

# Función para estimar la posición del robot utilizando el filtro de partículas
def estimate_position(particles, observations, landmarks):
    # Ajustar las dimensiones de los landmarks para que se puedan restar a observations
    landmarks_expanded = np.expand_dims(landmarks, axis=0)
    
    # Calcular la probabilidad de observar las características para cada partícula
    observation_prob = np.exp(-np.sum((observations[:, :, None] - landmarks_expanded)**2, axis=3))
    
    # Normalizar las probabilidades
    observation_prob /= np.sum(observation_prob, axis=2)[:, :, None]
    
    # Calcular la posición estimada como el promedio ponderado de las partículas
    estimated_position = np.average(particles, weights=observation_prob, axis=0)
    
    return estimated_position

# Definir el tamaño del mapa y el número de partículas
map_size = 10
num_particles = 1000

# Generar partículas aleatorias
particles = generate_particles(num_particles, map_size)

# Definir las ubicaciones de los landmarks
landmarks = np.array([[3, 3],
                       [7, 7],
                       [2, 8]])

# Simular observaciones de los landmarks
observations = np.array([landmarks + np.random.normal(scale=0.1, size=landmarks.shape) for _ in range(num_particles)])

# Estimar la posición del robot
estimated_position = estimate_position(particles, observations, landmarks)

# Visualizar los resultados
plt.figure(figsize=(8, 6))
plt.scatter(particles[:, 0], particles[:, 1], color='blue', alpha=0.5, label='Partículas')
plt.scatter(landmarks[:, 0], landmarks[:, 1], color='red', marker='x', label='Landmarks')
plt.scatter(estimated_position[0], estimated_position[1], color='green', marker='o', label='Posición estimada')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Estimación de posición utilizando filtro de partículas')
plt.legend()
plt.grid(True)
plt.axis([0, map_size, 0, map_size])
plt.show()
