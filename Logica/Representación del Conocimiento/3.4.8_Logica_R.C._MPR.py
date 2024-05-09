"""Dafne Sarahi Villanueva Ceja 21310176
Lógica---> Representación del Conocimiento ---> Modelo Probabilista Racional"""
import matplotlib.pyplot as plt

# Definimos las enfermedades y sus probabilidades a priori
enfermedades = ['Resfriado', 'Gripe', 'Infección de garganta']
probabilidades_a_priori = [0.3, 0.5, 0.2]

# Definimos la evidencia y sus probabilidades condicionales
evidencia = {
    'Fiebre': {'Resfriado': 0.2, 'Gripe': 0.8, 'Infección de garganta': 0.3},
    'Tos': {'Resfriado': 0.7, 'Gripe': 0.9, 'Infección de garganta': 0.1}
}

# Calculamos las probabilidades a posteriori usando el teorema de Bayes
def calcular_probabilidades_posteriori(evidencia, probabilidades_a_priori):
    probabilidades_posteriori = []
    for enfermedad in enfermedades:
        probabilidad_total = probabilidades_a_priori[enfermedades.index(enfermedad)]
        for sintoma, probabilidad_condicional in evidencia.items():
            probabilidad_total *= probabilidad_condicional[enfermedad]
        probabilidades_posteriori.append(probabilidad_total)
    return probabilidades_posteriori

# Función para graficar las probabilidades a posteriori
def graficar_probabilidades(enfermedades, probabilidades):
    plt.figure(figsize=(10, 6))
    plt.bar(enfermedades, probabilidades, color='skyblue')
    plt.title('Probabilidades a posteriori de cada enfermedad')
    plt.xlabel('Enfermedades')
    plt.ylabel('Probabilidad')
    plt.ylim(0, 1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Calculamos las probabilidades a posteriori y las graficamos
probabilidades_posteriori = calcular_probabilidades_posteriori(evidencia, probabilidades_a_priori)
graficar_probabilidades(enfermedades, probabilidades_posteriori)
