import sys
import os
from PIL import Image, ImageOps

OVERLAY_SHIRT = 'shirt.png'

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input_image> <output_image>")
        sys.exit(-1)

    input_img_path = sys.argv[1]
    output_img_path = sys.argv[2]

    # Validate file extensions
    input_extension = os.path.splitext(input_img_path)[-1].lower()
    output_extension = os.path.splitext(output_img_path)[-1].lower()
    accepted_extensions = [".jpg", ".jpeg", ".png"]

    if input_extension not in accepted_extensions or output_extension not in accepted_extensions:
        print("Invalid file extension. Please use .jpg, .jpeg, or .png")
        sys.exit(-1)

    if input_extension != output_extension:
        print("Input and output should have the same file extensions.")
        sys.exit(-1)

    # Check if input file exists
    if not os.path.isfile(input_img_path):
        print(f"File {input_img_path} does not exist.")
        sys.exit(-1)

    # Resize and crop the input image
    input_image = Image.open(input_img_path)
    shirt_image = Image.open(OVERLAY_SHIRT)
    fitted_image = ImageOps.fit(input_image, shirt_image.size)

    # Overlay the shirt.png on the input image
    fitted_image.paste(shirt_image, (0, 0), shirt_image)

    # Save the result
    fitted_image.save(output_img_path)

if __name__ == '__main__':
    main()
