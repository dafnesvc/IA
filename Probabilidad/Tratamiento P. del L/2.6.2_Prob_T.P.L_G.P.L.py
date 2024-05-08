"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Tratamiento Probabilistico del lenguaje---> Gramaticas probabilisticas lexicalizadas
Este script genera datos de ejemplo simulando una función seno con ruido y los visualiza utilizando matplotlib.
La aplicación de gramáticas probabilísticas lexicalizadas en este contexto podría implicar el análisis y 
la interpretación de estos datos para modelar la distribución probabilística subyacente.
"""
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)  # Agregar ruido a la función seno

# Visualizar los datos
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Datos')
plt.title('Gramáticas Probabilísticas Lexicalizadas: Datos de ejemplo')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
