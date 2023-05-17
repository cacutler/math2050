import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportion_confint
data = pd.read_csv("AAPL.csv")
df = pd.DataFrame(data)
print(df.columns)
print("Population Mean:", np.mean(df.Low))
Low = df["Low"]
smpl = Low.sample(80, random_state = 10)
print(smpl)
print(stats.t.interval(alpha = 0.95, df = len(smpl) - 1, loc = np.mean(Low), scale = stats.sem(Low)))
data1 = pd.read_csv("emails.csv")
df1 = pd.DataFrame(data1)
print(df1.columns)
print(np.sum(df1.spam), len(df1))
print("Population proportion of spams:", str(np.sum(df1.spam)/len(df1)))
spam = df1["spam"]
smpl = spam.sample(500)
x = np.sum(smpl)
n = 500
print(proportion_confint(x, n, alpha = 0.05))