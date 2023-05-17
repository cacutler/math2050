import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("FEV.DAT.xls", "FEV")
df = pd.DataFrame(data)
boys = df[df.Sex == 1]
girls = df[df.Sex == 0]
Sex = df.Sex
FEV = df.FEV
Ages = df.Age
Height = df.Hgt
Smoking = df.Smoke
boys_ages = boys.Age
girls_ages = girls.Age
boys_3_4 = df[df.Sex == 1][df.Age >= 3][df.Sex <= 4]
boys_5_9 = df[df.Sex == 1][df.Age >= 5][df.Sex <= 9]
boys_10_14 = df[df.Sex == 1][df.Age >= 10][df.Sex <= 14]
boys_15_19 = df[df.Sex == 1][df.Age >= 15][df.Sex <= 19]
girls_3_4 = df[df.Sex == 0][df.Age >= 3][df.Sex <= 4]
girls_5_9 = df[df.Sex == 0][df.Age >= 5][df.Sex <= 9]
girls_10_14 = df[df.Sex == 0][df.Age >= 10][df.Sex <= 14]
girls_15_19 = df[df.Sex == 0][df.Age >= 15][df.Sex <= 19]
boys_fev_to_ages = pd.DataFrame(data["Age"], data["FEV"])
print("Mean of FEV for boys 3-4", str(np.mean(boys_3_4.FEV)))
print("Mean of FEV for boys 5-9", str(np.mean(boys_5_9.FEV)))
print("Mean of FEV for boys 10-14", str(np.mean(boys_10_14.FEV)))
print("Mean of FEV for boys 15-19", str(np.mean(boys_15_19.FEV)))
print("Mean of FEV for girls 3-4", str(np.mean(girls_3_4.FEV)))
print("Mean of FEV for girls 5-9", str(np.mean(girls_5_9.FEV)))
print("Mean of FEV for girls 10-14", str(np.mean(girls_10_14.FEV)))
print("Mean of FEV for girls 15-19", str(np.mean(girls_15_19.FEV)))
average_FEV = [np.mean(boys_3_4.FEV), np.mean(boys_5_9.FEV), np.mean(boys_10_14.FEV), np.mean(boys_15_19.FEV), np.mean(girls_3_4.FEV), np.mean(girls_5_9.FEV), np.mean(girls_10_14.FEV), np.mean(girls_15_19.FEV)]
plt.title("FEV vs. Smoke")
plt.xlabel("Smoke")
plt.ylabel("FEV")
plt.scatter(df.Smoke, df.FEV)