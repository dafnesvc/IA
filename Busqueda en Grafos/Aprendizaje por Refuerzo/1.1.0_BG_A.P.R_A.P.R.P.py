""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Aprendizaje Por Refuerzo---> Aprendizaje por Refuerzo Pasivo
En este código, creamos un entorno de aprendizaje simple con 10 estados y 2 acciones.
Luego, implementamos un agente que realiza Aprendizaje por Refuerzo Pasivo para estimar
los valores de las acciones en cada estado. El agente realiza múltiples episodios de aprendizaje
y registra las recompensas obtenidas en cada episodio. Finalmente, graficamos las recompensas por 
episodio para observar cómo el agente mejora su desempeño a lo largo del tiempo."""

import numpy as np
import matplotlib.pyplot as plt

# Definir el entorno de aprendizaje
class Environment:
    def __init__(self):
        self.num_states = 10  # Número de estados
        self.num_actions = 2  # Número de acciones
        self.true_action_values = np.random.normal(0, 1, self.num_states)  # Valores verdaderos de las acciones
        self.reset()

    def reset(self):
        self.state = np.random.choice(self.num_states)  # Estado inicial

    def step(self, action):
        reward = np.random.normal(self.true_action_values[self.state], 1)  # Recompensa
        self.state = np.random.choice(self.num_states)  # Nuevo estado después de tomar una acción
        return reward

# Algoritmo de Aprendizaje por Refuerzo Pasivo
class PassiveReinforcementLearning:
    def __init__(self, env):
        self.env = env
        self.action_values = np.zeros(env.num_states)  # Valores estimados de las acciones

    def learn(self, num_episodes):
        rewards = np.zeros(num_episodes)  # Almacenar las recompensas de cada episodio
        for episode in range(num_episodes):
            self.env.reset()  # Reiniciar el entorno para un nuevo episodio
            total_reward = 0
            for _ in range(100):  # Duración máxima del episodio
                action = np.argmax(self.action_values[self.env.state])  # Elegir la acción con el mayor valor
                reward = self.env.step(action)  # Tomar la acción y obtener la recompensa
                total_reward += reward
                self.action_values[self.env.state] += 0.1 * (reward - self.action_values[self.env.state])  # Actualizar el valor de la acción
            rewards[episode] = total_reward
        return rewards

# Crear el entorno y el agente de aprendizaje
env = Environment()
agent = PassiveReinforcementLearning(env)

# Entrenar al agente y obtener las recompensas por episodio
num_episodes = 1000
rewards = agent.learn(num_episodes)

# Graficar las recompensas por episodio
plt.plot(np.arange(num_episodes), rewards)
plt.xlabel('Episodio')
plt.ylabel('Recompensa')
plt.title('Aprendizaje por Refuerzo Pasivo')
plt.show()
