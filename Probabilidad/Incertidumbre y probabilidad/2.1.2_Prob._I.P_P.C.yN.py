"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Incertidumbre y Probabilidad---> Probabilidad Condicionada y Normalización
Este script calculará y graficará las probabilidades condicionadas normalizadas para cada evento, mostrando 
cómo varía la probabilidad de cada evento condicionado a cada uno de los eventos base (A, B, C, D, E)."""

import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
events = ['A', 'B', 'C', 'D', 'E']
prob_events = np.array([0.1, 0.2, 0.3, 0.2, 0.2])  # Probabilidad de cada evento
prob_conditional = np.array([[0.2, 0.3, 0.1, 0.1, 0.3],   # Probabilidad condicionada de A dado cada evento
                             [0.1, 0.4, 0.2, 0.1, 0.2],   # Probabilidad condicionada de B dado cada evento
                             [0.3, 0.2, 0.1, 0.2, 0.2],   # Probabilidad condicionada de C dado cada evento
                             [0.2, 0.1, 0.3, 0.3, 0.1],   # Probabilidad condicionada de D dado cada evento
                             [0.1, 0.3, 0.2, 0.2, 0.2]])  # Probabilidad condicionada de E dado cada evento

# Función para calcular la probabilidad condicionada y normalizarla
def conditional_probability(event_index):
    p_conditional = prob_conditional[event_index] * prob_events[event_index]  # Multiplicar por la probabilidad del evento base
    p_conditional_normalized = p_conditional / np.sum(p_conditional)  # Normalizar la probabilidad
    return p_conditional_normalized

# Calcular la probabilidad condicionada y normalizada para cada evento
conditional_probs = [conditional_probability(i) for i in range(len(events))]

# Graficar las probabilidades condicionadas normalizadas
fig, ax = plt.subplots()
for i, event in enumerate(events):
    ax.bar(events, conditional_probs[i], label=f'Cond. dado {event}')

ax.set_xlabel('Eventos')
ax.set_ylabel('Probabilidad')
ax.set_title('Probabilidad Condicionada y Normalizada')
ax.legend()
plt.show()
