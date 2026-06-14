from openpyxl import load_workbook

wb = load_workbook("各班的成績管理4.xlsx")
ws = wb["C班"]
wb.remove(ws)
wb.save("各班的成績管理5.xlsx")
wb.close()
