from scipy import stats
p = 0.6
n = 100
X = stats.binom(n, p)
print("Mean of the data is", str(X.mean()))
print("Standard deviation of the data is", str(X.std()))