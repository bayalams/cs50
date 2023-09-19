def get_level():

    while True:
        level  = int(input("Level1: "))

        if level not in (1, 2, 3):
            level = int(input("Level2: "))
        else:
            print(f"The level is {level}")
            return level
        raise ValueError


get_level()


