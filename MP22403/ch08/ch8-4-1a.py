import pyodbc
import pandas as pd

# 括號是用來建立多行字串(Multiline String)或稱三重引號字串。
conn_str = (
  "DRIVER=Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb);"
  "DBQ=D:\\ExcelSQL\\ch08\\銷售系統.xlsx;"
  )
conn = pyodbc.connect(conn_str, autocommit=True)

cursor = conn.cursor()
sql = """SELECT *
         FROM [產品$]
         WHERE 入庫日期 = #2023-01-25#;
      """
cursor.execute(sql)
column_names = [column[0] for column in cursor.description]
print("欄位名稱:", column_names)
for row in cursor.fetchall():
    print(row)
print("---------------")    
df = pd.read_sql(sql, conn)
print(df)
conn.close()
        
    