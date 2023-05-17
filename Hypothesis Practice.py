from scipy import stats
import pandas as pd
data = pd.read_csv("heart.csv")
df = pd.DataFrame(data)
male = df[df.sex == 1]
female = df[df.sex == 0]
mchol = male.chol
fchol = female.chol
statistic, pvalue = stats.ttest_ind(mchol, fchol, alternative = "less")
print(statistic, pvalue)
stat, pval = stats.ttest_ind(mchol, fchol, alternative = "greater")
print(stat, pval)