from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)
args = parser.parse_args()
image = args.file
output = args.output
width = args.width
height = args.height

