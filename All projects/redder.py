from PIL import Image
import sys
pic = sys.argv[1]
lst = pic.split('.')
def redder(image):
    old = Image.open(image)
    new = Image.new(old.mode, old.size)
    w,h = old.size
    for i in range(w):
        for j in range(h):
            red,green,blue = old.getpixel((i,j))
            red = min(255, int(red*1.5))
            new.putpixel((i,j),(red,green,blue))
    new.save(lst[0] + '_red.' + lst[1])
    new.show()

redder(pic)
