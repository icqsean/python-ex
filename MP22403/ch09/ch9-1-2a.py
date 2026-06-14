import pandas as pd
from pandasql import sqldf
from datetime import datetime

employees = pd.read_excel("研發部.xlsx")
employees["年齡"] = datetime.now().year - employees["生日"].dt.year
result = employees[["編號","姓名","職稱","年齡"]]
print(result)
print("---------------")
result = sqldf("""SELECT 編號, 姓名, 職稱,
                     strftime('%Y', 'now') - strftime('%Y', 生日) AS 年齡
                  FROM employees;
               """)
print(result)