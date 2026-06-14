import pandas as pd
import shutil
from datetime import datetime

source = r"D:\ExcelSQL\ch08\銷售系統.xlsx"
target = r"D:\ExcelSQL\ch09\銷售系統.xlsx"
shutil.copyfile(source, target)

employees2 = pd.read_excel("研發部.xlsx", sheet_name="員工")
employees2["員工編號"] = employees2["編號"]
employees2["生日"] = pd.to_datetime(employees2["生日"])
employees2["年齡"] = (datetime.today().year - employees2["生日"].dt.year) 
employees2["分機"] = 100
employees2["住家地址"] = employees2["城市"] + '市' + employees2["街道"]
employees2["住家電話"] = employees2["電話"]
employees2 = employees2[["員工編號","姓名","性別","年齡","部門",
                         "職稱","薪水","分機","住家地址","住家電話"]]
print(employees2.head())
print("---------------")
employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
for rindex in range(len(employees2)):
    new_record = employees2.loc[rindex]
    employees = employees._append(new_record, ignore_index=True)
print(employees.tail())
