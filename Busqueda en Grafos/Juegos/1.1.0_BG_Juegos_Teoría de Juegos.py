""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Juegos---> Teoría de Juegos
ejemplifica el concepto de teoría de juegos al modelar la interacción entre dos jugadores
(el jugador humano y la computadora) y determinar el resultado en función de las estrategias 
elegidas por ambos."""
import random

# Definir las opciones del juego
opciones = ['piedra', 'papel', 'tijera']

# Función para que el jugador humano elija una opción
def seleccionar_opcion():
    print("Elige una opción: ")
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    seleccion = int(input("Tu elección: ")) - 1
    return opciones[seleccion]

# Función para que la computadora elija una opción al azar
def opcion_computadora():
    return random.choice(opciones)

# Función para determinar el resultado del juego
def determinar_ganador(opcion_jugador, opcion_computadora):
    if opcion_jugador == opcion_computadora:
        return "Empate"
    elif (opcion_jugador == 'piedra' and opcion_computadora == 'tijera') or \
         (opcion_jugador == 'papel' and opcion_computadora == 'piedra') or \
         (opcion_jugador == 'tijera' and opcion_computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

# Función principal del juego
def jugar_piedra_papel_tijera():
    print("Bienvenido al juego de piedra, papel o tijera.")
    while True:
        opcion_jugador = seleccionar_opcion()
        opcion_compu = opcion_computadora()
        print(f"La computadora elige: {opcion_compu}")
        resultado = determinar_ganador(opcion_jugador, opcion_compu)
        print(resultado)
        continuar = input("¿Quieres jugar de nuevo? (s/n): ")
        if continuar.lower() != 's':
            break

# Iniciar el juego
if __name__ == "__main__":
    jugar_piedra_papel_tijera()
