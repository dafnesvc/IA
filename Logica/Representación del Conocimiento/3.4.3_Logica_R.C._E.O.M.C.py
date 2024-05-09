"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Eventos y Objetos Mentales: Creencias"""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar las creencias
G = nx.DiGraph()

# Definimos las creencias y sus relaciones
creencias = {
    "Juan": ["Cree en Dios", "Cree en la amistad", "Cree en la honestidad"],
    "María": ["Cree en la amistad", "Cree en la justicia"],
    "Pedro": ["Cree en Dios", "Cree en la honestidad"],
    "Dios": ["Es justo", "Es bondadoso"]
}

# Añadimos nodos (personas y creencias) al grafo
for persona, lista_creencias in creencias.items():
    G.add_node(persona)
    G.add_nodes_from(lista_creencias)
    for creencia in lista_creencias:
        G.add_edge(persona, creencia)

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Calculamos la disposición de los nodos
nx.draw_networkx_nodes(G, pos, node_size=700)  # Dibujamos los nodos
nx.draw_networkx_labels(G, pos)  # Añadimos etiquetas a los nodos
nx.draw_networkx_edges(G, pos, arrows=True)  # Dibujamos los arcos con flechas

# Mostramos el grafo
plt.title("Creencias de las personas")
plt.axis("off")
plt.show()
