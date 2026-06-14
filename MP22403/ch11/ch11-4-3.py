import pandas as pd
from pandasql import sqldf

shoes = pd.read_excel("鞋價格表.xlsx",
                      sheet_name="尺寸分類")
shoes2 = shoes.copy()
shoes2["性別"] = shoes2["性別"].replace('not specified', 'male')
print(shoes2)
print("---------------")
shoes2["性別"] = shoes2["性別"].str.upper()
print(shoes2)
print("---------------")
result = sqldf("""SELECT *, REPLACE(性別, 'not specified', 'male')
                            AS 修改後的性別
                  FROM shoes;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT *, UPPER(性別) AS 大寫性別
                  FROM shoes;
               """)
print(result)