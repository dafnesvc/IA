"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Razonamiento por Defecto y No Monotónico
En este ejemplo, creamos un grafo dirigido donde cada nodo representa una proposición lógica y
cada arista representa una relación de implicación lógica o contradicción. Además, utilizamos el 
concepto de "razonamiento por defecto" para modelar situaciones donde ciertas proposiciones pueden 
ser válidas en circunstancias normales pero pueden ser contradichas por información adicional."""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar las relaciones semánticas
G = nx.DiGraph()

# Definimos las relaciones semánticas básicas
relaciones_semanticas = [
    ("A", "implica", "B"),
    ("B", "implica", "C"),
    ("C", "implica", "D"),
]

# Definimos las relaciones de excepción o razonamiento por defecto
razonamiento_defecto = [
    ("B", "contradice", "E"),
]

# Añadimos las relaciones semánticas al grafo
for rel in relaciones_semanticas:
    G.add_edge(rel[0], rel[2], label=rel[1])

# Añadimos las relaciones de razonamiento por defecto al grafo
for rel in razonamiento_defecto:
    G.add_edge(rel[0], rel[2], label=rel[1])

# Dibujamos el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostramos el grafo
plt.title("Razonamiento por Defecto y No Monotónico")
plt.axis("off")
plt.show()
