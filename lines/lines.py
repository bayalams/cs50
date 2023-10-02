import sys
import os


file = sys.argv[1]
print(file)

for filename in os.listdir(file):
    with open(file) as file:
        file.readlines()
