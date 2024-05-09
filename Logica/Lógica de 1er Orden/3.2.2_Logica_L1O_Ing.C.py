"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Ingeniería del Conocimiento"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.DiGraph()

# Agregar nodos (conceptos) al grafo
G.add_nodes_from(["IA", "Logica", "Programacion", "Grafos", "Conocimiento"])

# Agregar relaciones (conexiones) entre los nodos
G.add_edge("IA", "Logica")
G.add_edge("IA", "Programacion")
G.add_edge("Logica", "Grafos")
G.add_edge("Programacion", "Grafos")
G.add_edge("Grafos", "Conocimiento")

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=12, font_weight="bold", arrowsize=20)

# Mostrar el grafo
plt.title("Grafo de Conocimiento")
plt.show()
