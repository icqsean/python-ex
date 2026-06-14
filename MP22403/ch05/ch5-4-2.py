import pandas as pd

data = {"種類": ["Bike","Bus","Car","Truck"],
        "數量": [3,4,6,2],
        "輪數": ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"])
df["種類"] = df["種類"].astype("string")
df["輪數"] = df["輪數"].astype("int64")
print(df.info())
df.to_excel("車輛資料.xlsx", sheet_name="車輛")
df.to_excel("車輛資料2.xlsx", sheet_name="車輛",
            index=False)
