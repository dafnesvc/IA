"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Encadenamiento: Hacia Delante y Atrás"""
import networkx as nx
import matplotlib.pyplot as plt

def forward_chaining(knowledge_base, goal):
    # Implementación del encadenamiento hacia adelante
    pass

def backward_chaining(knowledge_base, goal):
    # Implementación del encadenamiento hacia atrás
    pass

# Base de conocimiento y objetivo
knowledge_base = [
    ({"tengo_fiebre"}, "enfermo"),
    ({"tengo_gripe"}, "enfermo"),
    ({"tengo_tos_seca"}, "enfermo"),
    ({"enfermo"}, "necesito_medicinas"),
    ({"necesito_medicinas"}, "visitar_medico")
]
goal = "visitar_medico"

# Realizar encadenamiento hacia adelante y hacia atrás
forward_result = forward_chaining(knowledge_base, goal)
backward_result = backward_chaining(knowledge_base, goal)
print("Encadenamiento hacia adelante:", forward_result)
print("Encadenamiento hacia atrás:", backward_result)

# Crear el grafo dirigido
G = nx.DiGraph()
# Convertir los conjuntos a tuplas antes de agregarlos al grafo
for rule in knowledge_base:
    G.add_edge(tuple(rule[0]), rule[1])

# Dibujar el grafo
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=12, font_weight="bold", arrowsize=20)
plt.title("Base de Conocimiento")
plt.show()
