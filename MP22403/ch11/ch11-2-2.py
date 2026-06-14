import pandas as pd

employees = pd.read_excel("員工資料.xlsx", sheet_name="員工")
result = employees.dropna(subset=["年齡"])
print(result)
print(len(result))
