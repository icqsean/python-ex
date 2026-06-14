import pandas as pd
from pandasql import sqldf

products = pd.read_excel("銷售系統.xlsx", sheet_name="產品")
products2 = products[["產品編號","產品名稱","產品說明","定價"]]
result = products2[products2["產品名稱"].str.contains('11') &
                   products2["產品說明"].str.contains('6.1')]
print(result)
print("---------------")
result = products2[products2["產品名稱"].str.contains('11') |
                   products2["產品說明"].str.contains('6.1')]
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 產品說明, 定價
                  FROM products
                  WHERE 產品名稱 LIKE '%11%' AND
                        產品說明 LIKE '%6.1%';
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 產品編號, 產品名稱, 產品說明, 定價
                  FROM products
                  WHERE 產品名稱 LIKE '%11%' OR
                        產品說明 LIKE '%6.1%';
               """)
print(result)

