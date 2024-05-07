""""Dafne Sarahi Villanueva Ceja 21310176 
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda Bidireccional"""
class Nodo:
    def __init__(self, estado, hijos=[]):
        self.estado = estado
        self.hijos = hijos
        self.padre_inicio = None
        self.padre_objetivo = None

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def buscar_bidireccional(inicial, objetivo):
    frontera_inicio = [inicial]
    frontera_objetivo = [objetivo]
    visitados_inicio = {inicial}
    visitados_objetivo = {objetivo}

    while frontera_inicio and frontera_objetivo:
        # Expandir desde el nodo inicial
        nodo_actual_inicio = frontera_inicio.pop(0)
        for hijo in nodo_actual_inicio.hijos:
            if hijo not in visitados_inicio:
                frontera_inicio.append(hijo)
                visitados_inicio.add(hijo)
                hijo.padre_inicio = nodo_actual_inicio

        # Verificar si se encuentra una intersección
        for nodo in frontera_inicio:
            if nodo in visitados_objetivo:
                return nodo

        # Expandir desde el nodo objetivo
        nodo_actual_objetivo = frontera_objetivo.pop(0)
        for hijo in nodo_actual_objetivo.hijos:
            if hijo not in visitados_objetivo:
                frontera_objetivo.append(hijo)
                visitados_objetivo.add(hijo)
                hijo.padre_objetivo = nodo_actual_objetivo

        # Verificar si se encuentra una intersección
        for nodo in frontera_objetivo:
            if nodo in visitados_inicio:
                return nodo

    return None


def reconstruir_camino(nodo_interseccion):
    camino_inicio = []
    while nodo_interseccion.padre_inicio:
        camino_inicio.append(nodo_interseccion.estado)
        nodo_interseccion = nodo_interseccion.padre_inicio
    camino_inicio.append(nodo_interseccion.estado)

    camino_objetivo = []
    while nodo_interseccion.padre_objetivo:
        camino_objetivo.append(nodo_interseccion.estado)
        nodo_interseccion = nodo_interseccion.padre_objetivo
    camino_objetivo.append(nodo_interseccion.estado)

    return list(reversed(camino_inicio)), camino_objetivo[1:]

# Ejemplo de uso
if __name__ == "__main__":
    # Construcción de un grafo de ejemplo
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
    nodo_c.agregar_hijo(nodo_d)
    nodo_d.agregar_hijo(nodo_f)  # Conexión directa de D a F
    nodo_e.agregar_hijo(nodo_f)  # Conexión directa de E a F

    # Búsqueda bidireccional
    nodo_interseccion = buscar_bidireccional(nodo_a, nodo_f)

    if nodo_interseccion:
        camino_inicio, camino_objetivo = reconstruir_camino(nodo_interseccion)
        camino = camino_inicio + camino_objetivo
        print("Camino encontrado:", camino)
    else:
        print("No se encontró un camino entre los nodos inicial y objetivo.")
