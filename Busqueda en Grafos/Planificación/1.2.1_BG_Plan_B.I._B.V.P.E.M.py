""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda informada --> Búsqueda Voraz Primero el Mejor"""

import heapq
# Definimos la clase Nodo para representar un nodo en el grafo
class Nodo:
    def __init__(self, estado, h):
        self.estado = estado  # El estado del nodo (posición en el grafo, por ejemplo)
        self.h = h            # Costo estimado desde este nodo hasta el nodo objetivo

    def __lt__(self, otro):
        return self.h < otro.h
    
# Función de búsqueda voraz
def busqueda_voraz(inicio, objetivo, obtener_vecinos, heuristica):
    frontera = [] # Inicializamos la frontera como una lista vacía
    heapq.heappush(frontera, inicio) # Agregamos el nodo inicial a la frontera usando heapq para mantenerla ordenada por la heurística
    visitados = set()  # Inicializamos un conjunto para mantener un registro de los nodos visitados

    # Mientras haya nodos en la frontera
    while frontera:
        nodo_actual = heapq.heappop(frontera)# Sacamos el nodo con menor heurística de la frontera

        # Si el nodo actual es el objetivo, hemos encontrado el camino
        if nodo_actual.estado == objetivo:
            return True  # Se encontró el objetivo

        visitados.add(nodo_actual.estado)

        # Iteramos sobre los vecinos del nodo actual
        for vecino in obtener_vecinos(nodo_actual.estado):
            if vecino in visitados: # Si el vecino ya ha sido visitado, lo ignoramos
                continue

            h_nuevo = heuristica(vecino, objetivo)  # Calculamos la heurística para el vecino
            nodo_vecino = Nodo(vecino, h_nuevo) # Creamos un nuevo nodo para el vecino


            heapq.heappush(frontera, nodo_vecino)# Agregamos el nodo vecino a la frontera

    return False  # No se encontró un camino hacia el objetivo

# Ejemplo de heurística (distancia Manhattan en un grafo cuadrado)
def heuristica_manhattan(pos_actual, pos_objetivo):
    x1, y1 = pos_actual
    x2, y2 = pos_objetivo
    return abs(x2 - x1) + abs(y2 - y1)

# Ejemplo de cómo definir obtener_vecinos para un grafo cuadrado
def obtener_vecinos_cuadrado(pos):
    x, y = pos
    vecinos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(nx, ny) for nx, ny in vecinos if 0 <= nx < 5 and 0 <= ny < 5]  # Limitamos el tamaño del cuadrado a 5x5

# Ejemplo de uso
inicio = Nodo((0, 0), heuristica_manhattan((0, 0), (4, 4)))
objetivo = (4, 4)
encontrado = busqueda_voraz(inicio, objetivo, obtener_vecinos_cuadrado, heuristica_manhattan)
if encontrado:
    print("Se encontró un camino hacia el objetivo.") # Si se encontró un camino, imprimimos un mensaje de éxito
else:
    print("No se encontró un camino hacia el objetivo.")  # Si no se encontró un camino, imprimimos un mensaje de fallo
