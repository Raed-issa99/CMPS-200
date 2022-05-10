from PIL import Image
a=Image.open("monkey.jpg")
def smooth(original):
    res = Image.new(original.mode, original.size)
    width, height = original.size
    for i in range(0, width):
        for j in range(0, height):
            red, green, blue = (0, 0, 0)
            numPixels = 0 # initialize counter of neighbors of pixel (i, j)
            for c in range(max(0, i-1), min(width, i+2)):
                for r in range(max(0, j-1), min(height, j+2)):
                    numPixels +=1
                    pixel = original.getpixel((c, r))
                    red = red + pixel[0]
                    green = green + pixel[1]
                    blue = blue + pixel[2]
# compute average of red, green, and blue colors
            red = red // numPixels
            green = green // numPixels
            blue = blue // numPixels
# color pixel (i, j) of res with average color
            res.putpixel((i, j), (red, green, blue))

    res.show()

smooth(a)
