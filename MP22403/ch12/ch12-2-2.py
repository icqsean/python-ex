import pandas as pd
from pandasql import sqldf

classes = pd.read_excel("選課資料.xlsx", sheet_name="班級")
result = classes.groupby("學號").size() \
                .reset_index(name="修課數")
result = result[result["修課數"] > 2]
print(result)
print("---------------")
result = classes[classes["教授編號"] == 'I003'] \
         .groupby("課程編號").size().reset_index(name="學生數")
result = result[result["學生數"] >= 2]
print(result)
print("---------------")
result = sqldf("""SELECT 學號, COUNT(*) AS 修課數
                  FROM classes
                  GROUP BY 學號
                  HAVING COUNT(*) > 2;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT 課程編號, COUNT(學號) AS 學生數
                  FROM classes
                  WHERE 教授編號 = 'I003'
                  GROUP BY 課程編號
                  HAVING COUNT(學號) >= 2;
               """)
print(result)