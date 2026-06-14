import pandas as pd
from pandasql import sqldf

shoes = pd.read_excel("鞋價格表.xlsx",
                      sheet_name="尺寸分類")
shoes["尺寸"] = shoes["尺寸"].astype("string")
print(shoes.info())
print("---------------")
shoes2 = shoes.copy()
shoes2["尺寸"] = shoes2["尺寸"].astype("Int64")
print(shoes2.info())
print("---------------")
result = sqldf("""SELECT *, CAST(尺寸 AS INTEGER) AS 轉換後的尺寸
                  FROM shoes;
               """)
print(result)