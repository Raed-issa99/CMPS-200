from PIL import Image

def smooth(original):
    res = Image.new(original.mode,original.size) #mode(ex RBG)
    width, height = original.size
    for i in range(width):
        for j in range(height):
            red, greenn, blue = (0,0,0)
            numPixels = 0 #initialize counter of neighbors of pixel(i,j)
            for c in range(max(0, i-1), min(width, i+2)):
                for r in range(max(0, j-1), min(height, j+2)):
                    numPixels += 1
                    pixel = original.getpixel((c,r))
                    red += pixel[0]
                    green += pixel[1]
                    blue += pixel[2]
                #compute average of red, green, and blue colors
                red = red// numPixels
                green = green // numPixels
                blue = blue // numPixels
                # color pixel(i,j) of res with average colors
                res.putpixel((i,j), (red,green,blue))
            return res

x = smooth('monkey.jpg')
print(type(x))
