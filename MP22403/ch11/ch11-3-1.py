import pandas as pd
from pandasql import sqldf

sales = pd.read_excel("業績資料.xlsx", sheet_name="業績")
result = sales.drop_duplicates()
print(result)
print("---------------")
result = sqldf("""SELECT DISTINCT *
                  FROM sales;
               """)
print(result)


