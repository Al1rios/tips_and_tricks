
from PIL import ImageDraw, Image, ImageFont


pic = Image.open('Calotes.jpg')

drawing = ImageDraw.Draw(pic)

fill_color = (255,250,250)

font = ImageFont.truetype("Verdana.ttf", 30)

position = (0,0)

drawing.text(position, text='Calotes is beautiful', fill = fill_color, font=font)

pic.show()

pic.save('watermarkedimg.jpg')
