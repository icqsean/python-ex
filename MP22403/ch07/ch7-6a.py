import pandas as pd
from pandasql import sqldf

books = pd.read_excel("圖書資料.xlsx")
print(books)
print("---------------")
df = sqldf("SELECT * FROM books")
print(df)

df.to_csv("圖書資料3.csv", index=False, encoding="big5")