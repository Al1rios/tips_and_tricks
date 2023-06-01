import PyPDF2

pdf_file = ('file1.pdf', 'rb')

read_file = PyPDF2.PdfFileReader(pdf_file)

page = read_file.getPage(1)

print(page.extracText())

pdf_file.close()