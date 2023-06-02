
from barcode import ISBN13
from barcode.writer import ImageWriter
from PIL import Image

num = '979117528719'

bar_code = ISBN13(num, writer=ImageWriter())
bar_code.save('bar_code')

img = Image.open('bar_code.png')
img.show()