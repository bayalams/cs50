import os
import sys

path = sys.argv[1]

with open(path, "r") as file:
    lines = file.readlines()
    print(lines)

