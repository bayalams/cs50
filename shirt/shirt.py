from PIL import Image
from PIL import Image
from PIL import ImageOps
import sys
import os


def check_puppet(file):
    return os.path.isfile(file)

puppet = sys.argv[1]
OVERLAY_SHIRT = 'shirt.png'
#puppet_with_shirt = sys.argv[2]


if __main__ == '__main__':
    if not check_puppet(file):
        print(f'invalid puppet {file}. exit.')
        exit(-1)

    img_puppet = Image.open(puppet)
    img_shirt = Image.open(OVERLAY_SHIRT)
    