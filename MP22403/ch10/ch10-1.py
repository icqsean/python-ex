import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
employees2 = employees[employees["薪水"] > 55000]
result = employees2[["員工編號","姓名","職稱","薪水"]]
print(result)
print("---------------")
result = sqldf("""SELECT 高薪員工.員工編號,高薪員工.姓名,
                         高薪員工.職稱,高薪員工.薪水
                  FROM (
                    SELECT 員工編號, 姓名, 職稱, 薪水
                    FROM employees
                    WHERE 薪水 > 55000
                  ) AS 高薪員工;
               """)
print(result)