import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
students = pd.read_excel("學生.xlsx", sheet_name="學生")
result = pd.concat([employees["姓名"], students["姓名"]],
                   axis=0,
                   ignore_index=True)
print(result)
print("---------------")
result = result.drop_duplicates()
print(result)
print("---------------")
result = sqldf("""SELECT 姓名 FROM employees
                  UNION
                  SELECT 姓名 FROM students;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 姓名 FROM employees
                  UNION ALL
                  SELECT 姓名 FROM students;
               """)
print(result)