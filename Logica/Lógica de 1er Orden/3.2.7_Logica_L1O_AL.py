"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Agentes Lógicos"""

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def breadth_first_search(graph, start, goal):
    """
    Realiza una búsqueda en amplitud en un grafo desde el nodo de inicio hasta el nodo objetivo.
    Devuelve el camino más corto encontrado.
    """
    # Inicializar la cola de nodos a visitar
    queue = deque([(start, [start])])
    
    # Mientras la cola no esté vacía
    while queue:
        # Obtener el nodo actual y el camino hasta ese nodo
        current_node, path = queue.popleft()
        
        # Si el nodo actual es el nodo objetivo, devolver el camino
        if current_node == goal:
            return path
        
        # Agregar los vecinos del nodo actual a la cola
        for neighbor in graph[current_node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    
    # Si no se encontró un camino al nodo objetivo, devolver None
    return None

# Crear un grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Crear un grafo dirigido a partir del grafo no dirigido para visualización
directed_graph = nx.DiGraph(graph)

# Obtener el camino más corto utilizando BFS
start_node = 'A'
goal_node = 'F'
shortest_path = breadth_first_search(graph, start_node, goal_node)

# Imprimir el camino más corto encontrado
print(f"El camino más corto desde {start_node} hasta {goal_node} es: {shortest_path}")

# Dibujar el grafo y resaltar el camino más corto
pos = nx.spring_layout(directed_graph)
nx.draw(directed_graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
nx.draw_networkx_nodes(directed_graph, pos, nodelist=shortest_path, node_color='red', node_size=1000)
nx.draw_networkx_edges(directed_graph, pos, width=1.0, alpha=0.5)
plt.title('Grafo con el camino más corto resaltado')
plt.show()
