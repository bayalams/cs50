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


if __name__ == '__main__':
    if not check_puppet(puppet):
        print(f'invalid puppet {puppet}. exit.')
        exit(-1)

    # load images
    img_puppet = Image.open(puppet)
    img_shirt = Image.open(OVERLAY_SHIRT)
    # resize shirt image
    img_shirt = img_shirt.resize(img_puppet.size)
    # paste shirt on top
    img_puppet.paste(img_shirt, (0,0), img_shirt)

    img_puppet.save(f'{puppet.split(".")[0]}_out.jpg')