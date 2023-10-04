import os
import sys

#path = sys.argv[1]
filtered_doc = []

try:
    with open("/workspaces/110493296/game/game.py", "r") as file:
        lines = file.readlines()
    #print(lines)

except FileNotFoundError:
    print("File not found.")
    sys.exit(1)


for line in lines:
    line = line.lstrip()
    if line == "":
        print(f"line = {line}")
    elif not line.startswith("#"):
        filtered_doc.append(line)

print(f"len = {len(filtered_doc)}")

