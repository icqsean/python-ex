from openpyxl import Workbook

wb = Workbook()
ws = wb.active
records = { "姓名": ["陳會安","江小魚"],
            "國文": [89, 78],
            "英文": [76, 90]}

ws.append(list(records.keys()))
print(records.values())
data = list(zip(*records.values()))
for item in data:
    ws.append(item)
    
wb.save("成績管理.xlsx")
wb.close()