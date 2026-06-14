from docxtpl import DocxTemplate

tpl = DocxTemplate("Word模版文件4.docx")

context = { 
       "table":[
                { "author" : "陳會安",
                  "date" : "2022-09-30",
                  "version" : "1.0",
                  "book" : "Python" }, 
                { "author" : "江小魚",
                  "date" : "2022-10-30",
                  "version" : "1.2",
                  "book" : "Excel"  } 
               ]
          }

tpl.render(context)
tpl.save("產生Wrod文件4.docx")
