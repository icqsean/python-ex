from pypdf import PdfReader
import os

pdf_path = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖.pdf")
pdfReader = PdfReader(pdf_path)
numberOfPages = len(pdfReader.pages)
print("頁數1:", numberOfPages)
numberOfPages = len(pdfReader.pages)
print("頁數2:", numberOfPages)
info = pdfReader.metadata
print("作者:", getattr(info, 'author', None))
print("標題:", getattr(info, 'title', None))
print("製作者:", getattr(info, 'producer', None))
