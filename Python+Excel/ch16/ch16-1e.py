from pypdf import PdfReader, PdfWriter
import os

pdf_path = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖.pdf")
watermark_path = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖_浮水印.pdf")
pdf_output = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖4.pdf")
watermarkReader = PdfReader(watermark_path)
watermarkpage = watermarkReader.pages[0]
pdfReader = PdfReader(pdf_path)
pdfWriter = PdfWriter()
for pageNo in range(len(pdfReader.pages)):
    page = pdfReader.pages[pageNo]
    page.merge_page(watermarkpage)
    pdfWriter.add_page(page)
with open(pdf_output, "wb") as fp:
    pdfWriter.write(fp)

