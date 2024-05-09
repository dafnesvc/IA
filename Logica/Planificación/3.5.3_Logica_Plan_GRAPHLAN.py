"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación ---> Grafos de Planificación: GRAPHPLAN"""

import networkx as nx
import matplotlib.pyplot as plt

# Definir una función para agregar niveles de acción al grafo de planificación
def add_action_levels(G, actions, level):
    # Agregar nodos para las acciones en el nivel actual
    for action in actions:
        G.add_node((level, action))
    
    # Agregar arcos para las acciones en el nivel actual y sus predecesores
    for action in actions:
        for pre_action in action_precursors[action]:
            G.add_edge((level-1, pre_action), (level, action))

# Definir las acciones y sus predecesores
action_precursors = {
    "Preparar tarta": [],
    "Hornear tarta": ["Preparar tarta"],
    "Decorar tarta": ["Hornear tarta"]
}

# Crear un grafo dirigido para representar el plan
G = nx.DiGraph()

# Agregar nodos y arcos para cada nivel de acción
add_action_levels(G, ["Preparar tarta"], 0)
add_action_levels(G, ["Hornear tarta"], 1)
add_action_levels(G, ["Decorar tarta"], 2)

# Dibujar el grafo de planificación
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
plt.title("Grafo de Planificación: GRAPHPLAN")
plt.show()
