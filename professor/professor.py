import random

level  = input("Level: ")

while True:
    if level not in (1, 2, 3):
        level = input("Level: ")
    else:
        break