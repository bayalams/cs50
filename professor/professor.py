import random

def main(random_int_1, random_int_2):

    result_list = []

    print(f"ri1 = {random_int_1}")
    print(f"ri12= {random_int_2}")
    result = random_int_1 + random_int_2
    
    while len(result_list) != 10:
        result_list.append(result)
        print(f"{random_int_1} + {random_int_2} = {result}")

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

    min_value = 10**(level - 1) #define o número mínimo de dígitos; 10 elevado a nível(e.g. 3) - 1 = 10 elevado a 3-1 = 10 elevado a 2 = 100
    max_value = 10**level - 1 #define o número máximo de dígitos; 10 elevado a nível menos 1. E.g 10 elevado a 3-1 = (10 elevado a 3) - 1 = 1000 - 1 = 999

    random_int_1 = random.randint(min_value, max_value)
    print(f"Random intenger 1 is {random_int_1}")

    random_int_2 = random.randint(min_value, max_value)
    print(f"Random intenger 2 is {random_int_2}")

    return (random_int_1, random_int_2)


if __name__ == "__main__":
    level = get_level()
    random_int_1, random_int_2 = generate_digits(level)

    main(random_int_1, random_int_2)