from PIL import Image
from PIL import Image
from PIL import ImageOps
import sys


puppet = sys.argv[1]
#puppet_with_shirt = sys.argv[2]


shirt = Image.open("shirt.png")
print(shirt.format, shirt.size, shirt.mode)

print('puppet', puppet)
im_puppet = Image.open(puppet)
img1 = ImageOps.fit(im_puppet, bleed=0.0, centering=(0.5, 0.5), size=shirt.size)

img1.save('result.jpg')
