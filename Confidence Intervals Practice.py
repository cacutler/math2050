import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest, test_proportions_2indep
import pandas as pd
data = [35.7, 37.2, 34.1, 38.9, 32.0, 41.3, 32.5, 37.1, 37.3, 38.8, 38.2, 39.6, 32.2, 40.9, 37.0, 36.0]
sample = []
data1 = pd.read_csv("ncbirths.csv")
df = pd.DataFrame(data1)
mage = df.mage
smoking = df[df.habit == "smoker"]
data2 = pd.read_csv("heart.csv")
df1 = pd.DataFrame(data2)
female = df1[df1.sex == 0]
male = df1[df1.sex == 1]
mchol = male.chol
fchol = female.chol
for i in range(1000):
    sample.append(np.mean(random.choices(data, k = 16)))
print("Sample mean is", str(np.mean(sample)))
print("Data mean is", str(np.mean(data)))
print(stats.t.interval(alpha = 0.95, df = len(sample) - 1, loc = np.mean(sample), scale = stats.sem(sample)))
print("Lower bound percentile", str(np.percentile(sample, 0.025)))
print("Upper bound percentile", str(np.percentile(sample, 0.975)))
plt.hist(sample)
smpl = stats.norm.rvs(66.5, 3, 25)
print(smpl)
print(stats.t.interval(alpha = 0.95, df = len(smpl) - 1, loc = np.mean(smpl), scale = stats.sem(smpl)))
tstat, pval = stats.ttest_1samp(a = mage, popmean = 25, alternative = "greater")
print(tstat, pval)
print(np.mean(mage))
print(data1.habit.value_counts())
stat, pvalue = proportions_ztest(126, 999, 0.1, alternative = "larger")
print(stat, pvalue)
t_stat, p_value = test_proportions_2indep(94, 207, 57, 96, alternative = "smaller")
print(t_stat, p_value)