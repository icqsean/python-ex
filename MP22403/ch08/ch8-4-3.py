import pandas as pd
from pandasql import sqldf

products = pd.read_excel("銷售系統.xlsx", sheet_name="產品")
products2 = products[["產品編號","產品名稱","產品說明","定價"]]
result = products2[~products2["產品說明"].str.contains('黃')]
print(result)
print("---------------")
products2 = products[["產品編號","產品名稱","定價","入庫日期"]]
result = products2[~((products2["入庫日期"] >= '2023-01-01') &
                    (products2["入庫日期"] <= '2023-03-31'))]
print(result)
print("---------------")
result = products2[~products2["產品編號"].isin(['P001','P003','P005'])]
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 產品說明, 定價
                  FROM products
                  WHERE NOT 產品說明 LIKE '%黃%';
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 定價, 入庫日期
                  FROM products
                  WHERE NOT DATE(入庫日期) BETWEEN '2023-01-01'
                                      AND '2023-03-31';
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 定價, 入庫日期
                  FROM products
                  WHERE 產品編號 NOT IN ('P001', 'P003', 'P005');
               """)
print(result)
