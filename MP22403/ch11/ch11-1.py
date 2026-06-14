import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("員工資料.xlsx", sheet_name="員工")
result = employees[employees["電話"].isnull()]
print(result)
print("---------------")
result = employees[employees["學號"].notna()]
print(result)
print("---------------")
result = sqldf("""SELECT *
                  FROM employees
                  WHERE 電話 IS NULL;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT *
                  FROM employees
                  WHERE 學號 IS NOT NULL;
               """)
print(result)

