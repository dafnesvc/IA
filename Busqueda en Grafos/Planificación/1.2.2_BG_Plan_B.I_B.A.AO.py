""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda informada --> Búsquedas A* y AO*"""
import heapq  # Importamos el módulo heapq para usar colas de prioridad

# Definimos la clase Nodo para representar un nodo en el grafo
class Nodo:
    def __init__(self, estado, h):
        self.estado = estado  # El estado del nodo (por ejemplo, posición en el grafo)
        self.h = h            # Costo estimado desde este nodo hasta el nodo objetivo

    def __lt__(self, otro):
        return self.h < otro.h  # Definimos el operador '<' para comparar nodos basados en su heurística

# Función de búsqueda voraz
def busqueda_voraz(inicio, objetivo, obtener_vecinos, heuristica):
    frontera = []  # Inicializamos la frontera como una lista vacía
    heapq.heappush(frontera, inicio)  # Agregamos el nodo inicial a la frontera usando heapq para mantenerla ordenada por la heurística
    visitados = set()  # Inicializamos un conjunto para mantener un registro de los nodos visitados

    while frontera:  # Mientras haya nodos en la frontera
        nodo_actual = heapq.heappop(frontera)  # Sacamos el nodo con menor heurística de la frontera

        if nodo_actual.estado == objetivo:  # Si el nodo actual es el objetivo, hemos encontrado el camino
            return True  # Retornamos True

        visitados.add(nodo_actual.estado)  # Marcamos el nodo actual como visitado

        # Iteramos sobre los vecinos del nodo actual
        for vecino in obtener_vecinos(nodo_actual.estado):
            if vecino in visitados:  # Si el vecino ya ha sido visitado, lo ignoramos
                continue

            h_nuevo = heuristica(vecino, objetivo)  # Calculamos la heurística para el vecino
            nodo_vecino = Nodo(vecino, h_nuevo)  # Creamos un nuevo nodo para el vecino

            heapq.heappush(frontera, nodo_vecino)  # Agregamos el nodo vecino a la frontera

    return False  # Si no se encuentra el objetivo, retornamos False

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
inicio = Nodo((0, 0), heuristica_manhattan((0, 0), (4, 4)))  # Nodo inicial en la esquina superior izquierda
objetivo = (4, 4)  # Nodo objetivo en la esquina inferior derecha
encontrado = busqueda_voraz(inicio, objetivo, obtener_vecinos_cuadrado, heuristica_manhattan)  # Realizamos la búsqueda voraz
if encontrado:
    print("Se encontró un camino hacia el objetivo.")  # Si se encontró un camino, imprimimos un mensaje de éxito
else:
    print("No se encontró un camino hacia el objetivo.")  # Si no se encontró un camino, imprimimos un mensaje de fallo
