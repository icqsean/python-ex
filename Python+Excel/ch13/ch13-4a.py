from win32com.client import Dispatch
import os

app = Dispatch("Excel.Application")
app.Visible = 1
app.DisplayAlerts = 0
xlsx = app.Workbooks.Open(os.getcwd()+"/ExcelVBA測試程式.xlsm")
result = app.Application.Run("ExcelVBA測試程式.xlsm!Module1.Add", 10, 20)
print(result)
xlsx.Close(False)
app.Quit()