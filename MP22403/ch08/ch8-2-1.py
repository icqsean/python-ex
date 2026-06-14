import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
print(employees)
print("---------------")
result = sqldf("SELECT * FROM employees;")
print(result)