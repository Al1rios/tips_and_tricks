
from pdf2docx import Converter
# path to your pdf file
pdf = 'file.pdf'
# Path to where the doc file will be saved
word_file = 'file.docx'
#instantiate converter
cv = Converter(pdf)
cv.convert(word_file)
#close file
cv.close()