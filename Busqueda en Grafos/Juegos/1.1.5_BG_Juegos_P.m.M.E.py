""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Juegos---> Posibilidad: MinimaxEsperado

Este algoritmo se utiliza para determinar la mejor jugada posible para el jugador maximizador,
asumiendo que el oponente también juega de manera óptima. En lugar de simplemente buscar el valor
mínimo o máximo en el árbol de juego como lo hace el Minimax tradicional, el Minimax Esperado utiliza 
la esperanza matemática para calcular el valor esperado de los posibles resultados del juego en un estado dado."""

import math

class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Valor asociado al nodo
        self.hijos = []     # Lista de hijos del nodo

def minimax_esperado(nodo, profundidad, es_maximizador):
    # Caso base: si alcanzamos la profundidad máxima o el nodo no tiene hijos, retornar su valor
    if profundidad == 0 or len(nodo.hijos) == 0:
        return nodo.valor
    
    if es_maximizador:
        max_eval = -math.inf  # Inicializar la mejor evaluación para un maximizador como menos infinito
        # Iterar sobre los hijos del nodo actual
        for hijo in nodo.hijos:
            # Llamada recursiva para obtener la mejor evaluación de los hijos
            eval = minimax_esperado(hijo, profundidad - 1, False)
            # Actualizar la mejor evaluación encontrada
            max_eval = max(max_eval, eval)
        return max_eval  # Retornar la mejor evaluación para el maximizador
    else:
        min_eval = math.inf  # Inicializar la mejor evaluación para un minimizador como infinito
        # Iterar sobre los hijos del nodo actual
        for hijo in nodo.hijos:
            # Llamada recursiva para obtener la mejor evaluación de los hijos
            eval = minimax_esperado(hijo, profundidad - 1, True)
            # Actualizar la mejor evaluación encontrada
            min_eval = min(min_eval, eval)
        return min_eval  # Retornar la mejor evaluación para el minimizador

# Ejemplo de uso
nodo1 = Nodo(3)
nodo2 = Nodo(5)
nodo3 = Nodo(2)
nodo4 = Nodo(9)
nodo5 = Nodo(7)

# Construcción del árbol de juego
nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]

profundidad_maxima = 2
es_maximizador = True

# Calcular el valor óptimo esperado utilizando el algoritmo Minimax
resultado = minimax_esperado(nodo1, profundidad_maxima, es_maximizador)
print("El valor óptimo esperado es:", resultado)

"""Esto se debe a que el algoritmo Minimax se ejecutará sobre el árbol de juego y determinará
 el valor óptimo esperado para el jugador maximizador en la profundidad máxima especificada.
   En este caso, el valor óptimo esperado es 7."""