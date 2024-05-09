"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación ---> Planificación Continua y Multiagente"""

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

# Definir las tareas y sub tareas para cada agente
agent1_tasks = {
    "Agente 1 - Planificación inicial": {
        "Tarea 1": None,
        "Tarea 2": {
            "Subtarea 1": None,
            "Subtarea 2": None
        },
        "Tarea 3": None
    },
    "Agente 1 - Planificación continua": {
        "Monitoreo": None,
        "Replanificación": None
    }
}

agent2_tasks = {
    "Agente 2 - Planificación inicial": {
        "Tarea A": None,
        "Tarea B": {
            "Subtarea X": None,
            "Subtarea Y": None
        },
        "Tarea C": None
    },
    "Agente 2 - Planificación continua": {
        "Monitoreo": None,
        "Replanificación": None
    }
}

# Crear un grafo dirigido para representar el plan de acciones de cada agente
G_agent1 = nx.DiGraph()
G_agent2 = nx.DiGraph()

# Agregar tareas al grafo para cada agente
add_tasks(G_agent1, agent1_tasks)
add_tasks(G_agent2, agent2_tasks)

# Dibujar el grafo de planificación para cada agente
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

pos1 = nx.spring_layout(G_agent1)
nx.draw(G_agent1, pos1, ax=axs[0], with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
axs[0].set_title("Agente 1")

pos2 = nx.spring_layout(G_agent2)
nx.draw(G_agent2, pos2, ax=axs[1], with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
axs[1].set_title("Agente 2")

plt.suptitle("Planificación Continua y Multiagente")
plt.show()

