from PIL import Image
import sys
n = int(sys.argv[2])
name = sys.argv[1]
im = Image.open(name)
w,h = im.size
for i in range(0,w,n):
    for j in range(0,h,n):
        numpixels = 0
        red,green,blue = (0,0,0)
        for r in range(i,min(i+n,w)):
            for c in range(j,min(j+n,h)):
                numpixels += 1
                re,g,b = im.getpixel((r,c))
                red += re
                green += g
                blue += b
        for r in range(i,min(i+n,w)):
            for c in range(j,min(j+n,h)):
                im.putpixel((r,c),(red//numpixels,green//numpixels,blue//numpixels))
im.show()
