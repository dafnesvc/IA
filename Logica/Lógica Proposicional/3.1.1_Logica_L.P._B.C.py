"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica Proposicional---> Base de Conocimiento"""

import networkx as nx
import matplotlib.pyplot as plt

# Función para agregar una regla a la base de conocimiento
def add_rule(knowledge_base, rule):
    knowledge_base.append(rule)

# Función para realizar una consulta en la base de conocimiento
def query(knowledge_base, query_str):
    for rule in knowledge_base:
        if query_str in rule:
            return True
    return False

# Base de conocimiento inicial
knowledge_base = [
    ("mamifero", "vive"),
    ("vive", "tierra"),
    ("perro", "es", "mamifero"),
    ("gato", "es", "mamifero"),
    ("delfin", "es", "mamifero"),
    ("tiburon", "no es", "mamifero"),
    ("ballena", "es", "mamifero"),
    ("ballena", "vive", "agua"),
    ("gato", "es", "felino"),
    ("perro", "es", "canino")
]

# Consulta de ejemplo
query_str = ("perro", "vive", "tierra")

# Verificar si la consulta está en la base de conocimiento
result = query(knowledge_base, query_str)
if result:
    print(f"La consulta {query_str} es verdadera en la base de conocimiento.")
else:
    print(f"La consulta {query_str} es falsa en la base de conocimiento.")

# Crear un grafo dirigido vacío
G = nx.DiGraph()

# Agregar nodos y aristas según las reglas de la base de conocimiento
for rule in knowledge_base:
    G.add_node(rule[0])
    G.add_node(rule[1])
    if len(rule) == 3:
        G.add_node(rule[2])
        G.add_edge(rule[0], rule[2])
    G.add_edge(rule[1], rule[0])

# Visualización del grafo
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("Base de Conocimiento")
plt.show()
