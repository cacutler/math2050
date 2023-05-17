import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
data = pd.read_excel("FEV.DAT.xls", "FEV")
df = pd.DataFrame(data)
boys = df[df.Sex == 1]
girls = df[df.Sex == 0]
boys_3_4 = df[df.Sex == 1][df.Age >= 3][df.Age <= 4]
boys_5_9 = df[df.Sex == 1][df.Age >= 5][df.Age <= 9]
boys_10_14 = df[df.Sex == 1][df.Age >= 10][df.Age <= 14]
boys_15_19 = df[df.Sex == 1][df.Age >= 15][df.Age <= 19]
girls_3_4 = df[df.Sex == 0][df.Age >= 3][df.Age <= 4]
girls_5_9 = df[df.Sex == 0][df.Age >= 5][df.Age <= 9]
girls_10_14 = df[df.Sex == 0][df.Age >= 10][df.Age <= 14]
girls_15_19 = df[df.Sex == 0][df.Age >= 15][df.Age <= 19]
boys_10_14_smoking = boys_10_14[boys_10_14.Smoke == 1]
boys_10_14_nonsmoking = boys_10_14[boys_10_14.Smoke == 0]
boys_15_19_smoking = boys_15_19[boys_15_19.Smoke == 1]
boys_15_19_nonsmoking = boys_15_19[boys_15_19.Smoke == 0]
boys_3_4_smoking = boys_3_4[boys_3_4.Smoke == 1]
boys_3_4_nonsmoking = boys_3_4[boys_3_4.Smoke == 0]
boys_5_9_smoking = boys_5_9[boys_5_9.Smoke == 1]
boys_5_9_nonsmoking = boys_5_9[boys_5_9.Smoke == 0]
girls_10_14_smoking = girls_10_14[girls_10_14.Smoke == 1]
girls_10_14_nonsmoking = girls_10_14[girls_10_14.Smoke == 0]
girls_15_19_smoking = girls_15_19[girls_15_19.Smoke == 1]
girls_15_19_nonsmoking = girls_15_19[girls_15_19.Smoke == 0]
girls_3_4_smoking = girls_3_4[girls_3_4.Smoke == 1]
girls_3_4_nonsmoking = girls_3_4[girls_3_4.Smoke == 0]
girls_5_9_smoking = girls_5_9[girls_5_9.Smoke == 1]
girls_5_9_nonsmoking = girls_5_9[girls_5_9.Smoke == 0]
boys_10_14_height = boys_10_14.Hgt
boys_15_19_height = boys_15_19.Hgt
boys_3_4_height = boys_3_4.Hgt
boys_5_9_height = boys_5_9.Hgt
girls_10_14_height = girls_10_14.Hgt
girls_15_19_height = girls_15_19.Hgt
girls_3_4_height = girls_3_4.Hgt
girls_5_9_height = girls_5_9.Hgt
boys_10_14_fev = boys_10_14.FEV
boys_15_19_fev = boys_15_19.FEV
boys_3_4_fev = boys_3_4.FEV
boys_5_9_fev = boys_5_9.FEV
girls_10_14_fev = girls_10_14.FEV
girls_15_19_fev = girls_15_19.FEV
girls_3_4_fev = girls_3_4.FEV
girls_5_9_fev = girls_5_9.FEV
plt.title('FEV vs. Age')
plt.xlabel('Age')
plt.ylabel('FEV')
print(np.mean(girls_15_19.Smoke))
print(np.median(girls_15_19.Smoke))
print(stats.mode(girls_15_19.Smoke))
plt.hist(girls_15_19.Smoke)