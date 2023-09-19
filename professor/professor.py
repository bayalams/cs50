import random

def main():

    print(f"ri1 = {random_int_1}")
    print(f"ri12= {random_int_2}")

    print(random_int_1 + random_int_2)

def get_level(): #number of digits of random ints

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

def generate_digits(level):
random_integer = generate_random_integer(num_digits)

    random_int_1 = random.randint(1, 10)
    print(f"Random intenger 1 is {random_int_1}")

    random_int_2 = random.randint(1, 10)
    print(f"Random intenger 2 is {random_int_2}")

    return random_int_1
    return random_int_2

if __name__ == "__main__":
    level = get_level()
    random_int_1 = generate_digits()
    random_int_2 = generate_digits()

    main()