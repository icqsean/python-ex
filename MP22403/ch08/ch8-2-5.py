import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
result = employees.iloc[2:5]
print(result)
print("---------------")
result = sqldf("SELECT * FROM employees LIMIT 2, 3;")
print(result)
print("---------------")
result = sqldf("SELECT * FROM employees LIMIT 3 OFFSET 2;")
print(result)
