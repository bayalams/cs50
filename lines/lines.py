import sys
import os


directory = sys.argv[1]
print(directory)

if not os.path.isdir(directory):
    print("Not directory")
    sys.exit(1)

for filename in os.listdir(directory):
    with open(directory) as file:
        file.readlines()
