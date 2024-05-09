"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Incertidumbre y Factores de Certeza"""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar las relaciones de incertidumbre y certeza
G = nx.DiGraph()

# Definimos las relaciones de incertidumbre
relaciones_incertidumbre = [
    ("A", "posiblemente_implica", "B"),
    ("B", "probablemente_implica", "C"),
]

# Definimos las relaciones de certeza
relaciones_certidumbre = [
    ("C", "definitivamente_implica", "D"),
]

# Añadimos las relaciones de incertidumbre al grafo
for rel in relaciones_incertidumbre:
    G.add_edge(rel[0], rel[2], label=rel[1], color="orange")

# Añadimos las relaciones de certeza al grafo
for rel in relaciones_certidumbre:
    G.add_edge(rel[0], rel[2], label=rel[1], color="green")

# Dibujamos el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
nx.draw_networkx_labels(G, pos)
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=colors, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostramos el grafo
plt.title("Incertidumbre y Factores de Certeza")
plt.axis("off")
plt.show()
