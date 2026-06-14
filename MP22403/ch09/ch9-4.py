import pandas as pd

sales = pd.read_excel("業績資料\業績資料.xlsx")
sales = sales[sales["Sales Rep"] != 'John']
print(sales)
print("---------------")
sales = sales.query("`Sales Rep` != 'John'")
print(sales)     