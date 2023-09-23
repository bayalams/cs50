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

    # 3. while user_answers are not the same as the number of questions, keep going...
    while len(user_answers) != NUMBER_OF_QUESTIONS:
        try:
            desired_result = ground_truth[current_question]
            a, b = questions[current_question]
            user_result = int(input(f"{a} + {b} = "))

            if user_result == desired_result:
                user_answers.append(user_result)
                current_question = current_question + 1
            elif user_result != desired_result:
                user_result = "EEE"
                user_answers.append(user_result)
                print("EEE")

            print('user_answers', user_answers)

        except ValueError:
            continue

    # print(f"result list: {result_list}")
    # print(f"user results: {user_result_list}")

    score_list = []
    #------->>>>>>> ERRADO, VOLTAR AQUI!!! <<<<------
    for result, user_result in zip(result_list, user_result_list):
        if user_result == result:
            score_list.append(user_result)
    #score_list vai buscar números duplicados, whyyy????
    #------->>>>>>> ERRADO, VOLTAR AQUI!!! <<<<------

    # print()
    # print(f"length of score list: {len(score_list)}")
    # print(f"score list: {score_list}")
    print(f"Score: {len(score_list)}")

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