"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación ---> Espacio de Estados

Este código crea un grafo dirigido que representa el espacio de estados de un problema
de planificación. Cada nodo representa un estado posible del mundo y cada arco representa
una acción que puede tomar el agente para pasar de un estado a otro. Los nodos "Inicio" y "Fin" 
representan el estado inicial y el estado objetivo respectivamente. """

import networkx as nx
import matplotlib.pyplot as plt

# Definición del grafo del problema de planificación (Espacio de Estados)
G = nx.DiGraph()

# Agregar nodos al grafo representando los estados del problema
G.add_nodes_from(["Inicio", "A", "B", "C", "Fin"])

# Agregar arcos que representan las acciones y transiciones entre estados
G.add_edge("Inicio", "A", action="Ir a A")
G.add_edge("A", "B", action="Ir a B")
G.add_edge("B", "C", action="Ir a C")
G.add_edge("C", "Fin", action="Ir a Fin")

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
edge_labels = {(n1, n2): G[n1][n2]['action'] for n1, n2 in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Espacio de Estados (Planificación)")
plt.show()
