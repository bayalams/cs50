from PIL import Image
from PIL import Image
from PIL import ImageOps
import sys


puppet = sys.argv[1]
#puppet_with_shirt = sys.argv[2]


shirt = Image.open("shirt.png")
print(shirt.format, shirt.size, shirt.mode)

img1 = ImageOps.fit(puppet, bleed=0.0, centering=(0.5, 0.5), size=shirt.size)
