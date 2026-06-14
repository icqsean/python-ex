from pypdf import PdfReader, PdfWriter
import os

pdf_path = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖.pdf")
pdf_output = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖2.pdf")
pdfReader = PdfReader(pdf_path)
pdfWriter = PdfWriter()
page1 = pdfReader.pages[0]
page1.rotate_clockwise(90)
pdfWriter.add_page(page1)
with open(pdf_output, "wb") as fp:
    pdfWriter.write(fp)
