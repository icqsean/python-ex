import pandas as pd

shoes = pd.read_excel("資料轉換\鞋價格表.xlsx",
                      sheet_name="尺寸分類")
size_mapping = {"XXL": 5,
                "XL": 4,
                "L": 3,
                "M": 2,
                "S": 1,
                "XS": 0}
shoes["尺寸"] = shoes["尺寸"].map(size_mapping)
print(shoes)
