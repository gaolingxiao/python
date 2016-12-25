from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)
args = parser.parse_args()
image = args.file
output = args.output
width = args.width
height = args.height
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
    unit = (256 + 1) / length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(image)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)
    if output:
        with open(output, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)

