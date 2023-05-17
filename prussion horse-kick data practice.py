import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
data = pd.read_csv("Prussion Horse-Kick Data.csv")
#print(data)
list = [data.C1, data.C2, data.C3, data.C4, data.C5, data.C6, data.C7, data.C8, data.C9, data.C10, data.C11, data.C14, data.C15]
#print(list)
val, cnt = np.unique(list, return_counts = True)
#print(val, cnt)
print(np.sum(cnt))
X = stats.poisson(0.6923076923076923)
print(X.pmf(val))
exp = X.pmf(val) * 260
print(exp, cnt)
plt.scatter(val, cnt, color = 'red')
plt.scatter(val, exp, color = 'blue')
plt.show()