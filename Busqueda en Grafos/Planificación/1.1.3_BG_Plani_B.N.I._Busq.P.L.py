""" Dafne Villanueva 21310176.
Busqueda en Gráfos --> Planificación --> Búsqueda no informada --> Busqueda en Profundidad Limitada

Este código define una clase Grafo que representa un grafo no dirigido y proporciona métodos para 
realizar una búsqueda en profundidad limitada (DLFS). 
El objetivo de este código es realizar una búsqueda en profundidad limitada (DLFS) en un grafo dado. 
La búsqueda en profundidad limitada es similar a la búsqueda en profundidad estándar (DFS), pero con
una restricción en la profundidad de búsqueda. Esto significa que el algoritmo se detiene después de
 alcanzar una profundidad máxima especificada, sin importar si se ha encontrado el nodo objetivo.
"""

class Grafo: #Se define una clase llamada Grafo, que representa un grafo no dirigido. 
    def __init__(self): #Dentro de la clase Grafo, se define el método especial __init__, que es el constructor de la clase. 
        self.grafo = {} #El constructor __init__ toma un parámetro adicional llamado self, que es una referencia al propio objeto que se está creando. Esta referencia self se utiliza para acceder a los atributos y métodos del objeto dentro de la clase.

    def agregar_arista(self, u, v): #El método agregar_arista permite agregar una arista al grafo entre los nodos u y v.
        if u not in self.grafo: #Si el nodo u no está presente en el grafo
            self.grafo[u] = [] # se agrega como una clave al diccionario grafo con una lista vacía asociada. 
        self.grafo[u].append(v) #Luego, se agrega el nodo v a la lista de adyacencia del nodo u

    def dls_util(self, nodo, objetivo, visitado, profundidad_limite): #El método dls_util es una función auxiliar para realizar la búsqueda en profundidad limitada (DLFS) de manera recursiva. Toma cinco parámetros: nodo (el nodo actual), objetivo (el nodo que se está buscando), visitado (un conjunto de nodos visitados) y profundidad_limite (la profundidad máxima permitida durante la búsqueda).
        if profundidad_limite >= 0: # erifica si la profundidad_limite es mayor o igual a cero. Si la profundidad límite es menor que cero, no tiene sentido continuar con la búsqueda, por lo que se detiene y retorna False.
            print(nodo, end=" ") #Esta línea imprime el nodo actual. 

            if nodo == objetivo: #Esta condición verifica si el nodo actual es igual al objetivo que estamos buscando. 
                return True #Si es así, significa que hemos encontrado el nodo objetivo y retornamos True, indicando que el objetivo ha sido encontrado.

            visitado.add(nodo) #Esta línea agrega el nodo actual al conjunto de visitado, lo que indica que hemos visitado este nodo durante el recorrido en profundidad y evita que lo visitemos nuevamente.

            if nodo in self.grafo: #itera a través de los vecinos del nodo actual en el grafo. 
                for vecino in self.grafo[nodo]:
                    if vecino not in visitado:
                        if self.dls_util(vecino, objetivo, visitado, profundidad_limite - 1): #Si el vecino no ha sido visitado aún, llamamos recursivamente a dls_util con el vecino como nuevo nodo
                            return True #disminuyendo la profundidad límite en 1. Si se encuentra el objetivo en alguno de los vecinos, retornamos True.

        return False #Si no se encuentra el objetivo en los vecinos del nodo actual o si la profundidad límite se ha alcanzado, retornamos False.

    def dls(self, inicio, objetivo, profundidad_limite): #El método dls es el punto de entrada para la búsqueda en profundidad limitada. Toma tres parámetros: inicio (el nodo desde el cual se inicia la búsqueda), objetivo (el nodo que se está buscando) y profundidad_limite (la profundidad máxima permitida durante la búsqueda). 
        visitado = set() #Inicializa un conjunto de nodos visitados
        return self.dls_util(inicio, objetivo, visitado, profundidad_limite) #y luego llama a la función auxiliar dls_util con los parámetros especificados.

# Ejemplo de uso
grafo = Grafo() #Se crea un grafo de ejemplo utilizando la clase Grafo y se agregan varias aristas al grafo.
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

inicio = 2 #Se define el nodo de inicio (inicio).
objetivo = 3 #el nodo objetivo (objetivo) 
profundidad_limite = 2 # la profundidad límite (profundidad_limite).

print("Recorrido DFS limitado comenzando desde el vértice 2:") #El resultado de la búsqueda se imprime en la consola para indicar si el nodo objetivo se encontró dentro de la profundidad límite especificada. 
if grafo.dls(inicio, objetivo, profundidad_limite): #Se llama al método dls del objeto grafo con los parámetros especificados para realizar la búsqueda en profundidad limitada.
    print(f"\nEl nodo {objetivo} se encontró dentro de la profundidad límite.")  #Si se encuentra, se imprime un mensaje indicando que el nodo objetivo se encontró dentro de la profundidad límite;
else:
    print(f"\nEl nodo {objetivo} no se encontró dentro de la profundidad límite.") #de lo contrario, se imprime un mensaje indicando que el nodo objetivo no se encontró dentro de la profundidad límite.
