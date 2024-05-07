""""" Dafne Villanueva 21310176.
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda en Anchura de costo uniforme 

Este código implementa la búsqueda en anchura de costo uniforme (UCS) en un grafo ponderado utilizando la cola
de prioridad para mantener el orden de los nodos a visitar.
"""

import heapq #Importa el módulo heapq, que proporciona funciones para trabajar con colas de prioridad.

class Grafo: # Define una clase llamada Grafo que representa un grafo ponderado.
    def __init__(self): #Define el constructor de la clase Grafo. En este método, se inicializa el atributo grafo como un diccionario vacío.
        self.grafo = {}

    def agregar_arista(self, u, v, peso): #Este método permite agregar una arista ponderada al grafo. Toma tres parámetros: u y v, que son los nodos que conecta la arista, y peso, que es el peso asociado a la arista.
        if u not in self.grafo: # Verifica si el nodo u no está en el diccionario grafo.
            self.grafo[u] = []  #  Si el nodo u no está en el diccionario, se crea una lista vacía asociada a él.
        self.grafo[u].append((v, peso)) #Se agrega una tupla (v, peso) a la lista de adyacencia del nodo u, indicando que hay una arista que conecta u y v con un peso determinado.

    def ucs(self, inicio, objetivo): #Este método implementa el algoritmo de búsqueda de costo uniforme (UCS). Toma dos parámetros: inicio, que es el nodo de inicio de la búsqueda, y objetivo, que es el nodo objetivo al que se desea llegar.
        cola_prioridad = [(0, inicio)] #Se inicializa la cola de prioridad con una tupla (0, inicio), donde 0 representa el costo acumulado para llegar al nodo inicio.
        visitado = set() #Se inicializa un conjunto para mantener un registro de los nodos visitados durante la búsqueda.

        while cola_prioridad: # Comienza un bucle que continuará hasta que la cola de prioridad esté vacía.
            costo, nodo = heapq.heappop(cola_prioridad) # Se extrae el nodo con el menor costo acumulado de la cola de prioridad.

            if nodo == objetivo: #Se verifica si el nodo extraído es igual al nodo objetivo. Si es así, se ha encontrado un camino y se devuelve el costo acumulado hasta ese nodo.
                return costo

            if nodo not in visitado: #Se verifica si el nodo no ha sido visitado previamente.
                visitado.add(nodo) #Se agrega el nodo al conjunto de nodos visitados.

                if nodo in self.grafo:
                    for vecino, costo_arista in self.grafo[nodo]: # Se itera sobre los vecinos del nodo actual y sus costos asociados.
                        if vecino not in visitado: #Se verifica si el vecino no ha sido visitado previamente.
                            heapq.heappush(cola_prioridad, (costo + costo_arista, vecino)) #Se agrega el vecino a la cola de prioridad con el costo acumulado actualizado.

        return float('inf')  # Si no se encuentra el objetivo, se devuelve infinito


# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 5)
grafo.agregar_arista('B', 'C', 2)
grafo.agregar_arista('B', 'D', 3)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('D', 'E', 2)

inicio = 'A' #Se define el nodo de inicio para la búsqueda en el grafo.
objetivo = 'E' #Se define el nodo objetivo al que se quiere llegar en el grafo.
costo_total = grafo.ucs(inicio, objetivo) #Se llama al método ucs del objeto grafo
if costo_total != float('inf'): #Se verifica si el costo total devuelto por la búsqueda es diferente de infinito.  (significa que no se encontró un camino desde el nodo de inicio hasta el nodo objetivo.)
    print(f"El costo mínimo desde {inicio} hasta {objetivo} es {costo_total}.") #Si se encontró un camino desde el nodo de inicio hasta el nodo objetivo se imprime un mensaje indicando el costo mínimo para llegar desde el nodo de inicio hasta el nodo objetivo.
else: #Si el costo total es infinito, significa que no se encontró un camino desde el nodo de inicio hasta el nodo objetivo.
    print(f"No se encontró un camino desde {inicio} hasta {objetivo}.") #En este caso, se imprime un mensaje indicando que no se encontró un camino desde el nodo de inicio hasta el nodo objetivo.

#Esto indica que el costo mínimo para llegar desde el nodo 'A' hasta el nodo 'E' en el grafo dado es de 6 unidades.