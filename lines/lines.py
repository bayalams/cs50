import os
import sys

path = sys.argv[1]

try:
    with open(path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)

print(len(lines))
for line in lines:
    if not line.startswith("#"):
        