import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
data = pd.read_csv("tested.csv")
df = pd.DataFrame(data)
survived = df[df.Survived == 1]
survived_sex = survived.Sex
survived_sibsp = survived.SibSp
survived_pclass = survived.Pclass
survived_parch = survived.Parch
print(np.mean(survived_parch))
print(np.median(survived_parch))
print(stats.mode(survived_parch))
plt.hist(survived_parch)
age = df.Age
sibsp = df.SibSp
parch = df.Parch
fare = df.Fare
q1 = np.percentile(fare, 25)
q2 = np.percentile(fare, 50)
q3 = np.percentile(fare, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
new_fare = fare[(fare > lower_bound) & (fare < upper_bound)]
#plt.hist(new_fare)