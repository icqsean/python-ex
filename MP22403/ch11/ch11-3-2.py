import pandas as pd

sales = pd.read_excel("業績資料.xlsx", sheet_name="業績")
result = sales.drop_duplicates("國家")
print(result)



