"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Taxonomías: Categorías y Objetos"""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar la taxonomía
G = nx.DiGraph()

# Añadimos nodos (categorías y objetos) al grafo
G.add_nodes_from(["Animal", "Mamífero", "Reptil", "Perro", "Gato", "Tortuga", "Labrador", "Siames"])

# Añadimos arcos (relaciones) al grafo
G.add_edges_from([("Animal", "Mamífero"), 
                  ("Animal", "Reptil"), 
                  ("Mamífero", "Perro"), 
                  ("Mamífero", "Gato"), 
                  ("Reptil", "Tortuga"), 
                  ("Perro", "Labrador"), 
                  ("Gato", "Siames")])

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Calculamos la disposición de los nodos
nx.draw_networkx_nodes(G, pos, node_size=700)  # Dibujamos los nodos
nx.draw_networkx_labels(G, pos)  # Añadimos etiquetas a los nodos
nx.draw_networkx_edges(G, pos, arrows=True)  # Dibujamos los arcos con flechas

# Mostramos el grafo
plt.title("Taxonomía de Animales")
plt.axis("off")
plt.show()
