import pandas as pd
from statsmodels.tools import add_constant
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
data = pd.read_csv("framingham.csv")
df = pd.DataFrame(data)
df.dropna(axis = 0, inplace = True)
df = add_constant(df)
x = df.drop(["TenYearCHD", "education", "currentSmoker", "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes", "diaBP", "BMI", "heartRate"], axis = 1)
y = df.TenYearCHD
model = sm.Logit(y, x).fit()
print(model.summary())
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)
model1 = sm.Logit(y_train, x_train).fit()
print(model1.summary())
predictions = model1.predict(x_test)
print(predictions)
logreg = LogisticRegression().fit(x_train, y_train)
y_pred = logreg.predict(x_test)
print(y_pred)
print(confusion_matrix(y_test, y_pred))