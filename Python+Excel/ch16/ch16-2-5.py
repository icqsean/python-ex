from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm

doc = DocxTemplate("Word模版文件6.docx")

img = InlineImage(doc, "penguins.png", Cm(5))
context = { "name": "陳會安",
            "image": img }

doc.render(context)
doc.save("產生Wrod文件6.docx")
