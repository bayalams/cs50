import os
import sys

path = sys.argv[1]

while True:
    try:
        with open(path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

