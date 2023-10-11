from PIL import Image
import sys, os

puppet = sys.argv[1]
#puppet_with_shirt = sys.argv[2]


shirt = Image.open("shirt.png")
print(shirt.format, shirt.size, shirt.mode)

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)

