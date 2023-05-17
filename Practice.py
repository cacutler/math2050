import pandas as pd
import matplotlib.pyplot as plt
a_list = [2, 3, 4, 5, 5, 4]
#plt.pie(a_list)
data = {"Numbers":[12000, 32000], "Percentage":[40.1, 59.9]}
df = pd.DataFrame(data, index={"Full-time", "Part-time"})
print(df)
#print(plt.pie(df["Percentage"]))
print(plt.bar(df.index, df["Numbers"]))