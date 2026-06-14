import docx

doc = docx.Document("自動化建立Word文件3.docx")
records = (
    ("王小明", 67, 78),
    ("陳小安", 88, 66),
    ("李四誠", 75, 85) )
table = doc.add_table(rows=1, cols=3)
row = table.rows[0]
row.cells[0].text = "姓名" 
row.cells[1].text = "國文"
row.cells[2].text = "英文"
for name, score1, score2 in records:
    row_cells = table.add_row().cells
    row_cells[0].text = name
    row_cells[1].text = str(score1)
    row_cells[2].text = str(score2)
doc.save("自動化建立Word文件4.docx")
 


