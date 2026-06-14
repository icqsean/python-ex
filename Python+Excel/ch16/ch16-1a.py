from pypdf import PdfReader
import os

pdf_path = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖.pdf")
pdfReader = PdfReader(pdf_path)
for pageNo in range(0, len(pdfReader.pages)):
    page = pdfReader.pages[pageNo]
    print(page.extract_text())
