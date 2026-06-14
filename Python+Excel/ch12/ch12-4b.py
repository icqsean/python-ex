from openpyxl import load_workbook

wb = load_workbook("各班的成績管理3.xlsx")
ws = wb.active
ws.title = "A班"
wb.save("各班的成績管理4.xlsx")
wb.close()

