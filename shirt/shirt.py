from PIL import Image
import sys

puppet = sys.argv[1]
puppet_with_shirt = sys.argv[2]


shirt = Image.open(puppet)
shirt.show()


