import pandas as pd

sheet_names = ["人事部", "業務部", "研發部", "製造部"]
df = pd.read_excel("文具用品採購\文具商品採購清單.xlsx",
                   sheet_name=sheet_names)
company = pd.DataFrame()
for name in sheet_names:
    items = df[name]
    items["部門"] = name
    items["金額"] = items["單價"] * items["數量"]
    result = items[["部門","分類","項目","數量","金額"]]
    company = pd.concat([company, result],
                        axis=0,
                        ignore_index=True)

print(company.info())
company.to_excel("文具商品採購清單2.xlsx",
                 sheet_name="全公司", index=False)

