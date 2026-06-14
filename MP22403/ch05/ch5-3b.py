import pandas as pd

df = pd.read_csv("2330.TW.csv")
print(df["Close"].unique())
print("---------------")
print(df["Close"].nunique())
print("---------------")
print(df["Close"].value_counts())
