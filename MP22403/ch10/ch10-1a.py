import pandas as pd
from pandasql import sqldf

df = pd.read_excel("銷售系統.xlsx", sheet_name=["員工", "訂單"])
employees = df["員工"]
orders = df["訂單"]
id = employees.loc[employees["姓名"] == '江小魚',
                   "員工編號"].values[0]
result = orders.loc[orders["員工編號"] == id,
                    "訂單編號"].count()
print(result)
print("---------------")
result = sqldf("""SELECT COUNT(*) AS 訂單數
                  FROM orders
                  WHERE 員工編號 IN (
                    SELECT 員工編號
                    FROM employees
                    WHERE 姓名 = '江小魚'
                  );
               """)
print(result)
print("---------------")
result = sqldf("""SELECT COUNT(*) AS 訂單數
                  FROM orders
                  WHERE 員工編號 = (
                    SELECT 員工編號
                    FROM employees
                    WHERE 姓名 = '江小魚'
                  );
               """)
print(result)