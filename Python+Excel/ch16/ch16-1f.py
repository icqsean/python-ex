from win32com.client import Dispatch
import os

wdFormatPDF = 17

app = Dispatch("Word.Application")
app.Visible = 1
app.DisplayAlerts = 0
docx = app.Documents.Open(os.getcwd()+"/自動化建立Word文件.docx")
docx.SaveAs(os.getcwd()+"/自動化建立Word文件.pdf", 
            FileFormat=wdFormatPDF)
docx.Close()
app.Quit()

