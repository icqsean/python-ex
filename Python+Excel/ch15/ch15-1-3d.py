import docx
from docx.shared import Cm

doc = docx.Document("自動化建立Word文件4.docx")
doc.add_picture("penguins.png", width=Cm(3))
doc.save("自動化建立Word文件5.docx")
