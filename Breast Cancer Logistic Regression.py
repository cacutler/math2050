import pandas as pd
from statsmodels.tools import add_constant
import statsmodels.api as sm
data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
df.dropna(axis = 1, inplace = True)
df = add_constant(df)
#df = pd.get_dummies(df, columns = ["diagnosis"], drop_first = True)
df["diagnosis"] = df["diagnosis"].map({"B":0, "M":1})
#df.isnull().sum()
df.dropna(axis = 1, inplace = True)
print(df)
x = df.drop(["id", "diagnosis"], axis = 1)
y = df.diagnosis
model = sm.Logit(y, x).fit()
print(model.summary())