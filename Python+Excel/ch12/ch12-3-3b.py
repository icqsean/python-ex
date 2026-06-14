from openpyxl import load_workbook

wb = load_workbook("成績管理4.xlsx")
ws = wb["Sheet"]
data = ws.values
for v in data:
    print(v)
wb.close()
