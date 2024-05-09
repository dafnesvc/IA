"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación ---> Algoritmos de Planificación: STRIPS y ADL"""
import networkx as nx
import matplotlib.pyplot as plt

# Definición del grafo del problema de planificación
G = nx.DiGraph()

# Agregar nodos al grafo
G.add_nodes_from(["Inicio", "Fin", "A", "B", "C", "D", "E"])

# Agregar arcos con acciones y precondiciones
G.add_edge("Inicio", "A", action="Ir a A", preconditions={"Inicio"})
G.add_edge("A", "B", action="Ir a B", preconditions={"A"})
G.add_edge("B", "C", action="Ir a C", preconditions={"B"})
G.add_edge("C", "Fin", action="Ir a Fin", preconditions={"C"})
G.add_edge("Inicio", "D", action="Ir a D", preconditions={"Inicio"})
G.add_edge("D", "E", action="Ir a E", preconditions={"D"})
G.add_edge("E", "Fin", action="Ir a Fin", preconditions={"E"})

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
edge_labels = {(n1, n2): G[n1][n2]['action'] for n1, n2 in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Grafo de planificación (Algoritmo STRIPS)")
plt.show()
