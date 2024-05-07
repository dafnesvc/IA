""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda informada --> Busqueda online

Este tipo de búsqueda se realiza de manera incremental, tomando decisiones en tiempo
real a medida que se recibe información sobre el entorno. En este caso, se utilizará
un enfoque similar al algoritmo A*, pero adaptado para la búsqueda en línea. """


import heapq  # Importamos el módulo heapq para utilizar colas de prioridad

class BusquedaOnline:
    def __init__(self, grafo):
        self.grafo = grafo  # Inicializamos el grafo sobre el que se realizará la búsqueda

    def a_estrella_online(self, inicio, objetivo, heuristicas):
        heap = [(0, inicio)]  # Cola de prioridad inicializada con el nodo inicial y su costo acumulado
        visitado = set()  # Conjunto para mantener un registro de los nodos visitados

        while heap:
            costo_actual, nodo_actual = heapq.heappop(heap)  # Extraemos el nodo con menor costo acumulado

            if nodo_actual == objetivo:  # Verificamos si hemos alcanzado el objetivo
                return costo_actual

            if nodo_actual not in visitado:  # Si el nodo no ha sido visitado aún
                visitado.add(nodo_actual)  # Lo agregamos al conjunto de nodos visitados

                if nodo_actual in self.grafo:  # Si el nodo tiene vecinos en el grafo
                    for vecino, peso in self.grafo[nodo_actual]:  # Iteramos sobre los vecinos
                        # Calculamos el costo acumulado hasta el vecino, sumando el costo actual,
                        # el peso de la arista y la heurística del vecino
                        heapq.heappush(heap, (costo_actual + peso + heuristicas[vecino], vecino))

        return float('inf')  # Si no se encuentra el objetivo, retornamos infinito

# Ejemplo de uso
grafo = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 4)],
    'C': [('D', 2)],
    'D': []
}
inicio = 'A'
objetivo = 'D'
heuristicas = {'A': 5, 'B': 3, 'C': 2, 'D': 0}  # Heurísticas para cada nodo

# Creamos una instancia de la búsqueda online y llamamos al método A* online para encontrar el camino mínimo
busqueda_online = BusquedaOnline(grafo)
costo_minimo = busqueda_online.a_estrella_online(inicio, objetivo, heuristicas)

# Imprimimos el resultado
print(f"El costo mínimo desde {inicio} hasta {objetivo} es {costo_minimo}.")
