"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> HW Robótico: Sensores y Actuadores
Este script simula el movimiento de un robot en una cuadrícula 2D con obstáculos aleatorios.
El robot puede moverse hacia arriba, abajo, izquierda o derecha, y tiene sensores para detectar 
obstáculos en su entorno. Los resultados de la detección de obstáculos se muestran en la consola,
y la trayectoria del robot junto con los obstáculos se grafican en una cuadrícula."""

import numpy as np
import matplotlib.pyplot as plt

# Función para simular el movimiento del robot
def move_robot(position, action):
    if action == 'up':
        position[0] -= 1
    elif action == 'down':
        position[0] += 1
    elif action == 'left':
        position[1] -= 1
    elif action == 'right':
        position[1] += 1
    return position

# Función para simular la detección de obstáculos por parte del robot
def detect_obstacle(position, grid):
    # Verificar si hay un obstáculo en la posición actual del robot
    if grid[position[0], position[1]] == 1:
        return True
    else:
        return False

# Crear una cuadrícula de 10x10 con obstáculos aleatorios
grid_size = 10
obstacle_density = 0.2
grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[1 - obstacle_density, obstacle_density])

# Posición inicial del robot
robot_position = [0, 0]

# Movimientos posibles del robot
possible_actions = ['up', 'down', 'left', 'right']

# Realizar 10 movimientos del robot y registrar los obstáculos detectados
detected_obstacles = []
for _ in range(10):
    # Elegir un movimiento al azar
    action = np.random.choice(possible_actions)
    
    # Mover el robot
    new_position = move_robot(robot_position.copy(), action)
    
    # Verificar si hay un obstáculo en la nueva posición
    obstacle_detected = detect_obstacle(new_position, grid)
    
    # Registrar la detección de obstáculos
    detected_obstacles.append(obstacle_detected)
    
    # Actualizar la posición del robot si no hay obstáculo
    if not obstacle_detected:
        robot_position = new_position

# Graficar la cuadrícula y la trayectoria del robot
plt.imshow(grid, cmap='binary')
plt.plot(robot_position[1], robot_position[0], 'ro')  # Posición actual del robot
plt.title('Simulación de Robot con Sensores y Actuadores')
plt.xlabel('Columna')
plt.ylabel('Fila')
plt.xticks(range(grid_size))
plt.yticks(range(grid_size))
plt.gca().invert_yaxis()  # Invertir el eje y para que la posición (0, 0) esté en la esquina superior izquierda
plt.grid(True)
plt.show()

# Imprimir los resultados de la detección de obstáculos
print("Detección de Obstáculos:", detected_obstacles)
