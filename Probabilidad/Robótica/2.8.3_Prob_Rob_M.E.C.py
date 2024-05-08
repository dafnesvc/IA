"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> Movimiento: Espacio de Configuración
Este script crea un espacio de configuración bidimensional y grafica el potencial en función
de las coordenadas X e Y. El potencial se calcula como la distancia euclidiana desde el origen (0,0).
El resultado se visualiza utilizando el contorno de nivel y un mapa de colores para representar el potencial."""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de costo (potencial)
def potential_function(x, y):
    return np.sqrt(x**2 + y**2)

# Generación del espacio de configuración
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = potential_function(X, Y)

# Graficar el espacio de configuración
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Potencial')
plt.title('Espacio de Configuración')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
