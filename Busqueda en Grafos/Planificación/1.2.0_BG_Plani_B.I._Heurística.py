""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda informada --> Heurística"""

import heapq  # Importamos el módulo heapq para utilizar colas de prioridad

class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializamos el grafo como un diccionario vacío

    def agregar_arista(self, u, v, peso):
        """
        Método para agregar una arista al grafo desde el nodo 'u' al nodo 'v' con un peso dado.
        """
        if u not in self.grafo:
            self.grafo[u] = []  # Si el nodo 'u' no está en el grafo, lo agregamos con una lista vacía como valor
        self.grafo[u].append((v, peso))  # Agregamos la arista al nodo 'u' con su peso como una tupla en la lista de adyacencia

    def a_estrella(self, inicio, objetivo, heuristicas):
        """
        Método para realizar la búsqueda A* desde el nodo 'inicio' hasta el nodo 'objetivo' con las heurísticas proporcionadas.
        """
        heap = [(0, inicio)]  # Creamos una cola de prioridad (heap) con una tupla (costo acumulado, nodo actual) iniciando desde el nodo 'inicio'
        visitado = set()  # Creamos un conjunto para mantener un registro de los nodos visitados

        while heap:  # Mientras haya elementos en la cola de prioridad
            costo_actual, nodo_actual = heapq.heappop(heap)  # Extraemos el nodo con el menor costo acumulado de la cola de prioridad

            if nodo_actual == objetivo:  # Si el nodo actual es el objetivo, hemos encontrado el camino óptimo
                return costo_actual  # Retornamos el costo acumulado hasta el nodo objetivo

            if nodo_actual not in visitado:  # Si el nodo actual no ha sido visitado
                visitado.add(nodo_actual)  # Marcamos el nodo actual como visitado

                if nodo_actual in self.grafo:  # Si el nodo actual tiene vecinos en el grafo
                    for vecino, peso in self.grafo[nodo_actual]:  # Iteramos sobre los vecinos del nodo actual
                        costo_hasta_vecino = costo_actual + peso  # Calculamos el costo acumulado hasta el vecino
                        costo_heuristico = costo_hasta_vecino + heuristicas[vecino]  # Calculamos el costo heurístico para el vecino
                        heapq.heappush(heap, (costo_heuristico, vecino))  # Agregamos el vecino a la cola de prioridad con su costo heurístico

        return float('inf')  # Si no se encuentra el objetivo, retornamos infinito

# Creamos una instancia del grafo
grafo = Grafo()

# Agregamos las aristas al grafo
grafo.agregar_arista('A', 'B', 5)
grafo.agregar_arista('A', 'C', 3)
grafo.agregar_arista('B', 'D', 4)
grafo.agregar_arista('C', 'D', 2)

# Definimos el nodo inicial, el nodo objetivo y las heurísticas para cada nodo
inicio = 'A'
objetivo = 'D'
heuristicas = {'A': 5, 'B': 3, 'C': 2, 'D': 0}

# Llamamos al método A* para encontrar el camino mínimo desde el nodo inicial hasta el nodo objetivo
costo_minimo = grafo.a_estrella(inicio, objetivo, heuristicas)

# Imprimimos el resultado
print(f"El costo mínimo desde {inicio} hasta {objetivo} es {costo_minimo}.")

#Esto indica que el algoritmo A* ha encontrado un camino desde el nodo 'A' hasta el nodo 'D' con un costo total de 7.