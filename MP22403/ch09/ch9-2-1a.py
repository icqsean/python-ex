import pandas as pd
import shutil

source = r"D:\ExcelSQL\ch08\銷售系統.xlsx"
target = r"D:\ExcelSQL\ch09\銷售系統.xlsx"
shutil.copyfile(source, target)

products = pd.read_excel("銷售系統.xlsx", sheet_name="產品")
new_record = pd.Series({"產品編號": 'P016',
                        "產品名稱": 'iPhone 13-128GB',
                        "產品說明": '福利品',
                        "定價": 15300,
                        "入庫日期": '2023/11/3',
                        "庫存量": 20,
                        "安全庫存": 2})
products = products._append(new_record, ignore_index=True)
print(products.tail())
