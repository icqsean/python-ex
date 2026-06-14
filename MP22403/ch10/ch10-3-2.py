import pandas as pd
from pandasql import sqldf

df = pd.read_excel("選課資料.xlsx",
                   sheet_name=["學生","教授","課程","班級"])
students = df["學生"]
classes = df["班級"]
courses = df["課程"]
professors = df["教授"]
result = pd.merge(students, classes, on="學號")
result = result[["學號","姓名","課程編號","教授編號"]]
print(result)
print("---------------")
result = pd.merge(pd.merge(students, classes, on="學號"),
                           courses, on="課程編號")
result = result[["學號","姓名","課程編號","名稱","學分","教授編號"]]
print(result)
print("---------------")
result = pd.merge(pd.merge(pd.merge(professors, classes,
                                    left_on="教授編號",
                                    right_on="教授編號"),
                           students, on="學號"),
                  courses, on="課程編號")
result = result[["學號","姓名","課程編號","名稱","學分",
                 "教授編號","職稱","科系","身份證字號"]]
print(result)
print("---------------")
result = sqldf("""SELECT 學生.學號, 學生.姓名,
                         班級.課程編號, 班級.教授編號
                  FROM students AS 學生 
                  INNER JOIN classes AS 班級
                  ON 學生.學號 = 班級.學號;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 結果.學號, 結果.姓名, 課程.*, 結果.教授編號
                  FROM courses AS 課程 
                  INNER JOIN result AS 結果  
                  ON 結果.課程編號 = 課程.課程編號;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 結果.學號, 結果.姓名, 結果.課程編號,
                         結果.名稱, 結果.學分, 教授.*
                  FROM professors AS 教授
                  INNER JOIN result AS 結果
                  ON 教授.教授編號 = 結果.教授編號;
               """)
print(result)