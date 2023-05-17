import numpy as np
import matplotlib.pyplot as plt
import igraph as ig
import random
from scipy import stats
p = 0.5
n = 10
x = np.random.binomial(n, p, size = 5000)
plt.hist(x, bins = 'auto')
random.seed(0)
g1 = ig.Graph.Erdos_Renyi(n = 15, p = 0.1, directed = True, loops = False)
ig.summary(g1)
fig, axs = plt.subplots(2, 2)
ig.plot(g1, target = axs[0, 0], layout = "circle")
print(np.math.factorial(15)/(np.math.factorial(4) * np.math.factorial(11)))
x2 = np.random.binomial(n, p, size = 5000)
plt.hist(x2, bins = 'auto')
x3 = stats.binom(20, 0.35)
print(x3.pmf(12))
print(1-x3.cdf(10))
print(x3.mean())
y = stats.geom(0.7)
print(y.pmf(3))