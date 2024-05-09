"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Acciones, Situaciones y Eventos: Marcos"""
import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar los marcos
G = nx.DiGraph()

# Definimos los marcos y sus relaciones
marcos = {
    "Comida": ["Pizza", "Hamburguesa", "Ensalada"],
    "Bebida": ["Refresco", "Agua", "Café"],
    "Postre": ["Pastel", "Helado"]
}

# Añadimos nodos (marcos y elementos) al grafo
for marco, elementos in marcos.items():
    G.add_node(marco)
    G.add_nodes_from(elementos)
    for elemento in elementos:
        G.add_edge(marco, elemento)

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Calculamos la disposición de los nodos
nx.draw_networkx_nodes(G, pos, node_size=700)  # Dibujamos los nodos
nx.draw_networkx_labels(G, pos)  # Añadimos etiquetas a los nodos
nx.draw_networkx_edges(G, pos, arrows=True)  # Dibujamos los arcos con flechas

# Mostramos el grafo
plt.title("Marcos de Acciones, Situaciones y Eventos")
plt.axis("off")
plt.show()

