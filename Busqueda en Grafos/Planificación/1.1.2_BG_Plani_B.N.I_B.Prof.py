"""" Dafne Villanueva 21310176.
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda en Profundidad

El objetivo del código es realizar un recorrido en profundidad (DFS) en un grafo dado.
Para lograr este objetivo, el código primero crea un grafo no dirigido utilizando la clase 
"Grafo" y agrega varias aristas al grafo. Luego, imprime un mensaje indicando que se realizará un
recorrido DFS comenzando desde un vértice específico (en este caso, el vértice 2). Finalmente, llama
al método dfs del objeto grafo, pasando el vértice de inicio como argumento, lo que inicia el recorrido DFS.
"""

class Grafo: #Se define una clase llamada Grafo.
    def __init__(self): #inicialización __init__
        self.grafo = {} # se crea un diccionario vacío llamado grafo, que será utilizado para almacenar las listas de adyacencia de los nodos.

    def agregar_arista(self, u, v): #El método agregar_arista permite agregar una arista al grafo entre los nodos u y v. 
        if u not in self.grafo: #Verifica si el nodo u ya existe en el grafo,
            self.grafo[u] = [] # si no, lo agrega como una clave con una lista vacía asociada
        self.grafo[u].append(v) # Luego, agrega v a la lista de adyacencia de u.

    def dfs_util(self, nodo, visitado): #El método dfs_util es una función auxiliar para realizar la búsqueda en profundidad (DFS) de manera recursiva. 
        visitado.add(nodo) #Toma un nodo y un conjunto de nodos visitados. 
        print(nodo, end=" ") # Marca el nodo actual como visitado, lo imprime 
        
        if nodo in self.grafo: #Verifica si el nodo actual tiene vecinos en el grafo. Si el nodo actual no tiene vecinos, el bucle for no se ejecutará.
            for vecino in self.grafo[nodo]: #Itera sobre todos los vecinos del nodo actual que se encuentran en la lista de adyacencia del nodo en el grafo.
                if vecino not in visitado: #Verifica si el vecino actual no ha sido visitado previamente durante el recorrido DFS.
                    self.dfs_util(vecino, visitado) #Llama recursivamente al método dfs_util con el vecino actual y el conjunto visitado|

    def dfs(self, inicio): #define un método llamado dfs dentro de la clase Grafo. Este método toma dos parámetros: self, que es una referencia a la instancia de la clase Grafo, y inicio, que es el nodo desde el cual comenzará la búsqueda en profundidad (DFS).
        visitado = set() #Aquí se inicializa un conjunto vacío llamado visitado
        self.dfs_util(inicio, visitado) #Esto inicia la búsqueda en profundidad desde el nodo de inicio especificado. La función dfs_util se encargará de realizar el recorrido DFS completo a partir del nodo de inicio.

# Ejemplo de uso
grafo = Grafo() #Se crea una instancia de la clase Grafo, inicializando así un nuevo objeto que representará nuestro grafo.
grafo.agregar_arista(0, 1) #Se agregan varias aristas al grafo utilizando el método agregar_arista
grafo.agregar_arista(0, 2) #Estas líneas definen las conexiones entre diferentes nodos del grafo.
grafo.agregar_arista(1, 2) #. Por ejemplo, la línea grafo.agregar_arista(1, 2) agrega una arista que conecta el nodo 1 con el nodo 2.
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido DFS comenzando desde el vértice 2:") #Se imprime un mensaje indicando que se realizará un recorrido en profundidad (DFS) comenzando desde el vértice 2.
grafo.dfs(2) #Esto inicia el recorrido en profundidad desde el vértice 2 en el grafo creado anteriormente.

