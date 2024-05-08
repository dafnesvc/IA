"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Robótica---> Incertidumbre"""
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios con cierta incertidumbre
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, size=len(x))  # Agregamos ruido gaussiano

# Calcular la incertidumbre como la desviación estándar del ruido
uncertainty = np.std(np.random.normal(0, 0.1, size=(len(x), 100)), axis=1)

# Graficar los datos con la incertidumbre
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Datos observados', color='blue')
plt.fill_between(x, y - uncertainty, y + uncertainty, color='gray', alpha=0.2, label='Incertidumbre')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Incertidumbre en datos observados')
plt.legend()
plt.grid(True)
plt.show()
