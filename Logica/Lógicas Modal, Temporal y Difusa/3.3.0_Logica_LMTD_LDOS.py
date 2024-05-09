"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Lógicas Modal, Temporal y Difusa ---> Lógicas de Orden Superior"""
import matplotlib.pyplot as plt

# Función de orden superior: mapeo
def map_function(func, iterable):
    """
    Aplica la función dada a cada elemento del iterable y devuelve una lista con los resultados.
    """
    return [func(x) for x in iterable]

# Función de orden superior: filtrado
def filter_function(func, iterable):
    """
    Filtra los elementos del iterable que cumplen con la condición dada por la función.
    """
    return [x for x in iterable if func(x)]

# Definir una lista de números
numbers = list(range(1, 11))

# Definir funciones simples para utilizar en las funciones de orden superior
square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0

# Aplicar mapeo y filtrado utilizando funciones de orden superior
squared_numbers = map_function(square, numbers)
even_numbers = filter_function(is_even, numbers)

# Visualizar los resultados utilizando Matplotlib
plt.figure(figsize=(10, 5))

# Graficar los números originales
plt.subplot(1, 2, 1)
plt.plot(numbers, 'b.-')
plt.title('Números Originales')
plt.xlabel('Índice')
plt.ylabel('Valor')

# Graficar los números al cuadrado
plt.subplot(1, 2, 2)
plt.plot(squared_numbers, 'r.-')
plt.title('Números al Cuadrado')
plt.xlabel('Índice')
plt.ylabel('Valor')

plt.tight_layout()
plt.show()

# Imprimir los números pares resultantes
print("Números pares:", even_numbers)
