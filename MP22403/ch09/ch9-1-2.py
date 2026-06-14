import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("研發部.xlsx")
result = employees.copy()
result["員工地址"] = result["城市"] + '巿' + result["街道"]
result = result[["編號","姓名","職稱","員工地址"]]
print(result)
print("---------------")
result = employees.copy()
result["住家電話"] = result["電話"].str.replace('-', ' ')
result = result[["編號","姓名","職稱","住家電話"]]
print(result)
print("---------------")
result = sqldf("""SELECT 編號, 姓名, 職稱,
                     [城市] || '市' || [街道] AS 員工地址
                  FROM employees;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 編號, 姓名, 職稱,
                  REPLACE(電話, "-", " ") AS 電話
                  FROM employees;
               """)
print(result)