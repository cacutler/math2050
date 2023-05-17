import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import random
import matplotlib.pyplot as plt
data = pd.read_csv("ais.csv")
print(data)
x = data.ferr
print(sns.distplot(x))
random.seed(10)
y = stats.geom.rvs(0.3, size = 100)
mu = []
for i in range(1000):
    sam = random.choices(y, k = 40)
    mu.append(np.mean(sam))
print(mu)
print(y)
print(np.mean(y))
print(np.std(y, ddof = 0))
print(plt.hist(mu))
print(np.mean(mu))