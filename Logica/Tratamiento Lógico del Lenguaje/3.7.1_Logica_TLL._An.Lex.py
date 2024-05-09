"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Tratamiento Lógico del Lenguaje ---> Análisis Léxico"""
# Importar las bibliotecas necesarias
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Oración de ejemplo
sentence = "El análisis léxico es el proceso de convertir una secuencia de caracteres en una secuencia de tokens o palabras."

# Tokenizar la oración
tokens = word_tokenize(sentence)

# Contar la frecuencia de cada token
token_freq = {}
for token in tokens:
    if token in token_freq:
        token_freq[token] += 1
    else:
        token_freq[token] = 1

# Crear gráfico de barras para mostrar la frecuencia de tokens
plt.figure(figsize=(10, 6))
plt.bar(token_freq.keys(), token_freq.values())
plt.xlabel('Tokens')
plt.ylabel('Frecuencia')
plt.title('Análisis Léxico: Frecuencia de Tokens')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
