import pandas as pd

df = pd.read_excel("進修班成績管理.xlsx", sheet_name="A班")
print(df)
print("----------------")
df2 = pd.read_excel("進修班成績管理.xlsx", sheet_name=[1, "C班"])
print(df2[1])    # 字典
print(df2["C班"])
print("----------------")
df3 = pd.read_excel("進修班成績管理.xlsx", sheet_name=None)
print(df3)
