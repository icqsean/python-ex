import pandas as pd
from pandasql import sqldf

products = pd.read_excel("銷售系統.xlsx", sheet_name="產品")
products2 = products[["產品編號","產品名稱","定價","入庫日期"]]
result = products2[(products2["入庫日期"] >= '2023-01-01') &
                  (products2["入庫日期"] <= '2023-03-31')]
print(result)
print("---------------")
result = products2[(products2["定價"] >= 15000) &
                   (products2["定價"] <= 25000)]
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 定價, 入庫日期
                  FROM products
                  WHERE DATE(入庫日期) BETWEEN '2023-01-01'
                                      AND '2023-03-31';
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 定價, 入庫日期
                  FROM products
                  WHERE 定價 BETWEEN 15000 AND 25000;
               """)
print(result)
