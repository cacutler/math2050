import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3]
p = [.4, .2, .4]
cp = np.cumsum(p)
plt.plot(x, p, label = 'pmf')
plt.plot(x, cp, label = 'cdf')
plt.vlines(x, 0, p)
plt.legend()