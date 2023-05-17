import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn import metrics
data = pd.read_csv("advertising.csv")
print(data)
df = pd.DataFrame(data)
x = df.TV
y = df.Sales
x1 = sm.add_constant(x)
model = sm.OLS(y, x1).fit()
print("TV Model Summary")
print(model.summary())
prediction = model.predict(x1)
pred = {"prediction":prediction, "actual":y}
df1 = pd.DataFrame(pred)
print("TV Predictions and Actual")
print(df1)
df1["error"] = y - prediction
print("TV Predictions, Actual, and Errors")
print(df1)
print(plt.boxplot(df1.error))
print(plt.scatter(df.TV, df1.error))
x2 = df.Newspaper
x3 = sm.add_constant(x2)
model1 = sm.OLS(y, x3).fit()
print("Newspaper Model Summary")
print(model1.summary())
prediction1 = model1.predict(x3)
pred1 = {"prediction":prediction1, "actual":y}
df2 = pd.DataFrame(pred1)
print("Newspaper Predictions and Actual")
print(df2)
df2["error"] = y - prediction1
print("Newspaper Predictions, Actual, and Errors")
print(df2)
print(plt.boxplot(df2.error))
x4 = df.Radio
x5 = sm.add_constant(x4)
model2 = sm.OLS(y, x5).fit()
print("Radio Model Summary")
print(model2.summary())
x6 = df[["TV", "Newspaper", "Radio"]]
x7 = sm.add_constant(x6)
x8 = df.drop("Sales", axis = 1)
x9 = sm.add_constant(x8)
print(x7)
r = df.corr(method = "pearson")
print(r)
x_train, x_test, y_train, y_test = train_test_split(x9, y, test_size = 0.3, random_state = 100)
model3 = sm.OLS(y_train, x_train).fit()
print(model3.summary())
predictions = model3.predict(x_test)
dataframe = {"Prediction":predictions, "y":y_test}
df3 = pd.DataFrame(dataframe)
print(df3)
df3["error"] = y_test - predictions
print(df3)
meanAbErr = metrics.mean_absolute_error(y_test, predictions)
print(meanAbErr)
meanSqErr = metrics.mean_squared_error(y_test, predictions)
print(meanSqErr)
rtMeanSqErr = np.sqrt(metrics.mean_absolute_error(y_test, predictions))
print(rtMeanSqErr)