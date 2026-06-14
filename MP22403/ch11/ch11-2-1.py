import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("員工資料.xlsx", sheet_name="員工")
print(employees.info())
print("---------------")
result = employees["年齡"].isnull().sum()
print(result)
print("---------------")
result = sqldf("""SELECT COUNT(*) AS 空值數
                  FROM employees
                  WHERE 年齡 IS NULL;
               """)
print(result)


