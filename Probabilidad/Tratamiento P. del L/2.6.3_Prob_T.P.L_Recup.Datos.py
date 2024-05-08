"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Tratamiento Probabilistico del lenguaje---> Recuperación de datos
Este script genera puntos de datos aleatorios en un plano 2D y luego encuentra los k puntos más cercanos
a un punto de consulta dado utilizando la distancia euclidiana. Finalmente, visualiza los datos y resalta 
los puntos más cercanos al punto de consulta en verde."""
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Función para recuperar los datos más cercanos a un punto de consulta
def retrieve_data(query_point, data_points, k=5):
    distances = [(idx, euclidean_distance(query_point, point)) for idx, point in enumerate(data_points)]
    distances.sort(key=lambda x: x[1])  # Ordenar distancias de menor a mayor
    return distances[:k]  # Devolver los primeros k puntos más cercanos

# Datos de ejemplo
data_points = np.random.rand(20, 2)  # 20 puntos de datos en 2D
query_point = np.array([0.5, 0.5])    # Punto de consulta

# Recuperar los datos más cercanos al punto de consulta
k_nearest = retrieve_data(query_point, data_points, k=5)

# Visualizar los datos y los puntos más cercanos al punto de consulta
plt.figure(figsize=(8, 6))
plt.scatter(data_points[:, 0], data_points[:, 1], color='blue', label='Datos')
plt.scatter(query_point[0], query_point[1], color='red', label='Punto de consulta')
for idx, dist in k_nearest:
    plt.scatter(data_points[idx][0], data_points[idx][1], color='green', label=f'Dist: {dist:.2f}')
plt.title('Recuperación de datos: Puntos más cercanos')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
