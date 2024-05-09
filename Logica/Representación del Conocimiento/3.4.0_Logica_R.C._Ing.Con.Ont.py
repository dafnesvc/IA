"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Ingeniería del Conocimiento: Ontologías"""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar la ontología
G = nx.DiGraph()

# Añadimos nodos (conceptos) al grafo
G.add_nodes_from(["Animal", "Mamífero", "Reptil", "Perro", "Gato", "Tortuga"])

# Añadimos arcos (relaciones) al grafo
G.add_edges_from([("Animal", "Mamífero"), 
                  ("Animal", "Reptil"), 
                  ("Mamífero", "Perro"), 
                  ("Mamífero", "Gato"), 
                  ("Reptil", "Tortuga")])

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Calculamos la disposición de los nodos
nx.draw_networkx_nodes(G, pos, node_size=700)  # Dibujamos los nodos
nx.draw_networkx_labels(G, pos)  # Añadimos etiquetas a los nodos
nx.draw_networkx_edges(G, pos, arrows=True)  # Dibujamos los arcos con flechas

# Mostramos el grafo
plt.title("Ontología de Animales")
plt.axis("off")
plt.show()
