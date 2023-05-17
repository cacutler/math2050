from scipy import stats
p = 0.85
n = 22
X = stats.binom(n, p)
print("Mean of the data is", str(X.mean()))
print("Probability that all 22 students attended graduation is", str(X.pmf(22)))