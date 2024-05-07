"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Razon. Probabil. en el Tiempo---> Procesos Estacionarios

Este script genera una serie de tiempo de datos aleatorios siguiendo una distribución normal,
lo que simula el comportamiento de un proceso estacionario. Luego, calcula la media móvil para 
suavizar la serie de tiempo y visualizar la tendencia a lo largo del tiempo. Los resultados se muestran
mediante un gráfico que muestra la serie de tiempo original y su media móvil."""


import numpy as np
import matplotlib.pyplot as plt

# Definir la media y la varianza del proceso estacionario
mu = 0
sigma = 1

# Generar una serie de tiempo de datos aleatorios siguiendo una distribución normal
# Esto simula el comportamiento de un proceso estacionario
num_steps = 1000
time_series = np.random.normal(mu, sigma, num_steps)

# Calcular la media móvil para suavizar la serie de tiempo y visualizar la tendencia
window_size = 20
moving_average = np.convolve(time_series, np.ones(window_size)/window_size, mode='valid')

# Visualizar la serie de tiempo y su media móvil
plt.figure(figsize=(10, 6))
plt.plot(time_series, label='Serie de Tiempo')
plt.plot(np.arange(window_size-1, num_steps), moving_average, label=f'Media Móvil ({window_size}-paso)')
plt.title('Proceso Estacionario y Media Móvil')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()
