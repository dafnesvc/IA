"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación --->Planificación Condicional"""

import networkx as nx
import matplotlib.pyplot as plt

# Función para agregar tareas condicionales al grafo de planificación
def add_conditional_tasks(G, tasks, parent=None):
    for task, conditions in tasks.items():
        # Agregar la tarea actual al grafo
        G.add_node(task)
        
        # Agregar un arco desde el padre a la tarea actual
        if parent:
            G.add_edge(parent, task)
        
        # Si la tarea tiene condiciones, agregar arcos condicionales
        if conditions:
            for condition in conditions:
                G.add_edge(condition, task, label=condition)

# Definir las tareas y condiciones
conditional_tasks = {
    "Realizar tarea A": ["Recursos disponibles"],
    "Realizar tarea B": ["Tarea A completada"],
    "Realizar tarea C": ["Tarea A completada", "Recursos asignados"]
}

# Crear un grafo dirigido para representar el plan de acciones
G = nx.DiGraph()

# Agregar tareas y condiciones al grafo
add_conditional_tasks(G, conditional_tasks)

# Dibujar el grafo de planificación condicional
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)

# Agregar etiquetas a los arcos condicionales
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Planificación Condicional")
plt.show()
