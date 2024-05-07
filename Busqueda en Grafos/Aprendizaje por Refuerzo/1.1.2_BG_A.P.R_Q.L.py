""""Dafne Sarahi Villanueva Ceja    21310176
Busqueda en grafos---> Aprendizaje Por Refuerzo---> Q-Learning

Este código simula un agente que aprende a navegar un entorno de cuadrícula con 
obstáculos para alcanzar un estado objetivo utilizando el algoritmo Q-Learning. 
El agente actualiza su tabla Q en cada paso utilizando la ecuación de Bellman y elige acciones
de acuerdo con una política epsilon-greedy. Finalmente, se grafican las recompensas obtenidas por
episodio para observar el aprendizaje del agente a lo largo del tiempo"""


import numpy as np
import matplotlib.pyplot as plt

# Definir el entorno de cuadrícula
class GridEnvironment:
    def __init__(self):
        self.grid_size = (5, 5)  # Tamaño de la cuadrícula
        self.num_actions = 4  # Número de acciones posibles (arriba, abajo, izquierda, derecha)
        self.goal_state = (4, 4)  # Estado objetivo
        self.obstacle_states = [(1, 1), (2, 2)]  # Estados de obstáculos
        self.reset()

    def reset(self):
        self.agent_state = (0, 0)  # Estado inicial del agente

    def step(self, action):
        # Mover el agente según la acción elegida
        if action == 0:  # Arriba
            next_state = (self.agent_state[0] - 1, self.agent_state[1])
        elif action == 1:  # Abajo
            next_state = (self.agent_state[0] + 1, self.agent_state[1])
        elif action == 2:  # Izquierda
            next_state = (self.agent_state[0], self.agent_state[1] - 1)
        elif action == 3:  # Derecha
            next_state = (self.agent_state[0], self.agent_state[1] + 1)

        # Verificar si el próximo estado es válido
        if next_state[0] >= 0 and next_state[0] < self.grid_size[0] \
                and next_state[1] >= 0 and next_state[1] < self.grid_size[1] \
                and next_state not in self.obstacle_states:
            self.agent_state = next_state

        # Calcular la recompensa (1 si alcanzó el estado objetivo, 0 en otro caso)
        reward = 1 if self.agent_state == self.goal_state else 0

        # Determinar si se alcanzó el estado objetivo
        done = self.agent_state == self.goal_state

        return reward, done

# Algoritmo Q-Learning
class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.env = env
        self.q_table = np.zeros((env.grid_size[0], env.grid_size[1], env.num_actions))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def choose_action(self, state):
        # Epsilon-greedy para elegir la acción
        if np.random.rand() < self.exploration_rate:
            return np.random.randint(self.env.num_actions)
        else:
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        # Actualizar la tabla Q utilizando la ecuación de Bellman
        self.q_table[state][action] += self.learning_rate * (
                    reward + self.discount_factor * np.max(self.q_table[next_state]) - self.q_table[state][action])

# Entrenamiento del agente
def train_agent(env, agent, num_episodes):
    rewards_per_episode = []  # Almacenar las recompensas por episodio
    for episode in range(num_episodes):
        env.reset()  # Reiniciar el entorno para un nuevo episodio
        total_reward = 0
        done = False
        while not done:
            state = env.agent_state
            action = agent.choose_action(state)
            reward, done = env.step(action)
            next_state = env.agent_state
            agent.update_q_table(state, action, reward, next_state)
            total_reward += reward
        rewards_per_episode.append(total_reward)
    return rewards_per_episode

# Crear el entorno y el agente
env = GridEnvironment()
agent = QLearningAgent(env)

# Entrenar al agente y obtener las recompensas por episodio
num_episodes = 1000
rewards_per_episode = train_agent(env, agent, num_episodes)

# Graficar las recompensas por episodio
plt.plot(np.arange(num_episodes), rewards_per_episode)
plt.xlabel('Episodio')
plt.ylabel('Recompensa')
plt.title('Aprendizaje por Refuerzo con Q-Learning')
plt.show()
