import pandas as pd
from pandasql import sqldf

df = pd.read_excel("文具商品採購清單.xlsx",
                   sheet_name="全公司")
pivot_products = df.pivot_table(index=["分類","項目"], 
                                values="金額",
                                aggfunc="sum")
pivot_products.rename(columns={"金額":"合計金額"},
                      inplace=True)
print(pivot_products)
pivot_products.to_excel("文具商品採購清單樞紐分析表3_py.xlsx")
print("---------------")
result = sqldf("""SELECT 分類, 項目, SUM(金額) AS 合計金額
                  FROM df
                  GROUP BY 分類, 項目;
               """)
print(result)