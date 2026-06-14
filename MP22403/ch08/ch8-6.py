import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
employees2 = employees[["姓名","薪水","住家電話"]]
result = employees2.sort_values("薪水",
                                ascending=False).head(3)
print(result)
print("---------------")
result = employees2.sort_values("薪水",
                                ascending=False).tail(3)
result = result.sort_values("薪水")
print(result)
print("---------------")
result = employees2.sort_values("薪水",
                                ascending=True).head(3)
print(result)
print("---------------")
result = sqldf("""SELECT 姓名, 薪水, 住家電話
                  FROM employees
                  ORDER BY 薪水 DESC
                  LIMIT 3;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 姓名, 薪水, 住家電話
                  FROM employees
                  ORDER BY 薪水 ASC
                  LIMIT 3;
               """)
print(result)
