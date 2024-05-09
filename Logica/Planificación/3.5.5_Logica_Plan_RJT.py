"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación ---> Redes Jerárquicas de Tareas"""

import networkx as nx
import matplotlib.pyplot as plt

# Definir una función para agregar tareas y sub-tareas al grafo de planificación
def add_tasks(G, tasks, parent=None):
    for task, subtasks in tasks.items():
        # Agregar la tarea actual al grafo
        G.add_node(task)
        
        # Agregar un arco desde el padre a la tarea actual
        if parent:
            G.add_edge(parent, task)
        
        # Si la tarea tiene sub-tareas, llamar recursivamente a la función para agregarlas
        if subtasks:
            add_tasks(G, subtasks, parent=task)

# Definir las tareas y sub-tareas
tasks = {
    "Planificar proyecto": {
        "Definir objetivos": {
            "Establecer alcance": None,
            "Identificar recursos": None
        },
        "Diseñar planificación": {
            "Establecer hitos": None,
            "Asignar responsabilidades": None
        }
    }
}

# Crear un grafo dirigido para representar la jerarquía de tareas
G = nx.DiGraph()

# Agregar tareas y sub-tareas al grafo
add_tasks(G, tasks)

# Dibujar el grafo de jerarquía de tareas
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
plt.title("Red Jerárquica de Tareas")
plt.show()
