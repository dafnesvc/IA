"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)--->Aprendizaje Probabilístico --->Algoritmo EM"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Generar datos de ejemplo
np.random.seed(0)
# Definimos los parámetros de los clusters
mean1 = [2, 2]
cov1 = [[1, 0], [0, 1]]
mean2 = [5, 5]
cov2 = [[1, 0], [0, 1]]
# Generamos muestras para cada cluster
cluster1 = np.random.multivariate_normal(mean1, cov1, 100)
cluster2 = np.random.multivariate_normal(mean2, cov2, 100)
# Combinamos las muestras en un único conjunto de datos
X = np.vstack((cluster1, cluster2))

# Inicialización de parámetros
# Número de clusters
K = 2
# Número de datos
N = X.shape[0]
# Inicializamos las medias y las matrices de covarianza de forma aleatoria
means = np.random.rand(K, X.shape[1])
covariances = np.zeros((K, X.shape[1], X.shape[1]))
for k in range(K):
    covariances[k] = np.diag(np.random.rand(X.shape[1]))
# Inicializamos las probabilidades a priori de los clusters de forma uniforme
pi = np.ones(K) / K

# Función de densidad de probabilidad multivariable gaussiana
def gaussian_pdf(X, mean, cov):
    return multivariate_normal(mean=mean, cov=cov).pdf(X)

# Algoritmo EM
num_iterations = 20
for iteration in range(num_iterations):
    # Expectation step
    # Calcular las probabilidades posteriores de pertenencia a cada cluster
    responsibilities = np.zeros((N, K))
    for k in range(K):
        responsibilities[:, k] = pi[k] * gaussian_pdf(X, means[k], covariances[k])
    responsibilities /= responsibilities.sum(axis=1, keepdims=True)
    
    # Maximization step
    # Actualizar los parámetros
    Nk = responsibilities.sum(axis=0)
    for k in range(K):
        means[k] = (responsibilities[:, k, None] * X).sum(axis=0) / Nk[k]
        diff = X - means[k]
        covariances[k] = np.dot(responsibilities[:, k] * diff.T, diff) / Nk[k]
    pi = Nk / N

# Visualización de los resultados
plt.scatter(X[:, 0], X[:, 1], c=responsibilities.argmax(axis=1), cmap='viridis')
plt.scatter(means[:, 0], means[:, 1], c='red', marker='x', s=100)
plt.title('Clustering con Algoritmo EM')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()
