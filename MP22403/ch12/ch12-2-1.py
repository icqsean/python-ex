import pandas as pd
from pandasql import sqldf

df = pd.read_excel("選課資料.xlsx",
                   sheet_name=["班級","學生"])
classes = df["班級"]
students = df["學生"]
result = classes.groupby("課程編號").size() \
                .reset_index(name="學生數")
print(result)
print("---------------")
result = students.groupby("性別").size() \
                 .reset_index(name="學生數")
print(result)
print("---------------")
result = sqldf("""SELECT 課程編號, COUNT(*) AS 學生數
                  FROM classes
                  GROUP BY 課程編號;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 性別, COUNT(*) AS 學生數
                  FROM students
                  GROUP BY 性別;
               """)
print(result)