from pypdf import PdfReader, PdfWriter
import os

pdf_output = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖3.pdf")
pdfReader1 = PdfReader(os.path.join(os.getcwd(), "PDF", "Python海龜繪圖_p1.pdf"))
pdfReader2 = PdfReader(os.path.join(os.getcwd(), "PDF", "Python海龜繪圖_p2.pdf"))
pdfReader3 = PdfReader(os.path.join(os.getcwd(), "PDF", "Python海龜繪圖_p3.pdf"))
pdfWriter = PdfWriter()
pdfWriter.add_page(pdfReader1.pages[0])
pdfWriter.add_page(pdfReader2.pages[0])
pdfWriter.add_page(pdfReader3.pages[0])
with open(pdf_output, "wb") as fp:
    pdfWriter.write(fp)

