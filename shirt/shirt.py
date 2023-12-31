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
    treat_images(input_img, output_img)

def check_puppet(file):
    return os.path.isfile(file)

def extension_validation(input_img, output_img):
    input_extension = os.path.splitext(input_img)[-1]
    output_extension = os.path.splitext(output_img)[-1]

    #print(input_extension, output_extension)
    accepted_extensions = [".jpg", ".jpeg", ".png"]

    if output_extension not in accepted_extensions:
        print("Invalid output")
        sys.exit(-1)
    elif input_extension != output_extension:
        print("Input and output have different extensions")
        sys.exit(-1)

#FALTA PÔR AS IMAGENS DO MESMO TAMANHO
def treat_images(input_img, output_img):

   # load images
    img_puppet = Image.open(input_img)
    img_shirt = Image.open(OVERLAY_SHIRT)

    puppet_width, puppet_height = img_puppet.size
    print(puppet_width, puppet_height)

    #resize shirt image
    img_puppet_resized = ImageOps.fit(img_puppet, (1200, 1600), method = 0,
                               bleed = 0.0, centering = (0.5, 0.5))
    img_shirt_resized = ImageOps.fit(img_shirt, (1200, 1600), method = 0,
                               bleed = 0.0, centering = (0.5, 0.5))

    # paste shirt on top
    img_puppet_resized.paste(img_shirt_resized)
    img_puppet_resized.save(output_img)



if __name__ == '__main__':
    main()

