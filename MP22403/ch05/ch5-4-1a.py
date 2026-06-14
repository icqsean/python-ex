import pandas as pd

df = pd.read_excel("進修班成績管理.xlsx",
                   usecols=['姓名', '國文', '數學'],
                   index_col=0)
print(df)
