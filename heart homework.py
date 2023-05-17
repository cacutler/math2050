import pandas as pd
data = pd.read_csv("heart.csv")
df = pd.DataFrame(data)
male = df[df.sex == 1]
female = df[df.sex == 0]
moderately_elevated_male = df[df.chol >= 200][df.chol <= 239][df.sex == 1]
moderately_elevated_female = df[df.chol >= 200][df.chol <= 239][df.sex == 0]
probability_of_male = len(male)/len(df)
probability_of_female = len(female)/len(df)
probability_of_moderately_elevated_male = len(moderately_elevated_male)/len(df)
probability_of_moderately_elevated_female = len(moderately_elevated_female)/len(df)
hypertension_and_over_60 = df[df.age > 60][df.trestbps >= 130]
over_60 = df[df.age > 60]
probability_of_over_60 = len(over_60)/len(df)
probability_of_hypertension_and_over_60 = len(hypertension_and_over_60)/len(df)
above_120_and_male = df[df.fbs == 1][df.sex == 1]
above_120_and_female = df[df.fbs == 1][df.sex == 0]
probability_of_above_120_and_male = len(above_120_and_male)/len(df)
probability_of_above_120_and_female = len(above_120_and_female)/len(df)
print("FBS over 120 given male probability is", str(probability_of_above_120_and_male/probability_of_male))
print("FBS over 120 given female probability is", str(probability_of_above_120_and_female/probability_of_female))
print("Moderately elevated serum given male probability is", str(probability_of_moderately_elevated_male/probability_of_male))
print("Moderately elevated serum given female probability is", str(probability_of_moderately_elevated_female/probability_of_female))
print("Hypertension given over 60 years old probability is", str(probability_of_hypertension_and_over_60/probability_of_over_60))