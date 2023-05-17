import pandas as pd
from scipy import stats
import numpy as np
data = pd.read_csv("soccer_results.csv")
df = pd.DataFrame(data)
print(df)
df["Total"] = df["home_score"] + df["away_score"]
print(df)
avg = np.sum(df.Total/len(df.Total))
val, cnt = np.unique(df.Total, return_counts = True)
print(val, cnt)
X = stats.poisson(avg)
print(X.pmf(val))
print(np.sum(cnt))
exp = X.pmf(val) * 41640
print(exp, cnt)