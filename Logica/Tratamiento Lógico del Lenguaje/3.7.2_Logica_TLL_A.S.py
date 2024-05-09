"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Tratamiento Lógico del Lenguaje ---> Análisis Sintáctico"""
# Importar las bibliotecas necesarias
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Oración de ejemplo
sentence = "El análisis sintáctico es la identificación de la estructura gramatical de una oración."

# Tokenizar la oración
tokens = word_tokenize(sentence)

# Realizar el etiquetado gramatical (POS tagging)
pos_tags = pos_tag(tokens)

# Obtener la lista de etiquetas gramaticales
tag_list = [tag[1] for tag in pos_tags]

# Contar la frecuencia de cada etiqueta gramatical
tag_freq = {}
for tag in tag_list:
    if tag in tag_freq:
        tag_freq[tag] += 1
    else:
        tag_freq[tag] = 1

# Crear gráfico de barras para mostrar la frecuencia de etiquetas gramaticales
plt.figure(figsize=(10, 6))
plt.bar(tag_freq.keys(), tag_freq.values())
plt.xlabel('Etiquetas Gramaticales')
plt.ylabel('Frecuencia')
plt.title('Análisis Sintáctico: Frecuencia de Etiquetas Gramaticales')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
