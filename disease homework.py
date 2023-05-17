from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
n = 30
n2 = 10
p = 0.173
X = stats.geom(p)
print("The probability for testing 30 people to find on with the disease is", str(X.pmf(n)))
print("The probability for asking 10 people to find one with the disease is", str(X.pmf(n2)))
print("The mean of the data is", str(X.mean()))
print("The standard deviation of the data is", str(X.std()))
sample = np.random.geometric(p, 10000)
bin = np.arange(0, 20, 1)
plt.hist(sample, bins=bin)