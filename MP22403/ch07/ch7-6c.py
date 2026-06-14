import pandas as pd
from pandasql import sqldf

books = pd.read_excel("圖書資料.xlsx")
print(books)
print("---------------")
df = sqldf("SELECT * FROM books")
print(df)

df.to_excel("圖書資料3.xlsx", sheet_name="圖書資料")