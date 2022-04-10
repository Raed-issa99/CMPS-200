from PIL import Image, ImageFont, ImageDraw
import textwrap
import sys

def decode_image(filename):
    img = Image.open(filename)
    img2= Image.new('LA',img.size)
    w,h = img.size
    for i in range(h):
        for j in range(w):
            p = img.getpixel((j,i))
            if p[0]%2 == 0:
                img2.putpixel((j,i),0)
            else:
                img2.putpixel((j,i),255)
    return img2

def write_text(text_to_write, image_size):
    '''Writes text to an RGB image.'''

    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    # Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text


def encode_image(text_to_encode, filename):
    '''encodes a text message into an image'''
    img = Image.open(filename)
    red, green, blue = img.split()   # the RGB bands, each is an L image
    width, height = img.size

    # text draw
    image_text = write_text(text_to_encode, img.size)
    bw_encode = image_text.convert('1')

    # encode text into image
    encoded_image = Image.new("RGB", img.size)
    pixels = encoded_image.load()
    for i in range(width):
        for j in range(height):
            red_pix = bin(red.getpixel((i,j)))
            tencode_pix = bin(bw_encode.getpixel((i,j)))

            if tencode_pix[-1] == '1':
                red_pix = red_pix[:-1] + '1'
            else:
                red_pix = red_pix[:-1] + '0'
            col = (int(red_pix, 2), green.getpixel((i,j)), blue.getpixel((i,j)))
            encoded_image.putpixel( (i,j), col)
    return encoded_image


# read user input and call encode/decode
operation = sys.argv[1]            # should be encode or decode
fname = sys.argv[2]
if operation == 'encode':
    text = sys.argv[3]
    encoded = encode_image(text, fname)
    encoded.save('encoded_image.png')
elif operation == 'decode':
    decoded = decode_image(fname)
    decoded.save('decoded_image.png')
    decoded.show()
else:
    print('Operation Invalid')
