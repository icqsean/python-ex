import pandas as pd

employees = pd.read_excel("員工資料.xlsx", sheet_name="員工")
employees["年齡"] = employees["年齡"].fillna(
                    employees["年齡"].mean())
print(employees)
