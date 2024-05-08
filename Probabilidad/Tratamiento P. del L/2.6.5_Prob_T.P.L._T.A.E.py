"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Tratamiento Probabilistico del lenguaje---> Traducción Automática Estadística"""
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = 2 * x + 3 + np.random.normal(0, 1, size=x.shape)  # y = 2x + 3 + ruido

# Visualizar los datos
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Datos')
plt.title('Traducción Automática Estadística: Ejemplo de Regresión Lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

