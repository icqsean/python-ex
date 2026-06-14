import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
result = employees[['姓名','薪水','住家電話']]
result = result.rename(columns={'姓名':'員工姓名',
                                '薪水':'員工薪水',
                                '住家電話': '員工電話'})
print(result)
print("---------------")
result = sqldf("""SELECT 
                     姓名 AS 員工姓名,
                     薪水 AS 員工薪水,
                     住家電話 AS 員工電話
                  FROM 
                     employees;
               """)
print(result)