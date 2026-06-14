from openpyxl import load_workbook

wb = load_workbook("成績管理4.xlsx")
ws = wb.active
for row in ws.rows:
    for cell in row:
        print(cell.value, end=" ")
    print()    
wb.close()
