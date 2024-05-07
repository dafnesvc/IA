"""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en grafos ---> Utilidad y Toma de Decisiones---> Teoría de Juegos: Equilibrios y Mecanismos

Este script calcula y visualiza las estrategias de equilibrio de Nash en un juego simple de dos jugadores
con dos acciones posibles para cada jugador. Las estrategias de equilibrio de Nash se calculan encontrando
las mejores respuestas para cada jugador dadas las estrategias del otro jugador. Luego, las estrategias de
equilibrio se visualizan utilizando un gráfico de barras donde cada jugador muestra la probabilidad de elegir
cada acción."""

import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de pagos para el jugador 1
payoff_matrix_player1 = np.array([[4, 1],
                                  [3, 2]])

# Definir la matriz de pagos para el jugador 2
payoff_matrix_player2 = np.array([[4, 3],
                                  [1, 2]])

# Calcular las estrategias de equilibrio de Nash para el jugador 1
nash_eq_player1 = np.where(payoff_matrix_player1 == np.max(payoff_matrix_player1, axis=0), 1, 0)
nash_eq_player1 = nash_eq_player1 / np.sum(nash_eq_player1, axis=0)  # Normalizar

# Calcular las estrategias de equilibrio de Nash para el jugador 2
nash_eq_player2 = np.where(payoff_matrix_player2 == np.max(payoff_matrix_player2, axis=1)[:, None], 1, 0)
nash_eq_player2 = nash_eq_player2 / np.sum(nash_eq_player2, axis=1)[:, None]  # Normalizar

# Imprimir las estrategias de equilibrio de Nash
print("Estrategias de Equilibrio de Nash para el jugador 1:", nash_eq_player1)
print("Estrategias de Equilibrio de Nash para el jugador 2:", nash_eq_player2)

# Visualizar el resultado
plt.figure(figsize=(8, 6))
plt.bar(np.arange(len(nash_eq_player1[0])), nash_eq_player1[0], color='b', alpha=0.5, label='Jugador 1, Acción A')
plt.bar(np.arange(len(nash_eq_player1[1])), nash_eq_player1[1], bottom=nash_eq_player1[0], color='b', alpha=0.5, label='Jugador 1, Acción B')
plt.bar(np.arange(len(nash_eq_player2[0])) + 0.35, nash_eq_player2[0], color='r', alpha=0.5, label='Jugador 2, Acción A')
plt.bar(np.arange(len(nash_eq_player2[1])) + 0.35, nash_eq_player2[1], bottom=nash_eq_player2[0], color='r', alpha=0.5, label='Jugador 2, Acción B')
plt.xlabel('Acciones')
plt.ylabel('Probabilidad')
plt.title('Estrategias de Equilibrio de Nash')
plt.xticks(np.arange(len(nash_eq_player1[0])) + 0.17, ['A', 'B'])
plt.legend()
plt.show()
