import numpy as np
import matplotlib
from scipy import stats
import seaborn as sns
import pandas as pd
data = [18, 21, 22, 25, 26, 29, 30, 31, 33, 36, 37, 41, 42, 47, 52, 55, 57, 58, 62, 64, 67, 69, 71, 72, 73, 74, 76, 77]
#print(np.percentile(data, .7))
#print(np.percentile(data, .83))
data2 = [3, 4, 5, 7, 7, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 11, 12, 12, 13, 14, 14 ,15, 15, 17, 17, 18, 19, 19, 19, 21, 21, 22, 22, 23, 24, 24, 24, 24]
#print(np.mean(data2))
#print(np.median(data2))
array = np.array(data2)
mode = stats.mode(array)
#print(mode[0])
matplotlib.pyplot.boxplot(data2)
matplotlib.pyplot.hist(data2)
sns.kdeplot(data)
#print(np.std(data2))
data3 = pd.read_csv("heart.csv")
#print(data3)
df = pd.DataFrame(data3)
male = df[df.sex == 1]
#print(male)
female = df[df.sex == 0]
#print(female)
print(male.describe())
print(female.describe())
#print(matplotlib.pyplot.boxplot(male.chol))