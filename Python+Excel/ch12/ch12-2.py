from openpyxl import Workbook

wb = Workbook()
ws = wb.active
    
wb.save("成績管理.xlsx")
wb.close()