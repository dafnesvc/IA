"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> Cinemática Inversa"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de cinemática inversa
def inverse_kinematics(x, y):
    # Longitudes de los brazos del robot
    l1 = 1.0
    l2 = 1.0
    
    # Cálculo del ángulo theta2 usando ley de cosenos
    D = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    theta2 = np.arctan2(-np.sqrt(1 - D**2), D)
    
    # Cálculo del ángulo theta1 usando trigonometría
    theta1 = np.arctan2(y, x) - np.arctan2(l2 * np.sin(theta2), l1 + l2 * np.cos(theta2))
    
    return theta1, theta2

# Generación de puntos en el espacio de trabajo
x_points = np.linspace(-2, 2, 50)
y_points = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x_points, y_points)

# Cálculo de los ángulos correspondientes a cada punto
theta1, theta2 = inverse_kinematics(X, Y)

# Graficar el resultado
fig, ax = plt.subplots()
ax.contourf(X, Y, theta1, cmap='viridis')
ax.set_title('Ángulo Theta1 (rad)')
ax.set_xlabel('Coordenada X')
ax.set_ylabel('Coordenada Y')
plt.colorbar(ax.contourf(X, Y, theta1, cmap='viridis'), label='Ángulo Theta1 (rad)')
plt.show()

fig, ax = plt.subplots()
ax.contourf(X, Y, theta2, cmap='viridis')
ax.set_title('Ángulo Theta2 (rad)')
ax.set_xlabel('Coordenada X')
ax.set_ylabel('Coordenada Y')
plt.colorbar(ax.contourf(X, Y, theta2, cmap='viridis'), label='Ángulo Theta2 (rad)')
plt.show()
