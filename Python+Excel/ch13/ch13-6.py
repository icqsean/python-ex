from win32com.client import Dispatch
import os

app = Dispatch("Excel.Application")
app.Visible = 1
app.DisplayAlerts = 0
xlsx = app.Workbooks.Open(os.getcwd()+"/ExcelVBA家庭收支流水帳.xlsm")
app.Application.Run("ExcelVBA家庭收支流水帳.xlsm!Module1.CreatePivotTable")
xlsx.SaveAs(os.getcwd()+"/ExcelVBA家庭收支流水帳2.xlsm")
xlsx.Close(False)
app.Quit()