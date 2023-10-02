import os
import sys

#path = sys.argv[1]
filtered_doc = []

try:
    with open("/workspaces/110493296/game/game.py", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)


print(len(lines))

for line in lines:
    line = line.lstrip()
    if line.startswith("#"):
        print(f"1.{line}")
        print(len(lines))

print(len())