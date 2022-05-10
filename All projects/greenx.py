from PIL import Image
import sys
def deface2(img,n):
    im = Image.open(img)
    w,h = im.size
    for i in range(w):
        for j in range(h):
            if j == int(i * (h/w)) or int(i * (h/w)) + j == h:
                for c in range(max(0,i-n//2),min(w,i+n//2)):
                    im.putpixel((c,j),(0,255,0))
    im.show()

n = int(sys.argv[2])
name = sys.argv[1]
deface2(name,n)
