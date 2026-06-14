# 請注意! adodbapi只支援Python 3.9之前版本, 並不支援3.10和之後版本
import adodbapi
import pandas as pd

# 括號是用來建立多行字串(Multiline String)或稱三重引號字串。
conn_str = (
  "PROVIDER=Microsoft.ACE.OLEDB.12.0;"
  "Data Source=圖書資料.xlsx;"
  "Extended Properties='Excel 12.0 Xml;HDR=YES'"
  )
conn = adodbapi.connect(conn_str)
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