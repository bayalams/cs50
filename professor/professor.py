def get_level():

    level  = int(input("Level1: "))

    while True:
        if level not in (1, 2, 3):
            level = int(input("Level2: "))
            return level
        else:
            break

get_level()