"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación ---> Vigilancia de Ejecución y Replanificación"""

import networkx as nx
import matplotlib.pyplot as plt

# Función para agregar tareas al grafo de planificación
def add_tasks(G, tasks, parent=None):
    for task in tasks:
        # Agregar la tarea actual al grafo
        G.add_node(task)
        
        # Agregar un arco desde el padre a la tarea actual
        if parent:
            G.add_edge(parent, task)
        
        # Si la tarea tiene subtareas, llamar recursivamente a la función add_tasks
        if isinstance(tasks[task], dict):
            add_tasks(G, tasks[task], parent=task)

# Definir las tareas y sub tareas
tasks = {
    "Planificación inicial": {
        "Tarea 1": None,
        "Tarea 2": {
            "Subtarea 1": None,
            "Subtarea 2": None
        },
        "Tarea 3": None
    },
    "Vigilancia de ejecución y replanificación": {
        "Monitoreo": None,
        "Replanificación": None
    }
}

# Crear un grafo dirigido para representar el plan de acciones
G = nx.DiGraph()

# Agregar tareas al grafo
add_tasks(G, tasks)

# Dibujar el grafo de planificación
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)

plt.title("Vigilancia de Ejecución y Replanificación")
plt.show()

