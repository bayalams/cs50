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

# for line in lines:
#     if line.isspace() or not line:
#         print("not line!")
#     else:
#         filtered_doc.append(line)

# print(filtered_doc)
# print(len(lines))


#falta tirar as linhas em branco
for line in lines:
    line = line.lstrip()
    if not line.startswith("#"):
        filtered_doc.append(line)

print(filtered_doc)

print(len(lines))