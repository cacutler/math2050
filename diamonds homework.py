import pandas as pd
data = pd.read_csv("diamonds.csv")
df = pd.DataFrame(data)
ideal = df[df.cut == "Ideal"]
vs1 = df[df.clarity == "VS1"]
premium_and_e = df[df.cut == "Premium"][df.color == "E"]
ideal_and_vs1 = df[df.clarity == "VS1"][df.cut == "Ideal"]
ideal_or_vs1 = len(ideal)/len(df) + len(vs1)/len(df) - len(ideal_and_vs1)/len(df)
very_good_and_e = df[df.cut == "Very Good"][df.color == "E"]
e = df[df.color == "E"]
probability_of_very_good_and_e = len(very_good_and_e)/len(df)
probability_of_e = len(e)/len(df)
print("Ideal probability is", str(len(ideal)/len(df)))
print("VS1 probability is", str(len(vs1)/len(df)))
print("Premium and E probability is", str(len(premium_and_e)/len(df)))
print("Ideal or VS1 probability is", str(ideal_or_vs1))
print("Very Good given E probability is", str(probability_of_very_good_and_e/probability_of_e))