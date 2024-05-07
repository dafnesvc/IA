"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Incertidumbre y Probabilidad--->Distribución de Probabilidad

Este script generará un gráfico de barras que muestra la distribución de probabilidad de cada evento. 
Cada barra representará la probabilidad de un evento específico en el eje y, y el nombre del evento estará
en el eje x. Esto proporciona una visualización clara de cómo se distribuyen las probabilidades entre diferentes 
eventos."""

import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
events = ['A', 'B', 'C', 'D', 'E']
prob_events = np.array([0.2, 0.3, 0.15, 0.1, 0.25])  # Probabilidad de cada evento

# Graficar la distribución de probabilidad
plt.bar(events, prob_events)
plt.xlabel('Eventos')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad')
plt.show()
