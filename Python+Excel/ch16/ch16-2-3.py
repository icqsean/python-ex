from docxtpl import DocxTemplate

tpl = DocxTemplate("Word模版文件2.docx")

context = { 
            "user" : "hueyan",
          }

tpl.render(context)
tpl.save("產生Wrod文件2.docx")
