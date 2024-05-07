""" Dafne Villanueva 2 Profundidad Iterativa
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda en Profundidad Iterativa

"""

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append(v)

    def dls(self, inicio, objetivo, profundidad_limite):
        visitado = set()
        stack = [(inicio, 0)]

        while stack:
            nodo, profundidad = stack.pop()

            if nodo == objetivo:
                return True

            if profundidad < profundidad_limite:
                if nodo not in visitado:
                    visitado.add(nodo)
                    if nodo in self.grafo:
                        for vecino in reversed(self.grafo[nodo]):
                            stack.append((vecino, profundidad + 1))

        return False

    def iddfs(self, inicio, objetivo, profundidad_limite):
        for limite in range(profundidad_limite + 1):
            if self.dls(inicio, objetivo, limite):
                return True
        return False

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

inicio = 2
objetivo = 3
profundidad_limite = 3

print("Búsqueda en profundidad iterativa comenzando desde el vértice 2:")
if grafo.iddfs(inicio, objetivo, profundidad_limite):
    print(f"\nSe encontró un camino desde {inicio} hasta {objetivo} dentro de la profundidad límite.")
else:
    print(f"\nNo se encontró un camino desde {inicio} hasta {objetivo} dentro de la profundidad límite.")
