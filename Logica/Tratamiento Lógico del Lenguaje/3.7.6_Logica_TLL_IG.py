"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Tratamiento Lógico del Lenguaje ---> Inducción Gramatical"""

import matplotlib.pyplot as plt

# Definimos una función para generar una secuencia binaria aleatoria
def generar_secuencia_binaria(longitud):
    import random
    return [random.choice([0, 1]) for _ in range(longitud)]

# Definimos una función para contar la cantidad de unos en una secuencia
def contar_unos(secuencia):
    return sum(secuencia)

# Definimos una función para graficar los resultados
def graficar_resultados(secuencias, conteos):
    secuencias_str = [''.join(map(str, secuencia)) for secuencia in secuencias]  # Convertimos las secuencias a cadenas de texto
    plt.bar(secuencias_str, conteos)  # Utilizamos las secuencias como etiquetas en el gráfico
    plt.xlabel('Secuencia Binaria')
    plt.ylabel('Cantidad de Unos')
    plt.title('Cantidad de Unos en Secuencias Binarias Aleatorias')
    plt.show()

# Generamos algunas secuencias binarias aleatorias
secuencias_binarias = [generar_secuencia_binaria(5) for _ in range(5)]

# Calculamos la cantidad de unos en cada secuencia
cantidad_de_unos = [contar_unos(secuencia) for secuencia in secuencias_binarias]

# Mostramos los resultados gráficamente
graficar_resultados(secuencias_binarias, cantidad_de_unos)
