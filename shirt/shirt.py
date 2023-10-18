from PIL import Image
from PIL import ImageOps
import sys
import os

OVERLAY_SHIRT = 'shirt.png'

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments.")
        sys.exit(-1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments.")

    input_img = sys.argv[1]
    output_img = sys.argv[2]

    if not check_puppet(input_img):
        print(f'invalid puppet {input_img}. exit.')
        exit(-1)

    extension_validation(input_img, output_img)

def check_puppet(file):
    return os.path.isfile(file)

def extension_validation(input_img, output_img):
    input_extension = os.path.splitext(input_img)[-1]
    output_extension = os.path.splitext(output_img)[-1]

    print(input_extension, output_extension)
    accepted_extensions = [".jpg", ".jpeg", ".png"]

    if output_extension not in accepted_extensions:
        print("Invalid output")
    else:
        sys.exit(-1)

    if input_extension != output_extension:
        print("Input and output have different extensions")
        sys.exit(-1)

if __name__ == '__main__':
    main()

    # load images
    #img_puppet = Image.open(input_img)
    #img_shirt = Image.open(OVERLAY_SHIRT)
    # resize shirt image
    #img_shirt = img_shirt.resize(img_input_img.size)
    # paste shirt on top
    #img_puppet.paste(img_shirt, (0,-100), img_shirt)

    #img_puppet.save(f'{input_img.split(".")[0]}_out.jpg')