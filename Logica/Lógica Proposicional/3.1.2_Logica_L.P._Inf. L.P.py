"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional---> Inferencia Lógica Proposicional
Este script implementa una base de conocimiento inicial con algunas reglas lógicas proposicionales
y luego realiza una inferencia lógica para verificar si una consulta específica es verdadera en base a 
esas reglas. Además, visualiza el grafo dirigido que representa las relaciones lógicas entre las proposiciones."""

import networkx as nx
import matplotlib.pyplot as plt

# Función para agregar una regla a la base de conocimiento
def add_rule(knowledge_base, rule):
    knowledge_base.append(rule)

# Función para realizar una inferencia lógica
def logical_inference(knowledge_base, query_str):
    for rule in knowledge_base:
        if query_str in rule:
            return True
    return False

# Base de conocimiento inicial
knowledge_base = [
    ("p", "=>", "q"),  # Regla: p implica q
    ("q", "=>", "r"),  # Regla: q implica r
    ("p", "=>", "s"),  # Regla: p implica s
    ("r", "=>", "t")   # Regla: r implica t
]

# Consulta de ejemplo
query_str = "t"  # Queremos verificar si t es verdadero

# Realizar inferencia lógica
result = logical_inference(knowledge_base, query_str)
if result:
    print(f"La consulta {query_str} es verdadera en la base de conocimiento.")
else:
    print(f"La consulta {query_str} es falsa en la base de conocimiento.")

# Crear un grafo dirigido vacío
G = nx.DiGraph()

# Agregar nodos y aristas según las reglas de la base de conocimiento
for rule in knowledge_base:
    G.add_node(rule[0])
    G.add_node(rule[2])
    G.add_edge(rule[0], rule[2])

# Visualización del grafo
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", font_size=12, font_weight="bold")
plt.title("Grafo de Inferencia Lógica Proposicional")
plt.show()
