import random

def main():
    NUMBER_OF_QUESTIONS = 10
    # 0. ask user for a correct level.
    level = get_level()
    # 1. generate all exercises
    questions = []
    ground_truth = []
    for i in range(NUMBER_OF_QUESTIONS):
        random_a, random_b = generate_digits(level)
        questions.append((random_a, random_b))
        ground_truth.append(random_a + random_b)

    # 2. initialise supporting list variables
    user_answers = []
    current_question = 0
    already_failed = False
    score = 0

    # 3. while user_answers are not the same as the number of questions, keep going...
    while len(user_answers) != NUMBER_OF_QUESTIONS:
        try:
            desired_result = ground_truth[current_question]
            a, b = questions[current_question]
            # print(f'nº: {current_question}, already failed? {already_failed}', f'{a} + {b} = {desired_result}', user_answers)

            user_result = int(input(f"{a} + {b} = "))

            if user_result == desired_result:
                if not already_failed:
                    score = score + 1
                current_question = current_question + 1
                already_failed = False

            elif user_result != desired_result:
                already_failed = True
                print("EEE")

        except ValueError:
            continue

    print(f"Score: {score)")

def get_level(): #number of digits of random ints

    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level

        except ValueError:
            continue

def generate_digits(level):
#confirmar se está a correr 2x, uma antes de main ser chamada, em que os resultados não são utilizados, e uma depois, em que os resultados já são utilizados na função; só correr 1x
    if (level == 1):
        min_value = 0
    else:
        min_value = 10**(level - 1) #define o número mínimo de dígitos; 10 elevado a nível(e.g. 3) - 1 = 10 elevado a 3-1 = 10 elevado a 2 = 100
    max_value = 10**level - 1 #define o número máximo de dígitos; 10 elevado a nível menos 1. E.g 10 elevado a 3-1 = (10 elevado a 3) - 1 = 1000 - 1 = 999

    random_int_1 = random.randint(min_value, max_value)
    #print(f"Random intenger 1 is {random_int_1}")

    random_int_2 = random.randint(min_value, max_value)
    #print(f"Random intenger 2 is {random_int_2}")

    return (random_int_1, random_int_2)


if __name__ == "__main__":
    main()