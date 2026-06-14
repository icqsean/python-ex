from win32com.client import Dispatch
import os

app = Dispatch("PowerPoint.Application")
app.Visible = 1
app.DisplayAlerts = 0
pptx = app.Presentations.Open(os.getcwd()+"\\自動化建立PPT簡報5.pptx")
copy_idx = 4   # 第4頁, 從1開始
ins_idx = copy_idx + 1
pptx.Slides(copy_idx).Copy()
pptx.Slides.Paste(Index=ins_idx)
pptx.SaveAs(os.getcwd()+"\\自動化PPT簡報的投影片管理_複製.pptx")
pptx.Close()
os.system('taskkill /F /IM POWERPNT.EXE')  #app.Quit() not work

