import os
import sys

path = sys.argv[1]
filtered_doc = []

try:
    with open(path) as file:
        lines = file.readlines()
    #print(lines)

except FileNotFoundError:
    print("File not found.")
    sys.exit(1)


for line in lines:
    line = line.lstrip()
    if line != "":
        #if the line is empty, nothing happens, it goes back to the beggining
        if not line.startswith("#"):
            #if the line isn't empty, it checks if it starts with an #. If it doesn't, it appends to the new list
            filtered_doc.append(line)

print(f"len = {len(filtered_doc)}")

