from random import choices
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
a_list = [1, 2, 3, 4, 5, 6]
sample_die = choices(a_list, k = 2000)
print(sample_die)
plt.hist(sample_die)
df1 = pd.Series(sample_die).value_counts().sort_index().reset_index().reset_index(drop=True)
df1.colums = ["Element", "Frequency"]
print(f"the original list : {sample_die}")
print(f"The list frequencty of elements is :\n {df1.to_string(index=False)}")
print(plt.bar(df1.colums[0], df1.colums[1]))
df1["rel_freq"] = df1.colums[1]/sum(df1.colums[1])
df1["cum_rel_freq"] = np.cumsum(df1["rel_freq"])
print(df1)