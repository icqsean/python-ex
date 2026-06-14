import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("研發部.xlsx")
employees["薪水淨額"] = employees["薪水"] - employees["公積金"]
result = employees[["編號","姓名","職稱","薪水淨額"]]
print(result)
print("---------------")
result = sqldf("""SELECT 編號, 姓名, 職稱, (薪水 - 公積金) AS 薪水淨額
                  FROM employees;
               """)
print(result)