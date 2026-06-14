import pandas as pd
from pandasql import sqldf

df = pd.read_excel("選課資料.xlsx",
                   sheet_name=["學生","班級"])
students = df["學生"]
classes = df["班級"]
result = pd.merge(students, classes, on="學號", how="left")
result = result[["學號","姓名","課程編號"]]
print(result)
print("---------------")
result = pd.merge(students, classes, on="學號", how="right")
result = result[["學號","姓名","課程編號"]]
print(result)
print("---------------")
result = sqldf("""SELECT 學生.學號, 學生.姓名, 班級.課程編號
                  FROM students AS 學生
                  LEFT JOIN classes AS 班級
                  ON 學生.學號 = 班級.學號;
               """)
print(result)

