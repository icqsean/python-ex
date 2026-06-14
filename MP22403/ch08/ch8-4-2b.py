import pandas as pd
from pandasql import sqldf

products = pd.read_excel("銷售系統.xlsx", sheet_name="產品")
products2 = products[["產品編號","產品名稱","定價","入庫日期"]]
result = products2[products2["產品編號"].isin(['P001','P003','P005'])]
print(result)
print("---------------")
result = products2[products2["定價"].isin([13900,21500])]
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 定價, 入庫日期
                  FROM products
                  WHERE 產品編號 IN ('P001', 'P003', 'P005');
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 定價, 入庫日期
                  FROM products
                  WHERE 定價 IN (13900, 21500);
               """)
print(result)
