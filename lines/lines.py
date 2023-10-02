import os
import sys

#path = sys.argv[1]

while True:
    try:
        with open("interpreter.py", "r") as file:
            lines = file.readlines()
    except FileNotFound:
        sys.exit(1)

