from PIL import Image
import sys

def band(w): #Creates a red band of height 20 and width = to that given to it
    band = Image.new('RGB', (w,20))
    for i in range(w):
        for j in range(20):
            band.putpixel((i,j),(255,0,0))
    return band


def deface1(img): #Pastes a band in the middle of the image given to it
    pepper = Image.open(img)
    w,h = pepper.size
    redb = band(w) #Creates a red band of width = to the img and height 20
    pepper.paste(redb,(0,h//2))
    pepper.show()

def deface2(img):
    im = Image.open(img)
    w,h = im.size
    for i in range(w):
        for j in range(h):
            if i == j or i + j == w:
                for c in range(max(0,i-10),min(w,i+10)):
                    im.putpixel((c,j),(255,0,0))
    im.show()

#myimage = sys.argv[1]
#deface1(myimage)
deface2('peppers.jpg')
