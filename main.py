import PyPDF2
pdfs=['pdf1.pdf','pdf2.pdf']
merger=PyPDF2.PdfMerger()
for file in pdfs:
    merger.append(file)

merger.write('final.pdf')




