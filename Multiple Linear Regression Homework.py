import pandas as pd
import statsmodels.api as sm
data = pd.read_csv("advertising.csv")
data1 = pd.read_csv("kc_house_data.csv")
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
z = df.Radio
x = sm.add_constant(z)
y = df.Sales
model = sm.OLS(y, x).fit()
print("Sales Model Summary based on Radio sales.")
print(model.summary())
z1 = df1.drop(["id", "date", "price", "waterfront", "yr_built", "yr_renovated", "zipcode", "lat", "long"], axis = 1)
x1 = sm.add_constant(z1)
y1 = df1.price
model1 = sm.OLS(y1, x1).fit()
print("House Price Model Summary based on bedrooms, bathrooms, sqft_living, sqft_lot, floors, view, condition, grade, sqft_above, sqft_basement, sqft_living15, and sqft_lot15 variables.")
print(model1.summary())
z2 = df1.drop(["id", "date", "price", "waterfront", "yr_built", "yr_renovated", "zipcode", "lat", "long", "sqft_living15", "floors", "sqft_lot"], axis = 1)
x2 = sm.add_constant(z2)
model2 = sm.OLS(y1, x2).fit()
print("Optimized House Price Model Summary based on bedrooms, bathrooms, sqft_living, view, condition, grade, sqft_above, sqft_basement, and sqft_lot15 variables.")
print(model2.summary())