import pandas as pd
from pandasql import sqldf

products = pd.read_excel("銷售系統.xlsx", sheet_name="產品")
products["定價"] = products["定價"].astype("string")
result = products.query("產品說明.str.contains('黃')")
print(result)
print("---------------")
result = products.query("入庫日期 == '2023-01-25'")
print(result)
print("---------------")
result = products.query("定價.str.contains('9..$')")
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 產品說明, 定價
                  FROM products
                  WHERE 產品說明 LIKE '%黃%';
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 產品說明, 定價
                  FROM products
                  WHERE 定價 LIKE '%9__';
               """)
print(result)
