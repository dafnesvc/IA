"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Tratamiento Probabilistico del lenguaje---> Gramaticas probabilisticas independientes del contexto"""

import nltk
import random
import matplotlib.pyplot as plt

# Definir la gramática probabilística
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [0.9] | VP [0.1]
    NP -> Det N [0.8] | NP PP [0.2]
    VP -> V NP [0.5] | VP PP [0.5]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'man' [0.5] | 'dog' [0.5]
    V -> 'saw' [0.5] | 'ate' [0.5]
    P -> 'with' [0.61] | 'in' [0.39]
""")

# Crear un parser para la gramática
parser = nltk.ViterbiParser(grammar)

# Generar varias oraciones aleatorias
generated_sentences = [sent for sent in parser.parse_random()][:100]

# Contar la longitud de cada oración generada
sentence_lengths = [len(sent.split()) for sent in generated_sentences]

# Crear un histograma de las longitudes de las oraciones generadas
plt.hist(sentence_lengths, bins=range(min(sentence_lengths), max(sentence_lengths) + 1, 1), edgecolor='black')
plt.xlabel('Longitud de la Oración')
plt.ylabel('Frecuencia')
plt.title('Distribución de Longitudes de Oraciones Generadas por la PCFG')
plt.grid(True)
plt.show()
