"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Reglas, Redes Semánticas y Lógica Descriptiva
Este código crea un grafo dirigido donde cada nodo representa un concepto y cada arista representa una 
relación semántica entre dos conceptos"""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar las relaciones semánticas
G = nx.DiGraph()

# Definimos las relaciones semánticas entre conceptos
relaciones_semanticas = [
    ("Animal", "Tiene", "Patas"),
    ("Animal", "Tiene", "Cola"),
    ("Perro", "Es", "Animal"),
    ("Perro", "Tiene", "Pelo"),
    ("Gato", "Es", "Animal"),
    ("Gato", "Tiene", "Bigotes"),
    ("Pato", "Es", "Animal"),
    ("Pato", "Tiene", "Pico"),
]

# Añadimos las relaciones semánticas al grafo
for rel in relaciones_semanticas:
    G.add_edge(rel[0], rel[2], label=rel[1])

# Dibujamos el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostramos el grafo
plt.title("Red Semántica de Relaciones")
plt.axis("off")
plt.show()
