import pandas as pd

data = {"種類": ["Bike","Bus","Car","Truck"],
        "數量": [3,4,6,2],
        "輪數": ["2","4","4","6"] }
df = pd.DataFrame(data, index=["A","B","C","D"])
df["種類"] = df["種類"].astype("string")
df["輪數"] = df["輪數"].astype("int64")
# 建立df2的DataFrame
df2 = df[["種類", "輪數"]]
print(df2)

with pd.ExcelWriter("車輛資料3.xlsx") as writer:
    df.to_excel(writer, sheet_name="車輛1")
    df2.to_excel(writer, sheet_name="車輛2")
