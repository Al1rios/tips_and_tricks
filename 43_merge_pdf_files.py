
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfReader

list1 = ['file1.pdf', 'file2.pdf']

merge = PyPDF2.PdfMerger(strict=True)
for file in list1:
    merge.append(PdfReader(file, 'rb+'))

merge.write('mergedfile.pdf')
merge.close()

create_file = PdfReader('mergedfile.pdf')
create_file