from PIL import Image
import sys, os

puppet = sys.argv[1]
#puppet_with_shirt = sys.argv[2]


shirt = Image.open("shirt.png")
print(shirt.format, shirt.size, shirt.mode)

img1 = ImageOps.fit(puppet, method = Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
