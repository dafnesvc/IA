"""Dafne Sarahi Villanueva Ceja 21310176
Lógica--->- Lógica 1er Orden ---> Sintaxis y Semántica: Cuantificadores"""

import matplotlib.pyplot as plt
import numpy as np

# Definición del dominio
dominio = np.linspace(-5, 5, 100)

# Definición de la función f(x) = x^2
funcion = lambda x: x ** 2

# Definición de los cuantificadores
cuantificador_existencial = lambda f, x: np.any(f(x))
cuantificador_universal = lambda f, x: np.all(f(x))

# Verificar si existe algún número en el dominio tal que la función sea mayor que 10
existe_mayor_que_10 = cuantificador_existencial(funcion, dominio)

# Verificar si todos los números en el dominio cumplen que la función es menor que 20
todos_menores_que_20 = cuantificador_universal(funcion, dominio)

# Visualizar la función y los resultados de los cuantificadores
plt.plot(dominio, funcion(dominio), label='f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Sintaxis y Semántica: Cuantificadores')
plt.grid(True)

if existe_mayor_que_10:
    plt.axhline(y=10, color='r', linestyle='--', label='y = 10 (Existencial)')
    plt.text(4, 12, 'Existe algún y > 10', fontsize=10, color='r')
else:
    plt.text(4, 12, 'No existe ningún y > 10', fontsize=10, color='r')

if todos_menores_que_20:
    plt.axhline(y=20, color='g', linestyle='--', label='y = 20 (Universal)')
    plt.text(4, 25, 'Todos los y < 20', fontsize=10, color='g')
else:
    plt.text(4, 25, 'No todos los y < 20', fontsize=10, color='g')

plt.legend()
plt.show()
