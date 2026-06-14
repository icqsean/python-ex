from win32com.client import Dispatch
import os

app = Dispatch("Excel.Application")
app.Visible = 1
app.DisplayAlerts = 0
xlsx = app.Workbooks.Open(os.getcwd()+"/ExcelVBA網路爬蟲.xlsm")
app.Application.Run("ExcelVBA網路爬蟲.xlsm!Module1.GetTable")
xlsx.SaveAs(os.getcwd()+"/ExcelVBA網路爬蟲2.xlsm")
xlsx.Close(False)
app.Quit()