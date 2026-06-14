from pypdf import PdfReader, PdfWriter
import os

pdf_path = os.path.join(os.getcwd(), "PDF", "Python海龜繪圖.pdf")
pdfReader = PdfReader(pdf_path)
fname = os.path.splitext(os.path.basename(pdf_path))[0]
for pageNo in range(len(pdfReader.pages)):
    pdfWriter = PdfWriter()
    page = pdfReader.pages[pageNo]
    pdfWriter.add_page(page)
    outputfname = os.path.join("PDF", f"{fname}_p{pageNo+1}.pdf")
    with open(outputfname, "wb") as fp:
        pdfWriter.write(fp)
        print("分割建立PDF檔:", outputfname)
