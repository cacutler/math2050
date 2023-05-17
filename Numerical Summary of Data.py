import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode
from random import choices
data = pd.read_csv("3_r_3-3.csv")
df = pd.DataFrame(data)
age = df.Age
range1 = max(age) - min(age)
age_sample = choices(age, k=4)
age_sample2 = choices(age, k=4)
data2 = pd.read_csv("3_r_4-1.csv")
df2 = pd.DataFrame(data2)
tickets = df2.Tickets_Issued
data3 = pd.read_csv("3_r_10-1.csv")
df3 = pd.DataFrame(data3)
words = df3.Presidential_Inaugural_Addresses
array3 = np.array(words)
q1 = np.percentile(array3, 25)
q2 = np.percentile(array3, 50)
q3 = np.percentile(array3, 75)
iqr = q3 - q1
print("Chief Justice mean age",str(np.mean(age)))
print("Chief Justice median age",str(np.median(age)))
print("Chief Justice mode age",str(mode(age)))
print("Chief Justice age range",str(range1))
print("Standard deviation of Chief Justice age",str(np.std(age)))
print("Mean of random sample 1",str(np.mean(age_sample)))
print("Standard deviation of random sample 1",str(np.std(age_sample)))
print("Mean of random sample 2",str(np.mean(age_sample2)))
print("Standard deviation of random sample 2",str(np.std(age_sample2)))
plt.hist(data2)
print("Number of Tickets mean",str(np.mean(tickets)))
print("Number of Tickets median",str(np.median(tickets)))
print("Number of Tickets mode",str(mode(tickets)))
print("Number of words in addresses mean ",str(np.mean(words)))
print("Number of words in addresses median",str(np.median(words)))
print("Words Quartile 1",str(q1))
print("Words Quartile 2",str(q2))
print("Words Quartile 3",str(q3))
print("Minimum number of words",str(min(words)))
print("Maximum number of words",str(max(words)))
print("Standard deviation of words",str(np.std(words)))
print("Interquartile range of words",str(iqr))
plt.boxplot(words)