"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razonamiento Probabilístico--->Muestreo Directo y Por Rechazo

Este script genera muestras aleatorias utilizando tanto el método de muestreo directo como el método 
de muestreo por rechazo, y luego las visualiza junto con la función de densidad de probabilidad (PDF) 
utilizando matplotlib."""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de densidad de probabilidad (PDF)
def pdf(x):
    return np.sin(x) ** 2

# Rango de valores para x
x_values = np.linspace(0, np.pi, 1000)

# Calcular el máximo de la PDF para el método de rechazo
max_pdf = np.max(pdf(x_values))

# Generar puntos aleatorios para el muestreo directo y por rechazo
num_samples = 1000
x_samples_directo = np.random.uniform(0, np.pi, num_samples)
y_samples_directo = pdf(x_samples_directo)

x_samples_rechazo = []
y_samples_rechazo = []
for _ in range(num_samples):
    x = np.random.uniform(0, np.pi)
    y = np.random.uniform(0, max_pdf)
    if y <= pdf(x):
        x_samples_rechazo.append(x)
        y_samples_rechazo.append(y)

# Visualización de los resultados
plt.figure(figsize=(10, 6))
plt.plot(x_values, pdf(x_values), label='PDF')
plt.scatter(x_samples_directo, y_samples_directo, color='red', alpha=0.5, label='Muestreo Directo')
plt.scatter(x_samples_rechazo, y_samples_rechazo, color='green', alpha=0.5, label='Muestreo por Rechazo')
plt.title('Muestreo Directo y Por Rechazo')
plt.xlabel('x')
plt.ylabel('PDF(x)')
plt.legend()
plt.grid(True)
plt.show()
