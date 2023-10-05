import os
import sys

path = "/workspaces/110493296/grocery/grocery.py"

for i in path:
    if path[2:] != ".py":
        print("file not .py")
        sys.exit(1)

filtered_doc = []

try:
    with open(path) as file:
        lines = file.readlines()

except FileNotFoundError:
    print("File not found.")
    sys.exit(1)


for line in lines:
    line = line.lstrip()
    #1.check if line is empty. If the line is empty, nothing happens, it goes back to the beggining, otherwise it continues
    if line != "":
        #if the line isn't empty, it checks if it starts with an #. If it doesn't, it appends to the new list
        if not line.startswith("#"):
            filtered_doc.append(line)

print(f"len = {len(filtered_doc)}")

