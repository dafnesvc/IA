"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Tratamiento Probabilistico del lenguaje---> Modelo probabilistico del lenguaje: Corpus"""
import matplotlib.pyplot as plt
from collections import Counter

# Definir una función para cargar el corpus de texto
def load_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        corpus = file.read()
    return corpus

# Definir una función para preprocesar el texto y obtener una lista de palabras
def preprocess_text(corpus):
    # Convertir el texto a minúsculas
    corpus = corpus.lower()
    # Dividir el texto en palabras
    words = corpus.split()
    return words

# Definir una función para calcular la frecuencia de las palabras en el corpus
def calculate_word_frequency(words):
    word_freq = Counter(words)
    return word_freq

# Definir una función para visualizar las palabras más frecuentes
def visualize_word_frequency(word_freq, num_words=10):
    # Obtener las palabras más frecuentes y sus frecuencias
    top_words = [word[0] for word in word_freq.most_common(num_words)]
    top_freqs = [word[1] for word in word_freq.most_common(num_words)]

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(range(num_words), top_freqs, tick_label=top_words, color='skyblue')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.title('Palabras más frecuentes en el corpus')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Ruta al archivo del corpus de texto
file_path = 'corpus.txt'

# Cargar el corpus de texto
corpus = load_corpus(file_path)

# Preprocesar el texto y obtener una lista de palabras
words = preprocess_text(corpus)

# Calcular la frecuencia de las palabras en el corpus
word_freq = calculate_word_frequency(words)

# Visualizar las palabras más frecuentes en el corpus
visualize_word_frequency(word_freq)
