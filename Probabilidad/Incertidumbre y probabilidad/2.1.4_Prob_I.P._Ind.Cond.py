"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Incertidumbre y Probabilidad---> Independencia Condicional
Este script generará tres gráficos de barras que muestran la probabilidad condicional de un conjunto
de eventos B dado diferentes valores de un evento A. Cada subgráfico representa la independencia condicional
entre A y B para diferentes valores de A."""

import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
events_A = ['A1', 'A2', 'A3']
events_B = ['B1', 'B2']
prob_A = np.array([0.4, 0.3, 0.3])  # Probabilidad de eventos para A
prob_B_given_A1 = np.array([0.6, 0.4])  # Probabilidad de eventos B dado A1
prob_B_given_A2 = np.array([0.5, 0.5])  # Probabilidad de eventos B dado A2
prob_B_given_A3 = np.array([0.3, 0.7])  # Probabilidad de eventos B dado A3

# Graficar la independencia condicional
fig, axs = plt.subplots(3, 1, figsize=(8, 6))

# Gráfico para A
axs[0].bar(events_A, prob_A)
axs[0].set_title('Probabilidad de A')

# Gráfico para B dado A1
axs[1].bar(events_B, prob_B_given_A1)
axs[1].set_title('Probabilidad de B dado A1')

# Gráfico para B dado A2
axs[2].bar(events_B, prob_B_given_A2)
axs[2].set_title('Probabilidad de B dado A2')

# Ajustar diseño de los subplots
plt.tight_layout()
plt.show()

