import docx

doc = docx.Document("自動化建立Word文件5.docx")
doc.add_page_break()
doc.save("自動化建立Word文件6.docx")
