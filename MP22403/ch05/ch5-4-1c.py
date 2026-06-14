import pandas as pd

df = pd.read_excel("進修班成績管理.xlsx",
                   dtype={
                       "姓名": str,
                       "國文": str,
                       "英文": str,
                       "數學": str
                   },
                   na_values=["江小魚", "66"])
print(df)
