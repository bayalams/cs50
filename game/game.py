import random

def main(guess, random_number):

    while guess != random_number:
        if guess > random_number:
            print("Too large!")
            guess = define_guess_number()
        elif guess < random_number:
            print("Too small!")
            guess = define_guess_number()
        else:
            print("Just right!")
            break


def guess_range():

    while True:
        try:
            level = int(input("Level: "))
            random_number = int(random.randint(1, level))
            #print(f"Random number: {random_number}")
            return random_number

        except ValueError:
            pass


def define_guess_number(): #não tem argumento porque o argumento é wildcard, o mesmo com o de cima
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                #print("bellow zero")
                continue #explain?????
        except ValueError:
            pass #why not continue????
        else:
            #print(f"define guess: {guess}")
            return guess



if __name__ == "__main__":
    random_number = guess_range() #a ordem é importante!!!!
    guess = define_guess_number() #got it, estamos a atribuir à variável o resultado da função para podermos usar noutra função
    main(guess, random_number)