from scipy import stats
n = 20
p = 29/192
X = stats.binom(n, p)
print("The mean/expected value of the binomal data is", str(X.mean()))
print("Probability that fewer than 10 pages will advertise footwear is", str(X.cdf(9)))
X2 = stats.geom(p)
print("Probability of finding one page advertising footwear within three pages is", str(X2.cdf(3)))
print("The mean/expected data of the geometric data is", str(X2.mean()))