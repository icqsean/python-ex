from openpyxl import Workbook

wb = Workbook()
ws = wb.active
records = [("姓名", "國文", "英文"),
           ("陳會安", 89, 76),
           ("江小魚", 78, 90) ]

for item in records:
    ws.append(item)
    
wb.save("成績管理.xlsx")
wb.close()