"""Dafne Villanueva 2131016
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda en Anchura

Este programa crea un grafo y luego realiza una búsqueda en anchura  comenzando desde un 
nodo dado (en este caso, el nodo 2). La búsqueda en anchura se realiza utilizando una cola
para mantener un seguimiento de los nodos que se deben visitar // El programa busca recorrer
el grafo de manera sistemática y eficiente, visitando todos los nodos alcanzables desde un nodo inicial dado.
Esto es útil en una variedad de problemas, como encontrar el camino más corto entre dos nodos, verificar si hay
un ciclo en el grafo, o simplemente para recorrer todos los nodos en orden.
 
"""


from collections import defaultdict, deque #Importamos las clases defaultdict y deque del módulo collections, defaultdict se utiliza para crear un diccionario con un valor predeterminado para cada clave, y deque es una cola optimizada para operaciones de inserción y eliminación en ambos extremos.
                                        
class Grafo: #Definimos una clase llamada Grafo para representar nuestro grafo.
    def __init__(self): # El método __init__ es el constructor de la clase Grafo. Aquí inicializamos el atributo grafo como un defaultdict vacío, que se utilizará para almacenar las listas de adyacencia de los vértices. 
        self.grafo = defaultdict(list) #inicializa el atributo grafo

    def agregar_arista(self, u, v): #Este método permite agregar una arista al grafo. Toma dos parámetros u y v, que son los vértices que conecta la arista.
        self.grafo[u].append(v)

    def bfs(self, inicio): #Este método realiza la búsqueda en anchura en el grafo a partir del vértice especificado por inicio.
        visitado = set()   #Creamos un conjunto para mantener un registro de los vértices que ya hemos visitado durante el recorrido.
        cola = deque([inicio]) #Creamos una cola (deque) que contendrá los vértices que aún no hemos explorado y que están listos para ser visitados. Inicializamos la cola con el vértice de inicio.
        visitado.add(inicio) #Marcamos el vértice de inicio como visitado

        while cola: #Comienza un bucle que continuará hasta que la cola esté vacía, lo que significa que hemos visitado todos los vértices alcanzables desde el vértice de inicio.
            vertice = cola.popleft() #Tomamos el vértice al frente de la cola para visitarlo y lo removemos de la cola.
            print(vertice, end=" ") # Imprimimos el vértice que estamos visitando.

            for vecino in self.grafo[vertice]: # Iteramos sobre todos los vecinos del vértice actual.
                if vecino not in visitado: #Verificamos si el vecino no ha sido visitado.
                    cola.append(vecino) # Si el vecino no ha sido visitado, lo agregamos a la cola para visitarlo más tarde.
                    visitado.add(vecino) #Marcamos el vecino como visitado.

# Ejemplo de uso
grafo = Grafo() #Se crea una instancia de la clase Grafo, lo que significa que se inicializa un nuevo objeto de la clase Grafo
grafo.agregar_arista(0, 1) # Se agrega una arista entre los nodos 0 y 1 al grafo. Esto significa que hay una conexión directa entre el nodo 0 y el nodo 1 en el grafo.
grafo.agregar_arista(0, 2) 
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido BFS comenzando desde el vértice 2:") #Imprimimos un mensaje antes de imprimir el recorrido BFS para mayor claridad.
grafo.bfs(2) # Llamamos al método bfs en el objeto grafo con el vértice de inicio 2 para realizar la búsqueda en anchura desde ese vértice.
