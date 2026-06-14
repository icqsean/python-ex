from docxtpl import DocxTemplate

tpl = DocxTemplate("Word模版文件.docx")

context = {
            "name" : "陳會安",
            "book" : "看圖學Python+Excel辦公室自動化"
          }

tpl.render(context)
tpl.save("產生Wrod文件.docx")
