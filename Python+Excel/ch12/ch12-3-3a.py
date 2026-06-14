from openpyxl import load_workbook

wb = load_workbook("成績管理4.xlsx")
ws = wb.active
for column in ws.columns:
    for cell in column:
        print(cell.value, end=" ")
    print()    
wb.close()
