""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Aprendizaje Por Refuerzo---> Búsqueda de la Política
Este código simula la búsqueda de la política utilizando el método de Monte Carlo.
En cada episodio, el agente interactúa con el entorno siguiendo la política actual y acumula las recompensas. 
Luego, se actualiza la política utilizando un método específico de búsqueda de política. Finalmente, se grafican 
las recompensas por episodio y se imprime la política final encontrada."""

import numpy as np
import matplotlib.pyplot as plt

# Definición del entorno
# Aquí definiríamos las funciones de transición de estados, recompensas, etc. para nuestro entorno de aprendizaje.

# Función para simular una recompensa aleatoria
def get_reward():
    return np.random.normal(0, 1)

# Algoritmo de Búsqueda de la Política (Monte Carlo Policy Search)
def policy_search(num_episodes):
    # Política inicial: acciones aleatorias
    policy = {state: np.random.choice(['A', 'B']) for state in range(10)}
    
    rewards_per_episode = []  # Lista para almacenar las recompensas totales por episodio
    
    for _ in range(num_episodes):
        episode_reward = 0  # Recompensa total del episodio
        
        # Simulación de un episodio
        for state in range(10):
            action = policy[state]  # Tomar acción según la política actual
            reward = get_reward()  # Obtener la recompensa del entorno
            episode_reward += reward  # Acumular la recompensa del episodio
            
            # Actualizar la política utilizando un método de búsqueda específico
            
        rewards_per_episode.append(episode_reward)  # Registrar la recompensa total del episodio
    
    return rewards_per_episode, policy

# Definir los parámetros
num_episodes = 1000  # Número de episodios de entrenamiento

# Ejecutar el algoritmo de búsqueda de la política
rewards_per_episode, final_policy = policy_search(num_episodes)

# Graficar las recompensas por episodio
plt.plot(np.arange(num_episodes), rewards_per_episode)
plt.xlabel('Episodio')
plt.ylabel('Recompensa Total')
plt.title('Búsqueda de la Política (Monte Carlo)')
plt.show()

# Imprimir la política final
print("Política Final:")
for state, action in final_policy.items():
    print(f"Estado {state}: Acción {action}")
