import random

def get_level():

    while True:
        try:
            level  = int(input("Level1: "))

            if level not in (1, 2, 3):
                level = int(input("Level2: "))
            else:
                print(f"The level is {level}")
                return level
        except ValueError:
            continue

get_level()

def generate_digits():



