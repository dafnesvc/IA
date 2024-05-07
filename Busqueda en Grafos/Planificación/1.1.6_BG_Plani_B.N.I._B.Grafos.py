""""Dafne Sarahi Villanueva Ceja 21310176
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda en Gráfos"""
from collections import deque

class Nodo:
    def __init__(self, estado, hijos=[]):
        self.estado = estado
        self.hijos = hijos

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def buscar_en_anchura(grafo, inicio, objetivo):
    frontera = deque([inicio])
    visitados = set([inicio])

    while frontera:
        nodo_actual = frontera.popleft()
        if nodo_actual.estado == objetivo:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            if hijo.estado not in visitados:
                frontera.append(hijo)
                visitados.add(hijo.estado)

    return None

# Ejemplo de uso
if __name__ == "__main__":
    # Construcción de un grafo de ejemplo
    nodo_a = Nodo("A")
    nodo_b = Nodo("B")
    nodo_c = Nodo("C")
    nodo_d = Nodo("D")
    nodo_e = Nodo("E")
    nodo_f = Nodo("F")

    nodo_a.agregar_hijo(nodo_b)
    nodo_a.agregar_hijo(nodo_c)
    nodo_b.agregar_hijo(nodo_d)
    nodo_b.agregar_hijo(nodo_e)
    nodo_c.agregar_hijo(nodo_f)

    # Búsqueda en anchura
    nodo_objetivo = buscar_en_anchura(nodo_a, nodo_a, "F")

    if nodo_objetivo:
        print("Objetivo encontrado:", nodo_objetivo.estado)
    else:
        print("Objetivo no encontrado.")
