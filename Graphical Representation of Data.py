import pandas as pd
import matplotlib.pyplot as plt
f0 = [1, 1, 5, 1, 1, 6, 4, 10, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 30 , 1, 9]
f1 = [16, 13, 9, 8, 13, 10, 15, 1, 17, 23, 10, 8, 12, 5, 20, 31, 12, 5, 30, 13, 7, 1, 5, 13, 1, 2, 5, 10, 1, 20, 5]
f2 = [7, 15, 2, 10, 23, 10, 7, 12, 8, 1, 8, 19, 5, 10, 15, 20, 10, 13, 20, 15, 13, 14, 1, 4, 2, 15, 30, 91, 11, 5]
f3 = [9, 20, 8, 16, 26, 36, 10, 20, 50, 17, 26, 31, 21, 30, 23, 28, 23, 35, 35, 15, 25, 30, 15, 22, 18, 58, 19, 23, 31, 13, 26, 40, 14, 11]
f4 = [120, 23, 23, 42, 47, 25, 22, 22, 34, 50, 38, 28, 39, 29, 28, 25, 34, 16, 40, 55, 124, 30, 30, 31]
f5 = [37, 69, 23, 52, 61, 122]
all_tornadoes = []
all_tornadoes.append(f0)
all_tornadoes.append(f1)
all_tornadoes.append(f2)
all_tornadoes.append(f3)
all_tornadoes.append(f4)
all_tornadoes.append(f5)
data = {"Number of Tornadoes":[22, 31, 30, 34, 24, 6]}
data1 = {"Deaths by Tornado Size":[0, 0, 14, 32, 129, 130]}
data2 = {"Deaths by Community Size":[99, 77, 63, 56, 10]}
plt.hist(f0)
plt.hist(f1)
plt.hist(f2)
plt.hist(f3)
plt.hist(f4)
plt.hist(f5)
plt.hist(all_tornadoes)
df = pd.DataFrame(data, index={0, 1, 2, 3, 4, 5})
df1 = pd.DataFrame(data1, index={0, 1, 2, 3, 4, 5})
df2 = pd.DataFrame(data2, index={1, 2, 3, 4, 5})
plt.bar(df1.index, df1["Deaths by Tornado Size"])
plt.bar(df2.index, df2["Deaths by Community Size"])
plt.bar(df.index, df["Number of Tornadoes"])
print(df)
print(df1)
print(df2)