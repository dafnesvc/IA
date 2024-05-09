"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Planificación ---> Planificación de Orden Parcial

Este código crea un grafo dirigido acíclico (DAG) que representa un problema de planificación
de orden parcial. Cada nodo del grafo representa una tarea, y los bordes representan las dependencias
entre tareas. Las tareas se definen en un diccionario donde las claves son los nombres de las tareas y
los valores son listas de las tareas de las que dependen."""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido acíclico (DAG) para representar el problema de planificación de orden parcial
G = nx.DiGraph()

# Definir las tareas y sus dependencias
tasks = {
    "Tarea 1": [],
    "Tarea 2": ["Tarea 1"],
    "Tarea 3": ["Tarea 1"],
    "Tarea 4": ["Tarea 2", "Tarea 3"],
    "Tarea 5": ["Tarea 2"],
    "Tarea 6": ["Tarea 3", "Tarea 5"]
}

# Agregar nodos al grafo para representar las tareas
for task in tasks:
    G.add_node(task)

# Agregar arcos al grafo para representar las dependencias entre tareas
for task, dependencies in tasks.items():
    for dependency in dependencies:
        G.add_edge(dependency, task)

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
plt.title("Planificación de Orden Parcial")
plt.show()
