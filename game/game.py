import random


def main(guess, random_number):

    if guess > random_number:
       print("Too large")
    elif guess < random_number:
       print("Too small")
    else:
       print("Just right")


def guess_range():

    while True:
        try:
            level = int(input("Level: "))
            random_number = int(random.randint(1, level))
            print(f"Random number: {random_number}")
            return random_number

        except ValueError:
            pass


def define_guess_number(guess):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                print("bellow zero")
                continue #explain?????
        except ValueError:
            pass #why not continue????
        else:
            print(f"define guess: {guess}")
            return guess



if __name__ == "__main__":
    guess = define_guess_number() #got it, estamos a atribuir à variável o resultado da função para podermos usar noutra função
    random_number = guess_range()
    main(guess, random_number)