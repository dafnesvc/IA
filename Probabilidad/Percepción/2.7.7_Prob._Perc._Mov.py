"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Percepción---> Movimiento"""
import numpy as np
import matplotlib.pyplot as plt

# Función para simular el movimiento
def simulate_motion(initial_position, initial_velocity, acceleration, time):
    # Calcular la posición en cada instante de tiempo
    position = initial_position + initial_velocity * time + 0.5 * acceleration * time**2
    return position

# Parámetros iniciales
initial_position = 0  # Posición inicial del objeto
initial_velocity = 5  # Velocidad inicial del objeto
acceleration = 2      # Aceleración del objeto
time = np.linspace(0, 10, 100)  # Tiempo de simulación de 0 a 10 segundos, dividido en 100 puntos

# Simular el movimiento
position = simulate_motion(initial_position, initial_velocity, acceleration, time)

# Graficar el movimiento
plt.plot(time, position, label='Posición')
plt.title('Simulación de Movimiento')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición')
plt.legend()
plt.grid(True)
plt.show()
