from scipy import stats
p = 0.8
n = 15
X = stats.binom(n, p)
print("Probability that 10 flights arrive on time is", str(X.pmf(10)))
print("Probability that fewer than 10 flights arrive on time is", str(X.cdf(9)))
print("Probability that at least 10 flights arrive on time is", str(X.cdf(15) - X.cdf(10)))
print("Probability that between 8 and 10 flights arrive on time is", str(X.cdf(10) - X.cdf(7)))