from openpyxl import load_workbook

wb = load_workbook("各班的成績管理4.xlsx")
ws = wb.active
print("目前工作表名稱:", ws.title)
wb.active = 2
ws = wb.active
print("目前工作表名稱:", ws.title)
ws2 = wb["B班"]
print("切換至B班:", ws2.title)
wb.close()
