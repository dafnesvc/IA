"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Tratamiento Lógico del Lenguaje ---> Ambigüedad"""
import matplotlib.pyplot as plt

# Definimos una frase ambigua
frase_ambigua = "Vi a la mujer con el telescopio."

# Definimos las posibles interpretaciones de la frase ambigua
interpretaciones = [
    "Vi a la mujer usando el telescopio.",
    "Vi a la mujer a través del telescopio."
]

# Función para graficar las interpretaciones
def graficar_interpretaciones(interpretaciones):
    plt.figure(figsize=(8, 4))
    plt.barh(range(len(interpretaciones)), [1] * len(interpretaciones), color='skyblue')
    plt.yticks(range(len(interpretaciones)), interpretaciones)
    plt.xlabel('Probabilidad')
    plt.title('Interpretaciones de la Frase Ambigua')
    plt.show()

# Mostramos las interpretaciones gráficamente
graficar_interpretaciones(interpretaciones)
