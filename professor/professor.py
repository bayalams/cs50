import random

def main():
    level = get_level()
    random_int_1, random_int_2 = generate_digits(level)

    result_list = []
    user_result_list = []

    # print(f"ri1 = {random_int_1}")
    # print(f"ri12= {random_int_2}")
    number_of_test = 10
    while len(user_result_list) != number_of_test:
        try:
            random_int_1, random_int_2 = generate_digits(level) #needs to be inside the loop so that it keeps generating new random ints
            result = random_int_1 + random_int_2
            # print(f"result = {result}")
            result_list.append(result)

            # print(f"{random_int_1} + {random_int_2} = ")
            #a resposta deve ser dada logo a seguir à pergunta, sem new line
            user_result = int(input(f"{random_int_1} + {random_int_2} = "))

            if user_result == result:
                user_result_list.append(user_result)
            elif user_result != result:
                user_result = "EEE"
                user_result_list.append(user_result)
                print("EEE")

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
            level  = int(input("Level: "))

            if level not in (1, 2, 3):
                level = int(input("Level: "))
            else:
                # print(f"The level is {level}")
                return level
        except ValueError:
            continue

def generate_digits(level):
#confirmar se está a correr 2x, uma antes de main ser chamada, em que os resultados não são utilizados, e uma depois, em que os resultados já são utilizados na função; só correr 1x

    min_value = 10**(level - 1) #define o número mínimo de dígitos; 10 elevado a nível(e.g. 3) - 1 = 10 elevado a 3-1 = 10 elevado a 2 = 100
    max_value = 10**level - 1 #define o número máximo de dígitos; 10 elevado a nível menos 1. E.g 10 elevado a 3-1 = (10 elevado a 3) - 1 = 1000 - 1 = 999

    random_int_1 = random.randint(min_value, max_value)
    #print(f"Random intenger 1 is {random_int_1}")

    random_int_2 = random.randint(min_value, max_value)
    #print(f"Random intenger 2 is {random_int_2}")

    return (random_int_1, random_int_2)


if __name__ == "__main__":
    main()