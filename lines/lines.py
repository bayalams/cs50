import sys
import os

file = sys.argv[1]
print(file)

with open("file") as file:
    file.readlines()
