"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Tratamiento Lógico del Lenguaje ---> Análisis Semántico"""

import matplotlib.pyplot as plt

# Definimos una lista de palabras y sus categorías semánticas
palabras = {
    "manzana": "sustantivo",
    "come": "verbo",
    "roja": "adjetivo"
}

# Función para visualizar las categorías semánticas de las palabras
def visualizar_categorias_semanticas(palabras):
    # Contamos la cantidad de palabras en cada categoría semántica
    categorias = {}
    for categoria in palabras.values():
        categorias[categoria] = categorias.get(categoria, 0) + 1
    
    # Creamos un gráfico de barras para mostrar las categorías semánticas
    plt.bar(categorias.keys(), categorias.values(), color='skyblue')
    plt.xlabel('Categoría Semántica')
    plt.ylabel('Cantidad de Palabras')
    plt.title('Análisis Semántico de Palabras')
    plt.show()

# Mostramos las categorías semánticas gráficamente
visualizar_categorias_semanticas(palabras)
