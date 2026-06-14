import pandas as pd

df = pd.read_excel("進修班成績管理.xlsx",
                   dtype={
                          "姓名": str,
                          "國文": int,
                          "英文": int,
                          "數學": float
                       })
print(df)
