import pandas as pd
from pandasql import sqldf

df = pd.read_excel("銷售系統.xlsx", sheet_name=["員工", "產品"])
employees = df["員工"]
products = df["產品"]
#print(employees)
#print(products)
result = employees[employees["姓名"] == '陳會安'][
                        ["姓名","薪水","住家電話"]]
print(result)
print("---------------")
result = employees[employees["薪水"] < 50000]
print(result)
print("---------------")
result = products[products["入庫日期"] == '2023-01-25']
print(result)
print("---------------")
result = sqldf("""SELECT 姓名, 薪水, 住家電話
                  FROM employees
                  WHERE 姓名 = '陳會安';
               """)
print(result)
print("---------------")
result = sqldf("""SELECT *
                  FROM employees
                  WHERE 薪水 < 50000;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT *
                  FROM products
                  WHERE DATE(入庫日期) = '2023-01-25';
               """)
print(result)