from PIL import Image
import sys

im = Image.open("monkey.jpg")
gray = im.convert(mode = "L")
gray.save('gray_monkey.jpg')
gray.show()
