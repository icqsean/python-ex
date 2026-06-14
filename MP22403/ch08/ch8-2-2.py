import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
result = employees[['姓名', '薪水', '住家電話']]
print(result)
print("---------------")
result = sqldf("SELECT 姓名, 薪水, 住家電話 FROM employees;")
print(result)