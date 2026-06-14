import pandas as pd
from pandasql import sqldf

df = pd.read_excel("各班的成績資料.xlsx",
                   sheet_name=["A班","B班","C班"])
classA = df["A班"]
classB = df["B班"]
classC = df["C班"]
result = pd.concat([classA, classB, classC],
                   axis=0,
                   ignore_index=True)
print(result)
print("---------------")
result = sqldf("""SELECT * FROM classA
                  UNION ALL
                  SELECT * FROM classB
                  UNION ALL
                  SELECT * FROM classC;
               """)
print(result)
