import pyodbc
import pandas as pd

print([x for x in pyodbc.drivers()
         if x.startswith('Microsoft Excel Driver')])
print("---------------")
# 括號是用來建立多行字串(Multiline String)或稱三重引號字串。
conn_str = (
  "DRIVER=Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb);"
  "DBQ=D:\\ExcelSQL\\ch07\\圖書資料.xlsx;"
  )
conn = pyodbc.connect(conn_str, autocommit=True)

cursor = conn.cursor()
sql = "SELECT * FROM [圖書資料$]"
cursor.execute(sql)
column_names = [column[0] for column in cursor.description]
print("欄位名稱:", column_names)
for row in cursor.fetchall():
    print(row)
print("---------------")    
df = pd.read_sql(sql, conn)
print(df)
conn.close()
        
    